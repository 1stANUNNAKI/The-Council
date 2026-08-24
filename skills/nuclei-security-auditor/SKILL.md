---
name: nuclei-security-auditor
description: Security configuration auditing and vulnerability assessment using Nuclei templates. Verifies security headers, Cloudflare edge settings, CORS, and deployment safety.
---

# 🎯 Nuclei Security Auditor Skill

## Overview
This skill executes vulnerability scans and configuration audits using Nuclei templates against the application's endpoints, testing Cloudflare Pages Functions, security headers, and API edge configurations.

## Assigned Agents
- **Primary Agent:** 🎯 **باهر (Agent 19)** — Automated QA & Security Tester
- **Support Agent:** 🔄 **مُسْتَمِر (Agent 17)** — CI/CD & Deployment Engineer

## Workflow Instructions
1. **Targeted Configuration Scan:**
   Run Nuclei against local or deployed endpoints using specific security templates (CORS, SSL, Headers, Misconfiguration).
   ```bash
   nuclei -u https://ag.bashartwaij.com -tags misconfig,exposure,headers -json-export nuclei_report.json
   ```
2. **Local Worker & API Audit:**
   Validate local Functions dev server response headers (`CORS`, `Content-Security-Policy`, `X-Frame-Options`).
3. **Remediation Directive:**
   - Report any missing HTTP security headers or improper CORS origins (`*` on sensitive endpoints).
   - Ensure Cloudflare Turnstile integration passes automated bot protection checks.
