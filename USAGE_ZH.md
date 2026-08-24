# 🏛️ MAJLIS — 议会 (The Council)
### 完整使用指南 | 版本 9.0

> **"一个大脑。贯通所有工具。"**
> 纪律严明的智能体议会：40个真实的专业智能体 + 90多个精选技能，一条命令安装到任何AI编程工具中，强制执行流水线：规划 → 构建 → 验证 → 安全门 → 编年记录 —— 并随每次发布自动更新自身。

---

## 1) 这到底是什么？
Majlis **不是**编辑器，也不是 Claude Code 或 OpenCode 的替代品。它是安装在您喜爱的工具**之上**的**纪律与团队层**。在任何工具中您都能获得：
- 拥有固定角色和最小权限的智能体团队
- 强制性的工作生命周期：没有测试证据和安全裁决就不允许交付代码
- 制度化记忆（`CHRONICLE.md`）与经验教训（`LESSONS.md`）

## 2) 安装

| 方式 | 命令 |
|---|---|
| **npm（推荐）** | `npx majlis-council --all` |
| 单一平台 | `npx majlis-council --claude`（也可 `--codex` `--opencode` `--gemini` `--universal`） |
| 为单个项目搭建脚手架 | `npx majlis-council --scaffold C:\path\project` |
| 从源码（Windows） | `powershell -File install_system.ps1` |

安装后在您的工具中打开任意会话——智能体、命令和技能即刻可用。

## 3) 四十位议会议员

| 调用方式 | 智能体 | 职责 | 权限 |
|----------|--------|------|------|
| `@hadi-maestro` | 🎼 Maestro Hadi | 战略规划与任务路由 | 只读 + git |
| `@rased-explorer` | 🔍 Rased | 360°代码库侦察 | 仅读取 |
| `@emad-api-shield` | ⚙️ Emad | 后端构建与 API 加固 | 完整 |
| `@baher-qa` | 🎯 Baher | 质量门：lint → typecheck → tests | 可执行，不可编辑 |
| `@sareem-security` | 🛡️ Sareem | 红色安全门：密钥/漏洞，PASS/FAIL 裁决 | 可执行，不可编辑 |
| `@nadif-clean-code` | 🧼 Nadif | 最终整洁代码审查（反谄媚规则） | 只读 + git |
| `@bayan-diagrams` | 📈 Bayan | Mermaid 架构与流程图 | 图表写入 |
| `@sajeel-logger` | 📝 Sajeel | CHRONICLE.md 时间戳审计追踪 | 仅追加 |
| `@hakim-mentor` | 🧠 Hakim | 复盘总结至 LESSONS.md | 受限编辑 |
| `@mubtakir-tools` | 🧰 Mubtakir | 工具与技能的搜索/评估/安装 | 完整 |
| `@balegh-docs` | 📣 Balegh | 双语文档与发布说明 | 文档写入 |

> 在没有子智能体系统的平台（Codex/Cursor/Gemini…）上，角色以 `/prompts:majlis-*` 命令提供，或按照主规则中的角色表进行角色扮演。


> **✦ 扩展（v9.2）：**经竞品研究新增13名专家（`@product-shaper` `@ux-researcher` `@brand-guardian` `@growth-analyst` `@code-polisher` `@test-engineer` `@perf-auditor` `@a11y-auditor` `@release-manager` `@incident-detective` `@prompt-smith` `@context-steward` `@portfolio-steward`）—— 议会达成 **40/40**。  
> **✦ 扩展议会（v9.1）：**其余成员现已成为真实智能体 —— 议会达成 **27/27**，可在所有平台上调用：`@agent-weaver` · `@data-modeler` · `@stream-partitioner` · `@integrative-architect` · `@risk-assessor` · `@cinematic-director` · `@design-system-master` · `@responsive-layout` · `@print-publisher` · `@motion-coder` · `@cicd-automator` · `@sandbox-isolator` · `@dep-manager` · `@voice-engineer` · `@data-engineer` · `@hadi-core`

## 4) 六大命令 — 生命周期

```
/majlis:start      初始化：引导式提问 → PROJECT + ROADMAP + STATE
/majlis:plan <n>   将阶段分解为带有强制验证契约的任务波
/majlis:build      通过相应议会智能体并行执行任务波
/majlis:review     由2-4名审查员组成的小组，采用反谄媚规则（最多3轮）
/majlis:security   红色安全门：密钥 → 配置暴露 → API 防御 → 裁决
/majlis:status     进度仪表板 + 精确路由到下一步行动
```

**各平台命令格式：**

| 平台 | 格式 |
|--------|--------|
| OpenCode | `/majlis-start` |
| Claude Code | `/majlis-start`（斜杠命令） |
| Codex | `/prompts:majlis-start` |
| Gemini CLI | `/majlis:start` |
| Cursor/Windsurf/Antigravity | 自然语言："run majlis start" |

## 5) 工作流地图

```mermaid
flowchart LR
    A[请求] --> B[/majlis:start]
    B --> C[/majlis:plan n]
    C --> D{🔍 Rased<br/>侦察}
    D --> E[/majlis:build]
    E --> F[⚙️ Emad 执行<br/>验证契约]
    F --> G[/majlis:review]
    G -->|BLOCKER| F
    G -->|PASS| H[/majlis:security]
    H -->|FAIL| F
    H -->|PASS| I[🧼 Nadif<br/>整洁代码门]
    I --> J[📝 Sajeel<br/>CHRONICLE.md]
    J --> K[✅ 交付]
    K -.-> L[🧠 Hakim LESSONS.md]
```

**三条黄金法则：**
1. 没有可运行的验证命令就没有任务 —— 否则计划将被拒绝
2. `SECURITY: FAIL` 的任何内容都不允许交付
3. 不接受"应该能运行" —— 要么有证据，要么保持沉默

## 6) 技能库（90+）
以标准 SKILL.md 格式自动部署到每个平台：
- **议会角色**（约20个）：编排、安全、质量、编年…
- **安全路径**：trufflehog-secret-scanner、nuclei-security-auditor、owasp-zap-api-shield
- **科学数据库**（约40个）：uniprot、pubmed、ensembl、gnomad…
- **创意制作**：remotion-video-engine、design-system-master-hsl…
- **Cloudflare**（13个）：workers、wrangler、durable-objects…

调用：OpenCode/Claude 通过技能工具自动发现 · Codex 使用 `$skill-name` · 或直接阅读 SKILL.md。

## 7) 自我更新
- 修改包文件 → 提升 `VERSION.txt` 版本号 → 下次 OpenCode 启动时静默重新部署到所有平台（约0.5秒）
- 日志：`~/.config/opencode/.majlis_bootstrap.log`
- npm 用户：`npx majlis-council@latest --all`

## 8) 包结构
```
majlis/
├── AGENTS.md            治理宪法（首先阅读）
├── VERSION.txt          版本号（驱动自我更新）
├── install_system.ps1   Windows 安装器
├── deploy_skills.ps1    仅部署技能
├── agents/              11个智能体（OpenCode 原生格式）
├── commands/            6个工作流命令
├── skills/              技能源头（已部署77个）
├── templates/           规则指针文本
├── plugins/             majlis-bootstrap.js（自我修复）
├── npm/                 全球分发包（bin/install.js）
├── USAGE_AR/EN/ZH.md    三语指南
└── _archive/            历史归档
```

## 9) 故障排除
| 问题 | 解决方法 |
|---------|------|
| @列表中缺少智能体 | 确认该平台的 agents 目录中存在对应文件；重新安装 |
| 技能未被识别 | 名称必须匹配 `[a-z0-9-]+` 且等于其文件夹名；重新运行 `--all` |
| 自愈未触发 | 检查 `.majlis_bootstrap.log` 和 `majlis_source.txt` 是否存在 |
| 新的/其他编辑器 | 在项目中使用 `--scaffold` —— 规则指针覆盖大多数工具 |

---
**许可证：** MIT · **身份：** Majlis Council · "先狩猎。干净交付。"
