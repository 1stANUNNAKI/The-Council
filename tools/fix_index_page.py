import re

html_path = 'index.html'
content = open(html_path, encoding='utf-8').read()

# 1. Update layout widths (Side margins reduction across the entire page)
content = content.replace(
    ".wrap{max-width:1180px;margin:auto;padding:0 clamp(18px,4vw,44px)}",
    ".wrap{max-width:1440px;margin:auto;padding:0 clamp(16px,2.5vw,40px)}"
)
content = content.replace(
    "section{max-width:1180px;margin:0 auto;padding:clamp(40px,8vw,96px) 0}",
    "section{max-width:1440px;margin:0 auto;padding:clamp(40px,6vw,90px) 0}"
)
content = content.replace(
    ".sub{color:var(--dim);margin-bottom:38px;max-width:820px;font-size:1.14rem;line-height:1.9}",
    ".sub{color:var(--dim);margin-bottom:38px;max-width:980px;font-size:1.15rem;line-height:1.9}"
)
content = content.replace(
    ".tag{max-width:760px;margin:auto;color:var(--dim);font-size:1.22rem;line-height:1.95;opacity:0;transform:translateY(18px);transition:.9s .2s}",
    ".tag{max-width:920px;margin:auto;color:var(--dim);font-size:1.22rem;line-height:1.95;opacity:0;transform:translateY(18px);transition:.9s .2s}"
)
content = content.replace(
    ".grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(258px,1fr));gap:22px}",
    ".grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:24px}"
)
content = content.replace(
    ".cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:16px}",
    ".cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}"
)
content = content.replace(
    ".pipe{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}",
    ".pipe{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px}"
)
content = content.replace(
    ".final p{color:#d3cdbd;max-width:600px;margin:0 auto 34px;font-size:1.14rem;line-height:1.9}",
    ".final p{color:#d3cdbd;max-width:780px;margin:0 auto 34px;font-size:1.15rem;line-height:1.9}"
)

# 2. Make the transparent top bar larger, taller, and more luxurious
old_nav_css = """/* NAV */
nav{position:sticky;top:0;z-index:70;backdrop-filter:blur(20px) saturate(1.8);-webkit-backdrop-filter:blur(20px) saturate(1.8);background:rgba(250,247,240,.45);border-bottom:1px solid rgba(233,225,207,.6);transition:box-shadow .3s,background .3s}
nav.scrolled{background:rgba(250,247,240,.75);box-shadow:0 10px 34px -22px rgba(40,33,12,.35)}
nav .in{display:flex;justify-content:space-between;align-items:center;padding:15px 0;gap:20px}
.brand{display:flex;gap:12px;align-items:center;font-weight:800;font-size:1.12rem;letter-spacing:-.01em;font-family:'Sora',sans-serif}
body[dir=rtl] .brand{font-family:'Amiri',serif;font-weight:700}
.brandmark{width:34px;height:34px;border-radius:10px;background:var(--ink);display:grid;place-items:center;color:var(--gold);box-shadow:inset 0 0 0 2px var(--gold-soft)}
.brand b{color:var(--gold-ink)}
.navlinks{display:flex;gap:4px;align-items:center}
.navlinks a{color:var(--dim);font-size:.98rem;font-weight:500;padding:9px 14px;border-radius:10px}
.navlinks a:hover{color:var(--ink);background:var(--bg2)}
.gh{display:inline-flex;gap:8px;align-items:center;border:1px solid var(--line2);padding:9px 16px;border-radius:12px;font-weight:600;color:var(--ink)!important}
.gh:hover{background:var(--bg2);transform:translateY(-1px)}
.actions{display:flex;gap:10px;align-items:center}
#langBtn{display:inline-flex;gap:9px;align-items:center;background:var(--bg2);border:1px solid var(--line2);color:var(--ink);padding:9px 16px;border-radius:12px;cursor:pointer;font-weight:600;font-family:inherit;font-size:.94rem;transition:.18s}
#langBtn:hover{border-color:var(--gold)}
#langBtn .dot-lg{width:9px;height:9px;border-radius:50%;background:var(--gold);display:inline-block}
.cta-nav{display:inline-flex;gap:8px;align-items:center;background:var(--ink);color:var(--bg);padding:10px 18px;border-radius:12px;font-weight:700;font-size:.94rem;font-family:inherit}
.cta-nav:hover{transform:translateY(-1px);box-shadow:var(--shadow-sm)}
.cta-nav i{color:var(--gold-soft)}"""

new_nav_css = """/* NAV */
nav{position:sticky;top:0;z-index:70;backdrop-filter:blur(24px) saturate(1.8);-webkit-backdrop-filter:blur(24px) saturate(1.8);background:rgba(250,247,240,.72);border-bottom:1px solid rgba(233,225,207,.85);transition:box-shadow .3s,background .3s;padding:6px 0}
nav.scrolled{background:rgba(250,247,240,.92);box-shadow:0 14px 40px -20px rgba(40,33,12,.35)}
nav .in{display:flex;justify-content:space-between;align-items:center;padding:18px 0;gap:24px}
.brand{display:flex;gap:14px;align-items:center;font-weight:800;font-size:1.24rem;letter-spacing:-.01em;font-family:'Sora',sans-serif}
body[dir=rtl] .brand{font-family:'Amiri',serif;font-weight:700}
.brandmark{width:44px;height:44px;border-radius:12px;background:var(--ink);display:grid;place-items:center;color:var(--gold);box-shadow:inset 0 0 0 2px var(--gold-soft)}
.brand b{color:var(--gold-ink)}
.navlinks{display:flex;gap:6px;align-items:center}
.navlinks a{color:var(--dim);font-size:1.02rem;font-weight:600;padding:11px 18px;border-radius:12px}
.navlinks a:hover{color:var(--ink);background:var(--bg2)}
.gh{display:inline-flex;gap:8px;align-items:center;border:1px solid var(--line2);padding:10px 18px;border-radius:12px;font-weight:600;color:var(--ink)!important;font-size:1.0rem}
.gh:hover{background:var(--bg2);transform:translateY(-1px)}
.actions{display:flex;gap:12px;align-items:center}
#langBtn{display:inline-flex;gap:10px;align-items:center;background:var(--bg2);border:1px solid var(--line2);color:var(--ink);padding:11px 18px;border-radius:12px;cursor:pointer;font-weight:600;font-family:inherit;font-size:1.0rem;transition:.18s}
#langBtn:hover{border-color:var(--gold)}
#langBtn .dot-lg{width:9px;height:9px;border-radius:50%;background:var(--gold);display:inline-block}
.cta-nav{display:inline-flex;gap:10px;align-items:center;background:var(--ink);color:var(--bg);padding:12px 24px;border-radius:12px;font-weight:700;font-size:1.02rem;font-family:inherit;cursor:pointer;transition:transform .2s,box-shadow .2s}
.cta-nav:hover{transform:translateY(-2px);box-shadow:var(--shadow)}
.cta-nav i{color:var(--gold-soft)}"""

assert old_nav_css in content, "old_nav_css not found!"
content = content.replace(old_nav_css, new_nav_css)

# 3. Fix terminal styling and visibility
old_term_css = """.termwrap{position:relative;opacity:0;transform:translateY(22px);transition:.9s}
.termwrap.in{opacity:1;transform:none}
.term{background:var(--ink);border:1px solid #2d2717;border-radius:22px;overflow:hidden;font-family:'JetBrains Mono',monospace;font-size:.92rem;color:#ddd9cd;box-shadow:var(--shadow)}
.term .bar{display:flex;gap:7px;padding:15px 20px;background:#1d1910;border-bottom:1px solid #2d2717;align-items:center}
.dot{width:11px;height:11px;border-radius:50%}
.term .bar span.ttl{margin-inline-start:14px;color:#8f8877;font-family:'Inter',sans-serif;font-size:.8rem;letter-spacing:.02em}
.tbody{padding:22px 24px;line-height:1.95;min-height:300px;max-height:430px;overflow:hidden;direction:ltr;text-align:left;font-size:.92rem;scroll-behavior:smooth}"""

new_term_css = """.termwrap{position:relative;opacity:1;transform:none;transition:opacity .6s ease,transform .6s ease}
.termwrap.in{opacity:1;transform:none}
.term{background:#110e08;border:1px solid #382e1b;border-radius:24px;overflow:hidden;font-family:'JetBrains Mono',monospace;font-size:.94rem;color:#ddd9cd;box-shadow:0 24px 60px -20px rgba(0,0,0,.45)}
.term .bar{display:flex;gap:8px;padding:16px 24px;background:#1b160d;border-bottom:1px solid #382e1b;align-items:center}
.dot{width:12px;height:12px;border-radius:50%}
.term .bar span.ttl{margin-inline-start:16px;color:#a89d87;font-family:'JetBrains Mono',monospace;font-size:.86rem;letter-spacing:.02em}
.tbody{padding:26px 28px;line-height:2.0;min-height:340px;max-height:460px;overflow-y:auto;overflow-x:hidden;direction:ltr;text-align:left;font-size:.94rem;scroll-behavior:smooth}"""

assert old_term_css in content, "old_term_css not found!"
content = content.replace(old_term_css, new_term_css)

# Update HTML for termwrap
content = content.replace('<div class="termwrap" id="termwrap">', '<div class="termwrap in reveal" id="termwrap">')

# 4. Enhance renderChips to add a dedicated Run button
old_chips_code = """function renderChips(){
 const d=t();
 $('chips').innerHTML=d.cmdsT.map(k=>
   `<button class="chip ${done.has(k)?'done':''}" onclick="runCmd('${k}')">${done.has(k)?'done':'▶'} ${k}</button>`).join('')+
   `<button class="chip" onclick="resetTerm()">${d.reset}</button>`;
}"""

new_chips_code = """function renderChips(){
 const d=t();
 const runPrompt = cur==='en' ? '▶ Run Demo: start' : '▶ شغّل المحاكاة: start';
 $('chips').innerHTML=
   `<button class="chip" style="background:var(--ink);color:var(--bg);font-weight:700;border-color:var(--gold);" onclick="runCmd('start')">${runPrompt}</button>`+
   d.cmdsT.map(k=>
     `<button class="chip ${done.has(k)?'done':''}" onclick="runCmd('${k}')">${done.has(k)?'✓':'▶'} ${k}</button>`).join('')+
   `<button class="chip" onclick="resetTerm()">${d.reset}</button>`;
}"""

assert old_chips_code in content, "old_chips_code not found!"
content = content.replace(old_chips_code, new_chips_code)

# 5. Add bindRunButtons function so clicking "شغّله" or "Run it" scrolls to terminal AND triggers runCmd('start')
old_init_code = """render();
initTerminalWelcome();
heroIn();
setTimeout(()=>{runCounters();},500);"""

new_init_code = """function bindRunButtons(){
  document.querySelectorAll('.cta-nav, #cta1, #fin_c1').forEach(btn=>{
    btn.addEventListener('click', (e)=>{
      e.preventDefault();
      const demoSec=document.getElementById('demo');
      if(demoSec){
        demoSec.scrollIntoView({behavior:'smooth'});
        setTimeout(()=>{
          if(!busy){
            runCmd('start');
          }
        }, 400);
      }
    });
  });
}

render();
initTerminalWelcome();
heroIn();
setTimeout(()=>{runCounters();},500);
bindRunButtons();"""

assert old_init_code in content, "old_init_code not found!"
content = content.replace(old_init_code, new_init_code)

open(html_path, 'w', encoding='utf-8').write(content)
print("Successfully updated index.html with wide layouts, larger navbar, visible terminal, and interactive run button!")
