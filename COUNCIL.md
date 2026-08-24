# 🏛️ كتالوج المجلس الكامل — Council Roster (40)

> مولَّد آلياً من ملفات الوكلاء الحقيقية — لا يدوى هنا. لكل وكيل: اسمه، فريقه، دوره، ومهارته المرجعية.

> Auto-generated from the actual agent files. Every seat: identity, team, mandate, reference skill.

## 1. القيادة والاستراتيجية — Command & Strategy (3)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@hadi-core` | محرك هادي المركزي | Supreme council brain (Hadi Core). Arbitrates escalations, resolves cross-agent conflicts, and owns final strategic calls. Use when normal flows stall, agents disagree, or a decision exceeds Maestro's authority. | `maestro-hadi-orchestration` |
| 2 | `@hadi-maestro` | مايسترو هادي | Strategic orchestrator (Agent 01 - Maestro Hadi). Plans complex tasks, decomposes them into agent-legion work packages, and routes each package to the right subagent or skill. Use for multi-step features, ambiguous requests, and project-level planning. | — |
| 3 | `@product-shaper` | صانع المنتج | Product shaper. Turns vague ideas into sharp PRDs, user stories and acceptance criteria. Use when requirements are vague or a feature needs product definition. | — |

## 2. الاستطلاع والمخاطر — Recon & Risk (3)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@incident-detective` | محقق الحوادث | Incident detective. Root-cause analysis for failures and regressions, blameless style. Use when something broke and symptoms hide the cause. | — |
| 2 | `@rased-explorer` | راصد | 360-degree codebase explorer (Agent 03 - Rased). Fast read-only reconnaissance: structure, conventions, dependencies, entry points, blast radius of a change. Use at the start of any task touching unfamiliar code. | — |
| 3 | `@risk-assessor` | ثاقب | Risk assessor (Thaqib). Technical feasibility studies, risk matrices and go/no-go input. Use when before committing to risky designs or new dependencies/platforms. | `risk-assessor-feasibility` |

## 3. الهندسة — Engineering (9)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@cicd-automator` | مُستَمِر | CI/CD automator (Mustamir). Builds and hardens continuous integration/deployment pipelines. Use when builds, releases, pipelines or deployment automation are touched. | `cicd-automation-deploy` |
| 2 | `@data-engineer` | بيانات | Data engineer & science-database router (Bayanaat). Routes bio/chem/data queries across ~40 database skills. Use when scientific data retrieval or ETL-style data engineering is needed. | — |
| 3 | `@data-modeler` | ناظم | Data modeling engineer (Naadem). Designs schemas, ERDs and normalized relation models. Use when databases, schemas or entity relationships are involved. | `data-modeler-schema` |
| 4 | `@dep-manager` | جاسر | Lightweight dependency manager (Jaasir). Audits, prunes and pins project dependencies. Use when dependencies are added, bloated, flagged or audited. | `lightweight-dep-manager` |
| 5 | `@emad-api-shield` | عماد | Backend/API engineer (Agent 16 - Emad). Implements and hardens server-side services: auth, validation, rate limiting, parameterized queries, secure error handling. Use for API endpoints and backend changes. | — |
| 6 | `@integrative-architect` | معمار | Integrative architect (Memar). Produces integration requirement docs and architecture blueprints. Use when new integrations, system boundaries or architecture docs are needed. | `integrative-architect-docs` |
| 7 | `@motion-coder` | فارس | Motion coder (Faaris). Implements Remotion compositions and FFmpeg assembly pipelines. Use when animations must become code or videos must be rendered/assembled. | `remotion-video-engine` |
| 8 | `@sandbox-isolator` | مَعْزُول | Sandbox isolator (Ma'zool). Runs risky code in isolated environments and contains blast radius. Use when untrusted code, destructive experiments or isolation is needed. | `isolated-sandbox-environment` |
| 9 | `@stream-partitioner` | مُقَسِّم | Big-data stream partitioner (Muqassim). Chunks large payloads and pipelines for memory-safe processing. Use when files/streams exceed comfortable memory or need batch pipelines. | `stream-partitioner-bigdata` |

## 4. الجودة والأمن — Quality & Security (7)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@a11y-auditor` | مدقق الوصولية | Accessibility auditor. Audits WCAG compliance, keyboard nav and semantic markup. Use when UI changes ship or accessibility complaints appear. | — |
| 2 | `@baher-qa` | باهر | QA and automated testing agent (Agent 19 - Baher). Discovers and runs lint/typecheck/tests, writes missing tests, and reports pass/fail evidence. Use to verify any change before it is considered done. | — |
| 3 | `@code-polisher` | مُصفّق الكود | Code polisher. Runs multi-pass cleanup: comments, simplification, readability, consistency. Use when after review passes and before shipping polish-sensitive work. | — |
| 4 | `@nadif-clean-code` | ندیف | Clean-code gatekeeper (Council Agent - Nadif). Final architectural review before acceptance: naming, structure, duplication, dead code, conventions adherence. Use as the last pass after QA and security. | — |
| 5 | `@perf-auditor` | مدقق الأداء | Performance auditor. Profiles hot paths, load-tests endpoints and tracks Core Web Vitals. Use when latency, throughput or bundle/load performance is questioned. | `k6-load-testing` |
| 6 | `@sareem-security` | صارم | Security auditor (Agent 22 - Sareem). Read-only offensive review: secrets leakage, SQLi/XSS/CSRF, auth flaws, dependency CVEs, config hardening. Use before any completion claim and on every security-sensitive change. | — |
| 7 | `@test-engineer` | مهندس الاختبار | Test engineer. Writes unit/integration/e2e suites following the project's existing framework. Use when coverage gaps or new test suites are needed. | `qa-automated-tester-unit` |

## 5. التجربة والهوية — Experience & Identity (7)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@bayan-diagrams` | بَيَان | Visual data storyteller (Agent 08 - Bayan). Produces Mermaid diagrams: architecture, ERD, sequence, flowchart, state. Use whenever relationships or flows need visualization in docs. | — |
| 2 | `@brand-guardian` | حارس العلامة | Brand guardian. Enforces voice, tone and visual identity consistency across outputs. Use when public-facing copy, identity assets or naming changes. | — |
| 3 | `@design-system-master` | رَفَل | Design-system master (Raffal). Owns tokens, dark modes, Shadcn/HSL palettes and magazine-grade identity. Use when UI identity, palettes, themes or design tokens change. | `design-system-master-hsl` |
| 4 | `@growth-analyst` | محلل النمو | Growth analyst. Designs funnels, experiments and conversion tracking wiring. Use when adoption, conversion or analytics instrumentation is discussed. | `marketing-funnel-skill` |
| 5 | `@print-publisher` | مَطْبُوع | Vector print publisher (Matboo). Produces print-ready vector PDFs and 300DPI layouts. Use when print/PDF/high-DPI output is required. | `vector-print-publisher-pdf` |
| 6 | `@responsive-layout` | مرن | Responsive layout engine (Murun). Guarantees multi-device correctness of layouts. Use when layouts, breakpoints or mobile behavior are touched. | `responsive-layout-engine` |
| 7 | `@ux-researcher` | باحث التجربة | UX researcher. Applies usability heuristics, journey maps and friction analysis. Use when user flows, onboarding or UI decisions need evidence. | — |

## 6. المعرفة والتشغيل — Knowledge & Ops (9)

| # | المعرف ID | الاسم | الدور Role | المهارة المرجعية |
|---|-----------|--------|-------------|------------------|
| 1 | `@agent-weaver` | مُجَنِّد / نَسَّاج | Agent weaver and recruiter. Creates new subagents and SKILL.md skills following platform validation rules. Use when a capability gap needs a new specialist or reusable skill. | `skill-creator` |
| 2 | `@balegh-docs` | بَليغ | Eloquent technical writer (Council Agent - Balegh). Produces bilingual (EN/AR) documentation, release notes, README sections, and announcement copy from real diffs. Use for docs tasks and launch materials. | — |
| 3 | `@context-steward` | أمين السياق | Context steward. Maintains the compressed knowledge index and context budgets of the Council. Use when sessions feel heavy or retrieval misses occur. | `majlis-rules` |
| 4 | `@hakim-mentor` | حكيم | Inner learner and retrospective agent (Agent 05 - Hakim). Extracts lessons learned from completed tasks, updates LESSONS.md patterns, and suggests system/process improvements. Use at milestones and post-incidents. | — |
| 5 | `@mubtakir-tools` | مبتكر | Tool innovator and skill fetcher (Council Agent 20 - Mubtakir). Searches GitHub/npm/skill registries for existing tools before building new ones, evaluates candidates, installs and wires the best fit. Use when a capability is missing. | — |
| 6 | `@portfolio-steward` | أمين المشاريع | Portfolio steward. Cross-project dashboard: health, dependencies and agent allocation. Use when managing several Majlis projects at once. | `maestro-hadi-orchestration` |
| 7 | `@prompt-smith` | صائغ الأوامر | Prompt smith. Forges and refines agent prompts, skill playbooks and command definitions. Use when an agent underperforms or a new playbook is drafted. | `skill-creator` |
| 8 | `@sajeel-logger` | سجيل | Chronicle historian (Agent 04 - Sajeel). Documents what was actually changed: timestamped entries of modifications, decisions, files touched, and verification results into CHRONICLE.md. Use after completing any multi-step task. | — |
| 9 | `@voice-engineer` | صوت | Voice engineer (Sawt). Handles TTS, narration and audio production pipelines. Use when voice-over, narration or audio assets are required. | — |

---

**المجموع Total: 40 وكيل حقيقي real subagents** — مدقَّق آلياً (709 فحوص).
