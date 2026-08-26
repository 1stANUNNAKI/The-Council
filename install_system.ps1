# install_system.ps1 v2 - Multi-platform installer for the Antigravity system.
# ASCII-only by design (PS 5.1 codepage safety); Arabic text lives in templates/*.md.
# Targets: opencode | claude | codex | universal
# Usage:
#   powershell -File install_system.ps1                                  # all global targets
#   powershell -File install_system.ps1 -Targets opencode,codex          # subset
#   powershell -File install_system.ps1 -ScaffoldProject C:\path\proj    # project pointers for ALL platforms
param(
  [string]$Targets = 'opencode,claude,codex,universal',
  [string]$ScaffoldProject = ''
)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ErrorActionPreference = 'Stop'
$pkg     = $PSScriptRoot
$version = (Get-Content (Join-Path $pkg 'VERSION.txt') -Raw).Trim()
$master  = Join-Path $pkg 'AGENTS.md'
$nameRegex = '^[a-z0-9]+(-[a-z0-9]+)*$'
$utf8    = New-Object System.Text.UTF8Encoding($false)

Write-Host "`n=== MAJLIS Council System Installer v$version (multi-platform) ===" -ForegroundColor Cyan

function Read-Template([string]$name) {
  $t = [System.IO.File]::ReadAllText((Join-Path $pkg "templates\$name"))
  return $t.Replace('{MASTER}', $master)
}

# ---------- 1) Normalize skill library once ----------
$descFix = @{
  'advanced-image-slicing-skill'    = 'Slice large images into responsive tiles/sprites and animate pan/zoom transitions for web layouts.'
  'majlis-rules'                    = 'Constitution and operating rules of the Majlis Council system: agent legion routing, security pipeline, clean-code standards, chronicle logging.'
  'explode-animation-skill'         = 'Create product explosion/fragment animations: layered disassembly sequences, timing curves, and Remotion/CSS implementations.'
  'marketing-funnel-skill'          = 'Design marketing funnels and data capture flows: stages, CTAs, tracking events, and conversion analytics wiring.'
  'premium-visual-polish-skill'     = 'Apply premium visual polish passes: spacing rhythm, shadows, gradients, micro-interactions, magazine-grade typography.'
  'psychological-copywriting-skill' = 'Write psychology-driven marketing copy using persuasion principles (scarcity, social proof, loss aversion).'
  'tech-background-skill'           = 'Generate animated technical backgrounds (circuits, grids, particles) as CSS canvas or video assets for hero sections.'
  'find-skills'                     = 'Search GitHub and skill registries for existing skills/tools before building new ones; returns candidates with install steps.'
  'skill-creator'                   = 'Create new SKILL.md skills and agent definitions following platform frontmatter conventions and validation rules.'
}
function Normalize-Name([string]$raw) {
  $n = $raw.ToLowerInvariant() -replace '_+','-' -replace '\s+','-'
  return (($n -replace '[^a-z0-9-]','') -replace '-{2,}','-').Trim('-')
}
$library = @{}
$skillDirs = @{}
$srcSkills = Join-Path $pkg 'skills'
foreach ($dir in (Get-ChildItem -LiteralPath $srcSkills -Directory)) {
  if ($dir.Name -eq 'science_skills_common') { continue }
  $f = Join-Path $dir.FullName 'SKILL.md'; if (-not (Test-Path $f)) { continue }
  $text = [System.IO.File]::ReadAllText($f)
  $m = [regex]::Match($text, '(?m)^name:\s*(.+?)\s*$')
  $fmName = if ($m.Success) { $m.Groups[1].Value.Trim() } else { '' }
  $target = if ($fmName -match $nameRegex) { $fmName } else { Normalize-Name $dir.Name }
  if ($target -notmatch $nameRegex -or $library.ContainsKey($target)) { continue }
  if ($descFix.ContainsKey($target)) {
    $pat = '(?ms)^(description:\s*)(>-\s*\r?\n(\s+.*\r?\n)*?|.+?)(?=\r?\n[a-zA-Z-]+:|\r?\n---)'
    $newText = [regex]::Replace($text, $pat, "`$1description: $($descFix[$target])", 1)
    if ($newText -ne $text) { $text = $newText }
  }
  $library[$target] = $text
  $skillDirs[$target] = $dir.FullName
}
function Deploy-SkillLibrary([string]$destRoot) {
  foreach ($k in $library.Keys) {
    $d = Join-Path $destRoot $k
    New-Item -ItemType Directory -Path $d -Force | Out-Null
    [System.IO.File]::WriteAllText((Join-Path $d 'SKILL.md'), $library[$k], $utf8)
    $srcD = $skillDirs[$k]
    foreach ($sub in (Get-ChildItem -LiteralPath $srcD -Directory)) {
      $dst = Join-Path $d $sub.Name
      if (Test-Path -LiteralPath $dst) { Remove-Item -LiteralPath $dst -Recurse -Force }
      Copy-Item -LiteralPath $sub.FullName -Destination $dst -Recurse -Force
    }
  }
  return $library.Count
}

# ---------- 2) Agent conversions ----------
$claudeTools = @{
  'hadi-maestro'    = 'Task, Bash, Read, Grep, Glob'
  'rased-explorer'  = 'Bash, Read, Grep, Glob'
  'sajeel-logger'   = 'Bash, Read, Edit, Write'
  'hakim-mentor'    = 'Grep, Glob, Read, Edit, Write'
  'bayan-diagrams'  = 'Glob, Read, Write'
  'emad-api-shield' = ''
  'baher-qa'        = 'Bash, Read, Grep, Glob'
  'sareem-security' = 'WebSearch, WebFetch, Bash, Glob, Read, Grep'
  'nadif-clean-code'= 'Bash, Read, Grep, Glob'
  'mubtakir-tools'  = 'WebSearch, WebFetch, Bash, Read, Edit, Write'
  'balegh-docs'     = 'Glob, Grep, Read, Edit, Write'
  'hadi-core'        = 'Read, Grep, Glob, Bash'
  'agent-weaver'     = 'Read, Write, Edit, Grep, Glob'
  'data-modeler'     = 'Read, Write, Edit, Grep, Glob'
  'stream-partitioner' = 'Read, Write, Edit, Bash'
  'integrative-architect' = 'Read, Write, Edit, Grep, Glob'
  'risk-assessor'    = 'Read, Grep, Glob'
  'cinematic-director' = 'Read, Write, Edit'
  'design-system-master' = 'Read, Write, Edit'
  'responsive-layout' = 'Read, Write, Edit, Bash'
  'print-publisher'  = 'Read, Write, Edit'
  'motion-coder'     = 'Bash, Read, Write, Edit'
  'cicd-automator'   = 'Bash, Read, Write, Edit'
  'sandbox-isolator' = 'Bash, Read, Write'
  'dep-manager'      = 'Bash, Read, Edit'
  'voice-engineer'   = 'Bash, Read, Write'
  'data-engineer'    = 'WebSearch, WebFetch, Read, Write'
  'product-shaper'   = 'Read, Write, Edit, Grep, Glob'
  'ux-researcher'    = 'Read, Grep, Glob, Bash'
  'brand-guardian'   = 'Read, Grep, Glob, Bash'
  'growth-analyst'   = 'Read, Write, Edit, Grep, Glob'
  'code-polisher'    = 'Bash, Read, Write, Edit, Grep, Glob'
  'test-engineer'    = 'Bash, Read, Write, Edit, Grep, Glob'
  'perf-auditor'     = 'Bash, Read, Write, Edit, Grep, Glob'
  'a11y-auditor'     = 'Read, Grep, Glob, Bash'
  'release-manager'  = 'Bash, Read, Write, Edit, Grep, Glob'
  'incident-detective' = 'Read, Grep, Glob, Bash'
  'prompt-smith'     = 'Read, Write, Edit, Grep, Glob'
  'context-steward'  = 'Read, Write, Edit, Grep, Glob'
  'portfolio-steward' = 'Read, Grep, Glob, Bash'
}
$agentsSrc = Join-Path $pkg 'agents'
$converted = @{}
foreach ($af in (Get-ChildItem "$agentsSrc\*.md")) {
  $raw  = [System.IO.File]::ReadAllText($af.FullName)
  $body = ($raw -replace '(?s)^---.*?---\s*', '').Trim()
  $descM = [regex]::Match($raw, '(?m)^description:\s*(.+?)$')
  $desc  = if ($descM.Success) { $descM.Groups[1].Value.Trim() } else { "Antigravity legion role $($af.BaseName)" }
  $converted[$af.BaseName] = @{ body = $body; desc = $desc }
}
function Deploy-Agents-Claude([string]$destRoot) {
  New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
  foreach ($id in $converted.Keys) {
    $fm = "---`nname: $id`ndescription: $($converted[$id].desc)`n"
    if ($claudeTools[$id]) { $fm += "tools: $($claudeTools[$id])`n" }
    [System.IO.File]::WriteAllText((Join-Path $destRoot "$id.md"), ($fm + "---`n`n" + $converted[$id].body + "`n"), $utf8)
  }
  return $converted.Count
}
function Deploy-Agents-CodexPrompts([string]$destRoot) {
  New-Item -ItemType Directory -Path $destRoot -Force | Out-Null
  foreach ($id in $converted.Keys) {
    $hint = "---`ndescription: Adopt the Antigravity '$id' role for this task.`nargument-hint: TASK`n---`n`n"
    $role = "Adopt the following agent role exactly, then execute the TASK supplied after the role definition.`n`n## Role: $id`n`n" + $converted[$id].body + "`n`n## TASK`n`$ARGUMENTS`n"
    [System.IO.File]::WriteAllText((Join-Path $destRoot "majlis-$id.md"), ($hint + $role), $utf8)
  }
  return $converted.Count
}

# ---------- 3) Pointer ----------
function Deploy-Pointer([string]$file) {
  $d = Split-Path -Parent $file
  if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
  [System.IO.File]::WriteAllText($file, (Read-Template 'pointer.md'), $utf8)
}

# ---------- 4) Execute targets ----------
$t = $Targets.Split(',') | ForEach-Object { $_.Trim().ToLowerInvariant() }
$results = @()

if ($t -contains 'universal') {
  $p = Join-Path $env:USERPROFILE '.agents\skills'
  $results += "universal : $(Deploy-SkillLibrary $p) skills -> $p"
}
if ($t -contains 'opencode') {
  $sk = Join-Path $env:USERPROFILE '.config\opencode\skills'
  $ag = Join-Path $env:USERPROFILE '.config\opencode\agents'
  $results += "opencode  : $(Deploy-SkillLibrary $sk) skills -> $sk"
  Copy-Item -Path "$agentsSrc\*.md" -Destination (New-Item -ItemType Directory -Path $ag -Force).FullName -Force
  $results += "            $($converted.Count) native subagents -> $ag"
  $cm = Join-Path $env:USERPROFILE '.config\opencode\command'
  New-Item -ItemType Directory -Path $cm -Force | Out-Null
  Copy-Item -Path "$pkg\commands\majlis-*.md" -Destination $cm -Force
  $results += "            6 native commands /majlis:* -> $cm"
  $plugDir = Join-Path $env:USERPROFILE '.config\opencode\plugins'
  New-Item -ItemType Directory -Path $plugDir -Force | Out-Null
  Remove-Item (Join-Path $plugDir 'antigravity-bootstrap.js') -Force -ErrorAction SilentlyContinue
  $pluginSrc = Join-Path $pkg 'plugins\majlis-bootstrap.js'
  if (Test-Path $pluginSrc) {
    Copy-Item $pluginSrc $plugDir -Force
    [System.IO.File]::WriteAllText((Join-Path $env:USERPROFILE '.config\opencode\majlis_source.txt'), $pkg, $utf8)
    [System.IO.File]::WriteAllText((Join-Path (Split-Path -Parent $plugDir) '.majlis_deployed'), $version, $utf8)
    Remove-Item (Join-Path $env:USERPROFILE '.config\opencode\antigravity_source.txt') -Force -ErrorAction SilentlyContinue
    Remove-Item (Join-Path (Split-Path -Parent $plugDir) '.antigravity_deployed') -Force -ErrorAction SilentlyContinue
    $results += "            majlis-bootstrap plugin armed (v$version)"
  } else {
    $results += "            WARN plugin missing in package"
  }
}
if ($t -contains 'claude') {
  $sk = Join-Path $env:USERPROFILE '.claude\skills'
  $ag = Join-Path $env:USERPROFILE '.claude\agents'
  $cm = Join-Path $env:USERPROFILE '.claude\commands'
  $results += "claude    : $(Deploy-SkillLibrary $sk) skills -> $sk"
  $results += "            $(Deploy-Agents-Claude $ag) subagents -> $ag"
  New-Item -ItemType Directory -Path $cm -Force | Out-Null
  Copy-Item -Path "$pkg\commands\majlis-*.md" -Destination $cm -Force
  $results += "            6 slash commands /majlis-* -> $cm"
  Deploy-Pointer (Join-Path $env:USERPROFILE '.claude\CLAUDE.md')
  $results += "            global memory pointer -> ~\.claude\CLAUDE.md"
}
if ($t -contains 'codex') {
  $sk = Join-Path $env:USERPROFILE '.codex\skills'
  $pr = Join-Path $env:USERPROFILE '.codex\prompts'
  $results += "codex     : $(Deploy-SkillLibrary $sk) skills (`$skill-name) -> $sk"
  $results += "            $(Deploy-Agents-CodexPrompts $pr) role prompts (/prompts:) -> $pr"
  foreach ($cf in (Get-ChildItem "$pkg\commands\majlis-*.md")) {
    [System.IO.File]::WriteAllText((Join-Path $pr ($cf.BaseName + '.md')), ("---`ndescription: Majlis workflow command`nargument-hint: ARGS`n---`n`n" + ([System.IO.File]::ReadAllText($cf.FullName))), $utf8)
  }
  $results += "            6 workflow commands (/prompts:majlis-*) -> $pr"
  Deploy-Pointer (Join-Path $env:USERPROFILE '.codex\AGENTS.md')
  $results += "            global AGENTS.md pointer -> ~\.codex\AGENTS.md"
}
if ($t -contains 'gemini') {
  $gm = Join-Path $env:USERPROFILE '.gemini\commands\majlis'
  New-Item -ItemType Directory -Path $gm -Force | Out-Null
  Copy-Item -Path "$pkg\commands\majlis-*.md" -Destination $gm -Force
  $results += "gemini    : 6 commands (/majlis:*) -> $gm"
}

# ---------- 5) Optional project scaffold (ALL platforms) ----------
if ($ScaffoldProject) {
  $proj = (Resolve-Path $ScaffoldProject).Path
  function W([string]$rel,[string]$content){
    $p = Join-Path $proj $rel; $d = Split-Path -Parent $p
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
    [System.IO.File]::WriteAllText($p, $content, $utf8)
  }
  $short = (Read-Template 'project-rules.md')
  W 'AGENTS.md'                       $short                                   # opencode/codex/gemini-cli/jules/zed...
  W 'CLAUDE.md'                        ("See AGENTS.md - it is binding.`n`n" + $short)   # claude code
  W 'GEMINI.md'                        ("See AGENTS.md - it is binding.`n`n" + $short)   # gemini cli
  W '.github\copilot-instructions.md'  $short                                   # github copilot
  W '.cursor\rules\majlis.mdc'         ("---`ndescription: Majlis Council rules (always apply)`nglobs:`nalwaysApply: true`n---`n`n" + $short)  # cursor
  W '.agent\rules\majlis-core.md'      $short                                   # antigravity / generic .agent convention
  W '.windsurf\rules\majlis.md'        $short                                   # windsurf
  $results += "scaffold   : 7 rule files -> $proj"
}

Write-Host ""
$results | ForEach-Object { Write-Host " [OK] $_" -ForegroundColor Green }
Write-Host "`nDone. Idempotent; bump VERSION.txt and re-run to push updates everywhere." -ForegroundColor Cyan
