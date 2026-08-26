# 🧼 Clean Code Review Rubric — سجل معايير نظافة الكود

> Data pack for `nadif-clean-code` review gate. Max 3 cycles; BLOCKER bounces; silence is not approval.

## Scoring rubric (score 0–2 each)
| Axis | 0 (BLOCKER) | 1 (NIT) | 2 (clean) |
|---|---|---|---|
| Naming | misleading names hide behavior | acceptable but vague | name tells the truth |
| Duplication | same logic 3+ places | small echoes | single source |
| Complexity | function does 3 jobs | long but linear | one job, obvious flow |
| Dead code | commented-out blocks shipped | unused imports | none |
| Test honesty | assertions weakened to pass | thin happy-path only | proves behavior incl. edge |

**Verdict:** any axis at 0 ⇒ `REVIEW: BLOCK` with file:line. Else APPROVE with NIT list.

## Anti-sycophancy clauses
- Vague praise ("great work!") without cited lines = invalid review
- Each BLOCKER must propose a concrete alternative phrasing
- Approval after a builder pushes changes requires re-reading the NEW diff — never carry-over trust

## Cycle limit law
Cycle 1: full review → Cycle 2: blockers only → Cycle 3: final verdict.
Unresolved after cycle 3 ⇒ escalate to @hadi-core with both positions summarized.

## العربية — خلاصة
اقرأ الفرق كاملاً قبل أي حكم ← قيّم المحاور الخمسة من صفر إلى اثنين ← أي محور صفري يعني إيقاعاً مع سطر وعمود وبديل مقترح ← المدح العام بلا أسطر مستشهدة مراجعة لاغية ← الموافقة على تعديل جديد تعيد قراءة الفرق الجديد كله ← ثلاث جولات ثم تصعيد.
