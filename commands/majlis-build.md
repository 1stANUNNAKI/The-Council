---
description: Execute current phase wave by wave - agents work in parallel honoring verification contracts
argument-hint: [--phase N]
---

You are running the Majlis build workflow. Resolve the phase from $ARGUMENTS or `.majlis/STATE.md` (first phase with status=planned).

## Execution rules
1. Read `.majlis/phases/P<n>-PLAN.md`. Validate every task has a `verify:` command; refuse to start and route back to `/majlis:plan` if any is missing.
2. Process waves sequentially. Within a wave, dispatch tasks in parallel:
   - If your runtime supports subagents/Task tool: spawn the assigned council agent (@emad-api-shield for backend, @baher-qa for tests, etc.) with the task block as its brief.
   - Otherwise: assume each agent's role yourself, one task at a time, stating `[role] executing`.
3. Each agent follows its own protocol (security non-negotiables for backend, evidence-only for QA...).
4. After each task: run its `verify:` command EXACTLY as written. Capture exit code + key output.
5. A task is DONE only when verify passes. On failure: fix within the same task scope (max 2 attempts), then escalate to user with findings.
6. Never touch `forbidden:` globs. Respect `sequential:` files — serialize those tasks even inside a wave.

## Wrap-up per wave
- Append results table to `.majlis/phases/P<n>-SUMMARY.md`: | task | agents | verify result | notes |
- Atomic git commit per completed wave (if repo): message = `majlis(P<n>): wave <k> - <summary>`
- Update STATE.md (status=built when last wave done), append CHRONICLE.md.

Handoff: "Run `/majlis:review` now." Security-sensitive changes also route @sareem-security before review.
