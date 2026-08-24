---
name: explode-animation-skill
description: Create product explosion/fragment animations: layered disassembly sequences, timing curves, and Remotion/CSS implementations.
---

# مهارة تفكيك وانفجار المنتج (Product Explosion Animation Skill)

هذه المهارة مخصصة لإنشاء تأثيرات بصرية مذهلة حيث يتفكك المنتج إلى أجزاء عند التمرير (Scroll) ويعاد تجميعه.

---

## 🛠️ القدرات التقنية:
*   **Shatter Effect:** تقسيم صورة المنتج إلى قطع (Tiles) أو أجزاء SVG.
*   **Scroll-Bound Motion:** ربط حركة كل قطعة بموضع التمرير باستخدام GSAP ScrollTrigger.
*   **3D Displacement:** تحريك القطع في فضاء ثلاثي الأبعاد (X, Y, Z) لتعزيز واقعية الانفجار.
*   **Reassembly:** إعادة تجميع المنتج بدقة 100% عند وصول المستخدم لنقطة معينة في الصفحة.

## 💻 الاستدعاء البرمجي الأساسي:
```javascript
// تقسيم المنتج إلى أجزاء
const parts = document.querySelectorAll('.product-part');

gsap.to(parts, {
  scrollTrigger: {
    trigger: ".section-explode",
    start: "top top",
    end: "+=1500",
    scrub: 1,
    pin: true
  },
  x: () => gsap.utils.random(-500, 500),
  y: () => gsap.utils.random(-500, 500),
  rotation: () => gsap.utils.random(-360, 360),
  opacity: 0.3,
  stagger: 0.01
});
```

## 📈 معايير الأداء:
1.  استخدم **SVG Paths** إذا كان المنتج عبارة عن رسم توضيحي.
2.  استخدم **Canvas API** إذا كان عدد القطع كبيراً جداً (أكثر من 100 قطعة) للحفاظ على سرعة 60fps.
3.  تأكد من تفعيل `will-change: transform` لتقليل استهلاك المعالج.
