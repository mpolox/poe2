# PoE2 Crafting Profit Methodology

Last Updated: February 13, 2026

---

## Core Profit Formula

### Basic Calculation
```
Profit = (Expected Final Item Value) - (Base Cost) - (Crafting Costs) - (Fees)

Where:
- Expected Final Item Value = Average selling price for successfully crafted items
- Base Cost = Cost to purchase empty base
- Crafting Costs = Currency spent (omens, alterations, etc.)
- Fees = NPC selling tax or marketplace commission (~5-10%)
```

### Advanced Formula (Risk-Adjusted)
```
Expected Profit = (Success Rate × Profit per Success) - (Failure Rate × Loss per Failure)

Where:
- Success Rate = % chance of hitting desired outcome
- Profit per Success = Profit if craft succeeds
- Failure Rate = % chance craft fails or results in unsellable item
- Loss per Failure = Cost to acquire base + crafting expenses
```

---

## Step-by-Step Analysis for Any Item

### 1. Identify Target Item
- Item type (boots, gloves, etc.)
- Base name
- Desired affixes (prefixes and suffixes)

### 2. Calculate Base Cost
```
Base Cost = Current Market Price of Empty Base
```
> Check [item-bases.md](../data/item-bases.md) for current prices

### 3. Determine Crafting Method
Options:
- Omen crafting (guided randomization)
- Alteration crafting (brute force)
- Hybrid approach (omens + alterations)

### 4. Calculate Crafting Investment
```
Crafting Cost = (Currency per attempt) × (Average attempts to succeed)
```

**Example:**
- Omen cost: 2 chaos
- Success rate: 40% (need 2.5 attempts on average)
- Total cost: 2 × 2.5 = 5 chaos per craft

### 5. Estimate Final Item Value
Research market prices for items with desired affixes:
- Check actively listed items
- Check completed sales
- Average the values
- Apply market conditions modifier

### 6. Calculate Net Profit
```
Profit = (Expected Value) - (Base Cost) - (Crafting Cost) - (Fees)
Profit Margin % = (Profit / Expected Value) × 100
```

**Example:**
- Expected Value: 50 chaos
- Base Cost: 5 chaos
- Crafting Cost: 5 chaos
- Fees (10%): 5 chaos
- **Net Profit: 35 chaos (70% margin!)**

---

## Success Rate Estimation

### Factors Affecting Success
1. **Omen Quality** - Powerful omens have better odds
2. **Base availability** - More suffixes = harder to craft
3. **Target affixes** - Rare affixes take longer
4. **Budget available** - More capital = more retry attempts

### Common Success Scenarios

| Scenario | Success Rate | Avg Attempts | Notes |
|----------|---|---|---|
| Basic craft (2-3 target mods) | 60-70% | 1.4-1.7 | Good for profit |
| Complex craft (4+ target mods) | 30-40% | 2.5-3.3 | Higher risk |
| Perfect roll all mods | < 10% | 10+ | Not recommended |
| Safe craft (1-2 mods) | 80%+ | 1.2-1.3 | Beginner friendly |

---

## Risk Assessment Framework

### Green Light (Recommended)
✅ Expected profit > 30 chaos  
✅ Success rate > 50%  
✅ Profit margin > 40%  
✅ Market demand = High  
✅ Base readily available  

### Yellow Light (Proceed with Caution)
⚠️ Expected profit: 10-30 chaos  
⚠️ Success rate: 30-50%  
⚠️ Profit margin: 20-40%  
⚠️ Market demand = Medium  
⚠️ Base sometimes scarce  

### Red Light (Avoid)
❌ Expected profit < 10 chaos  
❌ Success rate < 30%  
❌ Profit margin < 20%  
❌ Market demand = Low  
❌ Base hard to find  

---

## Scenario Analysis

### Bootstrap Strategy (Starting with low capital)
- Focus on bases costing < 5c
- Target profit per craft: 5-15c
- Success rate target: 70%+
- Volume strategy: Craft 10-15 items

### Growth Strategy (With 50-200c capital)
- Bases costing 5-15c
- Target profit per craft: 20-40c
- Success rate target: 50%+
- Quality over quantity

### Premium Strategy (With 200c+ capital)
- High-value bases (15-50c)
- Target profit per craft: 50-100c+
- Attempt complex crafts
- Build reputation with quality

---

## Break-Even Analysis

**Minimum selling price to not lose money:**
```
Break-Even Price = Base Cost + Crafting Cost + Fees
```

**Example:**
- Base: 5c
- Crafting: 5c
- Fees (10%): 1c
- **Break-Even: 11c minimum**

Never sell below break-even unless clearing inventory.

---

## Seasonal Adjustments

| League Phase | Strategy Adjustment | Reason |
|---|---|---|
| First Week | Limited item bases | Scarcity increases prices |
| Week 2-3 | All items available | Prices normalize, profit increases |
| Mid-League | High competition | Profit margins compress |
| Late-League | Niche items only | Bulk of demand satisfied |

---

## Profit Tracking Template

```
Item: [Base Name]
Date: [Date]
Base Cost: [X]c
Crafting Cost: [X]c
Attempts: [X]
Successful Crafts: [X]
Avg Sale Price: [X]c
Total Revenue: [X]c
Total Investment: [X]c
Total Profit: [X]c
Profit per Item: [X]c
Success Rate: [X%]
```

---

## Common Mistakes to Avoid

1. ❌ Crafting items with low market demand
2. ❌ Underestimating fees and taxes
3. ❌ Not accounting for failed attempts
4. ❌ Selling significant margin below market average
5. ❌ Overextending capital on risky crafts
6. ❌ Ignoring league economy changes

---

## Quick Profit Calculator

Use this template for rapid assessment:
| Input | Value |
|-------|-------|
| Item Base | [Type]c |
| Crafting Cost | [X]c |
| Expected Sale Price | [X]c |
| Success Rate | [X%] |
| Expected Profit | **[CALC]c** |
| Recommendation | ✅/⚠️/❌ |
