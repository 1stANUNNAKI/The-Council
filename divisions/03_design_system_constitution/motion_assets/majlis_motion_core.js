/**
 * 🎬 مكتبة الموشن والحركة التفاعلية القياسية لنظام المجلس (Majlis Motion Core)
 * تُحقن وتُنسخ تلقائياً في كل واجهة يتم إنتاجها بواسطة المجلس.
 */
class MajlisMotionCore {
  static initAll() {
    this.initSpotlight();
    this.initScrollReveal();
    this.initExplodeScroll();
  }

  static initSpotlight(selector = '.bento-card, .tilt-card') {
    document.querySelectorAll(selector).forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
        card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
      });
    });
  }

  static initScrollReveal(selector = '.reveal-on-scroll') {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) e.target.classList.add('revealed');
      });
    }, { threshold: 0.12 });
    document.querySelectorAll(selector).forEach(el => observer.observe(el));
  }

  static initExplodeScroll(containerSelector = '.explode-stage') {
    const container = document.querySelector(containerSelector);
    if (!container) return;
    window.addEventListener('scroll', () => {
      const rect = container.getBoundingClientRect();
      const progress = Math.max(0, Math.min(1, 1 - (rect.bottom / (window.innerHeight + rect.height))));
      container.style.setProperty('--explode-progress', progress.toFixed(3));
    });
  }
}

if (typeof module !== 'undefined') module.exports = { MajlisMotionCore };