# ⚙️ API Hardening Patterns — أنماط تحصين الـAPI

> Data pack for `emad-api-shield`. Patterns proven in production fights. Apply before Sareem ever looks.

## Identity & access
- AuthN once at edge middleware; handlers assume identity exists
- AuthZ per-resource: `can(user, action, resource)` — never role-string checks inline
- IDOR shield: fetch resource THROUGH user relation (`user.invoices.find(id)`), never `Invoice.find(id)`
- Refresh tokens rotate on use; reuse of old token kills the family

## Input boundary
- Validate at the door with schema lib (zod/pydantic): unknown fields stripped, sizes capped
- Content-Type enforced; JSON bodies size-limited (default 100KB)
- File uploads: magic-byte check, randomized storage names, never execute paths

## Money & state
- Idempotency keys REQUIRED on POST payment/webhook routes (store key→result 24h)
- State transitions validated: `pending→paid` legal, `refunded→paid` impossible
- Ledger pattern: money moves are append-only rows, balances derived

## Failure posture
- Errors: RFC-style `{error:{code,message,details}}`; internal causes logged, never echoed
- Timeouts + retries with jitter on outbound calls; circuit breaker on repeat failures
- Rate limits: strict on auth/search/write; return Retry-After, not silent drops

## The pre-Sareem self-test
Run these five abuse probes yourself before requesting the gate:
missing-auth · wrong-owner-ID · oversized-payload · replayed-webhook · nested-$lookup-injection

## العربية — خلاصة
الهوية تُثبت عند البوابة مرة والتفويض لكل مورد على حدة مع درع IDOR عبر علاقة المستخدم نفسها ← المدخل يُصفَّر عند الباب بمخطط صارم وحجم مقفول ← أموال الدولة بحركات ملحقة فقط ومفاتيح idempotency إلزامية على ما يخص المال ← أخطاء تُسجَّل داخلياً ولا تبوح بأسبابها ← اختبر نفسك بخمس هجمات قبل أن يفتح سريم بوابته.
