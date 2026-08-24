---
description: Initialize a Majlis project - guided questioning then generate PROJECT.md, ROADMAP.md and STATE.md
argument-hint: [project vision, optional]
---

You are orchestrating the Majlis Council initialization workflow.

## Phase 1 — Intake
If $ARGUMENTS is empty, ask the user (one question at a time, max 7 exchanges total):
1. What are we building? (vision in 2 sentences)
2. Who is it for + top 3 requirements?
3. Hard constraints? (stack, deadline, budget, integrations)
4. Definition of done for v1?

If arguments were provided, treat them as the vision and confirm missing pieces in ONE message.

## Phase 2 — Council sizing
Recommend 2-4 council agents per upcoming phase from this roster, with one-line justification:
- Planning: @hadi-maestro · Analysis: @rased-explorer · Backend/API: @emad-api-shield
- QA gates: @baher-qa · Security: @sareem-security · Diagrams: @bayan-diagrams
- Docs: @balegh-docs · Clean-code gate: @nadif-clean-code · Tools: @mubtakir-tools
- Chronicle: @sajeel-logger · Lessons: @hakim-mentor

## Phase 3 — Generate artifacts (directory `.majlis/`)
1. `PROJECT.md` — Vision / Requirements / Constraints / Agents-per-phase table.
2. `ROADMAP.md` — Phases P1..Pn; each phase = outcome sentence + bullet deliverables.
3. `STATE.md` — table: | phase | status (pending/planned/built/reviewed/done) | notes |. Set all pending.
4. Append an entry to `CHRONICLE.md`: project initialized (date + decisions).

## Phase 4 — Handoff
Show the user a compact summary and say: run `/majlis:plan 1` next.
