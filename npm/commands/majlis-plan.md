---
description: Plan phase N - decompose into waves with mandatory verification contracts and agent assignments
argument-hint: <phase number>
---

You are running the Majlis planning workflow for the given phase. Read `.majlis/STATE.md` to resolve the target phase if $ARGUMENTS is empty.

## Step 1 — Context load
Read `.majlis/PROJECT.md`, `.majlis/ROADMAP.md` (target phase), prior phases' notes in STATE.md. If the codebase is unfamiliar, dispatch @rased-explorer for recon first (facts / conventions / blast radius / risks).

## Step 2 — Decompose into waves
Break the phase into tasks grouped in dependency WAVES:
- Max 5 tasks per wave; waves execute sequentially, tasks within a wave in parallel.
- Every task MUST carry a **verification contract** block:

```
task: <id> <title>
agents: <primary> (+ support)
touches: <glob patterns>
forbidden: <globs this task must NOT touch>
verify: <exact runnable command(s) proving success>
done_when: <observable outcome>
```

A task without a runnable `verify:` command is INVALID — either find one or split the task. No "should work" language anywhere.

## Step 3 — Conflict scan
Flag BLOCKER if two tasks in the same wave touch overlapping `touches:` globs → move one to a later wave or mark the file `sequential`.

## Step 4 — Critique pass (anti-sycophancy)
Stress-test your own plan: pre-mortem ("this failed because...") on top 3 risks + hunt implicit assumptions; rate impact/evidence; fix the plan before presenting. Verdict per task: PASS / CAUTION / REWORK.

## Step 5 — Persist
Write `.majlis/phases/P<n>-PLAN.md`, update STATE.md (status=planned), append CHRONICLE.md entry. Tell the user: run `/majlis:build` next.
