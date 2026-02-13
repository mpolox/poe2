# PoE2 Crafting System - Manual Setup Checklist

**Created:** February 13, 2026  
**Status:** ✅ Structure Complete - Awaiting Manual Data

---

## 🎯 Your Next Steps

The system is **100% ready** - you just need to fill in the data!

---

## ⚠️ MANUAL INPUT REQUIRED

### Priority 1: Essential Data (Do First)

#### 1️⃣ Base Prices for Current League
**File:** `d:\Repos\poe2\data\item-bases.md`

Gather prices for these items:
- [ ] 3-5 boot bases (check trade sites)
- [ ] 3-5 glove bases
- [ ] 3-5 helmet bases
- [ ] 3-5 chest bases
- [ ] 2-3 shield bases
- [ ] 2-3 weapon bases
- [ ] 2-3 jewelry bases
- [ ] 1-2 flask bases

**How:** Use Path of Exile 2 trade site, search each base name, note the cheapest 3-5 listings

**Time:** ~20-30 minutes

---

#### 2️⃣ Omen Database
**File:** `d:\Repos\poe2\data\omens-database.md`

Fill in:
- [ ] List all omens available this league
- [ ] Add acquisition cost (how to get them)
- [ ] Add rarity (Unique/Powerful/Moderate/Minor)
- [ ] List best omens for each item type (based on synergies)

**How:** Reference PoE2 wiki or hover over omens in-game

**Time:** ~30-40 minutes

---

#### 3️⃣ Currency Exchange Rates
**File:** `d:\Repos\poe2\data\currency-guide.md`

Update:
- [ ] Chaos to other currency ratios
- [ ] Which currencies are most profitable to use

**How:** Check trade sites for currency pairs

**Time:** ~10 minutes

---

### Priority 2: League-Specific Info (Do Second)

#### 4️⃣ League Information
**File:** `d:\Repos\poe2\league-data\current-league.md`

Add:
- [ ] Current league name
- [ ] Patch notes affecting crafting
- [ ] Any new omens this league
- [ ] Hot builds (which items are in demand)

**How:** Check PoE2 official patch notes

**Time:** ~15 minutes

---

#### 5️⃣ Weekly Price Tracker
**File:** `d:\Repos\poe2\league-data\base-price-tracker.md`

Do this EVERY SUNDAY:
- [ ] Update prices for all bases
- [ ] Note if prices went ↑ or ↓
- [ ] Mark demand (High/Med/Low)

**How:** Same as step 1

**Time:** ~10-15 minutes/week

---

### Priority 3: Optional Enhancements

#### 6️⃣ Omen Combinations
**Files:** Individual guide files in `d:\Repos\poe2\guides\`

For each item type, test and document:
- [ ] Best omen combinations
- [ ] Success rates
- [ ] Profit per craft

**How:** Craft items, track results

**Time:** Best done as you craft (daily)

---

#### 7️⃣ Price History
**File:** `d:\Repos\poe2\league-data\base-price-tracker.md`

Track trends:
- [ ] Previous week's price (for comparison)
- [ ] Price trend indicator
- [ ] Upcoming price forecasts

**How:** Keep running notes

**Time:** ~5 minutes daily

---

## 🚀 Quick Start (Today)

**Get crafting in 1 hour:**

1. ✅ **Fill Priority 1 Data** (45 minutes)
   - [ ] Gather 5 boot base prices
   - [ ] List 5-10 omens with costs
   - [ ] Update currency rates

2. ✅ **Open Boots Guide** (5 minutes)
   - File: `d:\Repos\poe2\guides\boots-crafting.md`
   - Fill in top 3 bases with prices from step 1
   - Calculate expected profit

3. ✅ **Start Crafting!** (ongoing)
   - Buy bases
   - Use recommended omen combo
   - Sell and profit!

---

## 📝 Suggested Data Entry Plan

### This Week
- [x] Create system structure (DONE!)
- [ ] **Monday**: Add base prices
- [ ] **Monday**: Add omen database
- [ ] **Monday**: Update currency rates
- [ ] **Tuesday**: Start crafting and tracking

### This Month
- [ ] Weekly price updates (every Sunday)
- [ ] Track successful vs failed crafts
- [ ] Adjust omen recommendations based on results
- [ ] Update profit guides with real data

### Ongoing (Maintenance)
- [ ] 10 min: Sunday price check
- [ ] 5 min: Daily check for market shifts
- [ ] 15 min: Weekly guide review
- [ ] 30 min: Monthly full review

---

## 📂 Files Location Reference

**Quick access to files you need to fill:**

| Task | File | Priority |
|------|------|----------|
| Add base prices | `data/item-bases.md` | 🔴 HIGH |
| Add omens | `data/omens-database.md` | 🔴 HIGH |
| Add currency rates | `data/currency-guide.md` | 🔴 HIGH |
| Add league info | `league-data/current-league.md` | 🟡 MED |
| Weekly prices | `league-data/base-price-tracker.md` | 🟡 MED |
| Fill omen combos | `guides/boots-crafting.md` etc | 🟢 LOW |

---

## ✅ What's Already Done

All these files are created and ready to use:

- ✅ Directory structure `/data/`, `/guides/`, `/system/`, `/league-data/`
- ✅ Core data templates (just need your prices/omen data)
- ✅ 8 item-specific crafting guides (boots, gloves, helmet, etc.)
- ✅ Profit methodology & calculation system
- ✅ Agent query templates & instructions
- ✅ Master index with navigation
- ✅ Analysis templates for future use

---

## 💡 Pro Tips for Data Entry

### Efficient Price Gathering
1. Open PoE2 trade site in browser
2. Search "boots" base type
3. Sort by price (lowest first)
4. Note top 5 prices
5. Repeat for each base
6. Total time: ~2 minutes per base × number of bases

### Omen Research (Fastest Method)
1. Open PoE2 wiki → Omens section
2. Copy omen names & effects
3. For each, search trade site to see cost
4. Add to omens-database.md

### Price Tracking Automation
- Consider: Screenshot prices weekly
- Or: Keep a simple price history spreadsheet alongside the MD files
- Or: Use trade site API if available

---

## 🔄 Integration with Agent

Once you fill in the data files, the agent can:

**When you ask:**
- "What bases are good for boots?" → Pulls from guides/boots-crafting.md + current prices
- "What profit can I make?" → Calculates using profit-methodology.md
- "What omens should I use?" → Looks in omens-database.md + relevant guide
- "Should I craft X?" → Compares against league-data + other options

**All automatic!** Just fill in the data.

---

## 🎓 Learning Resources in System

Once data is filled, explore:
- [CRAFTING-INDEX.md](CRAFTING-INDEX.md) - Master guide & navigation
- [data/profit-methodology.md](data/profit-methodology.md) - Profit calculation deep dive
- [system/query-templates.md](system/query-templates.md) - What questions to ask
- [system/agent-instructions.md](system/agent-instructions.md) - How agent works

---

## 📞 Support

### If something is unclear:
1. Check [CRAFTING-INDEX.md](CRAFTING-INDEX.md) - answers most questions
2. Look at relevant guide file - templates show what to fill
3. See [templates/craft-analysis-template.md](templates/craft-analysis-template.md) for example format

### Common Questions
- **"Where do I get prices?"** → Path of Exile 2 trade site
- **"How often should I update?"** → Prices weekly (Sunday), track daily
- **"What if I don't know all omens?"** → Just add what you know, add more as you discover them
- **"Can I skip some data?"** → Start with boots, add others later as needed

---

## 🎯 Success Criteria

System is working when:
- [ ] You can open [guides/boots-crafting.md](guides/boots-crafting.md) and see current prices
- [ ] You can calculate profit using the formulas
- [ ] You know which omen combinations to use
- [ ] You make your first profitable craft
- [ ] Weekly updates take < 15 minutes

---

## 📊 Timeline Estimate

| Phase | Time | What You Get |
|-------|------|---|
| Initial Data Entry | 1-2 hours | Fully functional system ready to use |
| First Week Crafting | 30 min/day | Real data for profit optimization |
| Weekly Updates | 10-15 min | Perfectly tuned for current market |
| Monthly Review | 30 min | System improvements & refinements |

**Total time to profit: ~2 hours**

---

## 🚨 Start Today!

1. Pick up [CRAFTING-INDEX.md](CRAFTING-INDEX.md)
2. Follow → See [Data Input Checklist](#data-input-checklist)
3. Gather prices for boots (your first item)
4. Fill in [guides/boots-crafting.md](guides/boots-crafting.md)
5. Craft your first profitable item!

---

**Questions?** Everything you need is in [CRAFTING-INDEX.md](CRAFTING-INDEX.md) → Master Index section

**Ready to craft?** Let's go! 🚀

