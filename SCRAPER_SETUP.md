# Setup Guide for PoE2 Data Scraper

---

## Prerequisites

- **Python 3.9+** - Download from [python.org](https://www.python.org/downloads/)
- **Windows 10/11** (or any OS with Python support)
- **PoE2 Trade API Access** (automatically available)

---

## Installation Steps

### 1. Install Python Requirements

Open command prompt in the project root and run:

```bash
pip install -r requirements.txt
```

This installs:
- `requests` - HTTP requests
- `beautifulsoup4` - Web scraping
- `schedule` - Task scheduling
- `pandas` - Data handling

### 2. Verify Installation

```bash
python -c "import requests; print('OK')"
```

---

## Usage

### Option 1: One-Time Updates

**Update prices only:**
```bash
python main.py --prices
```

**Full update (prices, omens, leagues):**
```bash
python main.py --update
```

**Or double-click the batch file:**
- `run_scraper.bat` - Quick price update

---

### Option 2: Automated Weekly Scheduler

**Start scheduler (foreground):**
```bash
python main.py --schedule
```

**Start scheduler (background):**
```bash
python main.py --schedule-background
```

**Or double-click:**
- `start_scheduler.bat` - Background scheduler

---

### Option 3: Windows Task Scheduler (Hands-Off)

**To run automatically every Sunday at 10 AM:**

1. Open Windows Task Scheduler (`taskschd.msc`)
2. Click "Create Basic Task"
3. Give it a name: `PoE2 Price Update`
4. Set trigger: Weekly, Sunday, 10:00 AM
5. Set action: Start a program
   - Program: `python.exe`
   - Arguments: `main.py --prices`
   - Start in: `d:\Repos\poe2`
6. Click OK

The scraper will now run automatically!

---

## Configuration

Edit `config.py` to customize:

```python
# Update schedule
UPDATE_SCHEDULE = {
    'prices': 'weekly',    # Frequency for price updates
    'omens': 'monthly',    # Frequency for omen updates
    'currency': 'monthly', # Frequency for currency updates
    'league_info': 'weekly' # Frequency for league info
}

# How many bases to track per item type
BASES_PER_TYPE = 5

# Request timeout
REQUEST_TIMEOUT = 30
```

---

## File Structure

```
d:\Repos\poe2\
├── main.py              # Main entry point
├── config.py            # Configuration settings
├── scraper.py           # Data scraping logic
├── file_updater.py      # Update markdown files
├── scheduler.py         # Scheduling logic
├── utils.py             # Utility functions
├── requirements.txt     # Python dependencies
├── run_scraper.bat      # Quick update batch file
├── start_scheduler.bat  # Start scheduler batch file
└── logs/                # Log files (auto-created)
```

---

## Logging

Logs are saved to: `logs/poe2_scraper_YYYYMMDD.log`

View the current log:
```bash
type logs\poe2_scraper_*.log
```

Check last update:
```bash
Get-Content logs\poe2_scraper_*.log | Select-Object -Last 20
```

---

## Updates & Data Files

**Weekly Price Updates** → `league-data/base-price-tracker.md`  
**Monthly Omen Updates** → `data/omens-database.md`  
**Currency Rates** → `data/currency-guide.md`  
**League Info** → `league-data/current-league.md`  

---

## Troubleshooting

### "Python is not installed"
- Install Python from [python.org](https://www.python.org)
- Make sure to check "Add Python to PATH" during installation

### "No module named 'requests'"
```bash
pip install -r requirements.txt
```

### "API returned no results"
- Check internet connection
- PoE Trade API might be down temporarily
- Check logs for detailed error messages

### "Scheduler isn't running"
- Make sure Python is in your PATH
- Try running from command prompt instead of batch file
- Check logs for errors

### "Permissions denied"
- Run Command Prompt as Administrator
- Or save to a different directory with write permissions

---

## Performance

- **Price Update**: 30-60 seconds
- **Full Update**: 2-3 minutes
- **Scheduler Overhead**: < 1MB memory

---

## Next Steps

1. ✅ Install requirements: `pip install -r requirements.txt`
2. ✅ Test once: `python main.py --prices`
3. ✅ Setup scheduler: `python main.py --schedule-background`
4. ✅ Verify files updated: Check `league-data/base-price-tracker.md`

---

## Support

**Check logs:** `logs/poe2_scraper_*.log`  
**Test manually:** `python main.py --update`  
**Verify API:** Check `https://www.pathofexile.com/api/trade2/` availability  

---

**Automation Complete!** Your pricing data will now update automatically every week.
