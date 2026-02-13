@echo off
REM Install Python requirements for PoE2 Scraper
cd /d "%~dp0"

echo Installing Python dependencies...
"C:\Users\Alex Galvan\AppData\Local\Programs\Python\Python311\python.exe" -m pip install --no-input -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed
    pause
    exit /b 1
) else (
    echo.
    echo ✓ All dependencies installed successfully!
    pause
    exit /b 0
)
