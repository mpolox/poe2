# PoE2 Agent Query Templates

Last Updated: February 13, 2026

---

## Standard Query Patterns

Use these sentences to trigger specific crafting advice:

---

## Item Type Queries

### Boots
- "What bases are good for boots?"
- "Best boots to craft for profit?"
- "Which omen for boots?"
- "Boots crafting guide"
- "Most profitable boots this week?"
- "Boots base prices?"

### Gloves
- "What bases are good for gloves?"
- "Best gloves to craft?"
- "Gloves crafting strategy"
- "Most profitable gloves?"

### Helmet
- "Best helmet bases?"
- "Helmet crafting guide"
- "Profitable helmet builds?"

### Chest Armor
- "Best chest bases?"
- "Chest armor crafting?"
- "Chest armor strategy"

### Shields
- "Shield bases guide?"
- "Best shield crafts?"

### Weapons
- "Weapon crafting guide?"
- "Best weapon bases?"

### Jewelry
- "Ring crafting?"
- "Amulet strategy?"
- "Jewelry bases?"

### Flasks
- "Flask crafting?"
- "Best flask bases?"

---

## Specific Attribute Queries

### For Resistances/Defence
- "What base has [X% resistance]?"
- "Best base for defence?"
- "Armour scaling bases?"

### For Damage
- "Best damage bases?"
- "Crit scaling bases?"

### For Speed
- "Best Movement Speed bases?"
- "Fastest boots?"

---

## Profit/Economy Queries

### Profit Analysis
- "What's most profitable to craft?"
- "Best profit margin item?"
- "Should I craft [item]?"
- "Profit calculation for [base]?"

### Market Queries
- "What's the market price for [base]?"
- "How much does [item] sell for?"
- "Is there demand for [base]?"

### Budget Queries
- "What can I craft with 10 chaos?"
- "Best craft for low budget?"
- "High budget crafting options?"

---

## Omen/Currency Queries

### Omen Specific
- "What omens are best for [item]?"
- "Omen combination for [base]?"
- "What does [omen name] do?"
- "Cheapest effective omen?"

### Currency Queries
- "How much does [omen/currency] cost?"
- "Currency exchange rate?"
- "Total cost to craft [item]?"

---

## Comparison Queries

- "Which is more profitable: [base A] or [base B]?"
- "Compare [item 1] vs [item 2]"
- "Should I craft [item] or [item]?"

---

## Data Update Queries

- "Update prices"

---

## NEW: Specific Item Analysis Queries

### Item With Mods Provided
Use these formats to get analysis of items YOU ALREADY OWN:

**Format 1: Simple Item Description**
- "Analyze this [item type]:
  Current mods: [Mod 1], [Mod 2]
  Goal: [What you want]
  Budget: [X chaos]"

**Format 2: Detailed Item Description**
- "I have [base name] with:
  - [Mod 1]
  - [Mod 2]
  - [Mod 3]
  Can you tell me what omens to use?"

**Format 3: Problem-Focused**
- "My [item name] has [current mods]
  I want [desired outcome]
  What should I do?"

**Format 4: Technical Question**
- "How do I keep [Mod X] while adding [Mod Y]?"
- "Can I modify only prefixes on my [item]?"
- "My [item] is completely full. Any options?"

---

### Item Analysis Response Triggers
Asking about your SPECIFIC item will trigger:
1. ✅ Exact slot available calculation
2. ✅ Recommended omens matched to your situation
3. ✅ Success rate calculation based on slot status
4. ✅ Profit projection
5. ✅ Risk assessment

### Examples of Item Analysis Queries
- "I have Dragonscale Boots with +15% Fire Resist and need movement speed. Budget 10c."
- "My sword has: +20% Fire Damage, +10% Crit, +15 Fire Resist. Can I add cold resist?"
- "This amulet is full. What's the safest thing to try?"
- "Ranger Bow base. One prefix and both suffixes free. Best combo for profit?"
- "How do I keep my resistances while adding damage?"

---

### Key Differences

| Query Type | Example | Response |
|-----------|---------|----------|
| General | "Best boots?" | Generic guide with top 3 bases |
| Budget | "What can I make with 20c?" | Filtered options by price |
| Specific Item | "My boots have X mods, goal is Y" | Exact item analysis with slot math |

---

## Advanced Query Formats

### For Prefix/Suffix Specific Analysis
- Mention **exactly which mods** you want to keep
- Specify **which mods** are okay to change
- Ask about **slot availability** if unsure

### Example Advanced Queries
1. "My item has 3 resistances (suffixes). Can I add damage without losing resists?"
   → Answer: "Use prefix-only omens, suffixes stay safe"

2. "Both slots free: one prefix, one suffix. What should I fill first?"
   → Answer: Depends on build - shows both options

3. "I want to craft an item but have limited slots. What's the best use?"
   → Answer: Analyze slot scarcity, prioritize high-value mods

---

## How to Copy-Paste

**Use this template for easy item analysis request**:

```
Base: [Item name]
Current mods:
- [Mod 1]
- [Mod 2]
- [Mod 3]

Goal: [What you want]
Budget: [X chaos]
Constraints: [Any must-keeps?]
```

**Example**:
```
Base: Dragonscale Boots
Current mods:
- +20% Fire Damage
- +15% Fire Resistance

Goal: Add movement speed
Budget: 12c
Constraints: Must keep fire resist
```

→ Agent will respond with specific omen recommendations and slot analysis

---

## NEW: Item Replication Queries

### Want to Craft an Item Similar to One You Saw?

**Format 1: Simple Reference**
- "Can I craft something like the bow on PST?"
- "I want to make this item I saw on trade"
- "Replicate this amulet for me"

**Format 2: With Full Details**
- "I found this sword on trade:
  - Adds 15-22 Fire Damage
  - +25% Fire Damage
  - +120 Accuracy
  - +15% Fire Resistance
  
  How do I craft it? What's the cost?"

**Format 3: Budget Comparison**
- "This item costs 80c on market.
  Mods: [list mods]
  Can I craft it cheaper?"

**Format 4: Partial Information**
- "There's this amazing boots I want but I'm not sure all the mods.
  I know it has: +50% Movement Speed, resistances, and something else.
  What would complete it? Can I craft it?"

### Item Replication Response Includes:
✓ Identified prefix and suffix mods
✓ Recommended base item type
✓ Exact omen sequence needed
✓ Total crafting cost
✓ Comparison to market price
✓ Profitability decision: Craft or Buy?
✓ Step-by-step crafting checklist

### Examples of Replication Queries
1. "Analyze this bow from trade: Adds 18-25 Fire, +20% Fire, +15% Attack Speed, +18% Fire Resist. Should I craft or buy?"
2. "I want to make a fire caster amulet like this one: +25 Int, +20% Spell Damage, +12% Fire Res. How much?"
3. "My friend has this chest and I want one: +200 Life, resistances everywhere. What's the cheapest way?"
4. "Can I replicate this sword? [details] It's 60c on market right now..."

---

## See Also
- `/templates/item-analysis-template.md` - Full details on formatting item requests
- `/templates/item-query-examples.md` - Real example responses to item queries
- `/system/prefix-suffix-guide.md` - Technical details on prefix/suffix mechanics
- `/system/item-replication-guide.md` - How to request crafting replication of similar items
- "What's new this week?"
- "League economy update"
- "Demand changes?"

---

## How These Trigger Agent Responses

### Response Workflow
1. **Parse Query** - Identify item type and question type
2. **Lookup Relevant File** - Check guides/ and data/ directories
3. **Extract Key Info**:
   - Best bases from `/guides/[item]-crafting.md`
   - Current prices from `/league-data/base-price-tracker.md`
   - Omen combos from `/data/omens-database.md`
   - Profit calculations from `/data/profit-methodology.md`
4. **Format Response** - Present in clear checklist format
5. **Include Recommendation** - Green/Yellow/Red light assessment

---

## Response Format Template

```
📊 CRAFTING ADVICE: [Item Type]

✅ TOP BASES FOR PROFIT:
1. [Base Name] - [Cost]: [Profit/Margin]
2. [Base Name] - [Cost]: [Profit/Margin]

🔮 RECOMMENDED OMENS:
- [Omen 1] + [Omen 2]
- Cost: [X] chaos total
- Success Rate: [%]

💰 PROFIT ANALYSIS:
- Base: [X]c
- Crafting: [X]c
- Expected Sale: [X]c
- Net Profit: [X]c ✅/⚠️/❌

📋 QUICK CHECKLIST:
- [ ] Buy base
- [ ] Gather omens
- [ ] Apply omen sequence
- [ ] List for sale

⏰ MARKET NOTE: [Current condition]
```

---

## Priority Queries (Most Common)

1. "What should I craft?"
2. "What's most profitable?"
3. "Best boots bases?"
4. "How much profit?"
5. "What omens for [item]?"
