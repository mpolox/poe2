@echo off
REM Start PoE2 Data Scraper in background scheduler mode
REM This will run continuously and check for scheduled tasks

cd /d "%~dp0"

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed
    exit /b 1
)

REM Check if requirements are installed
python -m pip show schedule >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    python -m pip install -r requirements.txt
)

echo.
echo Starting PoE2 Data Scraper - Background Scheduler
echo This will run weekly updates automatically
echo Close this window to stop the scheduler
echo.

python main.py --schedule-background

pause
