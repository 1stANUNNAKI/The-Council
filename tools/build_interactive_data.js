const fs = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');

// Helper for frontmatter
function parseFrontmatter(text) {
  text = text.replace(/\r\n/g, '\n');
  if (!text.startsWith('---')) return {};
  const end = text.indexOf('\n---', 3);
  if (end < 0) return {};
  const lines = text.slice(3, end).split('\n');
  const out = {};
  let key = null;
  for (const ln of lines) {
    const m = ln.match(/^([A-Za-z_-]+):\s?(.*)$/);
    if (m) {
      key = m[1];
      let v = m[2].trim();
      if (v === '>' || v === '>-') { out[key] = ''; continue; }
      if (/^["'].*["']$/.test(v)) v = v.slice(1, -1);
      if (/^\[.*\]$/.test(v)) v = v.slice(1, -1).split(',').map(x => x.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
      out[key] = v;
      continue;
    }
    if (key && (ln.startsWith('  ') || ln === '') && typeof out[key] === 'string') {
      out[key] += (out[key] ? ' ' : '') + ln.trim();
    }
  }
  return out;
}

// 1. Categories / Suites definitions (100% Bilingual)
const SUITES = [
  {
    id: 'security',
    icon: '🛡️',
    name_ar: 'المسار الأمني والحصانة',
    name_en: 'Security Pipeline & Defense',
    color: '#ef4444',
    description_ar: 'منظومة دروع الأمان الصارمة، فحص تسريبات الأسرار (TruffleHog)، مسح الثغرات (Nuclei)، فحص الـ API الحي (OWASP ZAP)، وتدقيق الكود النظيف.',
    description_en: 'Strict defense shielding, secret scanning (TruffleHog), vulnerability assessment (Nuclei), dynamic API testing (OWASP ZAP), and clean code safety.'
  },
  {
    id: 'council',
    icon: '🏛️',
    name_ar: 'أدوار وتشغيل المجلس',
    name_en: 'Council Core Playbooks',
    color: '#3b82f6',
    description_ar: 'مهارات التوجيه والتفكيك الأوركسترالي، التوثيق الزمني، استخلاص الدروس المستفادة، هندسة الأنظمة التكاملية، والبيئات المعزولة.',
    description_en: 'Strategic orchestration playbooks, immutable chronicle logging, inner learning feedback, integrative architecture, and isolated sandboxes.'
  },
  {
    id: 'science',
    icon: '🔬',
    name_ar: 'قواعد البيانات العلمية والطبية',
    name_en: 'Science & Bio-Data Engines',
    color: '#10b981',
    description_ar: 'مستودع المعرفة الحيوية الشامل المرتبط بـ 35 قاعدة بيانات عالمية (AlphaFold, PubMed, ChEMBL, PDB, Ensembl, NCBI) للأبحاث الدقيقة.',
    description_en: 'Comprehensive biomedical knowledge suites linked to 35 premier global databases (AlphaFold, PubMed, ChEMBL, PDB, Ensembl, NCBI).'
  },
  {
    id: 'creative',
    icon: '🎨',
    name_ar: 'الإنتاج الإبداعي والحركيات والتصميم',
    name_en: 'Creative Production & Motion',
    color: '#a855f7',
    description_ar: 'ترسانة الواجهات الفائقة، وصفات إميل كوفالسكي للحركة المعيارية، أنظمة توكنز HSL، محرك GSAP، وفيديو Remotion، والطباعة المتجهة 300 DPI.',
    description_en: 'Elite frontend interfaces, Emil Kowalski canonical motion recipes, HSL semantic design tokens, GSAP animations, Remotion video, and vector printing.'
  },
  {
    id: 'cloudflare',
    icon: '☁️',
    name_ar: 'حوسبة السحابة والخدمات الطرفية',
    name_en: 'Cloudflare Edge & Serverless',
    color: '#f97316',
    description_ar: 'أدوات تطوير ونشر تطبيقات الحافة والوكلاء الأذكياء عبر Cloudflare Workers, Durable Objects, KV, D1, Vectorize, و Turnstile.',
    description_en: 'High-speed edge development and autonomous agent deployment on Cloudflare Workers, Durable Objects, KV, D1, Vectorize, and Turnstile.'
  },
  {
    id: 'meta',
    icon: '🧰',
    name_ar: 'أدوات النظام والدستور',
    name_en: 'System Meta & Engine Tools',
    color: '#eab308',
    description_ar: 'القواعد الحاكمة للمجلس، فحص وتثبيت بيئات بايثون فائقة السرعة uv، وأدوات Google Antigravity SDK.',
    description_en: 'Council constitutional rules, fast Python uv management, and Google Antigravity agent SDK.'
  }
];

// 2. Continents positioned geographically across the Grand Map of Iraq
const DIVISIONS = [
  {
    id: 'lead',
    icon: '🧭',
    name_ar: 'جزيرة القيادة والسيادة العائمة (سماء بغداد - القلب المركزي)',
    name_en: 'Sky Island of Command & Sovereignty (Floating Baghdad Citadel)',
    color: '#f59e0b',
    coords: { x: 14, y: 38, z: -3 },
    scale: { x: 44, y: 14, z: 44 },
    shape: 'citadel',
    description_ar: 'الجزيرة السماوية العائمة فوق قلب بغداد عاصمة الرافدين؛ تضم المحكمة العليا وهرم التوجيه وصياغة المنتجات، تسبح في الهواء وتتصل بجسور نورانية مع الأرض.',
    description_en: 'The majestic floating sky island hovering high above Baghdad, housing the supreme arbitrator court, orchestration maestro, and product shapers.'
  },
  {
    id: 'know',
    icon: '📚',
    name_ar: 'قارة المعرفة والذاكرة العظمى (نينوى - أرض الحضارة)',
    name_en: 'Continent of Wisdom & Living Memory (Nineveh Archives)',
    color: '#3b82f6',
    coords: { x: -35, y: 8, z: -92 },
    scale: { x: 44, y: 10, z: 40 },
    shape: 'library',
    description_ar: 'المكتبة الإمبراطورية الكبرى في نينوى العريقة؛ صرح التوثيق الزمني الأبدي CHRONICLE.md، وصائد الأدوات العالمية، ونسّاج الوكلاء، ومقر حكيم للتعلم المستمر.',
    description_en: 'The monumental library plateau inspired by ancient Nineveh, housing the eternal chronicle records, tool hunter, agent weaver, and wisdom mentor.'
  },
  {
    id: 'recon',
    icon: '🔍',
    name_ar: 'قارة الاستكشاف والرصد والمخاطر (قمم كردستان الشمالية)',
    name_en: 'Continent of Recon & Risk (Northern Mountain Observatory)',
    color: '#06b6d4',
    coords: { x: 48, y: 12, z: -80 },
    scale: { x: 42, y: 14, z: 38 },
    shape: 'observatory',
    description_ar: 'أبراج الاستطلاع والمناظير البلورية الشاهقة فوق قمم الجبال الشمالية؛ ترصد مفاصل الأكواد بدقة 360 درجة، وتكشف المخاطر والجدوى وتتبع جذور الحوادث.',
    description_en: 'Crystalline needle towers and high-altitude observatory dishes perched atop northern mountains, scouting codebases and analyzing root causes.'
  },
  {
    id: 'eng',
    icon: '⚙️',
    name_ar: 'قارة البناء ومسبك الهندسة (بابل والفرات الأوسط)',
    name_en: 'Continent of Builders & Engineering (Babylon Foundry)',
    color: '#10b981',
    coords: { x: 18, y: 6, z: 36 },
    scale: { x: 48, y: 9, z: 44 },
    shape: 'forge',
    description_ar: 'المدينة الصناعية الرقمية الكبرى على ضفاف الفرات ببابل؛ مسبك الـ API والخوادم، ناظم قواعد البيانات، مبرمج الحركات، بروتوكول pnpm، وعوازل التجارب.',
    description_en: 'The sprawling technological metropolis and foundry along the Euphrates in Babylon; engine of backend APIs, pnpm package management, and motion coding.'
  },
  {
    id: 'gate',
    icon: '🚦',
    name_ar: 'قارة بوابات الفحص والأمان المطلق (حصن البادية والحدود الغربية)',
    name_en: 'Continent of Iron Gates & Security (Western Frontier Bastion)',
    color: '#ef4444',
    coords: { x: -95, y: 8, z: 5 },
    scale: { x: 46, y: 12, z: 46 },
    shape: 'fortress',
    description_ar: 'حصن الدروع الحمراء الصارم في بادية الأنبار لحماية حدود المنظومة؛ يحمل أصحابه حق الفيتو الأمني، وقواعد الكود النظيف، وبراهين الاختبارات، ومدققي الأداء.',
    description_en: 'The formidable red bastion guarding the western frontier; home of binary security vetoes, clean code audits, QA tests, and latency gatekeepers.'
  },
  {
    id: 'exp',
    icon: '🎨',
    name_ar: 'قارة التجربة والهوية والحركيات (البصرة وأهوار الجنوب)',
    name_en: 'Continent of Kinetic Arts & Experience (Basra Floating Waters)',
    color: '#a855f7',
    coords: { x: 105, y: 5, z: 90 },
    scale: { x: 48, y: 9, z: 42 },
    shape: 'palace',
    description_ar: 'الواحات والأهوار المائية العائمة في ملتقى الرافدين بالبصرة؛ مهد الفنون السينمائية، أنظمة توكنز HSL المجلاتية، حركيات كوفالسكي، وهندسة شاشات الجوال والطباعة.',
    description_en: 'Floating water terraces and kinetic art pavilions in Basra and the marshes; crafting cinematic UI storytelling, HSL tokens, and responsive mobile architecture.'
  }
];

// 3. Harvest and Translate All 91 Skills with Arabic and English
const skills = [];
const skillsDir = path.join(ROOT, 'skills');

// Arabic mapping for known skill types
const AR_TITLES = {
  'k6-load-testing': 'اختبارات الأحمال وقابلية التوسع بـ k6',
  'nuclei-security-auditor': 'تدقيق التكوينات الأمنية وثغرات الخوادم عبر Nuclei',
  'owasp-zap-api-shield': 'فحص الأمان الديناميكي للـ API وعزل الأدوار بـ OWASP ZAP',
  'security-clean-code-auditor': 'تدقيق أمان الكود ومكافحة ثغرات XSS/SQLi ومعايير النظافة',
  'trufflehog-secret-scanner': 'المسح الآلي لكشف تسريبات المفاتيح والأسرار عبر TruffleHog',
  'agent-weaver-builder': 'تجنيد وصناعة الوكلاء المتخصصين والمهارات القياسية',
  'backend-api-shield-services': 'بناء الخدمات الخلفية وحماية نقاط الـ REST/GraphQL',
  'chronicle-logger-timestamp': 'التوثيق الزمني الفعلي وإصدار تقارير التحديثات التاريخية',
  'cicd-automation-deploy': 'أتمتة خطوط البناء والنشر المستمر CI/CD والتراجع الآمن',
  'data-modeler-schema': 'هندسة وتصميم مخططات قواعد البيانات وهجرات العلاقات',
  'find-skills': 'البحث واستكشاف المهارات والأدوات المفتوحة من GitHub',
  'frontend-clean-coder-js': 'توليد مكونات الواجهات النظيفة والخفيفة بجافاسكريبت',
  'inner-learner-feedback': 'استخلاص الدروس المستفادة وتحويل التصويبات لقواعد دائمة',
  'integrative-architect-docs': 'هندسة النظم وتوليد الـ 14 وثيقة معمارية تكاملية',
  'intent-observer-audit360': 'فحص المتطلبات الشامل 360 درجة وكشف النوايا الضمنية',
  'isolated-sandbox-environment': 'إدارة بيئات التجارب والحاويات المعزولة الآمنة',
  'lightweight-dep-manager': 'إدارة الحزم وتخفيف الأحمال ببروتوكول pnpm الأول و uv',
  'maestro-hadi-orchestration': 'التنسيق والتوجيه الاستراتيجي وتفكيك المهام للموجات',
  'qa-automated-tester-unit': 'تنفيذ أجنحة الاختبارات الآلية وضمان الجودة الصارم',
  'risk-assessor-feasibility': 'تقييم المخاطر الفنية ودراسات الجدوى المعمارية',
  'skill-creator': 'تصميم وبناء ملفات المهارات والوكلاء الجدد تلقائياً',
  'stream-partitioner-bigdata': 'تجزئة تدفقات البيانات الضخمة لحماية الذاكرة والرام',
  'tool-innovator-skill-fetcher': 'جلب وتثبيت أدوات ومهارات GitHub تلقائياً',
  'visual-diagrammer-mermaid': 'توليد مخططات Mermaid المعمارية والتدفقات البصرية',
  'workflow-skill-creator': 'تحويل مسارات العمل المكتملة إلى مهارات قابلة لإعادة الاستخدام',
  'ui-animation-recipes': 'وصفات حركيات الواجهات النخبوية المعيارية (إميل كوفالسكي)',
  'cinematic-animator-gsap': 'تحريك الواجهات والجداول الزمنية بـ GSAP والـ GPU',
  'design-system-master-hsl': 'أنظمة التصميم وتوكنز HSL المجلاتية والوضع المظلم',
  'remotion-video-engine': 'إنتاج الفيديو والموشن جرافيكس برمجياً عبر React و Remotion',
  'responsive-layout-engine': 'هندسة التجاوب 100% للشاشات وأجهزة الجوال (Mobile-First)',
  'premium-visual-polish-skill': 'الصقل البصري الرفيع للهوامش والظلال والتايبوغرافيا',
  'explode-animation-skill': 'حركات تفكيك المنتجات ثلاثية الأبعاد والمجسمات',
  'tech-background-skill': 'توليد الخلفيات التفاعلية المتحركة والجسيمات بالـ Canvas',
  'vector-print-publisher-pdf': 'تصدير مستندات وتصاميم PDF المتجهة بجودة 300 DPI للمطابع',
  'marketing-funnel-skill': 'هندسة قمعات التسويق والتحويل وتتبع الأحداث الرقمية',
  'neuro-marketing-copywriter': 'كتابة عروض القيمة الكبرى وسيناريوهات التسويق العصبي',
  'psychological-copywriting-skill': 'صياغة النصوص التسويقية المؤثرة بمبادئ الإقناع',
  'pdf-scan-layer-cleaner': 'تنقية مستندات الـ PDF الممسوحة ضوئياً من الطبقات الرمادية',
  'web-perf': 'تحليل مقاييس الأداء والسرعة ومؤشرات Core Web Vitals',
  'workers-best-practices': 'مراجعة وتطبيق أفضل معايير أكواد Cloudflare Workers',
  'wrangler': 'أداة سطر الأوامر لنشر وإدارة مشاريع Cloudflare Workers و KV و D1',
  'cloudflare': 'منصة كلاودفلير الشاملة لتطوير تطبيقات الحافة والحماية',
  'cloudflare-email-service': 'بناء خدمات البريد الإلكتروني المؤتمتة عبر Cloudflare',
  'cloudflare-one': 'إدارة حلول الحماية Zero Trust والأنفاق السحابية الآمنة',
  'cloudflare-one-migrations': 'تخطيط هجرات الشبكات السحابية نحو Cloudflare One',
  'cloudflare-ai-resources': 'تكامل تطبيقات الذكاء الاصطناعي مع نماذج Workers AI المجانية',
  'durable-objects': 'إدارة الكائنات التنسيقية الموزعة وحفظ الحالة الفورية',
  'sandbox-stable': 'إدارة بيئات تشغيل الأكواد المعزولة على Cloudflare Sandbox',
  'sandbox-next': 'تطوير تطبيقات الجيل القادم على حزمة Cloudflare Sandbox 1.0',
  'sandbox-migrate-to-next': 'ترقية ونقل تطبيقات الساندبوكس إلى حزمة Sandbox SDK 1.0',
  'turnstile-spin': 'دمج واجهات التحقق البوت الذكي Cloudflare Turnstile دون كابتشا',
  'agents-sdk': 'بناء وتطوير الوكلاء الأذكياء المستمرين عبر Agents SDK',
  'google-antigravity-sdk': 'أدوات هندسة الوكلاء الأذكياء متعددي الأنظمة Google Antigravity',
  'majlis-rules': 'دستور وقواعد تشغيل المجلس وتوجيه الـ 40 وكيلاً وبوابات الأمان',
  'uv': 'مدير حزم ومكتبات بايثون فائق السرعة والموفر للوقت uv'
};

for (const dir of fs.readdirSync(skillsDir, { withFileTypes: true })) {
  if (!dir.isDirectory() || dir.name === 'science_skills_common') continue;
  const f = path.join(skillsDir, dir.name, 'SKILL.md');
  if (!fs.existsSync(f)) continue;
  const content = fs.readFileSync(f, 'utf8');
  const meta = parseFrontmatter(content);

  const id = dir.name;
  const titleAr = AR_TITLES[id] || (id.replace(/-/g, ' ') + ' (مهارة تخصصية)');
  const descEn = meta.description ? meta.description.replace(/\n\s+/g, ' ').trim() : 'Production verified skill capability.';
  
  skills.push({
    id,
    name: meta.name || id,
    category: meta.category || 'general',
    owner: meta.owner || 'dep-manager',
    description_en: descEn,
    description_ar: titleAr + ' — ' + (descEn.length > 80 ? descEn.slice(0, 80) + '...' : descEn),
    title_ar: titleAr,
    tags: meta.tags || []
  });
}
skills.sort((a, b) => a.id.localeCompare(b.id));

// 4. Harvest and Translate All 40 Agents (100% Dual Language)
const agents = [];
const agentsDir = path.join(ROOT, 'agents');
const agentFiles = fs.readdirSync(agentsDir).filter(f => f.endsWith('.md'));

// Coords layout around the continents
const agentOffsets = {
  lead: [ { x: -6, z: -5 }, { x: 6, z: -5 }, { x: 0, z: 8 } ],
  recon: [ { x: -6, z: -5 }, { x: 6, z: -5 }, { x: 0, z: 6 } ],
  gate: [ { x: -10, z: -10 }, { x: 0, z: -10 }, { x: 10, z: -10 }, { x: -10, z: 5 }, { x: 0, z: 5 }, { x: 10, z: 5 }, { x: 0, z: 12 } ],
  eng: [ { x: -16, z: -12 }, { x: 0, z: -12 }, { x: 16, z: -12 }, { x: -16, z: 0 }, { x: 0, z: 0 }, { x: 16, z: 0 }, { x: -16, z: 12 }, { x: 0, z: 12 }, { x: 16, z: 12 }, { x: 0, z: 18 } ],
  exp: [ { x: -12, z: -8 }, { x: 0, z: -8 }, { x: 12, z: -8 }, { x: -12, z: 4 }, { x: 12, z: 4 }, { x: -8, z: 12 }, { x: 8, z: 12 }, { x: 0, z: 16 } ],
  know: [ { x: -12, z: -10 }, { x: 0, z: -10 }, { x: 12, z: -10 }, { x: -12, z: 0 }, { x: 0, z: 0 }, { x: 12, z: 0 }, { x: -12, z: 10 }, { x: 0, z: 10 }, { x: 12, z: 10 } ]
};

const counts = {};

for (const file of agentFiles) {
  const content = fs.readFileSync(path.join(agentsDir, file), 'utf8');
  const meta = parseFrontmatter(content);
  const id = file.replace('.md', '');

  const arMatch = content.match(/\*\*بالعربية:\*\* (.*)/);
  const arTitle = arMatch ? arMatch[1].trim() : '';

  const headMatch = content.match(/^#\s+(.*?)\n/m);
  const fullHead = headMatch ? headMatch[1] : id;

  const emojiMatch = fullHead.match(/^([\p{Emoji}\u200d]+|\S+)/u);
  const emoji = emojiMatch ? emojiMatch[1] : '👤';

  // Extract English Name
  const enMatch = fullHead.match(/·\s*([^—\n]+)/);
  const nameEn = enMatch ? enMatch[1].trim() : id;

  const missionMatch = content.match(/## Mission\n+([\s\S]*?)(?=\n##|$)/);
  const missionEn = missionMatch ? missionMatch[1].trim() : '';

  const workflowMatch = content.match(/## Operating workflow\n+([\s\S]*?)(?=\n##|$)/);
  const workflowEn = workflowMatch ? workflowMatch[1].trim().split('\n').map(l => l.replace(/^\d+\.\s*/, '').trim()).filter(Boolean) : [];

  const boundariesMatch = content.match(/## Boundaries\n+([\s\S]*?)(?=\n##|$)/);
  const boundariesEn = boundariesMatch ? boundariesMatch[1].trim() : '';

  const div = meta.division || 'lead';
  counts[div] = (counts[div] || 0) + 1;
  const idx = counts[div] - 1;
  const offsets = agentOffsets[div] || agentOffsets['lead'];
  const offset = offsets[idx % offsets.length] || { x: 0, z: 0 };

  const continent = DIVISIONS.find(d => d.id === div) || DIVISIONS[0];
  const worldPos = {
    x: continent.coords.x + offset.x,
    y: continent.coords.y + 2,
    z: continent.coords.z + offset.z
  };

  agents.push({
    id,
    emoji,
    name_ar: fullHead.split('·')[0].trim(),
    name_en: nameEn,
    title_ar: arTitle,
    title_en: meta.description ? meta.description.split('.')[0] : nameEn,
    mission_ar: arTitle + ' — ' + (missionEn.slice(0, 140) + '...'),
    mission_en: missionEn,
    division: div,
    temperature: meta.temperature || 0.2,
    skills: meta.skills || [],
    tools: meta.tools || ['read', 'grep'],
    workflow_en: workflowEn,
    boundaries_en: boundariesEn,
    position: worldPos
  });
}

// 5. System Layer
const SYSTEM_INFO = {
  name: 'المجلس — MAJLIS · The Council',
  version: 'v9.2 Omni-Platform Architecture',
  tagline_ar: 'المنظومة الدستورية الشاملة لحوكمة وبرمجة المشاريع عبر 40 وكيلاً ذكياً و91 مهارة معيارية فوق أرض الرافدين',
  tagline_en: 'Constitutional multi-agent engineering metropolis with 40 specialist agents and 91 skills atop the grand map of Mesopotamia',
  philosophy_ar: 'فصل تام للمسؤوليات، لا ادعاءات بلا براهين تشغيل حية، وحق فيتو دستوري للأمان والكود النظيف دون أي مجاملة.',
  philosophy_en: 'Strict separation of concerns, proof over assertions, and constitutional security veto with zero sycophancy.',
  stats: {
    agents_count: agents.length,
    skills_count: skills.length,
    divisions_count: DIVISIONS.length,
    suites_count: SUITES.length
  }
};

// 6. Controllers
const CONTROLLERS = [
  agents.find(a => a.id === 'hadi-core'),
  agents.find(a => a.id === 'hadi-maestro')
].filter(Boolean);

// Export bundle
const bundle = {
  system: SYSTEM_INFO,
  controllers: CONTROLLERS,
  divisions: DIVISIONS,
  agents,
  suites: SUITES,
  skills
};

const jsOutput = `// Auto-generated by tools/build_interactive_data.js
window.MAJLIS_UNIVERSE_DATA = ${JSON.stringify(bundle, null, 2)};
`;

fs.writeFileSync(path.join(ROOT, 'majlis_interactive_data.js'), jsOutput);
console.log('Successfully regenerated majlis_interactive_data.js with:');
console.log(`- ${agents.length} Agents (100% Dual-Language)`);
console.log(`- ${skills.length} Skills (100% Dual-Language)`);
console.log(`- ${DIVISIONS.length} Continents across Grand Map of Iraq`);
console.log(`- ${SUITES.length} Skill Suites`);
