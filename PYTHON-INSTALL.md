# Python Installation Guide for PoE2 Scraper

## ⚠️ Current Status
**Python is NOT installed** on this system. We need to set it up first.

---

## Installation Methods

### Method 1: Official Python Installer (Recommended)

1. **Download Python 3.11+**
   - Go to: https://www.python.org/downloads/
   - Click "Download Python 3.11" (or latest)
   - Windows installer will download

2. **Run the Installer**
   - Double-click the `.exe` file
   - `√ Add Python to PATH` ← **IMPORTANT: Check this box!**
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation**
   ```powershell
   python --version
   ```
   Should show: `Python 3.11.x` (or your version)

4. **Install Requirements**
   ```powershell
   cd d:\Repos\poe2
   pip install -r requirements.txt
   ```

---

### Method 2: Windows Store (Easier)

1. Open **Microsoft Store**
2. Search for **"Python"**
3. Click the official Python app
4. Click "Install"
5. Wait for installation

Then verify:
```powershell
python --version
```

---

### Method 3: Chocolatey (For Advanced Users)

```powershell
# Run PowerShell as Administrator
choco install python
```

---

## What Gets Installed

`requirements.txt` contains:
- **requests** - HTTP library for API calls
- **beautifulsoup4** - Web scraping
- **schedule** - Task scheduling
- **python-dateutil** - Date handling
- **pandas** - Data processing
- **lxml** - XML parsing

Total size: ~100-150 MB

---

## Quick Installation Checklist

- [ ] Download Python from python.org
- [ ] Run installer
- [ ] ✅ Check "Add Python to PATH"
- [ ] Complete installation
- [ ] Verify: `python --version`
- [ ] Install deps: `pip install -r requirements.txt`
- [ ] Test: `python main.py --prices`

---

## Troubleshooting

### "Python is not installed" in Microsoft Store
- This is a Windows alias that redirects to Microsoft Store
- Install Python from https://www.python.org instead

### "pip: command not found"
- Python wasn't added to PATH
- Reinstall Python and CHECK "Add Python to PATH"
- Or use full path: `C:\Users\[YourUsername]\AppData\Local\Programs\Python\Python311\Scripts\pip`

### Installation hangs
- Try Windows Store method instead
- Or download Python 3.10 (slightly older, more stable)

### After installing, still "python not found"
- Close and reopen PowerShell
- Or restart computer
- Verify in Command Prompt (cmd.exe) instead of PowerShell

---

## Next Steps After Installation

1. **Verify Python works:**
   ```powershell
   python --version
   pip --version
   ```

2. **Install requirements:**
   ```powershell
   cd d:\Repos\poe2
   pip install -r requirements.txt
   ```

3. **Run test:**
   ```powershell
   python main.py --update
   ```

4. **Check logs:**
   ```powershell
   Get-Content logs\poe2_scraper_*.log | Select-Object -Last 20
   ```

---

## Installation Time Estimate

- Download Python: 2-3 minutes (size ~25-30 MB)
- Installation: 1-2 minutes
- Installing deps: 2-3 minutes
- **Total: ~5-10 minutes**

---

## Support

**Still stuck?**
1. Post error message in console
2. Check system Python: `where python`
3. Try Windows Store installation
4. Reinstall with admin privileges

---

**Once installtion is complete, reply and I'll install all requirements and test!**
