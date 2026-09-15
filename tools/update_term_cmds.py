import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """async function runInput(raw){
 const v=raw.toLowerCase().replace(/^\\/+/, '');
 if(v==='clear'){tb().innerHTML='';makeInputLine();return;}
 if(v==='help'){await printHelp();makeInputLine();return;}
 if(v==='agents'){await printAgents();makeInputLine();return;}
 if(v==='status'){await printStatus();makeInputLine();return;}
 if(['start','plan','build','security'].includes(v)){done.add(v);renderChips();await playScript(v);makeInputLine();return;}
 await typeCmd(raw);
 termLine('<span class="r">✖ unknown command: '+escapeHtml(raw)+'  —  try: help</span>');
 makeInputLine();
}"""

new_block = """function normalizeCmd(raw){
  let v = (raw||'').trim().toLowerCase();
  v = v.replace(/^\\/+/, '');
  v = v.replace(/^majlis:/, '');
  const aliases = {
    'ابدأ': 'start', 'تشغيل': 'start', 'شغل': 'start', 'بدء': 'start',
    'خطط': 'plan', 'تخطيط': 'plan', 'خطة': 'plan',
    'ابن': 'build', 'بناء': 'build', 'ابني': 'build',
    'أمن': 'security', 'امان': 'security', 'حماية': 'security', 'sec': 'security', 'امن': 'security',
    'مراجعة': 'review', 'نظافة': 'review', 'clean': 'review', 'كود-نظيف': 'review', 'نديف': 'review',
    'اختبار': 'qa', 'اختبارات': 'qa', 'فحص-جودة': 'qa', 'test': 'qa', 'tests': 'qa', 'باهر': 'qa',
    'فحص': 'audit', 'مخاطر': 'audit', 'تدقيق': 'audit', 'scan': 'audit', 'ثاقب': 'audit',
    'مهارات': 'skills', 'ادوات': 'skills', 'أدوات': 'skills', 'مكتبات': 'skills', 'tools': 'skills', 'skill': 'skills', 'مبتكر': 'skills',
    'حالة': 'status', 'الحالة': 'status',
    'وكلاء': 'agents', 'مقاعد': 'agents', 'seats': 'agents', 'الوكلاء': 'agents', 'المجلس': 'agents',
    'مساعدة': 'help', 'اوامر': 'help', 'أوامر': 'help', 'الأوامر': 'help', '?': 'help', '؟': 'help',
    'امسح': 'clear', 'مسح': 'clear', 'نظف': 'clear', 'cls': 'clear'
  };
  return aliases[v] || v;
}

async function runInput(raw){
  const trimmed = (raw||'').trim();
  if(!trimmed){ makeInputLine(); return; }
  const v = normalizeCmd(trimmed);
  if(v==='clear'){ tb().innerHTML=''; makeInputLine(); return; }
  if(v==='help'){ await printHelp(); makeInputLine(); return; }
  if(v==='agents'){ await printAgents(); makeInputLine(); return; }
  if(v==='status'){ await printStatus(); makeInputLine(); return; }
  if(SCR[cur] && SCR[cur][v]){
    done.add(v);
    renderChips();
    await typeCmd(trimmed);
    await playScript(v);
    makeInputLine();
    return;
  }
  await typeCmd(trimmed);
  const isEn = cur === 'en';
  termLine('<span class="r">✖ ' + (isEn ? 'unknown command: ' : 'أمر غير معروف: ') + escapeHtml(trimmed) + '</span>');
  termLine('<span class="d">  ' + (isEn ? 'supported commands: ' : 'الأوامر المدعومة: ') + '<span class="y">start, plan, build, security, review, qa, audit, skills, status, agents, help, clear</span></span>');
  termLine('<span class="b">  💡 ' + (isEn ? 'Tip: Tap "All Executable Simulation Commands" below to run or copy any command.' : 'تلميح: انقر زر "استعراض كافة الأوامر والوكلاء" أدناه لتشغيل أو نسخ أي أمر بنقرة واحدة.') + '</span>');
  makeInputLine();
}"""

old_run_cmd = """async function runCmd(k){ if(busy)return; if(k==='start'||k==='plan'||k==='build'||k==='security'){await typeCmd(k);done.add(k);renderChips();await playScript(k);makeInputLine();} }"""

new_run_cmd = """async function runCmd(k){
  if(busy) return;
  const v = normalizeCmd(k);
  if(v==='clear'){ tb().innerHTML=''; makeInputLine(); return; }
  if(v==='help'){ await printHelp(); makeInputLine(); return; }
  if(v==='agents'){ await printAgents(); makeInputLine(); return; }
  if(v==='status'){ await printStatus(); makeInputLine(); return; }
  if(SCR[cur] && SCR[cur][v]){
    await typeCmd(k);
    done.add(v);
    renderChips();
    await playScript(v);
    makeInputLine();
  }
}"""

content_norm = content.replace('\r\n', '\n')
old_block_norm = old_block.replace('\r\n', '\n')
old_run_cmd_norm = old_run_cmd.replace('\r\n', '\n')

if old_block_norm in content_norm:
    content_norm = content_norm.replace(old_block_norm, new_block)
    print('Replaced runInput successfully!')
else:
    print('old_block not found in content!')

if old_run_cmd_norm in content_norm:
    content_norm = content_norm.replace(old_run_cmd_norm, new_run_cmd)
    print('Replaced runCmd successfully!')
else:
    print('old_run_cmd not found in content!')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content_norm)
print('Done!')
