# 🍳 وصفات حركيات الواجهات المعيارية · UI Animation Recipes
### (كود تشغيلي جاهز ومختبر طبقا لفلسفة التصميم الهندسي العالمي)

تعتمد جميع الوصفات أدناه على المتغيرات القياسية المعتمدة في `:root`:
```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

---

## 1. نقرة الأزرار (Button Press Feedback)
استجابة فورية وحسية تؤكد للمستخدم أن الواجهة سمعت نقرته.
```css
.button {
  transition: transform 160ms var(--ease-out);
}

.button:active {
  transform: scale(0.97);
}
```
* **الملاحظة الفنية:** `scale()` يصغر العنصر وأيقوناته ونصوصه معاً بنسبة 3% فقط، مما يمنحه إحساساً بالنقر الفيزيائي الواقعي.

---

## 2. القوائم المنسدلة والـ Popovers
يجب أن تنبثق القائمة من الزر الذي ضغط عليه المستخدم (`transform-origin`)، وليس من الفراغ.
```css
.popover {
  transform-origin: var(--transform-origin, top right);
  transition:
    opacity 200ms var(--ease-out),
    transform 200ms var(--ease-out);
}

.popover[data-starting-style],
.popover[data-ending-style] {
  opacity: 0;
  transform: scale(0.95);
}
```

---

## 3. التولتيب التفاعلي السريع (Tooltip with Instant Neighbors)
سريع وخفيف (125ms)، وبمجرد فتح تولتيب واحد، تفتح التولتيبات المجاورة فورياً بدون تأخير.
```css
.tooltip {
  transform-origin: var(--transform-origin, bottom center);
  transition:
    transform 125ms var(--ease-out),
    opacity 125ms var(--ease-out);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* بمجرد فتح تولتيب، تصبح التولتيبات المجاورة فورية */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

---

## 4. النوافذ المنبثقة المركزية (Modal / Dialog)
النافذة الوحيدة المستثناة من نقطة الأصل، وتكون دائماً في المنتصف.
```css
.modal {
  transform-origin: center;
  transition:
    opacity 250ms var(--ease-out),
    transform 250ms var(--ease-out);
}

.modal[data-starting-style],
.modal[data-ending-style] {
  opacity: 0;
  transform: scale(0.96);
}

.modal-backdrop {
  transition: opacity 250ms var(--ease-out);
}
```

---

## 5. الأدراج والشاشات السفلية (Drawer / Bottom Sheet)
منحنى iOS الشبيه بالفيزياء الطبيعية.
```css
.drawer {
  transform: translateY(0);
  transition: transform 500ms var(--ease-drawer);
}

.drawer[data-closed] {
  transform: translateY(100%);
}
```

---

## 6. إشعارات التوست الأنيقة (Sonner-style Toast)
تتحرك بـ `ease` وتستقر بسلاسة من الأسفل للأعلى.
```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity 350ms ease,
    transform 350ms ease;

  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
}
```

---

## 7. الدخول المتتالي للقوائم (Staggered Group Entrance)
يُستخدم للقوائم التي تظهر لأول مرة، دون تعطيل تفاعل المستخدم.
```css
.item {
  opacity: 0;
  transform: translateY(8px);
  animation: itemFadeIn 300ms var(--ease-out) forwards;
}

.item:nth-child(1) { animation-delay: 0ms; }
.item:nth-child(2) { animation-delay: 40ms; }
.item:nth-child(3) { animation-delay: 80ms; }
.item:nth-child(4) { animation-delay: 120ms; }

@keyframes itemFadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

## 8. الضغط المطول للتأكيد (Hold to Confirm)
للإجراءات الخطيرة (الحذف النهائي). الحركة البطيئة تكون `linear` أثناء الضغط، وتكون سريعة وفورية `ease-out` عند الإفلات.
```css
.overlay-fill {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms var(--ease-out); /* الإفلات السريع */
}

.button:active .overlay-fill {
  clip-path: inset(0 0 0 0);
  transition: clip-path 1.8s linear;            /* الضغط المتعمد */
}

.button:active {
  transform: scale(0.97);
}
```

---

## 9. مؤشر التبويبات المتزامن دون وميض (Synced Tab Indicator)
استخدام تقنية الاقتطاع (Clipping) المتزامن بدلاً من محاولة تبديل ألوان النصوص:
```css
.tabs-active-layer {
  clip-path: inset(0 66% 0 0); /* يُدار ديناميكياً بموقع التبويب الفعال */
  transition: clip-path 220ms var(--ease-in-out);
}
```

---

## 10. إخفاء عيوب التداخل اللوني (Blur Crossfade Mask)
عند التحول بين حالتين قد تتشابكان بصرياً أثناء الانتقال، يتم استخدام بلور خفيف (2px) لدمج الحواف بسلاسة:
```css
.content-area {
  transition: filter 200ms ease, opacity 200ms ease;
}

.content-area.transitioning {
  filter: blur(2px);
  opacity: 0.8;
}
```

---

## 11. الأتمتة البرمجية عبر WAAPI (بدون مكتبات خارجية)
أداء كرت الشاشة (GPU) الكامل برمجياً دون تضخيم حجم الحزم:
```javascript
function smoothReveal(element) {
  return element.animate(
    [
      { opacity: 0, transform: 'translateY(12px) scale(0.97)' },
      { opacity: 1, transform: 'translateY(0px) scale(1)' }
    ],
    {
      duration: 250,
      easing: 'cubic-bezier(0.23, 1, 0.32, 1)',
      fill: 'forwards'
    }
  );
}
```
