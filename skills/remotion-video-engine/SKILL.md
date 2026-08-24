---
name: remotion-video-engine
description: >
  وثيقة مهارة مخصصة لإنشاء وإنتاج الموشن جرافيكس والفيديوهات البرمجية الديناميكية باستخدام Remotion و React.
  تغطي آلية معالجة المدخلات من مجلد start/<project_name> وقراءة الصور والبرومبت والطلبات، وتحويلها إلى مقاطع فيديو متكاملة وحفظها في out/.
---

# 🎬 وثيقة استخدام مهارة ريموشن (Remotion Motion Graphics Skill)

## 📋 Agent Metadata & Team Identity
- **اسم المهارة:** وثيقة استخدام مهارة ريموشن (Remotion Motion Graphics Engine)
- **اسم الوكيل:** 🎨 إلهام (Agent 11) بالتعاون مع 💻 فارس (Agent 15) و 🧰 مبتكر (Agent 20)
- **الإيموجي:** 🎬⚡
- **التسلسل الفني في الفريق:** Agent 11 / Agent 15 / Agent 20
- **الموقع في خط الإنتاج:** هندسة إنتاج الموشن جرافيكس والوسائط التفاعلية الأوتوماتيكية (Automated Motion Graphics & Video Generation Pipeline)
- **سلسلة العمل:**
  1. استقبال الأصول والبرومبت والطلبات من مجلد المشروع الفرعي داخل `start/<project_name>/`.
  2. تحليل الهيكلية البصرية وتوزيع الإطارات الزمنية (`FPS` و `durationInFrames`).
  3. ربط الصور والوسائط والنصوص الديناميكية بمكونات React وRemotion Primitives.
  4. تطبيق الحركات والأنيميشن باستخدام `interpolate` و `spring` و `useCurrentFrame`.
  5. رندرة وتصدير الفيديو النهائي بدقة عالية إلى مجلد `out/<project_name>.mp4`.

---

## 🛠️ Prerequisites (الاعتماديات والبيئة)
1. **Node.js**: إصدار 18 أو أحدث.
2. **FFmpeg**: مثبت ومسجل في متغيرات النظام (PATH) لتنفيذ المعالجة البصرية والصوتية.
3. **Remotion Packages**: `@remotion/cli`, `remotion`, `@remotion/player`, `@remotion/media-utils`.
4. **مسارات النظام الأساسية**:
   - مسار المشروع الرئيسي: `E:\مساحة عمل مشتركة لانتيغرافيتي\remotion-video-project`
   - مجلد استقبال المشاريع والمدخلات: `E:\مساحة عمل مشتركة لانتيغرافيتي\remotion-video-project\start`
   - مجلد المخرجات والفيديوهات النهائيات: `E:\مساحة عمل مشتركة لانتيغرافيتي\remotion-video-project\out`

---

## 🔍 Overview (نظرة عامة وآلية العمل)
تتيح مهارة Remotion تحويل الأفكار والرسوم والطلبات المقدمة من المستخدم إلى مقاطع فيديو موشن جرافيك احترافية باستخدام كود React الصارم والتفاعلي.

### 🔄 آلية عمل مجلد المدخلات (`start/` Pipeline):
```
[User Input] ──► start/<project_name>/
                     ├── assets/ (الصور والوسائط)
                     ├── prompt.txt (وصف الفيديو والتحريك)
                     └── config.json (الإعدادات والألوان)
                           │
                           ▼
               [Remotion Dynamic Engine]
                           │
                           ▼
                  out/<project_name>.mp4
```

**Do NOT use when:**
- الحالات التي تتطلب مونتاجاً يدوياً شاشاتGUI تقليدية بدون أتمتة برمجية.
- الفيديوهات غير المبنية على كود أو التي لا تعتمد على نظام المكونات الديناميكية.

---

## ⚙️ Core Rules (القواعد الصارمة لإعادة الهيكلة وجودة الكود)

1. **[قاعدة الرندر المسبق الحتمي - Deterministic Rendering]:**
   يمنع منعاً باتاً استخدام `Date.now()` أو `Math.random()` غير المشفر داخل المكونات. يجب الاعتماد الحصري على `useCurrentFrame()` و `useVideoConfig()`.

2. **[قاعدة مكونات الوسائط الآمنة - Safe Media Components]:**
   استخدام `<Img />` بدلاً من `<img />` القياسية، واستخدام `<Audio />` و `<OffthreadVideo />` لمنع حدوث تسريب في الذاكرة أو انقطاع في الإطارات أثناء التصدير.

3. **[قاعدة التحقق المبكر - Fail Fast Validation]:**
   فحص وجود مجلد المشروع داخل `start/<project_name>` وقراءة ملف `config.json` أو `prompt.txt` قبل بدء عملية التصدير.

4. **[قاعدة الأمان والتوثيق الحاد - Zero Breaking Policy]:**
   عدم تعديل أية وظائف سابقة في المشروع، وتوثيق كل عملية رندر أو إضافة في مجلد `تقارير التحديثات` وتدوين ملخص الجلسة في مجلد `وثائق العمل`.

---

## 🚀 Quick Start (بدء سريع وكود تأسيسي)

### 1️⃣ هيكلية المدخلات النموذجية داخل `start/`:
عند إضافة مشروع جديد باسم `promo_demo`:
`E:\مساحة عمل مشتركة لانتيغرافيتي\remotion-video-project\start\promo_demo\`
- `config.json`
- `prompt.txt`
- `assets/logo.png`
- `assets/bg.jpg`

### 2️⃣ نموذج ملف التهيئة (`config.json`):
```json
{
  "projectName": "promo_demo",
  "title": "مرحباً بكم في نظام أنتيغرافيتي للموشن جرافيك",
  "subtitle": "إنتاج فيديو برمجي عالي الدقة",
  "primaryColor": "#6366f1",
  "fps": 30,
  "durationInSeconds": 5
}
```

### 3️⃣ كود المكون الديناميكي في Remotion (`src/Video.tsx`):
```tsx
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring, Img } from 'remotion';

export interface MotionGraphicsProps {
  title: string;
  subtitle: string;
  logoPath?: string;
  primaryColor?: string;
}

export const MotionGraphicsComposition: React.FC<MotionGraphicsProps> = ({
  title,
  subtitle,
  logoPath,
  primaryColor = '#6366f1',
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // تأثير ظهور العنوان بالحرية والانسيابية (Spring Animation)
  const titleScale = spring({
    frame,
    fps,
    config: { damping: 12 },
  });

  // شفافية النص الفرعي
  const opacity = interpolate(frame, [15, 45], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#0f172a',
        color: '#ffffff',
        justifyContent: 'center',
        alignItems: 'center',
        fontFamily: 'sans-serif',
      }}
    >
      <div style={{ transform: `scale(${titleScale})`, textAlign: 'center' }}>
        <h1 style={{ fontSize: 70, color: primaryColor, marginBottom: 10 }}>{title}</h1>
        <p style={{ fontSize: 32, opacity, color: '#94a3b8' }}>{subtitle}</p>
      </div>
    </AbsoluteFill>
  );
};
```

---

## 🍳 Common Recipes (وصفات واستخدامات شائعة)

- **وصفة 1: النصوص المتحركة السينمائية (Kinetic Typography)** — تحريك النصوص كلمة بكلمة باستخدام `interpolate` و `spring`.
- **وصفة 2: عرض الصور الديناميكي (Dynamic Image Carousel)** — سحب الصور من مجلد `start/<project>/assets` وتطبيق انتقالات سلسة بينها.
- **وصفة 3: مزامنة الصوت والمؤثرات (Audio Sync)** — استخدام `<Audio src="..." />` ودمج المؤثرات عند انتقال الإطارات.
- **وصفة 4: البطاقات التعريفية والمخططات البيانية (Animated Infographics)** — بناء مخططات بيانية متحركة كودياً تعكس البيانات الواردة في الطلب.

---

## 📊 Interpreting Output (مخرجات النظام والتصحيح)
- **الملف المخرج النهائي:** يتم حفظ الفيديو الناتج في `out/<project_name>.mp4`.
- **سجلات التوثيق:**
  - `وثائق العمل/وثيقة_استخدام_مهارة_ريموشن.md`
  - `تقارير التحديثات/تقرير_تحديث_...md`
