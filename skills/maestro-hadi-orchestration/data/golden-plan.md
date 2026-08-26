# 📐 The Golden Plan — نموذج الخطة الذهبية

> Data pack for `hadi-maestro`. What a PLAN LOCKED must look like. A wave table without verify contracts is rejected on sight.

## Anatomy
Every row answers three questions: WHO executes, WHAT proves it done, WHAT must finish first.

```markdown
PLAN LOCKED — billing-api · v2 waves
GOAL: Stripe webhooks become idempotent + audited

WAVE 1 (foundation)
| TASK                          | EXECUTOR            | VERIFY CONTRACT                    | DEPENDS |
|-------------------------------|---------------------|------------------------------------|---------|
| invoices table + migration    | @data-modeler       | npm run migrate && npm test db     | —       |
| idempotency-keys util         | @emad-api-shield    | npm test utils/idempotency         | —       |

WAVE 2 (integration)
| webhook handler hardening     | @emad-api-shield    | npm test billing/webhooks          | W1      |
| replay-attempt e2e test       | @test-engineer      | npm run e2e replay                 | W1      |

GATES: QA(@baher-qa) → SECURITY(@sareem-security) → CLEAN-CODE(@nadif-clean-code)
FORBIDDEN: src/legacy/** · any file matching *.bak
```

## Laws encoded above
1. Verify contracts are COMMANDS, not descriptions ("tested" is not a contract)
2. Dependencies are explicit; parallel means truly independent
3. Forbidden globs declared upfront — builders cannot plead ignorance
4. Gates named BEFORE execution starts, never improvised after

## Rejection reasons (instant)
- Any task missing VERIFY CONTRACT
- Executor is "@hadi-maestro" (conductor conducts, never plays)
- Wave mixing foundation + integration work
- No gates row

## العربية — خلاصة
الخطة جدول من موجات؛ كل مهمة فيها من ينفذها وأمر التحقق الذي يثبت نجاحها ومن يجب أن يسبقها ← عقود التحقق أوامر تشغيلية لا أوصاف ← الممنوعات تُعلن قبل التنفيذ ← البوابات تُسمّى قبل أول سطر كود وإلا فالخطة مرفوضة فوراً.
