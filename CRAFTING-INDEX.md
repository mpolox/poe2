# PoE2 CRAFTING SYSTEM - Master Index

**Last Updated:** February 13, 2026  
**System Ready for Data Input:** ✅ YES

---

## 🚀 Quick Start Guide

1. **First Time?** → Start with [Data Input Checklist](#data-input-checklist) below
2. **Want to craft boots?** → Go to [Boots Guide](guides/boots-crafting.md)
3. **Not sure what to craft?** → Check [What Should I Craft?](#what-should-i-craft)
4. **Calculating profit?** → Use [Profit Methodology](data/profit-methodology.md)
5. **⭐ NEW: Want to craft an item like one you saw?** → Use [Item Replication Guide](system/item-replication-guide.md)

---

## 📁 Directory Structure

```
/data/                          # Core Knowledge Base
├── item-bases.md              # All item bases by type
├── omens-database.md          # All omens with effects & costs
├── currency-guide.md          # Currency rates & costs
└── profit-methodology.md      # How to calculate profit

/guides/                        # Item-Specific Crafting Guides
├── boots-crafting.md          # Boots optimization guide ⭐ START HERE
├── gloves-crafting.md         # Gloves guide
├── helmet-crafting.md         # Helmets guide
├── chest-crafting.md          # Chest armor guide
├── shield-crafting.md         # Shields guide
├── weapon-crafting.md         # Weapons guide
├── jewelry-crafting.md        # Rings & Amulets guide
└── flasks-crafting.md         # Flasks guide

/system/                        # Agent System Files
├── query-templates.md         # Standard questions & triggers
├── agent-instructions.md      # How agent responds & looks up data
├── prefix-suffix-guide.md     # ⭐ NEW: Prefix/Suffix mechanics explained
├── item-replication-guide.md  # ⭐ NEW: Replicate items from trade sites
└── item-analysis-template.md  # ⭐ NEW: How to request item analysis

/league-data/                   # Dynamic League Information
├── current-league.md          # Active league info & notes
└── base-price-tracker.md      # Weekly price updates

/templates/                     # Reusable Templates
├── craft-analysis-template.md # Template for analyzing crafts
├── item-analysis-template.md  # ⭐ NEW: Template for item queries
└── item-query-examples.md     # ⭐ NEW: Example analysis/replication responses

/CRAFTING-INDEX.md            # THIS FILE (Master navigation)
```

---

## 📋 Data Input Checklist

**⚠️ BEFORE YOU START CRAFTING: Fill these in manually**

### Essential Data Needed

#### 1. Item Base Prices (Priority: HIGH)
- [ ] Check `/data/item-bases.md`
- [ ] Add current market prices for boots, gloves, helmet, chest
- [ ] Add 3-5 bases per item type
- [ ] Update volume/demand indicators

**How**: Search Path of Exile 2 trade sites for each base, note cheapest listing

#### 2. Omen Database (Priority: HIGH)
- [ ] Check `/data/omens-database.md`
- [ ] List all available omens this league
- [ ] Add acquisition cost for each omen
- [ ] Fill rarity tiers
- [ ] Add omen combinations for each item type

**How**: Reference PoE2 wiki or in-game omen descriptions

#### 3. Currency Exchange Rates (Priority: MEDIUM)
- [ ] Update `/data/currency-guide.md`
- [ ] Add chaos-equivalent for all currencies
- [ ] Note which currencies are used for crafting

**How**: Check trade sites for currency ratios

#### 4. League Information (Priority: MEDIUM)
- [ ] Update `/league-data/current-league.md`
- [ ] Enter current league name & stage
- [ ] Note any crafting changes or new omens
- [ ] Update patch notes relevant to item crafting

**How**: Check Path of Exile 2 official patch notes

#### 5. Weekly Price Updates (Priority: ONGOING)
- [ ] Schedule weekly updates to `/league-data/base-price-tracker.md`
- [ ] Every Sunday: Update all base prices
- [ ] Note trends (↑/↓) and demand changes

**How**: Spend 10-15 minutes checking active listings

---

## 🎯 What Should I Craft?

### For Maximum Profit
1. Open [guides/boots-crafting.md](guides/boots-crafting.md) → Check "Top Profitable Bases"
2. Open [league-data/base-price-tracker.md](league-data/base-price-tracker.md) → Verify current price
3. Calculate: Investment vs Expected Profit using [data/profit-methodology.md](data/profit-methodology.md)
4. **Action**: Buy base if profit margin > 30%

### By Budget

**5-10 Chaos Budget**
- Craft Tier 3 budget bases (flasks or boots)
- Use 1-2 omen combos
- Expected profit: 3-8c per craft
- Volume: 5-10 items

**20-50 Chaos Budget**
- Craft Tier 2 bases (gloves, helmets)
- Use 2-3 omen combos
- Expected profit: 10-20c per craft
- Volume: 10-15 items

**100+ Chaos Budget**
- Craft Tier 1 premium bases (chest, weapons)
- Complex omen combinations
- Expected profit: 25-50c+ per craft
- Volume: 20-30 items

### By Item Type

| Item | Difficulty | Profit | Speed | Best For |
|------|-----------|--------|-------|----------|
| Flasks | ⭐ Easy | Low | Fast | Volume farming |
| Gloves | ⭐⭐ Easy | Medium | Med | Steady profit |
| Boots | ⭐⭐ Easy | Medium | Med | Popular, reliable |
| Helmet | ⭐⭐ Easy | Medium | Med | Build-specific |
| Shield | ⭐⭐ Easy | Medium | Slow | Niche demand |
| Jewelry | ⭐⭐⭐ Hard | High | Slow | High-value items |
| Weapon | ⭐⭐⭐ Hard | High | Slow | Best margins |
| Chest | ⭐⭐⭐ Hard | High | Slow | High-risk/reward |

---

## 🔍 Search & Navigation

### Find a Specific Item Type
- **Boots** → [guides/boots-crafting.md](guides/boots-crafting.md)
- **Gloves** → [guides/gloves-crafting.md](guides/gloves-crafting.md)
- **Helmet** → [guides/helmet-crafting.md](guides/helmet-crafting.md)
- **Chest** → [guides/chest-crafting.md](guides/chest-crafting.md)
- **Shield** → [guides/shield-crafting.md](guides/shield-crafting.md)
- **Weapon** → [guides/weapon-crafting.md](guides/weapon-crafting.md)
- **Jewelry** → [guides/jewelry-crafting.md](guides/jewelry-crafting.md)
- **Flask** → [guides/flasks-crafting.md](guides/flasks-crafting.md)

### Find Specific Information
- **"What's the profit formula?"** → [data/profit-methodology.md](data/profit-methodology.md)
- **"What omens exist?"** → [data/omens-database.md](data/omens-database.md)
- **"What are base prices?"** → [league-data/base-price-tracker.md](league-data/base-price-tracker.md)
- **"How much does currency cost?"** → [data/currency-guide.md](data/currency-guide.md)
- **"All bases listed?"** → [data/item-bases.md](data/item-bases.md)
- **"Prefix vs Suffix mechanics?"** → [system/prefix-suffix-guide.md](system/prefix-suffix-guide.md) ⭐ NEW
- **"How do I request item analysis?"** → [templates/item-analysis-template.md](templates/item-analysis-template.md) ⭐ NEW

---

## 💡 Agent Query Examples

### General Queries
- "What bases are good for boots?"
- "What's the most profitable item to craft?"
- "Can I make profit with 10 chaos?"
- "What omens should I use for [item]?"
- "What's the market price for [base]?"
- "Should I craft boots or gloves?"

### ⭐ NEW: Specific Item Analysis
**Give the agent details about an item YOU OWN to get exact crafting recommendations!**

- "Analyze this bow: +15% Physical, +10 Strength, 1 empty suffix. Goal: add accuracy with 15c budget"
- "My sword has: Adds 8-15 Fire Damage, +12% Fire Damage, +18% Fire Resist, +8% Block. Full suffixes! Can I add more fire?"
- "Gold Amulet completely full mods. Should I try to upgrade it or sell as-is?"
- "How do I keep my resistances while adding damage?"

**Agent will provide:**
1. ✅ Exact slot availability analysis
2. ✅ Recommended prefix/suffix-specific omens
3. ✅ Success rate calculations based on slot status
4. ✅ Profit and risk projections
5. ✅ Alternatives if primary path is risky

**See:**
- [templates/item-analysis-template.md](templates/item-analysis-template.md) - How to format your item
- [templates/item-query-examples.md](templates/item-query-examples.md) - Example responses to item queries
- [system/prefix-suffix-guide.md](system/prefix-suffix-guide.md) - Technical details on how prefixes/suffixes work

---

### ⭐ NEW: Item Replication
**Show the agent a finished item from trade and get detailed crafting instructions!**

- "I found this bow on PST and want to make one. Mods: [list]. Can I craft it cheaper?"
- "This amulet is 55c but I have 50c. Can I make something similar?"
- "There's an expensive weapon I love. Should I craft it or just buy it?"
- "Can I replicate this item? What's the exact omen sequence?"

**Agent will provide:**
1. ✅ Identified base item type
2. ✅ Exact omen sequence needed (step-by-step)
3. ✅ Total crafting cost calculation
4. ✅ Comparison to market price
5. ✅ Recommendation: Craft vs Buy decision

**Craft vs Buy Decision Framework:**
- Savings > 30c + Success > 60%? → ✅ **Craft it**
- Savings 10-30c + Success > 50%? → 🟡 **Maybe**
- Savings < 10c or Success < 50%? → ❌ **Buy it**

**See:**
- [system/item-replication-guide.md](system/item-replication-guide.md) - Complete replication mechanics
- [templates/item-query-examples.md](templates/item-query-examples.md) - Examples 5-7 show replication

---

## 💡 Query Reference

See [system/query-templates.md](system/query-templates.md) for all question patterns and formats

---

## 📊 Profit Calculation Template

Quick profit check for any item:

```
Item: _______________
Base Cost: _____ c
Crafting Cost: _____ c
Expected Sale: _____ c
Fees (10%): _____ c

Profit = Sale - Base - Crafting - Fees = _____ c
Margin = (Profit / Sale) × 100 = _____ %

Recommendation: ✅ / ⚠️ / ❌
```

Full methodology: [data/profit-methodology.md](data/profit-methodology.md)

---

## 📅 Maintenance Schedule

### Daily
- Check new listings for price shifts
- Track hottest items

### Weekly (Every Sunday)
- Update base prices → [league-data/base-price-tracker.md](league-data/base-price-tracker.md)
- Review profit margins
- Update "Hot Bases" in [league-data/current-league.md](league-data/current-league.md)
- Check for new omen combos

### Bi-Weekly
- Review successful crafts
- Adjust omen recommendations
- Update profit thresholds

### Monthly
- Full market review
- Update profit methodology with real data
- Refresh all guides with latest information

---

## 🎓 Learning Path

**New to PoE2 crafting?**

1. Read: [What is Crafting?](data/profit-methodology.md#overview) (2 min read)
2. Example: [Boots Guide](guides/boots-crafting.md) (5 min read)
3. Check: [Base Prices](league-data/base-price-tracker.md) (1 min)
4. Calculate: Profit for a boots craft (2 min)
5. Action: Buy 5 boots bases and craft!

**Want to optimize profits?**

1. Study: [Profit Methodology](data/profit-methodology.md) (10 min)
2. Compare: Different item types in guides/ (5 min)
3. Analyze: Current market conditions in [league-data/](league-data/current-league.md) (3 min)
4. Plan: Your crafting strategy
5. Execute: With calculated expectations

---

## ⚙️ System Files

### For Agents/Automation
- [system/query-templates.md](system/query-templates.md) - Question patterns that trigger responses
- [system/agent-instructions.md](system/agent-instructions.md) - How agent processes queries and looks up data

These files tell the agent HOW to respond to crafting questions.

---

## 📝 How to Update Files Efficiently

### Adding a New Base
1. Go to relevant item guide (e.g., [guides/boots-crafting.md](guides/boots-crafting.md))
2. Add row to "Top Profitable Bases" table
3. Update [league-data/base-price-tracker.md](league-data/base-price-tracker.md)
4. Update [data/item-bases.md](data/item-bases.md)

### Adding New Omen Combo
1. Go to [data/omens-database.md](data/omens-database.md)
2. Add omen to appropriate tier
3. Add combo to relevant item guide
4. Test success rate manually

### Weekly Price Update (Fast!)
1. Open [league-data/base-price-tracker.md](league-data/base-price-tracker.md)
2. Check top 3 items in each category for price
3. Update values
4. Done! (takes ~10 minutes)

---

## 🚨 Common Issues & Solutions

### "I don't know what bases to craft"
→ Open [guides/boots-crafting.md](guides/boots-crafting.md) → Check Top 3 bases → Done!

### "Am I making enough profit?"
→ Use this: [data/profit-methodology.md](data/profit-methodology.md#profit-calculation-procedure)

### "Prices changed, need updates"
→ Update: [league-data/base-price-tracker.md](league-data/base-price-tracker.md)

### "What omen should I use?"
→ Check: [data/omens-database.md](data/omens-database.md) or item-specific guide

### "This guide is outdated"
→ Check last updated date at top of file, update with current data

---

## 📞 Quick Reference

**Most Used Files:**
1. [guides/boots-crafting.md](guides/boots-crafting.md) - Start here
2. [league-data/base-price-tracker.md](league-data/base-price-tracker.md) - Check prices
3. [data/profit-methodology.md](data/profit-methodology.md) - Calculate profit
4. [data/omens-database.md](data/omens-database.md) - Find omen combos

**Need Help?**
- Profit calculation → [data/profit-methodology.md](data/profit-methodology.md)
- All bases overview → [data/item-bases.md](data/item-bases.md)
- Current market → [league-data/current-league.md](league-data/current-league.md)
- Ask questions → See [system/query-templates.md](system/query-templates.md)

---

## ✅ Implementation Complete

**Status**: Ready for use  
**Awaiting**: Manual data input from user (prices, omens, currency rates)  
**Time to first craft**: ~1 hour after data entry  
**Estimated setup**: Fill in data files, then start crafting!

---

**Next Steps:**
1. Fill in [data/item-bases.md](data/item-bases.md) with current prices
2. Fill in [data/omens-database.md](data/omens-database.md) with omen info
3. Update [league-data/base-price-tracker.md](league-data/base-price-tracker.md) with prices
4. Set weekly reminder to update prices every Sunday
5. Start with [guides/boots-crafting.md](guides/boots-crafting.md) and craft!
