# Majlis Project Rules

> This project inherits the **Majlis Council v9.3** installed globally on this machine:
> 40 agents · 90 skills · 6 governing commands · mandatory QA/security/clean-code gates.
> Governing root on this machine: `{MASTER}`

## Operating law

1. Plan before executing: multi-step requests go through `/majlis:plan` or `@hadi-maestro`; every task carries a runnable verify contract.
2. Three gates are non-negotiable before any delivery: `@baher-qa` → `@sareem-security` (binary PASS/FAIL) → `@nadif-clean-code`.
3. Recon first: `@rased-explorer` maps the blast radius before any edit.
4. Memory: `@sajeel-logger` appends to CHRONICLE.md after every multi-step task; `@hakim-mentor` distills lessons on failure.
5. Permissions are sacred: each agent obeys its declared scope; escalation goes to `@hadi-core`.

Priority: explicit user request in the current message → this file → anything else.
