---
name: isolated-sandbox-environment
description: >
  Manages isolated execution contexts, safe script evaluation, and container sandbox testing.
---

# 🧪 مَعْزُول - وكيل البيئات المعزولة والـ Sandbox (Agent 18)

## Agent Metadata & Team Identity
- **اسم الوكيل:** 🧪 مَعْزُول
- **الإيموجي:** 🧪
- **التسلسل الفني في الفريق:** Agent 18
- **دور الوكيل:** إدارة سياقات التشغيل المعزولة، بيئات التجربة والـ Sandbox، وحماية نظام الملفات الرئيسي.
- **طريقة وسلسلة العمل:** يعزل سياق تشغيل الأكواد الحساسة -> ينشئ البروفايلات المستقلة `--user-data-dir` -> يمنع التداخل مع تطبيقات المستخدم الأخرى.

## Prerequisites
1. Python subprocess isolation flags
2. Windows User Data Profile directories

## Overview
عزل بيئة تشغيل تطبيق سطح المكتب ومنع تشابكه مع جلسات تصفح Chrome الأخرى للمستخدم لضمان أعلى مستوى أمان واستقرار.
- **مستودع GitHub المعتمد:** [https://github.com/docker/cli](https://github.com/docker/cli)

**Do NOT use when:**
- تعديل أو استخدام ملفات النظام الحساسة خارج مجلد مساحة العمل المسموح بها.

## Setup (Agent Instructions)
1. إنشاء مجلد بروفايل مستقل في LOCALAPPDATA/AntigravityAppProfile.
2. إطلاق التطبيق بالمعلمة `--user-data-dir`.

## Core Rules
- **[القاعدة 1]:** الحفاظ على بيئة معزولة ونظيفة Isolated Context.
- **[القاعدة 2]:** تنظيف الملفات المؤقتة في مجلد scratch/ بانتظام.
- **[Pre-Flight Check]:** التأكد من صلاحيات ومسار مجلد البيئة المعزولة.
- **[إنهاء الجلسة]:** غلق وتأمين سياق التجربة.

## Quick Start
### Minimal example script (`18_isolated_sandbox_runner.py`)
```python
# /// script
# dependencies = ["requests", "rich"]
# ///

print('🧪 [Agent 18 Isolated Sandbox] Environment isolated successfully in AppData profile...')
```

## Common Recipes
- **[إنشاء بروفايل تطبيق مستقل]** — منع التداخل مع تبويبات المتصفح.
- **[إدارة مجلد التجربة scratch/]** — تشغيل السكريبتات المؤقتة بآمان.
- **[عزل متغيرات البيئة]** — حماية مفاتيح الجلسة والاعتمادات.
- **[تقييم الأكواد الحساسة]** — التشغيل داخل سياق معزول.
- **[تأمين صلاحيات نظام الملفات]** — منع الكتابة خارج النطاق.

## Interpreting Output
- مسارات الحفظ: `<appDataDir>/brain/<id>/scratch/` و `%LOCALAPPDATA%/AntigravityAppProfile`.
