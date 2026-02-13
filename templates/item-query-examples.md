# Specific Item Query Examples

Last Updated: February 13, 2026

---

## Example 1: User Provides a Bow

### User Input
> "I have this bow I want to craft. It has:
> - +15% Physical Damage
> - +10 to Strength
> - And one empty suffix slot I think?
> 
> I want to make it better for physical damage builds. I have 15c budget for omens.
> What should I do?"

### Agent Response

```
📍 ITEM ANALYSIS: Ranger Bow

**SLOT STATUS**:
- Prefixes: 2/3 occupied (1 slot available ✓)
- Suffixes: 1/3 occupied (2 slots available ✓)

**CURRENT MODS**:
- Prefix 1: +15% Physical Damage
- Prefix 2: +10 to Strength
- Suffix 1: [Will ask user for this]
- Suffix 2-3: EMPTY

**RECOMMENDED OMEN SEQUENCE** (Cost: 15c):

1. Omen of Slaughter (8c) → Adds +25% Physical Damage prefix
   • Targets: Empty prefix slot #3
   • Success Rate: 70%
   • Effect: Doubles your physical scaling

2. Omen of Accuracy (5c) → Adds +120 Accuracy suffix
   • Targets: Empty suffix slot #2
   • Success Rate: 75%
   • Effect: Ensures your attacks hit

3. [Alternative] Omen of Vitality (4c) → Adds +3% Life Leech suffix
   • Targets: Empty suffix slot #3
   • Success Rate: 75%
   • Effect: Sustain for long fights

**EXPECTED FINAL ITEM** (using options 1+2):
- Prefix 1: +15% Physical Damage (original)
- Prefix 2: +10 to Strength (original)
- Prefix 3: +25% Physical Damage (NEW from Omen of Slaughter)
- Suffix 1: [Your current suffix]
- Suffix 2: +120 Accuracy Rating (NEW from Omen of Accuracy)
- Suffix 3: EMPTY

**VALUE ANALYSIS**:
- Investment: 5c base + 8c + 5c = 18c total
- Expected Sell Value: 55-65c
- NET Profit: 37-47c (65-72% margin) ✅ EXCELLENT

**CRAFTING CHECKLIST**:
- [x] Base already owned
- [ ] Acquire Omen of Slaughter (8c)
- [ ] Acquire Omen of Accuracy (5c)
- [ ] Apply Omen of Slaughter first
- [ ] Apply Omen of Accuracy second
- [ ] List for sale at 60c

**WHY THIS WORKS**:
✅ Physical builds love stacking damage mult
✅ Accuracy critical for hitting enemies
✅ You have perfect open slots (no conflicts)
✅ Both omens target different slot types (safe combo)

**RISK LEVEL**: 🟢 LOW
- Success: ~70% × 75% = ~52% for full sequence
- If one fails, item still has value (30-40c)
- Can retry individual omens if needed
```

---

## Example 2: User Provides a Full Fire Sword

### User Input
> "I crafted this sword and it's almost perfect but I'm stuck:
> 
> Current mods:
> - Prefix: Adds 8-15 Fire Damage
> - Prefix: +12% Fire Damage  
> - Suffix: +18% Fire Resistance
> - Suffix: +8% Block Chance
> - Suffix: ??? (I forget the last one, but slot is taken)
> 
> I want to add MORE fire damage but I can't take away resistances or block.
> Help?"

### Agent Response

```
📍 ITEM ANALYSIS: Fire Scaling Sword

**SLOT STATUS**:
- Prefixes: 2/3 occupied (1 slot available ✓)
- Suffixes: 3/3 FULL (0 slots available ✗)

**IMPORTANT**: All suffix slots are occuped - this limits your options!

**CURRENT MODS**:
- Prefix 1: Adds 8-15 Fire Damage
- Prefix 2: +12% Fire Damage
- Prefix 3: [EMPTY - Can use this!]
- Suffix 1: +18% Fire Resistance (keeper!)
- Suffix 2: +8% Block Chance (keeper!)
- Suffix 3: [Unknown but FULL]

**CHALLENGE**: You want more fire damage but:
❌ Can't modify suffixes (all 3 occupied, would lose resist/block)
✅ CAN modify prefixes (1 slot free)

**RECOMMENDED SOLUTION** (Cost: 15c):

1. Omen of Burning (15c) → Adds +20% Fire Damage prefix
   • Targets: Empty prefix slot #3 ONLY
   • Success Rate: 68%
   • KEY: Uses PREFIX-ONLY omen (won't touch suffixes)

**EXPECTED FINAL ITEM**:
- Prefix 1: Adds 8-15 Fire Damage
- Prefix 2: +12% Fire Damage
- Prefix 3: +20% Fire Damage (NEW)
- Suffix 1: +18% Fire Resistance (PRESERVED)
- Suffix 2: +8% Block Chance (PRESERVED)
- Suffix 3: [Unknown] (PRESERVED)

**VALUE ANALYSIS**:
- Investment: 8c base + 15c omen = 23c
- Expected Sell: 70-80c
- Profit: 47-57c (65-71% margin) ✅ VERY GOOD

**RISK LEVEL**: 🟢 MEDIUM-LOW
- By using PREFIX-ONLY omen, suffixes are SAFE
- Success rate: 68%
- If fails: Item keeps current state (value: 50-60c still good)

**WHY THIS SPECIFIC OMEN**:
✅ "Omen of Burning" specifically targets FIRE and PREFIXES
✅ Won't touch your resistances/block (suffix-safe)
✅ Triple fire scaling is fire caster's dream
✅ Overcap resistance not useful, but fire damage always helps

**IMPORTANT WARNING**:
⚠️ DO NOT use "Omen of Prosperity" (adds random mod - might overwrite prefix!)
⚠️ DO NOT use general omens (too risky with full suffixes)
⚠️ MUST use prefix-specific omen (Omen of Burning is perfect choice)

**NEXT STEPS**:
1. Farm/trade for Omen of Burning (15c)
2. Apply to sword
3. If succeeds: Sell for 70-80c, profit 47-57c ✅
4. If fails: Retry with different approach or accept as-is
```

---

## Example 3: User Has Full Item (Risky)

### User Input
> "I have this amulet that's almost perfect but COMPLETELY FULL:
> - +20 Strength
> - +15% Spell Damage
> - (3rd prefix occupied)
> - +18% Fire Resist
> - +12% Cold Resist
> - (3rd suffix occupied)
> 
> I want it better. I have 25c. What can I do?"

### Agent Response

```
📍 ITEM ANALYSIS: Premium Amulet (Advanced)

**SLOT STATUS**:
- Prefixes: 3/3 FULL (0 slots) ✗
- Suffixes: 3/3 FULL (0 slots) ✗

**STATUS**: This item has NO free slots!!

**CURRENT MODS**:
- Prefix 1: +20 Strength
- Prefix 2: +15% Spell Damage
- Prefix 3: [FULL - unknown]
- Suffix 1: +18% Fire Resistance
- Suffix 2: +12% Cold Resistance
- Suffix 3: [FULL - unknown]

⚠️ **CRITICAL**: All slots occupied. You have 2 options:

---

## OPTION 1: UPGRADE STRATEGY (Aggressive, 60% Success)

**What It Does**: Use Omen of Prosperity to REPLACE one mod with a better one

**How It Works**:
1. Omen identifies your "weakest" or "lowest tier" mod
2. Attempts to REPLACE it with better version of same type
3. Result: Upgraded amulet OR unchanged amulet

**Recommended Approach**:
1. Omen of Prosperity (20c) → Attempts to upgrade one suffix
   • Targets: The lowest offensive suffix for upgrade potential
   • Success Rate: 60% (risky because slots are full)
   • Outcome A (60%): Fire Resist upgraded to 22%+ OR replaced with different good suffix
   • Outcome B (40%): Item unchanged, 20c wasted

**VALUE IF SUCCESSFUL**:
- Investment: 24c base + 20c omen = 44c
- Expected Sell: 100-110c
- Profit: 56-66c (55% margin)

**RISK ASSESSMENT**: 🟡 MEDIUM-HIGH
- 60% success rate means 40% loss potential
- If it works: Very profitable
- If it fails: You're out 20c with no improvement

**VERDICT**: ONLY DO THIS if:
✓ Item is already 80+ chaos value
✓ You can afford to lose 20c
✓ You're comfortable with risk

---

## OPTION 2: SIT TIGHT (Conservative, 0% Risk)

**What To Do**: Don't craft it. Sell as-is.

**Why**:
✓ Item is complete/functional
✓ Already valuable (80-90c range estimated)
✓ Full items don't craft well (success rates drop to 50-60%)
✓ High risk for minimal reward gains

**Alternative**: Sell current amulet, use 24c + 25c budget = 49c 
→ Buy 2-3 PARTLY FILLED bases to craft instead
→ Much higher success rates (70-75%)
→ Overall profit likely higher

---

## RECOMMENDATION

**I suggest**: OPTION 2 (Sell current, craft new bases)

**Reasoning**:
1. Your current amulet is complete - good to sell as-is
2. Applying omens to completely full items = risky
3. Better ROI: Use 50c to craft 2-3 partially-empty bases
4. Each gets 70%+ success vs your 60% here
5. Volume strategy = higher overall profit

**MARKET NOTE**:
Full amulets sell well "as-is" to players building endgame chars.
Don't risk it - complete items are valuable!
```

---

## Example 4: Mixed Response - Partial Data Provided

### User Input
> "Dragonscale Boots base. Has +20 Fire Resist and... I forget what else. 
> Empty suffix slots I think. Want it crafted with your best combo for profit.
> What do I do?"

### Agent Response

```
📍 ITEM ANALYSIS: Dragonscale Boots (Partial Data)

**SLOT STATUS**: Need clarification!
- I can see: +20 Fire Resistance (1 suffix occupied)
- Unknown: Current prefixes (need details!)
- Unknown: Other suffix mods

**QUICK QUESTIONS**:
Q1: "What prefixes does it have?" (Looking for offensive mods like damage/speed)
Q2: "What's the second suffix?" (If any)
Q3: "You want offense (damage) or defense (resist/life)?"

---

**In the meantime, here's the standard Dragonscale combo**:

Based on /guides/boots-crafting.md → Combo 1 (Best for Profit):

1. Omen of Swiftness (12-15c) → Adds Movement Speed prefix
2. Omen of Resistance (3-5c) → Adds Resistance suffix

**Expected Result**: 55-60c sell value, 30-40c profit ✅

**Once you clarify prefixes above, I can give you EXACT recommendation!**
```

---

## Key Takeaways for Item Queries

1. **Always ask for specific mod names** - Not just "damage" but "+12% Physical Damage"
2. **Confirm slot counts** - Count prefixes (usually top) vs suffixes (usually bottom)
3. **Match omen types to goals**:
   - Want more offense? Use prefix-specific omens
   - Want defenses? Use suffix-specific omens
   - Want mixed? Use full-item omens (Prosperity, etc)
4. **Warn about full items** - Success rates drop significantly
5. **Provide alternatives** - If primary path is risky, suggest backups
6. **Reference mechanics** - Link to `/system/prefix-suffix-guide.md` for detailed explanation

---

# Item Replication Examples

These examples show how to use the system to craft items similar to ones you find on trade sites.

---

## Example 5: "Replicate This Bow from Market"

### User Input
> "I found this bow on the trade site and want to make one:
> - Adds 18-25 Fire Damage
> - +22% Fire Damage
> - +15% Attack Speed
> - +12% Fire Resistance
> 
> It's selling for 65c. Should I just buy it or can I craft cheaper?"

### Agent Response

```
📍 ITEM REPLICATION: Fire Scaling Bow

**TARGET ITEM**:
Market Price: 65c
- Prefix 1: Adds 18-25 Fire Damage
- Prefix 2: +22% Fire Damage
- Prefix 3: +15% Attack Speed
- Suffix 1: +12% Fire Resistance

**CRAFTING PATH**:
Base: Ranger Bow (6c)
Omens:
1. Omen of Burning (12c) → +20% Fire Damage
2. Omen of Burning (12c) → Adds Fire Damage
3. Omen of Swiftness (5c) → +15% Attack Speed
4. Omen of Resistance (3c) → Fire Resistance

**COST**: 6c base + 32c omens = 38c
**Attempts needed**: ~4-5 (success rates 70%+ each)
**All-in average**: ~50c

**VS MARKET**: 65c market - 50c craft = **15c savings** ✅ CRAFT IT
```

---

## Example 6: "Buy Partial or Build From Scratch?"

### User Input
> "I want this amulet. It's 55c but I have 50c budget.
> 
> Mods:
> - +20 Strength
> - +18% Spell Damage
> - +12% Fire Resistance
> - +15% Cold Resistance"

### Agent Response

```
📍 ITEM REPLICATION: Support Amulet

**ANALYSIS**:
- Prefixes: 2/3 (1 slot open!)
- Suffixes: 2/3 (1 slot open!)

**OPTION A: Build from scratch**
- Base: 24c + Omens: 13-18c = 37-42c all-in ✅

**OPTION B: Buy partial (BETTER)**
- Partially-done amulet: 32-35c
- Add 1-2 omens to complete: 5-8c
- Total: 37-43c
- Success rate: Much higher
- Time: Much faster

**RECOMMENDATION**: Hunt for partials. Same cost, better outcome!
```

---

## Example 7: "Should I Craft This Expensive Weapon?"

### User Input
> "Expensive sword (90c). Can I make it cheaper?
> 
> Full mods:
> - Adds 25-35 Physical
> - +35% Physical Damage
> - +20% Attack Speed
> - +140 Accuracy
> - +15% Life Leech"

### Agent Response

```
📍 ITEM REPLICATION: Premium Weapon

**ANALYSIS**:
- Prefixes: 3/3 FULL
- Suffixes: 2/3 FULL
- Complexity: HIGH (5 mods needed)

**CRAFTING COST**: 65-75c all-in (with attempts)
**MARKET PRICE**: 90c
**SAVINGS**: 15-20c

**RISK ASSESSMENT**: 🟡 MEDIUM-HIGH
- Need ~5-6 attempts
- Each failure costs resources
- 15c margin is thin

**VERDICT**:
✅ If experienced + well-funded: Craft it
⚠️ If new to crafting: Too complex, buy it
❌ If budget-conscious: Craft 3 cheaper items instead
```

---

## Decision Framework: Craft vs Buy

When deciding if YOU should replicate an item:

```
1. Calculate: Crafting Cost = Base + (Omens × Average Attempts)
2. Identify: Savings = Market Price - Crafting Cost
3. Assess: Success Rate = Multiply individual omen success rates
4. Decide:

If Savings > 30c AND Success Rate > 60%:
   → ✅ CRAFT IT (Good value + reliable)

If Savings 10-30c AND Success Rate > 50%:
   → 🟡 MAYBE (Decent value, moderate risk)

If Savings < 10c OR Success Rate < 50%:
   → ❌ BUY IT (Not worth the effort)
```

See `/system/item-replication-guide.md` for full mechanics.
