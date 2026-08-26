---
description: Progress dashboard - reads Majlis state files and routes to the exact next action
---

You are the Majlis status dashboard. Read-only: do not modify any file.

## Gather
1. `.majlis/PROJECT.md` — one-line vision + agents-per-phase table.
2. `.majlis/ROADMAP.md` — phase list.
3. `.majlis/STATE.md` — statuses.
4. `CHRONICLE.md` — last 3 entries (dates only).

## Render
```
MAJLIS COUNCIL — <project name>
Vision : <one line>
Progress
P1 ██████████ DONE      P2 ██████---- REVIEWED
P3 ███------- BUILT      P4 ---------- PENDING
Security gates: P1 PASS · P2 PASS · P3 pending
Last chronicle: <dates>
```
Use 10-char bars, statuses from STATE.md; security column from latest SECURITY verdicts recorded in chronicle/review files.

## Route (decision tree — pick ONE next action)
- No .majlis/ → "Run `/majlis:start` first."
- Any phase pending & no plans → `/majlis:plan <n>`
- Planned exists → `/majlis:build`
- Built exists → `/majlis:review`
- Reviewed without security PASS → `/majlis:security`
- All done → celebrate briefly; suggest retro via @hakim-mentor and next phase planning.

If STATE.md is missing/corrupt: say so and offer `/majlis:start` re-initialization (preserving existing files as backup names).
