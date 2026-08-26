# 🔍 Golden Recon Report — نموذج تقرير الرصد الذهبي

> Data pack for `rased-explorer` consumers (@intent-observer-audit360 workflow). Facts with paths; opinions have no seat here.

## Required sections

```markdown
RECON — <request title>
MAP
  entry points : server.ts:12 · worker.ts:3
  feature home : src/billing/* (7 files)
  shared utils : src/lib/http.ts (used by 11 modules)
CONVENTIONS (observed, not preferred)
  framework    : FastAPI + SQLAlchemy 2.0 style
  naming       : snake_case routes, PascalCase models
  testing      : pytest, fixtures in tests/conftest.py
BLAST RADIUS (if we change billing/)
  direct   : 9 files
  indirect : 3 importers (src/api/router.ts, jobs/invoice.ts, admin/report.ts)
  migrations: 1 pending (004_add_tax.py) — unapplied
HIDDEN COUPLING
  config key BILLING_WEBHOOK_SECRET read in 2 places, set nowhere in repo
  circular risk: billing ↔ accounts (import cycle via types only — safe today)
OPEN QUESTIONS FOR PLANNER
  1. apply pending migration first? (blocks W1)
  2. who owns webhook secret provisioning?
```

## Quality bar
- Every claim carries `file:line` or directory evidence
- Conventions reported AS FOUND — recommending comes later, elsewhere
- Open questions section hands the planner real decisions, not filler

## العربية — خلاصة
خريطة نقاط الدخول وموطن الخاصية والعادات المشتركة ← العادات تُنقل كما وُجدت لا كما نحب ← نطاق الانفجار مباشراً وغير مباشر وهجرات معلقة ← اقترانات خفية ومفاتيح إعدادات يتيمة ← أسئلة مفتوحة حقيقية تسلَّم للمخطِّط قراراً لا حشواً.
