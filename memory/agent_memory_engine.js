/**
 * 🧠 محرك الذاكرة التاريخية واستخلاص الدروس الذاتية
 * Agent Historical Memory & Continuous Self-Learner v10.0
 */
const fs = require('fs');
const path = require('path');

class AgentHistoricalMemory {
  constructor(projectRoot = process.cwd()) {
    this.memoryDir = path.join(projectRoot, 'memory');
    this.lessonsDir = path.join(this.memoryDir, 'lessons_learned');
    this.chronicleDir = path.join(this.memoryDir, 'chronicle_history');
    this.initStorage();
  }

  initStorage() {
    [this.memoryDir, this.lessonsDir, this.chronicleDir].forEach(d => {
      if (!fs.existsSync(d)) fs.mkdirSync(d, { recursive: true });
    });
  }

  /**
   * تسجيل خطأ تم تجاوزه كدرس مستفاد دائم
   */
  recordLesson(agentId, errorPattern, rootCause, successfulFix) {
    const cleanId = agentId.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = cleanId + '_lessons.json';
    const filePath = path.join(this.lessonsDir, fileName);
    let lessons = [];

    if (fs.existsSync(filePath)) {
      try {
        lessons = JSON.parse(fs.readFileSync(filePath, 'utf8'));
      } catch (e) {
        lessons = [];
      }
    }

    const newLesson = {
      id: 'L-' + Date.now(),
      timestamp: new Date().toISOString(),
      agentId: agentId,
      errorPattern: errorPattern,
      rootCause: rootCause,
      successfulFix: successfulFix,
      repetitionCount: 1
    };

    const existingIndex = lessons.findIndex(l => l.errorPattern === errorPattern);
    if (existingIndex >= 0) {
      lessons[existingIndex].repetitionCount += 1;
      lessons[existingIndex].lastSeen = new Date().toISOString();
      lessons[existingIndex].successfulFix = successfulFix;
    } else {
      lessons.push(newLesson);
    }

    fs.writeFileSync(filePath, JSON.stringify(lessons, null, 2), 'utf8');
    return newLesson;
  }

  /**
   * استرجاع الدروس السابقة لوكيل معين لمنع تكرار الخطأ
   */
  queryLessons(agentId, contextQuery = '') {
    const cleanId = agentId.replace(/[^a-zA-Z0-9_-]/g, '_');
    const fileName = cleanId + '_lessons.json';
    const filePath = path.join(this.lessonsDir, fileName);
    if (!fs.existsSync(filePath)) return [];

    try {
      const lessons = JSON.parse(fs.readFileSync(filePath, 'utf8'));
      if (!contextQuery) return lessons;
      return lessons.filter(l => 
        l.errorPattern.toLowerCase().includes(contextQuery.toLowerCase()) ||
        l.rootCause.toLowerCase().includes(contextQuery.toLowerCase())
      );
    } catch (e) {
      return [];
    }
  }
}

module.exports = { AgentHistoricalMemory };