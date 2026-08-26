---
description: Council review cycle - multi-reviewer panel with anti-sycophancy rubrics, fix routing, max 3 cycles
argument-hint: [--phase N]
---

You are running the Majlis review workflow. Resolve phase from $ARGUMENTS or STATE.md (status=built).

## Panel composition (pick 2-4 reviewers by domain)
- Always: @baher-qa (verification completeness)
- Code quality: @nadif-clean-code · Backend/API: @emad-api-shield
- Architecture/diagrams when relevant: @bayan-diagrams
- Docs touched: @balegh-docs

## Anti-sycophancy contract (inject into every reviewer)
- No performative agreement; disagreement is a duty, not rudeness.
- Every finding: `file:line | what | why it matters | how to fix` + severity BLOCKER/WARNING/SUGGESTION.
- Non-overlapping rubric per reviewer (QA=verification, nadif=structure/style, emad=security/perf, balegh=clarity).
- Mandatory verdict: PASS / FAIL with blockers enumerated.

## Cycle loop (max 3)
1. Dispatch reviewers in parallel over the changed-file set (from git diff vs plan's touches).
2. Merge findings, dedupe, triage must-fix vs nice-to-have.
3. Route fixes: grouped by domain → same agent roles execute fixes (respecting forbidden globs).
4. Re-review scoped to modified files only. Record "cycle delta" each round (is it converging?).
5. Blockers persisting after 3 cycles → ESCALATE to user with history + options (fix manually / accept-as-is / investigate).

## On PASS
Run security gate `/majlis:security` if not yet run this phase. Then write `.majlis/phases/P<n>-REVIEW.md`, set status=reviewed→done after security PASS, CHRONICLE.md entry. Suggest next: `/majlis:plan <n+1>`.
