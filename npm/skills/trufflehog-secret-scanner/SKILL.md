---
name: trufflehog-secret-scanner
description: Automated secret scanning and credential leakage prevention using TruffleHog. Scans git repositories, commits, environment files, and build artifacts to prevent API key and credential leaks.
version: 1.0.0
category: security
owner: sareem-security
tags: [secrets, git-history, credentials]
lang: [en, ar]
---

# 🛡️ TruffleHog Secret Scanner Skill

## Overview
This skill provides automated scanning for leaked secrets, API keys, private tokens, and credentials across the codebase. It ensures high security compliance before code commits or production deployments.

## Assigned Agents
- **Primary Agent:** 🛡️ **صارم (Agent 22)** — Security & Clean Code Auditor
- **Support Agent:** 📦 **جاسر (Agent 21)** — Dependency & Package Manager

## Workflow Instructions
1. **Pre-Commit Secret Inspection:**
   Run scan on modified files or staged git commits to detect plain-text tokens.
   ```bash
   trufflehog git file://./ --only-verified --json
   ```
2. **Directory & Artifact Audit:**
   Scan local directories while ignoring node_modules and temporary build artifacts.
   ```bash
   trufflehog filesystem ./ --exclude-paths .gitignore --json
   ```
3. **Remediation Directive:**
   - If any secret is detected, immediately flag the exact file path and line number.
   - Do NOT commit the secret. Revoke/rotate the leaked key and replace it with environment variables (`process.env` / `env.BINDING`).
