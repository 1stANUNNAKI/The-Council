# 🎯 QA Evidence Checklist — قائمة أدلة الجودة

> Data pack for `baher-qa`. Evidence-only discipline. Feelings are not evidence; raw command output is.

## Discovery (never assume)
- [ ] Detected real test framework from lockfile/config (jest·vitest·pytest·go test…)
- [ ] Located lint + typecheck commands actually used by THIS project
- [ ] Confirmed suites run locally before judging CI

## Execution order
1. Lint → capture exit code + error count
2. Types (`tsc --noEmit` / equivalent) → capture
3. Unit suites → counts passed/failed/skipped
4. Integration/e2e subset relevant to changed code

## Claim verification
- [ ] Every "done" claim traced to a runnable verify command + its output
- [ ] New behavior has a test that FAILED before the fix and PASSES after
- [ ] Coverage delta recorded (not as vanity metric — as honesty metric)

## Missing tests rule
When a task claims completion with no test:
1. Write the minimal failing test proving the claimed behavior
2. Hand it to the owning builder to make green — never fake it yourself

## Evidence block format
```
LINT   : <cmd>        exit=0   errors=0
TYPES  : <cmd>        exit=0
TESTS  : <cmd>        exit=0   passed=47 failed=0 skipped=2
COVER  : statements 82% (+3.1)
VERDICT: QA PASS — evidence attached above
```

## العربية — خلاصة
اكتشف إطار الاختبار الحقيقي للمشروع ولا تفترض ← شغّل الفحص والأنواع والاختبارات بالترتيب والتقط المخرجات الخام ← أي «انتهيت» بلا أمر تحقق يُكتب له اختبار فاشل أولاً ويُعاد لبانيه ليخضّره ← الحكم بأرقام لا بانطباعات.
