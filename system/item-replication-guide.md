# Item Replication Guide

**Last Updated**: February 13, 2026

---

## What is Item Replication?

**Scenario**: You see a finished item on trade that you love. You ask the agent to analyze it and tell you HOW TO CRAFT IT YOURSELF.

**System Response**: 
- Exact omen sequence needed
- Cost calculation
- Success rate estimation
- Profit vs buying finished item
- Step-by-step crafting path from base

---

## How Item Replication Works

### Step 1: Identify the Target Item
You find a finished bow on trade that looks perfect:
- Adds 18-25 Fire Damage
- +20% Fire Damage  
- +15% Attack Speed
- +18% Fire Resistance

### Step 2: Reverse-Engineering (What Agent Does)
Agent analyzes what you described:
1. Identifies which mods are **prefixes** (left side)
2. Identifies which mods are **suffixes** (right side)
3. Calculates required **omen combinations** to achieve this result
4. Determines **base item type** and cost
5. Calculates **crafting cost** vs **buying finished item**

### Step 3: Recommendation
Agent provides:
- ✅ Which base to buy
- ✅ Which omens to use in which order
- ✅ Success rate of the sequence
- ✅ Total cost comparison
- ✅ Risk assessment

---

## How to Request Item Replication

### Format 1: Full Item Description
```
I saw this item on trade and want to craft something like it:

Base: Ranger Bow
Mods:
- Adds 18-25 Fire Damage
- +20% Fire Damage
- +15% Attack Speed
- +18% Fire Resistance

How do I craft this? What's the cost?
```

### Format 2: Direct Screenshot/Description
```
There's this bow I love on the marketplace:
- Fire damage scaling (high)
- Good attack speed
- Fire resistance for survivability

Can I craft it? Should I just buy it?
```

### Format 3: Comparison Request
```
I found this sword but it's expensive (80c).
Mods: +30% Physical Damage, Adds 15-20 Physical, +15% Crit, +18% Attack Speed

Can I craft it cheaper? How much would it cost?
```

---

## Item Replication Response Format

### Example: Agent Analyzes the Bow

```
📍 ITEM REPLICATION ANALYSIS: Fire Damage Bow

**TARGET ITEM SUMMARY**:
- Adds 18-25 Fire Damage (Prefix)
- +20% Fire Damage (Prefix)
- +15% Attack Speed (Prefix)
- +18% Fire Resistance (Suffix)

**SLOT ANALYSIS**:
- Prefixes: 3/3 FULL (all occupied)
- Suffixes: 1/3 occupied (2 slots remain)
- Status: Complex - requires specific base and crafting sequence

---

**CRAFTING PATH OPTION 1: Build from Scratch**

**Step 1: Choose Your Base**
- Recommended: Ranger Bow (5-6c buy)
- Alternative: Iron Bow (3-4c buy)
- Why: Natural affinity for fire damage mods

**Step 2: Omen Sequence** (Total: 22-27c)

1. Omen of Burning (12c)
   → Adds +20% Fire Damage (PREFIX)
   → Success: 70%

2. Omen of Burning (12c)
   → Adds Adds 18-25 Fire Damage (PREFIX)
   → Success: 70% (now have 2 fire prefixes)

3. Omen of Swiftness (5c)
   → Adds +15% Attack Speed (PREFIX, fills 3/3)
   → Success: 65%

4. Omen of Resistance (3c)
   → Adds +18% Fire Resistance (SUFFIX)
   → Success: 75%

**Step 3: Final Result**
- All 3 prefixes filled with fire damage + attack speed
- 1 suffix filled with resistance
- Item matches your target!

**COST BREAKDOWN**:
- Base (Ranger Bow): 6c
- Omen of Burning ×2: 24c
- Omen of Swiftness: 5c
- Omen of Resistance: 3c
- **TOTAL COST: 38c**
- Average attempts needed: 1.5x sequence = ~57c all-in

---

**CRAFTING PATH OPTION 2: Buy Partially-Finished Item**

Sometimes other crafters leave items with 2/3 prefixes done:

**If you find**: Bow with +20% Fire + Adds Fire (missing attack speed)
- Buy cost: 25-30c
- Add: Omen of Swiftness (5c) + Omen of Resistance (3c)
- **TOTAL: 33-38c** (same cost, but faster!)
- Success rate: Higher (fewer steps)

---

**COMPARISON WITH BUYING FINISHED**:

| Option | Cost | Time | Control | Risk |
|--------|------|------|---------|------|
| Craft from scratch | 40-60c | 20 min | High | Medium |
| Buy partially done | 35-50c | 5 min | Medium | Low |
| Buy finished (market) | 65-80c | 0 min | None | None |

**RECOMMENDATION**: 🔵 **CRAFT IT**
- Saves 20-30c vs buying finished
- Less risky alternative (Option 2) if you want speed
- Learning experience for fire crafting

**NEXT STEPS**:
1. [ ] Buy Ranger Bow base (6c)
2. [ ] Acquire Omen of Burning ×2 (24c)
3. [ ] Acquire Omen of Swiftness (5c)
4. [ ] Acquire Omen of Resistance (3c)
5. [ ] Apply omens in order above
6. [ ] List finished bow (target: 70c)
7. [ ] Profit: 10-30c!
```

---

## Key Replication Features

### 1. Prefix/Suffix Identification
Agent automatically identifies which mods are prefixes vs suffixes from description

### 2. Alternative Omen Sequences
If exact omen combo unknown, agent offers:
- Most likely sequence based on mod types
- Backup sequences if first approach fails
- Risk-adjusted recommendations

### 3. Comparison Metrics
Agent compares:
- Cost to craft vs market price
- Success rate vs effort
- Risk/reward of crafting vs buying

### 4. Base Selection
Agent recommends:
- Best base item for those mods
- Alternative bases if better value
- Why certain bases work better

### 5. Financial Decision
Agent helps you decide:
- ✅ Worth crafting? (If <80% market price)
- ⚠️ Risky but possible? (50-80% market price)
- ❌ Not worth it? (Same cost or more)

---

## Replication Examples

### Example 1: "Craft This Sword"

**User Input**:
```
There's this fire sword I want:
- Adds 15-22 Fire Damage
- +25% Fire Damage
- +120 Accuracy
- +15% Fire Resistance

How much to craft? Can I do it cheaper than market?
```

**Agent Response**:
```
📍 REPLICATION: Fire Precision Sword

**ANALYSIS**:
- 3 prefixes needed: Fire prefixes + damage
- 1 suffix needed: Accuracy or Resistance

**CRAFTING COST**: ~25-30c
**MARKET PRICE**: ~60-70c
**SAVINGS**: 30-45c by crafting ✅ WORTH IT

**Step-by-step omens**:
1. Omen of Burning (12c) → Fire scaling prefix
2. Omen of Fortune (8c) → Accuracy prefix/scaling
3. Omen of Resistance (3c) → Fire Resistance suffix

**Recommended base**: Ranger Sword (8c)
**Total: 31c → Sell for 65c = 34c profit**
```

### Example 2: "Craft This Amulet"

**User Input**:
```
This amulet on PST has everything I need:
- +25 to Strength
- +20% Spell Damage
- +12% Fire Resistance
- +15% Cold Resistance

But it's 55c. Can I craft cheaper?
```

**Agent Response**:
```
📍 REPLICATION: Balanced Support Amulet

**ANALYSIS**:
- 2 prefixes: Strength + Spell Damage
- 2 suffixes: Both resistances
- Challenge: Need both resist suffixes (not common)

**CRAFTING COST**: 30-35c
**MARKET PRICE**: 55c
**SAVINGS**: 20c by crafting ✅ RECOMMENDED

**Proposed sequence**:
1. Omen of Intellect (8c) → Strength + Spell Damage
2. Omen of Resistance (3c) → Mixed resistance suffix
3. Omen of Winter (2c) → Cold Resistance suffix

**Alternative**: Buy partially-filled version at 30c, add 1 omen
**RECOMMENDATION**: Look for 2/4 filled amulets first (faster craft)
```

### Example 3: "Is It Worth Crafting?"

**User Input**:
```
I found this expensive chest and want to know:
Mods: +200 Life, +30% Fire Resistance, +20% Cold Resistance, +15 Armour

Market price: 120c

Should I just buy it or can I craft it cheaper?
```

**Agent Response**:
```
📍 REPLICATION: Premium Tank Chest

**ANALYSIS**:
- 1-2 prefixes: Mix of life + defense
- 2-3 suffixes: Resistances + armor
- Challenge: High-tier rare with good rolls

**ESTIMATED CRAFT COST**: 60-75c
**MARKET PRICE**: 120c
**SAVINGS**: 45-60c by crafting ✅ STRONG YES

BUT: Realistic success rate ~55-60% (need multiple attempts)

**Expected all-in cost with failures**: 80-90c
**Still saves**: 30-40c ✅

**VERDICT**: Worth crafting if you're comfortable with 2-3 attempts
Otherwise: Just buy the finished item
```

---

## Advanced: Reverse Engineering Unknown Items

Sometimes you see an item but don't know all the mods:

**What agent needs**:
- Base type (bow, sword, amulet, etc.)
- Visible mods (even partial list)
- Approximate item value
- What you're using it for

**What agent provides**:
- List of likely 4th/5th mods based on demand
- Most profitable possible combinations
- "If it has THIS mod, then ignore MY advice"
- Contingency crafting paths

---

## Item Replication Decision Tree

```
START: "I want to craft an item like this"
   ↓
QUESTION 1: Do you have all the mods listed?
   → YES: Go to AGENT ANALYSIS
   → NO: Agent asks for clarification
   ↓
AGENT ANALYSIS: Identify base + omen sequence
   ↓
QUESTION 2: Craft cost < 80% market price?
   → YES: "Craft it!" ✅
   → NO/EXPENSIVE: "Buy finished instead" ❌
   ↓
QUESTION 3: Success rate > 70%?
   → YES: Straightforward craft
   → NO: Offer backup strategies
   ↓
RECOMMENDATION: Step-by-step crafting path
```

---

## Pro Tips for Replication

1. **Screenshot Everything**: If you see a good item, screenshot the mods
2. **Note the Base**: Base type matters (Ranger vs Iron sword = different crafting)
3. **Check Pricing First**: Compare crafting cost vs market before committing
4. **Look for Partially-Done**: Sometimes buying 50% done is faster than 0% done
5. **Consider Volume**: Replicate high-demand items for better resale

---

## See Also
- [system/prefix-suffix-guide.md](../system/prefix-suffix-guide.md) - How prefixes/suffixes work
- [templates/item-analysis-template.md](../templates/item-analysis-template.md) - How to format item requests
- [templates/item-query-examples.md](../templates/item-query-examples.md) - Example responses
