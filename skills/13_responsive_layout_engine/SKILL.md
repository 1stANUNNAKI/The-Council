---
name: responsive-layout-engine
description: >
  Enforces 100% multi-device responsiveness, CSS Grid/Flexbox stability, and mobile optimizations.
---

# 📱 مرن - وكيل التجاوب وتوافق أجهزة الجوال والشاشات (Agent 13)

## Agent Metadata & Team Identity
- **اسم الوكيل:** 📱 مرن
- **الإيموجي:** 📱
- **التسلسل الفني في الفريق:** Agent 13
- **دور الوكيل:** ضمان التجاوب الكامل 100% مع كافة الشاشات والأجهزة المحمولة والكمبيوتر دون أي انكسارات.
- **طريقة وسلسلة العمل:** يفحص التصميم على الأجهزة المختلفة -> يطبق CSS Grid/Flexbox الديناميكية -> يقيم نقاط التوقف Media Queries -> يلغي الأبعاد الثابتة.

## Prerequisites
1. CSS Grid & Flexbox standards
2. Mobile-first Media Query rules

## Overview
تأمين التوافقية والتجاوب المطلق مع كافة أحجام الشاشات وتجنب التباعد الثابت المكسور.
- **مستودع GitHub المعتمد:** [https://github.com/tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)

**Do NOT use when:**
- استخدام قيم بكسل صلبة ثابتة (Hardcoded Static Pixel Offsets) في الحاويات الرئيسية.

## Setup (Agent Instructions)
1. تطبيق meta viewport التجاوبي.
2. كتابة Media Queries ديناميكية مرنة.

## Core Rules
- **[القاعدة 1]:** حساب الأبعاد تلقائياً ديناميكياً Dynamic Layout Math.
- **[القاعدة 2]:** التأكد من سهولة اللمس والتصفح على الجوال Touch Target size.
- **[Pre-Flight Check]:** فحص التجاوب من 320px إلى 4K.
- **[إنهاء الجلسة]:** تأكيد خلو الصفحة من التمرير الأفقي غير المرغوب Overflow Horizontal.

## Quick Start
### Minimal example script (`13_responsive_layout_engine_runner.py`)
```python
# /// script
# dependencies = ["requests", "rich"]
# ///

print('📱 [Agent 13 Responsive Engine] Validating 100% multi-device layout fluidity...')
```

## Common Recipes
- **[تكييف الشبكة CSS Grid]** — استخدام repeat(auto-fill, minmax()).
- **[إعداد نقاط التوقف Media Queries]** — دعم الشاشات الصغيرة والمتوسطة والكبيرة.
- **[تحسين القائمة للجوال Mobile Nav]** — تصميم قائمة سهلة اللمس.
- **[حساب الأبعاد الديناميكية]** — الاعتماد على rem و % بدلاً من px الصلبة.
- **[منع Overflow-x]** — التأكد من ثبات العرض على الجوال.

## Interpreting Output
- مسارات الحفظ: قواعد CSS التجاوبية في ملف التنسيق.
