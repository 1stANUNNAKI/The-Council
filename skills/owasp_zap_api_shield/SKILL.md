---
name: owasp_zap_api_shield
description: Dynamic API security analysis and role-based isolation testing using OWASP ZAP in isolated sandbox environments.
---

# 🛡️ OWASP ZAP API Shield Skill

## Overview
This skill provides automated dynamic application security testing (DAST) for API endpoints (`/api/*`), assessing multi-tenant isolation, authorization bypass defenses, and session security.

## Assigned Agents
- **Primary Agent:** ⚙️ **عماد (Agent 16)** — Backend API Shield Developer
- **Support Agent:** 🧪 **مَعْزُول (Agent 18)** — Sandbox & Isolated Environment Manager

## Workflow Instructions
1. **Isolated Sandbox API Scan:**
   Deploy local dev API server inside an isolated environment and run ZAP baseline scan.
   ```bash
   zap-cli quick-scan --self-contained -l Informational http://localhost:3000/api
   ```
2. **Multi-Tenant Isolation Audit:**
   - Test endpoints with tokens of different roles (Admin vs Counselor vs Coordinator).
   - Ensure a Counselor from School A cannot query entities belonging to School B.
3. **Remediation Directive:**
   - Enforce early guard clauses and D1 `WHERE school_id = ?` query isolation on every endpoint.
   - Sanitize all parameters against SQL injection and cross-site scripting attempts.
