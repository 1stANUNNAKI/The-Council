---
description: Mandatory red-team security gate - secrets, config exposure, API defenses, manual audit - ends with SECURITY PASS/FAIL verdict
argument-hint: [--phase N | --all]
---

You are executing the Majlis Security Pipeline (no work ships without it). Scope = $ARGUMENTS or current built phase's touched files.

Run stages in order; collect evidence at each:

## Stage 1 — Secrets sweep
Load skill `trufflehog-secret-scanner`. Run `trufflehog filesystem <scope>` if available; else grep patterns: api keys, tokens (`sk-`, `ghp_`, AKIA...), private key headers, connection strings with credentials. Report file:line per hit.

## Stage 2 — Config & dependency exposure
Load skill `nuclei-security-auditor` when a live/cloud target exists. Otherwise audit configs: debug flags in prod configs, open CORS (`*`), default creds, exposed `.env`, outdated deps with known CVEs (check lockfiles).

## Stage 3 — Endpoint defenses (only when API surface changed)
Load skill `owasp-zap-api-shield` guidance. Static pass over new/changed endpoints: AuthN+AuthZ present? Input validation at boundary? Parameterized queries only? Rate limiting? CSRF on mutations? Errors leak stacks/secrets?

## Stage 4 — Human-grade audit (@sareem-security role)
Manual checklist: IDOR, path traversal, unsafe deserialization, open redirects, XSS sinks, mass-assignment.

## Verdict
Table: | Severity | Location | Issue | Fix |
Counts by CRITICAL/HIGH/MEDIUM/LOW.
Final line — exactly one of:
`SECURITY: PASS` (zero CRITICAL/HIGH) → update STATE.md gate + CHRONICLE.
`SECURITY: FAIL` → list blockers as must-fix tasks and route back to `/majlis:build` scope-fix loop.
