# 📝 Chronicle Format Spec — مواصفة السجل

> Data pack for `sajeel-logger`. Append-only law: corrections are NEW entries referencing old ones.

## Entry anatomy
```markdown
## [2026-08-26T14:32Z] billing idempotency hardened
CHANGE   : src/billing/webhooks.ts (+84 −12) · new migration 005_idempotency.sql
DECIDED  : ULID keys over UUIDv4 — sortable, shorter index (ruled by @hadi-core)
EVIDENCE : pytest billing/ → 31 passed · SECURITY: PASS (sareem #A17)
PRECEDENT: follows [2026-08-19T09:10Z] webhook-replay incident RCA
FILES    : list every touched path with nature (created/modified/deleted)
```

## Field laws
| Field | Law |
|---|---|
| TIMESTAMP | ISO-8601 UTC, real clock — backdating forbidden |
| CHANGE | what happened, past tense, measurable |
| DECIDED | decisions WITH their ruler — anonymous decisions invalid |
| EVIDENCE | commands + results, or link to artifact |
| PRECEDENT | optional link enabling future sessions to cite history |
| FILES | exhaustive — "misc fixes" is banned phrasing |

## Corrections
Mistake discovered? New entry: `[...ts] CORRECTS [...old-ts]: what was wrong, what is true now`.
Old entries remain untouched forever — that is the audit trail.

## العربية — خلاصة
كل مدخل: زمن حقيقي بصيغة ISO، ما تغيّر فعلاً، القرارات مع اسم حاكمها، أدلة تشغيلية، وسوابق مربوطة، وقائمة ملفات شاملة يمنع فيها «إصلاحات متفرقة» ← التصحيح مدخل جديد يشير للقديم ولا يمسّه — هذا هو أثر التدقيق الذي لا يُمحى.
