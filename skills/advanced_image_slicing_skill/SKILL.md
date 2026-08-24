---
name: advanced_image_slicing_skill
description: Custom specialized skill for advanced_image_slicing_skill.
---

# مهارة تقطيع وتحريك الصور المتقدمة (Advanced Image Slicing Skill)

مهارة برمجية تتيح تفكيك صورة واحدة إلى أجزاء متعددة وتحريكها بشكل مستقل لخلق تأثيرات "انفجار" واقعية.

---

## 🛠️ التقنيات:
*   **Background Mapping:** استخدام نفس الصورة كخلفية لعدة عناصر (`divs`) مع تغيير `background-position`.
*   **Clip-Path Slicing:** استخدام مسارات CSS لقص الصورة بأشكال هندسية معقدة.
*   **Coordinate Sync:** مزامنة إحداثيات كل قطعة لتظهر كصورة واحدة عند تجميعها.

## 💻 مثال برمجى (CSS/JS):
```javascript
// تكرار الصورة في 4 قطع
const parts = document.querySelectorAll('.part');
parts.forEach((part, i) => {
    part.style.backgroundImage = `url('product.png')`;
    part.style.backgroundPosition = `${(i % 2) * 100}% ${(Math.floor(i / 2)) * 100}%`;
});
```

## 📈 معايير الأداء:
*   استخدام صورة عالية الدقة (High Res) لضمان عدم ضياع التفاصيل عند التقريب.
*   استخدام `background-size: 200%` أو أكثر حسب عدد القطع.
