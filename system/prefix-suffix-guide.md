# Prefix/Suffix Mechanics & Omen Crafting Guide

Last Updated: February 13, 2026

---

## Understanding Prefixes vs Suffixes

### Prefix Rules
- **Position**: On the left side of mod list
- **Typical Content**: Offensive mods, stats, special effects
- **Max on Item**: 3 prefixes maximum
- **Examples**: +12 to Strength, +20% Physical Damage, Adds 5-10 Fire Damage

### Suffix Rules
- **Position**: On the right side of mod list (below prefixes)
- **Typical Content**: Resistances, defenses, utility
- **Max on Item**: 3 suffixes maximum
- **Examples**: +20% Fire Resistance, +5% Block Chance, 10% Increased Rarity

---

## Omen Behavior by Target

### Full Item Omens (Affect Both Prefixes & Suffixes)
- `Omen of Prosperity` → Adds a new powerful mod (prefix or suffix randomly)
- `Omen of Burning` → Convert fire resistance to fire damage (mixed)
- `Omen of Swiftness` → Add movement speed or attack speed (prefix)

### Prefix-Specific Omens
- `Omen of Slaughter` → Adds/strengthens physical damage prefix
- `Omen of Intellect` → Adds intelligence and spell scaling prefixes
- `Omen of Defiance` → Adds armor/evasion/ward prefixes
- `Omen of Fortune` → Adds critical strike prefixes

### Suffix-Specific Omens
- `Omen of Resistance` → Adds resistance suffixes (+15% all = 1 suffix)
- `Omen of Winter` → Adds cold resistance suffix
- `Omen of Accuracy` → Adds accuracy rating suffix
- `Omen of Vitality` → Adds life regeneration or max life suffix

---

## Crafting Strategies for Full Item Analysis

### Strategy 1: Fill Empty Prefix Slots First
**When to use**: You want offensive stats but need slots
1. Check current prefixes (max 3)
2. If slots available: Use prefix-specific omens (Slaughter, Intellect, etc.)
3. Benefit: Safe, predictable, doesn't overwrite

### Strategy 2: Fill Empty Suffix Slots First
**When to use**: You need defensive stats or resistances
1. Check current suffixes (max 3)
2. If slots available: Use suffix-specific omens (Resistance, Vitality, etc.)
3. Benefit: Defensive, reliable, doesn't conflict with offense

### Strategy 3: Multi-Omen Combo (Hybrid Approach)
**When to use**: Crafting end-game gear where both prefix and suffix matter
1. First omen: Prefix-specific (adds offensive power)
2. Second omen: Suffix-specific (adds defensive/resistance)
3. Expected result: Complete item with both offense and defense

---

## Item Analysis Template

### Input Format
```
Base: [Item Name] ([Item Type])
Current Stats:
- [Prefix 1]: [Value]
- [Prefix 2]: [Value]
- Suffix 1: [Value]
- Suffix 2: [Value]

Goal: [What you want to achieve]
Budget: [X chaos] for omens
```

### Crafting Recommendation Format
```
✅ RECOMMENDATION: [Item Name] → [Target Stats]

**Current Slots**:
- Prefixes: 2/3 occupied (1 slot available)
- Suffixes: 2/3 occupied (1 slot available)

**Proposed Fix**:
1. Apply [Omen Name] (Xc) → Adds [Effect] as [Prefix/Suffix]
   - Targeting: [Specific slot]
   - Success Rate: Y%
   
**Expected Result**:
- Final mods: [Complete mod list after craft]
- Sell value: Xc
- Profit: Xc

**Success Criteria**: [What makes this a good craft]
```

---

## Common Item Examples

### Example 1: BOW with Physical Damage Focus

**Input**:
```
Base: Ranger Bow (5c buy)
Current Stats:
- Prefix 1: +15% Physical Damage
- Prefix 2: Empty
- Suffix 1: +15% Fire Resistance
- Suffix 2: Empty

Goal: Maximum physical damage for attack builds
Budget: 15c for omens
```

**Analysis**:
- Slots: 1 prefix available, 1 suffix available
- Current issue: Only 1 offensive mod, missing attack scaling

**Recommendation**:
```
✅ RECOMMENDATION: Physical Damage Bow Build

**Slot Analysis**:
- Prefixes: 1/3 occupied (2 slots available!) ← KEY OPPORTUNITY
- Suffixes: 1/3 occupied (2 slots available)

**Proposed Omen Sequence** (Cost: 15c):
1. Omen of Slaughter (8c) → Adds +25% Physical Damage prefix
   - Targets empty prefix slot
   - Success Rate: 70%
   
2. Omen of Accuracy (5c) → Adds accuracy suffix  
   - Targets empty suffix slot
   - Success Rate: 75%

**Expected Result After Craft**:
- Prefix 1: +15% Physical Damage (original)
- Prefix 2: +25% Physical Damage (NEW - from Omen of Slaughter)
- Suffix 1: +15% Fire Resistance (original)
- Suffix 2: +120 Accuracy Rating (NEW - from Omen of Accuracy)

**Final Item Value**: 55-65c
**Profit**: 30-40c (40% margin)
**Total Investment**: 5c (base) + 8c + 5c = 18c
```

### Example 2: SWORD with Fire Scaling

**Input**:
```
Base: Ranger Sword (8c buy)
Current Stats:
- Prefix 1: Adds 8-15 Fire Damage
- Prefix 2: +10% Fire Damage
- Suffix 1: +12% Fire Resistance
- Suffix 2: +8% Block Chance
- Suffix 3: FULL - No slots!

Goal: Add more fire damage without losing resistances
Budget: 20c for omens
Problem: No suffix slots available
```

**Analysis**:
- Cannot add more suffixes (full at 3/3)
- CAN add 1 more prefix (2/3 occupied)
- Strategy: Must use PREFIX-ONLY omens to avoid conflicts

**Recommendation**:
```
✅ RECOMMENDATION: Fire Scaling Sword (Conservative Approach)

**Slot Analysis**:
- Prefixes: 2/3 occupied (1 slot available) ✓
- Suffixes: 3/3 FULL - NO SPACE (Cannot add more!)

**Proposed Omen** (Cost: 15c):
1. Omen of Burning (15c) → Adds +18% Fire Damage prefix
   - Targets empty prefix slot #3
   - Success Rate: 68%
   - AVOIDS touching full suffix list

**Why This Works**:
- Only modifies prefixes (safe)
- Preserves all resistances/defenses
- Adds fire scaling without conflict

**Expected Result**:
- Prefix 1: Adds 8-15 Fire Damage
- Prefix 2: +10% Fire Damage  
- Prefix 3: +18% Fire Damage (NEW)
- Suffixes: UNCHANGED (all 3 preserved)

**Final Item Value**: 70-80c
**Profit**: 35-45c (50% margin)
**Risk Level**: LOW (no suffix changes)
```

### Example 3: AMULET - Full Crowded Item

**Input**:
```
Base: Gold Amulet (24c buy)
Current Stats:
- Prefix 1: +20 to Strength
- Prefix 2: +15% Spell Damage
- Prefix 3: FULL
- Suffix 1: +18% Fire Resistance
- Suffix 2: +12% Cold Resistance
- Suffix 3: FULL

Goal: Increase spell scaling without removing resistances
Budget: 25c for omens
Challenge: ALL SLOTS FULL (3/3 prefixes and suffixes)
```

**Analysis**:
- PROBLEM: No free slots at all!
- SOLUTION: Use omens that UPGRADE existing mods rather than add new ones
- Must use "replacement" approach

**Recommendation**:
```
⚠️ RECOMMENDATION: Amulet Upgrade (Advanced Approach)

**Slot Analysis**:
- Prefixes: 3/3 FULL
- Suffixes: 3/3 FULL
- Status: No free slots - Must use UPGRADE omnens

**Strategy - Replace Lowest Value Mod**:
1. Identify: Suffix 1 (+18% Fire Resistance) is lowest tier
2. Apply: Omen of Prosperity (20c)
   - Attempts to REPLACE lowest suffix with better one
   - Success Rate: 60% (riskier due to crowding)
   
**Outcomes**:
- 60% Success: Replaces Fire Resistance with +25% Fire Resistance OR different good suffix
- 40% Failure: Item unchanged, 20c wasted

**Expected Result (if successful)**:
- Prefix 1-3: UNCHANGED  
- Suffix 1: +25% Fire Resistance (UPGRADED)
- Suffix 2-3: UNCHANGED

**Final Item Value**: 85-95c
**Potential Profit**: 35-45c
**Risk Assessment**: MEDIUM (60% success, high value at stake)

**ALTERNATIVE (Lower Risk)**:
Skip this craft and find items with open slots for safer 70%+ success rates.
```

---

## Key Takeaways

1. **Always check slot availability first** (3 prefixes, 3 suffixes max)
2. **Match omen type to your goal**: Prefix-heavy build → suffix-specific omens
3. **Avoid full items** unless using deliberately for replacement strategy
4. **Success rates drop when slots are full** (competition for placement)
5. **Use prefix-specific omens to guarantee prefix modification**
6. **Use suffix-specific omens to guarantee suffix modification**

---

## Advanced: Omen Affinity Chart

| Build Type | Primary Omen | Secondary Omen | Why |
|-----------|----------|-----------|-----|
| Physical Attacker | Omen of Slaughter | Omen of Accuracy | Damage + Hit Chance |
| Fire Caster | Omen of Burning | Omen of Intellect | Spell damage + mana |
| Defensive Tank | Omen of Defiance | Omen of Resistance | Armor + Resistances |
| Critical Striker | Omen of Fortune | Omen of Slaughter | Crit + Phys hybrid |
| All-rounder | Omen of Prosperity | Omen of Prosperity | Flexible additions |
