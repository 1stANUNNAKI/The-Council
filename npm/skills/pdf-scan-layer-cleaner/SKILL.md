---
name: pdf-scan-layer-cleaner
description: >
  مهارات تنظيف مستندات كتب الـ PDF الممسوحة ضوئياً من الطبقات المضللة، الخفيات الرمادية، الصور المزدوجة، ومسارات القص مع الحفاظ على النص الناصع وإمكانية البحث والنسخ دون ظهور مستطيلات سوداء.
version: 1.0.0
category: science
owner: print-publisher
tags: [ocr-layers, documents]
lang: [ar, en]
---

# مهارة تنظيف المستندات من الطبقات المضللة (PDF Scan Layer Cleaner)

## Agent Metadata & Team Identity
- **اسم الوكيل:** 🧰 مبتكر (Agent 20) / 💻 فارس (Agent 15)
- **الإيموجي:** 🧹📄
- **التسلسل الفني في الفريق:** Agent 20
- **الموقع في خط الإنتاج:** المعالجة الفنية والتجهيز المسبق للكتب والمستندات الرقمية (Pre-processing & Clean-up)
- **طريقة وسلسلة العمل:** 
  1. فحص البنية الهيكلية لتدفقات PDF (Streams).
  2. عزل وحذف تدفق صورة خلفية الورق الرمادية (`fzImg0` / `<Non-Native Art>`).
  3. الإبقاء على تدفق صورة النص الحقيقي الحاد (`fzImg1` / `<Image>`).
  4. الإبقاء على طبقة النص المخفي (`3 Tr` / `GlyphLessFont`) للبحث والتحديد بدون رسم مستطيلات سوداء.

## Prerequisites
1. تثبيت مكتبة Python PyMuPDF (`fitz`):
```bash
pip install pymupdf
```
2. وجود ملف الـ PDF الممسوح ضوئياً ذي الطبقات المتعددة.

## Overview
تُستخدم هذه المهارة عند معالجة كتب ومستندات PDF الممسوحة ضوئياً عبر برامج مثل Adobe Acrobat OCR أو FineReader والتي تُنشئ طبقتين من الصور لكل صفحة:
- **الصورة الأولى (`fzImg0` / خلفية الورق):** تظهر في Illustrator كـ `<Non-Native Art>` أو `<Clipping Path>` وتكون ذات لون رمادي أو أصفر وممتلئة بالشوائب.
- **الصورة الثانية (`fzImg1` / حبر الكلمات):** تظهر في Illustrator كـ `<Image>` وتضم النص الحقيقي الناصع.
- **طبقة OCR (`3 Tr` / `GlyphLessFont`):** خط غير مرئي لتحديد الكلمات.

**تحذير حاسم (Do NOT use when):**
- يمنع تحويل `3 Tr` إلى `0 Tr` للمستندات التي تستخدم خطوط `GlyphLessFont` لأن ذلك يؤدي لرسم مستطيلات سوداء كاملة بدلاً من الحروف.

## Setup (Agent Instructions)
1. قراءة تدفقات الصفحة (`page.get_contents()`).
2. تحديد تدفق الصورة الأولى (الخلفية الرمادية) وإفراغه عبر `doc.update_stream(xref, b'')`.
3. إعادة حفظ المستند بخيار `garbage=4, deflate=True, clean=True`.

## Core Rules
- **[قاعدة 1 - الاحتفاظ بالحبر النقائي]:** لا تحذف صورة النص `fzImg1` بل احذف فقط صورة خلفية الورق `fzImg0`.
- **[قاعدة 2 - حماية طبقة التحديد]:** اترك وضعية `3 Tr` كما هي لتوفير إمكانية النسخ والبحث دون تخريب الشكل البصري.
- **[التحقق ما قبل التشغيل Pre-Flight Check]:** افحص قيم البيكسلات بعد المعالجة وتأكد من أن المتوسط المتري يقترب من 250 (أبيض ناصع) وأن الحبر الأسود موجود ومقروء.

## Quick Start

### Minimal example script (`clean_pdf_layers.py`)
```python
import fitz
import sys

def clean_pdf_layers(input_pdf_path, output_pdf_path):
    doc = fitz.open(input_pdf_path)
    print(f"إجمالي الصفحات: {len(doc)}")
    
    for i, page in enumerate(doc):
        contents = page.get_contents()
        if len(contents) >= 3:
            # Stream 0: /fzImg0 Do (خلفية الورق الرمادية)
            first_xref = contents[0]
            first_stream = doc.xref_stream(first_xref)
            if b'fzImg0' in first_stream or b'Do' in first_stream:
                doc.update_stream(first_xref, b'')
                
                # حذف مرجع الصورة إن أمكن
                for img in page.get_images():
                    if img[7] == 'fzImg0':
                        try:
                            page.delete_image(img[0])
                        except Exception:
                            pass

    doc.save(output_pdf_path, garbage=4, deflate=True, clean=True)
    print(f"تم حفظ المستند المنظف بنجاح: {output_pdf_path}")

if __name__ == "__main__":
    clean_pdf_layers("input.pdf", "cleaned_output.pdf")
```

## Common Recipes
- **تفريغ خلفية المسح الرمادية** — لحذف الشوائب وجعل الخلفية بيضاء ناصعة 100%.
- **تسريع وتخفيض حجم الـ PDF** — تقليل الحجم دون فقدان دقة القراءة والطباعة.
- **تجهيز الكتب للعرض الرقمي والطباعة 300DPI** — إنتاج صفحات عالية الجودة جاهزة للمطابع.

## Interpreting Output
- **حجم الملف:** ينخفض الملف بشكل ملحوظ عند تنظيف المراجع أو ينخفض زمن المعالجة والتحميل بنسبة تزيد عن 90%.
- **الجودة البصرية:** صفحات بيضاء ناصعة تماماً مع حبر أسود حاد وقابلية تامة للنسخ والبحث.
