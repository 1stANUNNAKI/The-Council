@echo off
chcp 65001 >nul
if "%~1"=="" (
    node "%~dp0run.js" "تنفيذ وتدقيق مهام المشروع الشاملة"
) else (
    node "%~dp0run.js" "%*"
)