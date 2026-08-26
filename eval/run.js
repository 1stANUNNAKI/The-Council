/* Majlis v9.3 — eval/run.js : shipped evaluation harness.
   Verifies structural truth of the whole council. Exit 1 on any FAIL.
   Run: node eval/run.js */
const fs=require('fs'),path=require('path');
const ROOT=path.join(__dirname,'..');
let pass=0,fail=0;const F=[];
const ok=(cond,label)=>{if(cond){pass++}else{fail++;F.push(label)}};
function fm(t0){const text=t0.replace(/\r\n/g,'\n');if(!text.startsWith('---'))return{};const end=text.indexOf('\n---',3);if(end<0)return{};const lines=text.slice(3,end).split('\n');const out={};let key=null;for(const ln of lines){const m=ln.match(/^([A-Za-z_-]+):\s?(.*)$/);if(m){key=m[1];let v=m[2].trim();if(v==='>'||v==='>-'){out[key]='';continue}if(/^".*"$/.test(v)||/^'.*'$/.test(v))v=v.slice(1,-1);if(/^\[.*\]$/.test(v))v=v.slice(1,-1).split(',').map(x=>x.trim().replace(/^["']|["']$/g,'')).filter(Boolean);out[key]=v;continue}if(key&&typeof out[key]==='string'&&out[key]!==undefined&&(ln.startsWith('  ')||ln==='')){out[key]+=(out[key]?' ':'')+ln.trim()}}return out}
/* ---------- agents ---------- */
const DIVS=['lead','recon','eng','gate','exp','know'];
const agDir=path.join(ROOT,'agents');
const agFiles=fs.readdirSync(agDir).filter(f=>f.endsWith('.md'));
ok(agFiles.length===40,'agents count = '+agFiles.length+' (want 40)');
const agentIds=new Set();const agentMeta={};
for(const f of agFiles){
  const id=f.replace('.md','');agentIds.add(id);
  const t=fs.readFileSync(path.join(agDir,f),'utf8');const m=fm(t);agentMeta[id]=m;
  ok(DIVS.includes(m.division),id+': division');
  ok(typeof m.temperature==='number'||parseFloat(m.temperature)>0,id+': temperature');
  ok(Array.isArray(m.tools)&&m.tools.length>0,id+': tools list');
  ok(/permission:\n/.test(t)&&/(edit: (deny|ask|allow))/.test(t),id+': permission block');
  ok((m.description||'').length>80,id+': description depth');
  ['## Mission','## When to summon me','## Operating workflow','## Output contract','## Handoff','## Boundaries'].every(s=>{ok(t.includes(s),id+': section '+s);return true});
  ok(/\*\*بالعربية:\*\* \S/.test(t),id+': arabic role line');
  ok(!t.includes('27-agent'),id+': stale legion ref');
  for(const sk of (m.skills||[])){ok(fs.existsSync(path.join(ROOT,'skills',sk,'SKILL.md')),id+': skill ref '+sk)}
}
/* ---------- skills ---------- */
const CATS=['security','council','science','creative','cloudflare','meta'];
const skDir=path.join(ROOT,'skills');
const skIds=fs.readdirSync(skDir,{withFileTypes:true}).filter(d=>d.isDirectory()&&d.name!=='science_skills_common').map(d=>d.name);
ok(skIds.length===90,'skills count = '+skIds.length+' (want 90)');
for(const id of skIds){
  const t=fs.readFileSync(path.join(skDir,id,'SKILL.md'),'utf8');const m=fm(t);
  ok(m.name===id,id+': name==folder');
  ok((m.description||'').length>=20,id+': description min');
  ok(CATS.includes(m.category),id+': category');
  ok(agentIds.has(m.owner),id+': owner is real agent ('+m.owner+')');
  ok(Array.isArray(m.tags)&&m.tags.length>0,id+': tags');
  ok(Array.isArray(m.lang)&&m.lang.length>0,id+': lang');
  ok(/^\d+\.\d+\.\d+$/.test(m.version||''),id+': semver');
}
/* ---------- data packs ---------- */
const packs=[
['majlis-rules','security-red-gate-checklist.md'],
['qa-automated-tester-unit','qa-evidence-checklist.md'],
['security-clean-code-auditor','clean-code-rubric.md'],
['maestro-hadi-orchestration','golden-plan.md'],
['intent-observer-audit360','golden-recon-report.md'],
['chronicle-logger-timestamp','chronicle-format-spec.md'],
['backend-api-shield-services','api-hardening-patterns.md']];
for(const [sk,f] of packs){
  const p=path.join(skDir,sk,'data',f);
  ok(fs.existsSync(p),'pack exists: '+sk+'/'+f);
  ok(fs.readFileSync(path.join(skDir,sk,'SKILL.md'),'utf8').includes(f),'pointer wired: '+sk);
}
/* ---------- branding ---------- */
function walk(dir,out=[]){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p,out);else if(e.name.endsWith('.md'))out.push(p)}return out}
const mdFiles=[...walk(path.join(ROOT,'agents')),...walk(path.join(skDir)),...walk(path.join(ROOT,'commands'))];
for(const f of mdFiles){if(f.includes('google-antigravity-sdk'))continue;const t=fs.readFileSync(f,'utf8');ok(!/antigravity/i.test(t.replace(/google[\s-]*antigravity[\s-]*sdk/gi,'')),'branding clean: '+path.basename(f))}
/* ---------- catalog freshness ---------- */
const catP=path.join(ROOT,'SKILLS_CATALOG.md'),couP=path.join(ROOT,'COUNCIL.md');
const before=fs.readFileSync(catP,'utf8')+fs.readFileSync(couP,'utf8');
require('child_process').execSync('node tools/generate_catalogs.js',{cwd:ROOT,stdio:'ignore'});
const after=fs.readFileSync(catP,'utf8')+fs.readFileSync(couP,'utf8');
ok(before===after,'catalogs are generated-fresh (regeneration idempotent)');
/* ---------- adoption safety: deployers must NEVER touch editor settings or credentials ----------
   Law L-2026-08-26-01: a law without a mechanical guard is a suggestion.
   Incident: user's models + API key vanished after a repair wiped their config while our
   deploy pipeline was (correctly) innocent. These checks keep that innocence provable. */
const DEPLOYERS = ['install_system.ps1', 'npm/bin/install.js', 'plugins/majlis-bootstrap.js'];
const FORBIDDEN = [/opencode\.json/i, /auth\.json/i, /\.local[\/\\]share/i, /auth\s+login/i];
for (const rel of DEPLOYERS) {
  const t = fs.readFileSync(path.join(ROOT, rel), 'utf8');
  for (const rx of FORBIDDEN) ok(!rx.test(t), 'deployer never references settings/credential files: ' + rel + ' :: /' + rx.source + '/');
}
ok(/WRITE-GUARD/.test(fs.readFileSync(path.join(ROOT, 'plugins', 'majlis-bootstrap.js'), 'utf8')), 'bootstrap carries runtime WRITE-GUARD');
/* ---------- report ---------- */
const line='─'.repeat(46);
console.log(line);
console.log(`  MAJLIS EVAL — ${pass} PASS · ${fail} FAIL`);
console.log(line);
if(fail){F.slice(0,30).forEach(x=>console.log('  ✗ '+x));if(F.length>30)console.log('  … +'+(F.length-30)+' more');process.exit(1)}
console.log('  All structural laws hold. The council is real.');
