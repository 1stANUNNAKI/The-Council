---
name: tech-background-skill
description: Generate animated technical backgrounds (circuits, grids, particles) as CSS canvas or video assets for hero sections.
version: 1.0.0
category: creative
owner: cinematic-director
tags: [visual, production]
lang: [en, ar]
---

# مهارة الخلفيات التقنية المتحركة (Tech Background Skill)

خلق بيئة بصرية غامرة تعبر عن التكنولوجيا المتقدمة والذكاء الاصطناعي.

---

## 🌌 العناصر البصرية:
*   **Animated Grids:** شبكة هندسية تتحرك ببطء في الخلفية لتعطي عمقاً مكانياً.
*   **Floating Particles:** جزيئات ضوئية عشوائية تتحرك بمرونة (Floating).
*   **Vignette & Blur:** تركيز الضوء في المنتصف وتعتيم الحواف لزيادة التركيز على المنتج.

## 💻 كود الخلفية الشبكية (CSS):
```css
.bg-grid {
  background-image: linear-gradient(rgba(0, 242, 254, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 242, 254, 0.05) 1px, transparent 1px);
  background-size: 50px 50px;
  mask-image: radial-gradient(ellipse at center, black, transparent 80%);
}
```

## 📈 معايير الأداء:
*   استخدام `CSS patterns` بدلاً من صور الخلفية الثقيلة.
*   تجنب استخدام `Canvas` إذا كان من الممكن تحقيق نفس التأثير بـ `CSS` لتقليل استهلاك البطارية.
