@echo off
rem =============================================
rem  BP Analyse Docs
rem  Double-click this file to start the wiki.
rem  Close this window to stop it.
rem =============================================

echo.
echo   Starting BP Analyse Docs...
echo.

rem Check Python (Windows uses "python", not "python3")
where python >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON=python"
    goto :found
)
where python3 >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON=python3"
    goto :found
)

echo   Error: Python is not installed.
echo   Install it from https://www.python.org/downloads/
echo   Make sure to check "Add Python to PATH" during installation.
echo.
pause
exit /b 1

:found
rem Open browser after a short delay
start "" "http://localhost:8000"

rem Run server (use %~dp0 = directory of this .bat file)
%PYTHON% "%~dp0_docs-site\server.py"
