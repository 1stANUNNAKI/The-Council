# Majlis Project Rules

> This project inherits the **Majlis Council v9.5** installed globally on this machine:
> 40 agents · 90 skills · 6 governing commands · mandatory QA/security/clean-code gates.
> Governing root on this machine: `{MASTER}`
> Core directives & rules: `{CORE_DIRECTIVES}`

## Operating law & Core Directives (النواة التوجيهية الحاكمة)

1. **الاستمرارية والتناغم والتخطيط المسبق:** تذكر دائماً كل ما تم إجراؤه لضمان تناغم التعديلات اللاحقة، ويُمنع منعاً باتاً كسر أو تخريب أي وظيفة قائمة. التخطيط الكامل يسبق أي تعديل.
2. **الأمان الوقائي الصارم (Proactive Security):** تطهير المدخلات، حماية كاملة ضد SQLi و XSS و CSRF، ولا أسرار في الكود أو السجلات؛ حكم SECURITY PASS إلزامي عبر `@sareem-security`.
3. **توجيه هادي المركزي (Hadi Auto-Routing):**
   - تصميم، معمارية، وهيكلة: `[hadi_architect]`
   - كتابة كود، أمان، وحل مشاكل: `[hadi_coder]`
   - تبسيط وشرح مفاهيم: `[hadi_mentor]`
4. **منسق الأكواد النظيفة (`@nadif-clean-code`):** مبدأ المسؤولية الواحدة (SRP)، قاعدة الـ 20 سطراً، كود يقرأ ويفسر نفسه، و Guard Clauses بدلاً من التداخل العميق.
5. **بوابات التحقق الثلاثية الإلزامية:** `@baher-qa` (lint + typecheck + tests) ← `@sareem-security` (PASS/FAIL) ← `@nadif-clean-code`.
6. **حوكمة الأرشفة والتوثيق:** إنشاء مجلدي `وثائق العمل/` و `تقارير التحديثات/`، والتوثيق الزمني الإلزامي لكل تعديل وتاريخه وساعته في `CHRONICLE.md` والدروس في `LESSONS.md`.
7. **شرح الهدف والسبب (Why before How):** تقديم شرح دقيق ومختصر لما يجب فعله بعد كل خطوة لتحسين الأداء والسرعة والتوافق. الخطط بالعربية الفصحى والأكواد بالإنجليزية.

Priority: explicit user request in the current message → this file → anything else.

