# Item Analysis Template

Use this template to request specific crafting recommendations for items with detailed attributes.

---

## Copy-Paste Template

```
## Item Analysis Request: [Item Name]

### Base Information
- **Base Name**: [e.g., Ranger Bow, Iron Sword, Gold Amulet]
- **Base Type**: [e.g., One-Handed Sword, Body Armour, Gloves]
- **Buy Cost**: [Xc]
- **Target Sell Price**: [Yc]

### Current Modifiers

#### Prefixes (Offensive/Scaling)
- [ ] Prefix 1: [Mod name + value] (e.g., +15% Physical Damage)
- [ ] Prefix 2: [Mod name + value]
- [ ] Prefix 3: [Empty / Occupied]

#### Suffixes (Defensive/Utility)
- [ ] Suffix 1: [Mod name + value] (e.g., +18% Fire Resistance)
- [ ] Suffix 2: [Mod name + value]
- [ ] Suffix 3: [Empty / Occupied]

### Crafting Goal
**What I want**: [Describe desired final stats]
**Priority**: [Offense / Defense / Balanced]
**Budget**: [Xc maximum to spend on omens]

### Constraints
- [ ] Must keep: [Specific mods you don't want removed]
- [ ] Can modify: [Mods you're okay changing]
- [ ] Avoid: [Specific effects you don't want]

### Additional Notes
[Any other details about build or playstyle]
```

---

## Completed Examples

### Example A: Bow with Physical Damage
```
## Item Analysis Request: Physical Damage Bow

### Base Information
- **Base Name**: Ranger Bow
- **Base Type**: Bow (Two-Handed)
- **Buy Cost**: 5c
- **Target Sell Price**: 55-65c

### Current Modifiers

#### Prefixes (Offensive/Scaling)
- [x] Prefix 1: +15% Physical Damage
- [ ] Prefix 2: [Empty - Available]
- [ ] Prefix 3: [Empty - Available]

#### Suffixes (Defensive/Utility)
- [x] Suffix 1: +15% Fire Resistance
- [ ] Suffix 2: [Empty - Available]
- [ ] Suffix 3: [Empty - Available]

### Crafting Goal
**What I want**: Maximize physical damage output with accuracy
**Priority**: Offense
**Budget**: 15c

### Constraints
- [x] Must keep: Fire Resistance (for survivability)
- [x] Can modify: Any empty slots
- [x] Avoid: Negative attributes
```

**→ See Prefix/Suffix Mechanics Guide for full analysis**

---

### Example B: Sword with Fire Scaling (Full Suffixes)
```
## Item Analysis Request: Fire Scaling Sword

### Base Information
- **Base Name**: Ranger Sword
- **Base Type**: One-Handed Sword
- **Buy Cost**: 8c
- **Target Sell Price**: 70-80c

### Current Modifiers

#### Prefixes (Offensive/Scaling)
- [x] Prefix 1: Adds 8-15 Fire Damage
- [x] Prefix 2: +10% Fire Damage
- [ ] Prefix 3: [Empty - Available]

#### Suffixes (Defensive/Utility)
- [x] Suffix 1: +12% Fire Resistance
- [x] Suffix 2: +8% Block Chance
- [x] Suffix 3: Reserved (FULL)

### Crafting Goal
**What I want**: Add more fire scaling without losing defenses
**Priority**: Offense with defense preservation
**Budget**: 15c

### Constraints
- [x] Must keep: Fire & Block (essential for build)
- [x] Can modify: Prefixes only (suffixes at max)
- [x] Avoid: Suffix overwrite (would lose resistances)
```

**→ See Prefix/Suffix Mechanics Guide for full analysis**

---

### Example C: Amulet (All Slots Full)
```
## Item Analysis Request: Full Amulet Upgrade

### Base Information
- **Base Name**: Gold Amulet
- **Base Type**: Amulet
- **Buy Cost**: 24c
- **Target Sell Price**: 85-95c

### Current Modifiers

#### Prefixes (Offensive/Scaling)
- [x] Prefix 1: +20 to Strength
- [x] Prefix 2: +15% Spell Damage
- [x] Prefix 3: [FULL]

#### Suffixes (Defensive/Utility)
- [x] Suffix 1: +18% Fire Resistance
- [x] Suffix 2: +12% Cold Resistance
- [x] Suffix 3: [FULL]

### Crafting Goal
**What I want**: Enhance spell scaling while preserving resistances
**Priority**: Offense (but keep defenses)
**Budget**: 25c for risky upgrade

### Constraints
- [x] Must keep: Both resistances (survivability critical)
- [x] Can modify: Fire resistance can be upgraded OR replaced
- [x] Avoid: Losing more than one stat
```

**→ See Prefix/Suffix Mechanics Guide for full analysis (Advanced Section)**

---

## How to Use This System

1. **Pick the right template** based on your item's slot status
2. **Fill in current mods** exactly as they appear on the item
3. **State your goal clearly** - don't be vague
4. **Set a budget** - this determines what omens are feasible
5. **Mention constraints** - what you MUST keep vs can change
6. **Submit** - AI will provide detailed crafting path with success rates

### Example Query Format
> "Analyze this item for me:
> 
> Base: Iron Treads (boots)
> Current: +15% Fire Damage, +20 Evasion, +15% Fire Resistance
> Goal: Add cold resistance without losing fire resist
> Budget: 10c
> 
> I'm a fire caster and need both resistances for endgame."

---

## Analysis Output Includes

✓ Slot availability assessment  
✓ Omen recommendations (specific omens by name)  
✓ Expected success rates  
✓ Final mod list after craft  
✓ Profit calculation  
✓ Risk assessment  
✓ Alternative strategies if applicable  

---

## Pro Tips

- **Items with 2-3 open slots**: Easiest to craft (70%+ success)
- **Items with 1 open slot**: Moderate difficulty (65-70% success)  
- **Items with NO open slots**: Advanced only (50-60% success, risky)
- **Full items**: Consider restarting unless upgrade yield high value
- **Balanced items**: Better to fill offense first, then defense

---

## Quick Reference: Slot Status

| Prefix Slots | Suffix Slots | Difficulty | Strategy |
|----------|----------|------------|----------|
| 0/3 (Full) | 0/3 (Full) | 🔴 Extreme | Use replacement omens only |
| 1/3 (1 slot) | 1/3 (1 slot) | 🟢 Easy | Use specific-type omens |
| 2/3 (2 slots) | 1/3 (1 slot) | 🟢 Easy | Fill prefixes first |
| 0/3 (Full) | 2/3 (1 slot) | 🟡 Medium | Must use suffix-only omen |
| 1/3 (1 slot) | 0/3 (Full) | 🟡 Medium | Must use prefix-only omen |
