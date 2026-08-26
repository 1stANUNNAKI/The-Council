/* build_npm.js — release pipeline: sync repo-root assets INTO npm/ so the
   published tarball is self-contained. Run before every `npm publish`.
   Usage: node tools/build_npm.js */
const fs=require('fs'),path=require('path');
const ROOT=path.join(__dirname,'..');
const NPM=path.join(ROOT,'npm');
const cp=(src,dst)=>{fs.rmSync(dst,{recursive:true,force:true});fs.cpSync(src,dst,{recursive:true})};
let copied={};
/* skills minus excluded */
const EX=new Set(['science_skills_common']);
fs.rmSync(path.join(NPM,'skills'),{recursive:true,force:true});
fs.mkdirSync(path.join(NPM,'skills'));
let sk=0;
for(const d of fs.readdirSync(path.join(ROOT,'skills'),{withFileTypes:true})){
  if(!d.isDirectory()||EX.has(d.name))continue;
  if(!fs.existsSync(path.join(ROOT,'skills',d.name,'SKILL.md')))continue;
  cp(path.join(ROOT,'skills',d.name),path.join(NPM,'skills',d.name));sk++;
}
copied.skills=sk;
for(const [name,filter] of [
  ['agents',f=>f.endsWith('.md')],
  ['commands',f=>f.startsWith('majlis-')&&f.endsWith('.md')],
  ['templates',()=>true]
]){
  cp(path.join(ROOT,name),path.join(NPM,name));
  copied[name]=fs.readdirSync(path.join(NPM,name)).length;
}
fs.mkdirSync(path.join(NPM,'plugins'),{recursive:true});
fs.copyFileSync(path.join(ROOT,'plugins','majlis-bootstrap.js'),path.join(NPM,'plugins','majlis-bootstrap.js'));
for(const f of ['AGENTS.md','VERSION.txt','USAGE_EN.md','USAGE_AR.md','USAGE_ZH.md','README.md'])
  fs.copyFileSync(path.join(ROOT,f),path.join(NPM,f));
/* sync version + modern description into package.json */
const ver=fs.readFileSync(path.join(ROOT,'VERSION.txt'),'utf8').trim();
const pjPath=path.join(NPM,'package.json');
const pj=JSON.parse(fs.readFileSync(pjPath,'utf8'));
pj.version=ver;
pj.description=`MAJLIS - The Council: one command installs a disciplined council of 40 real AI agents + 90 curated trilingual skills into OpenCode, Claude Code, Codex, Gemini CLI and 26+ more platforms. Mandatory QA/security gates. MIT.`;
pj.engines={node:'>=18'};
pj.files=['bin/install.js','skills/','agents/','commands/','templates/','plugins/majlis-bootstrap.js','AGENTS.md','VERSION.txt','USAGE_EN.md','USAGE_AR.md','USAGE_ZH.md','README.md'];
fs.writeFileSync(pjPath,JSON.stringify(pj,null,2)+'\n');
console.log('npm package synced:',JSON.stringify(copied),'version='+ver);
