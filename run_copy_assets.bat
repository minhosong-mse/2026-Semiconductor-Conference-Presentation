@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if errorlevel 1 (
  echo ERROR: Python launcher "py" was not found.
  pause
  exit /b 1
)
py copy_assets_from_main.py
pause
