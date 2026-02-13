# Quick Setup Guide for Second PC

**Last Updated:** February 13, 2026

---

## Step 1: Clone the Repository

Open PowerShell or Command Prompt and run:

```powershell
git clone https://github.com/mpolox/poe2
cd poe2
```

This will copy everything to your second PC.

---

## Step 2: Check if Python 3.11+ is Installed

```powershell
python --version
```

**If NOT installed:**
```powershell
winget install Python.Python.3.11
```

**If installed but not in PATH, use full path:**
```powershell
$pythonPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python311\python.exe"
& $pythonPath --version
```

---

## Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

This installs all 15 packages needed:
- requests
- beautifulsoup4
- schedule
- pandas
- lxml
- python-dateutil
- python-dotenv
- And 8 more

---

## Step 4: Understand the Structure

```
poe2/
├── data/                       # Knowledge base
│   ├── omens-database.md       # All omens with costs/effects
│   ├── currency-guide.md       # Exchange rates
│   ├── item-bases.md           # All item bases
│   └── profit-methodology.md   # Profit formulas
│
├── guides/                     # Crafting guides (8 item types)
│   ├── boots-crafting.md       # ⭐ START HERE
│   ├── gloves-crafting.md
│   ├── helmet-crafting.md
│   ├── chest-crafting.md
│   ├── shield-crafting.md
│   ├── weapon-crafting.md
│   ├── jewelry-crafting.md
│   └── flasks-crafting.md
│
├── system/                     # Agent system
│   ├── query-templates.md      # How to ask questions
│   ├── agent-instructions.md    # Agent behavior rules
│   ├── prefix-suffix-guide.md  # Prefix/suffix mechanics
│   └── item-replication-guide.md # Replicate items from trade
│
├── league-data/                # Dynamic data
│   ├── current-league.md        # League info
│   └── base-price-tracker.md   # Item prices
│
├── templates/                  # Templates
│   ├── item-analysis-template.md
│   ├── item-query-examples.md
│   └── craft-analysis-template.md
│
├── CRAFTING-INDEX.md           # Master navigation
├── QUICK-START.md              # 5-min setup
├── main.py                     # Python CLI tool
├── config.py                   # Configuration
├── scraper.py                  # Web scraper
├── requirements.txt            # Dependencies
└── ...other files
```

---

## Step 5: How to Use on Second PC

### Option A: Read the Guides (No Code Needed)

Perfect for learning what to craft:

1. Open `CRAFTING-INDEX.md` for overview
2. Read `/guides/boots-crafting.md` for boot crafting strategies
3. Check `/league-data/base-price-tracker.md` for current prices
4. Use `/system/prefix-suffix-guide.md` to understand prefix/suffix mechanics

**No installation required, just read markdown files!**

---

### Option B: Use Python Automation Scripts

Update prices automatically:

```powershell
# One-time price update
python main.py --update

# Start weekly scheduler
python main.py --schedule-background

# Use with full path if needed
& "C:\Program Files\Python311\python.exe" main.py --update
```

---

### Option C: Test Item Analysis System

Copy example requests from `/templates/item-analysis-template.md`:

```
Base: Dragonscale Boots
Current mods:
- +20% Fire Damage
- +15% Fire Resistance

Goal: Add movement speed
Budget: 12c
```

Save this in a text file and reference it when asking the AI agent questions.

---

## Step 6: Test Everything Works

### Test 1: Verify Python is ready
```powershell
cd poe2
python main.py --help
```

Should show command options.

### Test 2: Check all files exist
```powershell
Get-ChildItem guides/ | Measure-Object
# Should show 8 guides
```

### Test 3: Read a guide
```powershell
Get-Content guides/boots-crafting.md | Select-Object -First 50
```

---

## Step 7: Start Using It

### For Profit Crafting:
1. Open `guides/boots-crafting.md` (or your item type)
2. Check top bases and their profit margins
3. Check `/league-data/base-price-tracker.md` for current prices
4. Use `/data/profit-methodology.md` formula to verify profit

### For Item Analysis:
1. Read `/system/prefix-suffix-guide.md` to understand how mods work
2. Use `/templates/item-analysis-template.md` format
3. Ask AI agent: "Analyze this item: [your mods]. Goal: [what you want]"

### For Replication:
1. Find an item you like on trade site
2. List its mods (prefixes + suffixes)
3. Ask AI agent: "Can I craft this? Mods: [list]. Budget: [amount]"
4. Get exact crafting path with omen sequence and cost

---

## Step 8: Keep It Updated

Weekly update prices:

```powershell
cd poe2
python main.py --update
```

Or manually update `/league-data/base-price-tracker.md` with current market prices.

---

## Troubleshooting

### Q: "python not found"
A: Use full path: `C:\Program Files\Python311\python.exe main.py --help`

### Q: "git not found"
A: Install: `winget install Git.Git`

### Q: "pip can't install packages"
A: Use: `python -m pip install -r requirements.txt`

### Q: "ModuleNotFoundError"
A: Reinstall: `python -m pip install --force-reinstall -r requirements.txt`

### Q: Changes not showing after git pull
A: Pull again: `git pull origin main`

---

## What You Have

✅ **8 complete crafting guides** (boots, gloves, helmet, chest, shield, weapon, jewelry, flasks)
✅ **12 omens documented** with costs and effects
✅ **30+ item bases** with prices and profit calculations
✅ **Python automation** for weekly price updates
✅ **Prefix/suffix mechanics** fully explained
✅ **Item analysis system** for custom items
✅ **Item replication system** to craft items from trade
✅ **Agent instructions** for AI-powered recommendations

---

## Quick Command Reference

```powershell
# First time setup
git clone https://github.com/mpolox/poe2
cd poe2
python -m pip install -r requirements.txt

# Check what's available
Get-Content CRAFTING-INDEX.md | Select-Object -First 100

# Read a guide
Get-Content guides/boots-crafting.md

# Run automation
python main.py --update

# Pull latest changes
git pull origin main
```

---

## Next Steps

1. **Read** `/guides/boots-crafting.md` to understand the format
2. **Check** `/league-data/base-price-tracker.md` for current economy
3. **Try** one item analysis using `/templates/item-analysis-template.md`
4. **Use** `/system/item-replication-guide.md` to replicate items you like

That's it! Everything is ready to use.
