@echo off
REM Windows Batch File for PoE2 Data Scraper
REM Place this in the root directory of the project

cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.9+ and try again
    pause
    exit /b 1
)

REM Check if requirements are installed
python -m pip show requests >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install requirements
        pause
        exit /b 1
    )
)

REM Run the scraper
echo.
echo Starting PoE2 Data Scraper - Price Update
echo.
python main.py --prices

if errorlevel 1 (
    echo.
    echo ✗ Scraper failed
    pause
    exit /b 1
) else (
    echo.
    echo ✓ Scraper completed successfully
    pause
    exit /b 0
)
