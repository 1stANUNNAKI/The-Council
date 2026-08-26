// majlis-bootstrap.js - OpenCode plugin.
// Self-healing deployer: on startup, if the installed Majlis system is missing
// or older than the package VERSION, redeploy skills/agents PURELY in-process with
// node fs (no external processes -> immune to host env issues). Never blocks startup.
//
// ══════════════════════════════════════════════════════════════════
// WRITE GUARD LAW: this plugin may ONLY create/overwrite files under
// skill/agent/command asset directories (see SAFE_ROOTS below).
// It must NEVER read, write, delete or rename the editor's settings,
// credential stores, database, or any file outside SAFE_ROOTS.
// Enforced at runtime by w() — and by eval/run.js adoption-safety suite.
// ══════════════════════════════════════════════════════════════════
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'

let ran = false

const CLAUDE_TOOLS = {
  'hadi-maestro': 'Task, Bash, Read, Grep, Glob',
  'rased-explorer': 'Bash, Read, Grep, Glob',
  'sajeel-logger': 'Bash, Read, Edit, Write',
  'hakim-mentor': 'Grep, Glob, Read, Edit, Write',
  'bayan-diagrams': 'Glob, Read, Write',
  'emad-api-shield': '',
  'baher-qa': 'Bash, Read, Grep, Glob',
  'sareem-security': 'WebSearch, WebFetch, Bash, Glob, Read, Grep'
}
const EXCLUDE = new Set(['science_skills_common'])
const NAME_RE = /^[a-z0-9]+(-[a-z0-9]+)*$/

function normalizeName(raw) {
  return raw.toLowerCase().replace(/_+/g, '-').replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '').replace(/-{2,}/g, '-').replace(/^-+|-+$/g, '')
}

export const MajlisBootstrap = async ({ client }) => {
  if (ran) return {}
  ran = true
  const home = os.homedir()
  const cfg = path.join(home, '.config', 'opencode')
  /* runtime write guard: every write must land inside one of these roots,
     or be one of the two explicit marker files this plugin owns */
  const SAFE_ROOTS = [
    path.join(cfg, 'skills'),
    path.join(cfg, 'agents'),
    path.join(cfg, 'command'),
    path.join(home, '.claude', 'skills'),
    path.join(home, '.claude', 'agents'),
    path.join(home, '.claude', 'commands'),
    path.join(home, '.codex', 'skills'),
    path.join(home, '.codex', 'prompts'),
    path.join(home, '.agents', 'skills')
  ]
  const srcHint = path.join(cfg, 'majlis_source.txt')
  const marker = path.join(cfg, '.majlis_deployed')
  const OWNED_FILES = new Set([srcHint, marker].map(p => path.resolve(p)))
  const w = (file, data, enc) => {
    const p = path.resolve(file)
    if (!OWNED_FILES.has(p) && !SAFE_ROOTS.some(r => p.startsWith(path.resolve(r) + path.sep))) {
      throw new Error(`WRITE-GUARD: refusing to touch ${p} (outside Majlis asset scope)`)
    }
    fs.writeFileSync(file, data, enc)
  }
  const logFile = path.join(cfg, '.majlis_bootstrap.log')
  const say = (level, msg) => { try { fs.appendFileSync(logFile, `[${new Date().toISOString()}] ${level}: ${msg}\n`) } catch (_) {} }
  try {
    if (!fs.existsSync(srcHint)) return {}
    const pkgDir = fs.readFileSync(srcHint, 'utf8').trim()
    const versionFile = path.join(pkgDir, 'VERSION.txt')
    if (!fs.existsSync(versionFile)) { say('error', `bad source hint: ${pkgDir.slice(0, 60)}`); return {} }
    const want = fs.readFileSync(versionFile, 'utf8').trim()
    const have = fs.existsSync(marker) ? fs.readFileSync(marker, 'utf8').trim() : null
    const healthy =
      fs.existsSync(path.join(cfg, 'skills', 'trufflehog-secret-scanner', 'SKILL.md')) &&
      fs.existsSync(path.join(cfg, 'agents', 'hadi-maestro.md'))
    if (have === want && healthy) return {}

    say('info', `heal needed: have=${have} want=${want} healthy=${healthy}`)
    const utf8 = { encoding: 'utf8' }

    // ---- build normalized skill library from package ----
    const lib = {}
    const srcSkills = path.join(pkgDir, 'skills')
    for (const dir of fs.readdirSync(srcSkills, { withFileTypes: true })) {
      if (!dir.isDirectory() || EXCLUDE.has(dir.name)) continue
      const f = path.join(srcSkills, dir.name, 'SKILL.md')
      if (!fs.existsSync(f)) continue
      let text = fs.readFileSync(f, 'utf8')
      const m = text.match(/^name:\s*(.+)\s*$/m)
      const fmName = m ? m[1].trim() : ''
      const target = NAME_RE.test(fmName) ? fmName : normalizeName(dir.name)
      if (!NAME_RE.test(target) || lib[target]) continue
      lib[target] = text
    }

    // ---- deploy skills to every platform dir ----
    const skillDests = [
      path.join(cfg, 'skills'),
      path.join(home, '.claude', 'skills'),
      path.join(home, '.codex', 'skills'),
      path.join(home, '.agents', 'skills')
    ]
    let count = 0
    for (const destRoot of skillDests) {
      for (const [name, text] of Object.entries(lib)) {
        const d = path.join(destRoot, name)
        fs.mkdirSync(d, { recursive: true })
        w(path.join(d, 'SKILL.md'), text, utf8)
        count++
      }
    }

    // ---- deploy agents: opencode native + claude converted + codex prompts ----
    const agSrc = path.join(pkgDir, 'agents')
    const agOc = path.join(cfg, 'agents'); fs.mkdirSync(agOc, { recursive: true })
    const agCl = path.join(home, '.claude', 'agents'); fs.mkdirSync(agCl, { recursive: true })
    const prCx = path.join(home, '.codex', 'prompts'); fs.mkdirSync(prCx, { recursive: true })
    let agents = 0
    for (const f of fs.readdirSync(agSrc).filter(f => f.endsWith('.md'))) {
      const id = f.replace(/\.md$/, '')
      const raw = fs.readFileSync(path.join(agSrc, f), 'utf8')
      const body = raw.replace(/^---[\s\S]*?---\s*/, '').trim()
      const dm = raw.match(/^description:\s*(.+)$/m)
      const desc = dm ? dm[1].trim() : `Majlis Council role ${id}`
      w(path.join(agOc, f), raw, utf8)
      const tools = CLAUDE_TOOLS[id]
      let cl = `---\nname: ${id}\ndescription: ${desc}\n`
      if (tools) cl += `tools: ${tools}\n`
      cl += `---\n\n${body}\n`
      w(path.join(agCl, f), cl, utf8)
      const px = `---\ndescription: Adopt the Majlis '${id}' role for this task.\nargument-hint: TASK\n---\n\nAdopt the following agent role exactly, then execute the TASK supplied after the role definition.\n\n## Role: ${id}\n\n${body}\n\n## TASK\n$ARGUMENTS\n`
      w(path.join(prCx, `majlis-${f}`), px, utf8)
      agents++
    }

    // ---- keep source hint canonical & mark deployed ----
    try { w(srcHint, pkgDir, utf8) } catch (_) {}
    w(marker, want, utf8)
    say('info', `healed v${want}: ${count} skill copies across ${skillDests.length} platforms, ${agents} agents x3 formats`)
    await client?.app?.log?.({ body: { service: 'majlis-bootstrap', level: 'info', message: `Majlis healed to v${want}` } }).catch?.(() => {})
  } catch (e) {
    say('error', String(e && e.stack || e))
  }
  return {}
}
