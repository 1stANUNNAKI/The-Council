# 🛡️ Red Gate Checklist — قائمة البوابة الحمراء

> Data pack for `sareem-security`. Bilingual: English operating list, Arabic summary.
> Verdict law: **PASS ships · FAIL freezes**. No agent may overrule FAIL without a documented waiver from @hadi-core.

## 1 · Secrets sweep (TruffleHog)
- [ ] `trufflehog filesystem .` over working tree — zero verified secrets
- [ ] Full git history scanned (`git log -p | trufflehog`) — including renamed files
- [ ] Build artifacts & dist folders contain no embedded keys
- [ ] `.env*` files gitignored AND absent from history (rewrite if leaked)

## 2 · Config exposure (Nuclei / manual)
- [ ] No `DEBUG=true`, verbose stack traces, or admin panels reachable in prod config
- [ ] Security headers present: HSTS, X-Content-Type-Options, CSP baseline
- [ ] CORS: no wildcard origins paired with credentials
- [ ] Known CVEs on exposed services checked against current feed

## 3 · API defenses (ZAP-style)
- [ ] Every endpoint enforces authn **and** authz (IDOR probe on IDs)
- [ ] Input validation rejects malformed payloads at boundary (injection probes)
- [ ] Rate limiting on auth, search and write endpoints
- [ ] CSRF protection stateful flows; cookies SameSite+Secure+HttpOnly
- [ ] Error responses leak no stack traces, SQL, or internal paths

## 4 · Findings & verdict
| Grade | Meaning | Action |
|---|---|---|
| CRITICAL | exploitable now, data/money at risk | auto-FAIL, immediate bounce |
| HIGH | exploitable with preconditions | FAIL until fixed or waived |
| MEDIUM | defense-in-depth gap | fix or documented waiver |
| LOW | hygiene | backlog ticket |

**Final line format:** `SECURITY: PASS` — only when zero unresolved CRITICAL/HIGH. Otherwise `SECURITY: FAIL` + blocker table.

## العربية — خلاصة
افتحس أسرار Git بالكامل ← افحص إعدادات الإنتاج المكشوفة ← اختبر دفاعات كل نقطة API (من يدخل؟ وماذا يُدخل؟ وكم مرة؟) ← صنّف النتائج ← أصدر حكماً ثنائياً. الفشل يجمّد التسليم، ولا رفع للحكم إلا بتنازل موثق من هادي النواة.
