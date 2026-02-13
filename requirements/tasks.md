# PoE2 Crafting Optimization - Task Checklist

## Overview
Build a comprehensive crafting optimization system that provides item-specific guides with profitable bases, omens, and currency recommendations.

---

## Phase 1: Core Knowledge Base Files

### 1.1 Data & Reference Structures
- [x] **Create `/data/item-bases.md`** - Comprehensive database of all item bases ✅ DONE
  - Organized by item type (boots, gloves, helmet, chest, shield, weapon, etc.)
  - Include base stats, drop location, rarity tier
  - Flag high-demand bases for profit potential
  
- [x] **Create `/data/omens-database.md`** - Complete omen database ✅ DONE - 12 omens populated
  - List all available omens with effects
  - Categorize by power level (Unique, Powerful, Moderate, Minor)
  - Include recommended omens per item type
  - Note rarity and acquisition cost
  
- [x] **Create `/data/currency-guide.md`** - Currency efficiency reference ✅ DONE
  - Currency types and exchange rates
  - Cost breakdown for different crafting methods
  - Budget calculation templates
  - Profit margin calculations

### 1.2 Profit Analysis Framework
- [x] **Create `/data/profit-methodology.md`** - How to calculate crafting profit ✅ DONE
  - Item base cost + crafting cost - expected final value = profit
  - Risk multiplier for uncertain outcomes
  - Market demand factors
  - Break-even analysis templates

---

## Phase 2: Item-Specific Crafting Guides

### 2.1 Boots Crafting Guide
- [x] **Create `/guides/boots-crafting.md`** - Detailed boots crafting guide ✅ DONE
  - Best bases for profit (early vs late league)
  - Recommended omen combinations
  - Required currency per craft attempt
  - Expected profit margins
  - Quick reference checklist

### 2.2 Additional Item Guides (Create similar structure)
- [x] **Create `/guides/gloves-crafting.md`** - Gloves optimization guide ✅ DONE
- [x] **Create `/guides/helmet-crafting.md`** - Helmet crafting strategies ✅ DONE
- [x] **Create `/guides/chest-crafting.md`** - Chest armor guide ✅ DONE
- [x] **Create `/guides/shield-crafting.md`** - Shield crafting guide ✅ DONE
- [x] **Create `/guides/weapon-crafting.md`** - Weapon crafting strategies ✅ DONE
- [x] **Create `/guides/jewelry-crafting.md`** - Ring/Amulet guide ✅ DONE
- [x] **Create `/guides/flasks-crafting.md`** - Flask crafting optimization ✅ DONE

### 2.3 Guide Template Structure (Each file should include)
- [ ] List of 3-5 best bases by profit potential
- [ ] For each base:
  - Required omen sequence
  - Estimated crafting cost (in currency)
  - Expected final value
  - Profit per successful craft
  - Success rate estimates
- [ ] Quick reference checklist
- [ ] Market conditions impact notes

---

## Phase 3: Dynamic Lookup System

### 3.1 Query System Files
- [x] **Create `/system/query-templates.md`** - Standard question patterns ✅ DONE
  - "What bases are good for [item]?"
  - "What omens for [item type]?"
  - "How much currency for [craft]?"
  - "What's the profit margin for [base]?"

- [x] **Create `/system/agent-instructions.md`** - Agent behavior guide ✅ DONE
  - How to respond to crafting queries
  - Data lookup procedures
  - Profit calculation steps
  - Profit threshold recommendations

---

## Phase 4: League-Specific Updates

- [x] **Create `/league-data/current-league.md`** - Active league information ✅ DONE
  - Current patch notes relevant to crafting
  - Hot bases this league
  - Changed omens/currencies
  - Market prices (snapshot)
  - Seasonal trends

- [x] **Create `/league-data/base-price-tracker.md`** - Item base prices ✅ DONE - 30+ bases with prices
  - Updated prices by base name
  - Volume demand indicators
  - Price trend (↑/↓)

---

## Phase 5: Implementation & Integration

- [x] Organize MD files in logical directory structure ✅ DONE
  ```
  /data/
    - item-bases.md ✅
    - omens-database.md ✅
    - currency-guide.md ✅
    - profit-methodology.md ✅
  /guides/
    - boots-crafting.md ✅
    - gloves-crafting.md ✅
    - helmet-crafting.md ✅
    - chest-crafting.md ✅
    - shield-crafting.md ✅
    - weapon-crafting.md ✅
    - jewelry-crafting.md ✅
    - flasks-crafting.md ✅
  /system/
    - query-templates.md ✅
    - agent-instructions.md ✅
  /league-data/
    - current-league.md ✅
    - base-price-tracker.md ✅
  ```

- [x] Create index file: **`/CRAFTING-INDEX.md`** ✅ DONE
  - Master navigation document
  - Quick links to all guides
  - Search terms mapping
  - Last updated timestamps

- [x] Create template: **`/templates/craft-analysis-template.md`** ✅ DONE
  - Reusable format for analyzing new bases
  - Copy-paste structure for quick updates

---

## Phase 6: Continuous Improvement

- [x] **Update frequency schedule** ✅ CONFIGURED
  - Daily: Base price tracker (Python automation ready)
  - Weekly: Omen recommendations based on market (Scheduled Sundays 10 AM)
  - Bi-weekly: Guide accuracy reviews (Manual)
  - Monthly: Profit methodology review (Manual)

- [x] **Performance metrics tracking** ✅ SYSTEM READY
  - Most profitable items per week (Tracked in base-price-tracker.md)
  - Successful craft rate by guide (Documented in craft templates)
  - User feedback integration (Agent instructions ready)

---

## Quick Reference: Guide File Template

Each crafting guide (`/guides/*.md`) should follow this structure:

```markdown
# [Item Name] Crafting Guide

## Top Profitable Bases
| Base | Cost | Best Implicit | Profit | Success % |
|------|------|---|---------|---------|
| | | | | |

## Recommended Omen Sequences
1. **Combo A** - [Description]
   - Cost: X currency
   - Success: Y%
   
## Crafting Checklist
- [ ] Buy base
- [ ] Apply omens in order
- [ ] Check results
- [ ] List for profit

## Market Notes
- [Current market conditions]

## Risk Assessment
- Break-even price: X
- Target price: Y
```

---

**STATUS**: Ready for implementation
**PRIORITY**: Start with Phase 1 & 2, especially boots guide for immediate agent deployment
