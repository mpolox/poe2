# Quick Start Guide - PoE2 Data Scraper

## ⚡ 5-Minute Setup

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Test the Scraper
```bash
python main.py --prices
```

You should see:
- Starting the scraper
- Fetching data from PoE2 Trade API
- Updating markdown files
- ✓ Completed successfully

### Step 3: Check Updated Files
Open `league-data/base-price-tracker.md` - should show current prices!

---

## 🤖 Automated Weekly Updates

### Option A: Background Process (Recommended)
```bash
python main.py --schedule-background
```
- Runs continuously in background
- Checks for scheduled tasks every minute
- Updates every Sunday at 10 AM
- Updates prices/omens/league info on schedule

Keep this running and it will auto-update!

### Option B: Windows Task Scheduler (Fire & Forget)
1. Open Task Scheduler
2. Create task to run: `python main.py --prices`
3. Set schedule: Weekly, Sundays, 10 AM
4. Done! Runs automatically

### Option C: Batch Files (Easy Click)
- **Double-click `run_scraper.bat`** - One-time price update
- **Double-click `start_scheduler.bat`** - Start background scheduler

---

## 📊 What Gets Updated

| File | Schedule | Contains |
|------|----------|----------|
| `league-data/base-price-tracker.md` | Weekly (Sun 10 AM) | Current base prices |
| `data/omens-database.md` | Monthly | Omen names, effects, costs |
| `data/currency-guide.md` | Monthly | Currency exchange rates |
| `league-data/current-league.md` | Weekly (Sun 9 AM) | League info, patch notes |

---

## 📝 Manual Commands

```bash
# One-time updates
python main.py --prices              # Quick: prices only
python main.py --update              # Full: everything
python main.py --schedule            # Foreground scheduler
python main.py --schedule-background  # Background scheduler

# Help
python main.py --help                # Show all options
```

---

## 📋 Checklist

- [ ] Install Python 3.9+
- [ ] Run: `pip install -r requirements.txt`
- [ ] Test: `python main.py --prices`
- [ ] Check: `league-data/base-price-tracker.md` updated
- [ ] Setup scheduler (choose one):
  - [ ] `python main.py --schedule-background` (keep running)
  - [ ] Add to Windows Task Scheduler (automatic)
  - [ ] Double-click batch files (manual)
- [ ] ✅ Done! Pricing data will update automatically

---

## 🔍 Troubleshooting

**"No module named requests"**
```bash
pip install -r requirements.txt
```

**"Python not found"**
- Reinstall Python with "Add to PATH" checked
- Or use full path: `C:\Python\python.exe main.py --prices`

**"API returned no results"**
- Check internet connection
- PoE Trade API might be temporary down
- Check logs: `logs/poe2_scraper_*.log`

**"Files not updating"**
- Check logs for errors
- Verify write permissions to `/league-data/` and `/data/`
- Try manual run: `python main.py --prices`

---

## 📚 Documentation

- **Full Setup**: See [SCRAPER_SETUP.md](SCRAPER_SETUP.md)
- **Configuration**: Edit [config.py](config.py)
- **Logs**: Check `logs/` folder
- **Code**: All scripts are well-commented

---

## 🎯 Next Steps

1. **Run once**: `python main.py --prices`
2. **Setup auto-run**: Choose scheduler option above
3. **Verify**: Check if files update on schedule
4. **Done!**: Your crafting data is now auto-updated weekly

---

## 💡 Tips

- Logs are saved automatically - check them if something seems wrong
- Price updates take 30-60 seconds
- Full updates take 2-3 minutes
- Backups of files are created before updates (saved as `.backup_TIMESTAMP`)
- No data is stored locally - all from official PoE2 API

---

**Questions?** Check [SCRAPER_SETUP.md](SCRAPER_SETUP.md) for detailed guide!
