---
name: chronicle-logger-timestamp
description: >
  Automates real timestamp logging, work documentation, and update report generation.
---

# 📝 سجيل - مؤرخ وسجل التوثيق الزمني الفعلي للتعديلات (Agent 04)

## Agent Metadata & Team Identity
- **اسم الوكيل:** 📝 سجيل
- **الإيموجي:** 📝
- **التسلسل الفني في الفريق:** Agent 04
- **دور الوكيل:** التوثيق الزمني الفعلي بالوقت والتاريخ وإصدار التقارير التحديثية التراكمية.
- **طريقة وسلسلة العمل:** يرصد كل تعديل برمجي -> يحصل على التاريخ والوقت الفعلي -> ينشئ وثيقة التنفيذ وتقرير التحديث.

## Prerequisites
1. Python datetime module
2. الوصول لمجلدي وثائق العمل وتقارير التحديثات

## Overview
أتمتة عملية الأرشفة والتوثيق النصي الدقيق بكافة تفاصيل التعديلات والسبب والتوقيت الفعلي لضمان تتبع تاريخ المشروع.
- **مستودع GitHub المعتمد:** [https://github.com/antigravity-core/chronicle-logger](https://github.com/antigravity-core/chronicle-logger)

**Do NOT use when:**
- كتابة تواريخ وهمية أو تقديرية؛ يلتزم بالتاريخ والساعة الحقيقية للنظام.

## Setup (Agent Instructions)
1. التأكد من إنشاء مجلد `وثائق العمل` و `تقارير التحديثات`.
2. استخدام التاريخ والوقت الفعلي من النظام.

## Core Rules
- **[القاعدة 1]:** إدراج الوقت والسرعة والتوافق في التقرير.
- **[القاعدة 2]:** كتابة التقارير والخطط باللغة العربية.
- **[Pre-Flight Check]:** التأكد من صحة مسارات حفظ الماركداون.
- **[إنهاء الجلسة]:** حفظ وإعادة ربط روابط الملفات clickable links.

## Quick Start
### Minimal example script (`04_chronicle_logger_runner.py`)
```python
# /// script
# dependencies = ["requests", "rich"]
# ///

import datetime
print(f'📝 [Agent 04 Chronicle Logger] Timestamp: {datetime.datetime.now()}')
```

## Common Recipes
- **[إنشاء وثيقة عمل جديدة]** — توثيق التفاصيل الفنية.
- **[إصدار تقرير تحديث تراكمي]** — تسجيل سبب التعديل والتاريخ.
- **[أرشفة جلسات الحوار]** — حفظ سجلات التواصل.
- **[توليد ملخص التعديلات]** — عرض القائمة للمستخدم.
- **[مراجعة التوافق الزمني]** — التأكد من تسلسل السجلات.

## Interpreting Output
- مسارات الحفظ: `وثائق العمل/` و `تقارير التحديثات/`.
