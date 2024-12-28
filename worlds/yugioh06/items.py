from typing import Dict, List

item_to_index: Dict[str, int] = {
    "LEGEND OF B.E.W.D.": 1,
    "METAL RAIDERS": 2,
    "PHARAOH'S SERVANT": 3,
    "PHARAONIC GUARDIAN": 4,
    "SPELL RULER": 5,
    "LABYRINTH OF NIGHTMARE": 6,
    "LEGACY OF DARKNESS": 7,
    "MAGICIAN'S FORCE": 8,
    "DARK CRISIS": 9,
    "INVASION OF CHAOS": 10,
    "ANCIENT SANCTUARY": 11,
    "SOUL OF THE DUELIST": 12,
    "RISE OF DESTINY": 13,
    "FLAMING ETERNITY": 14,
    "THE LOST MILLENIUM": 15,
    "CYBERNETIC REVOLUTION": 16,
    "ELEMENTAL ENERGY": 17,
    "SHADOW OF INFINITY": 18,
    "GAME GIFT COLLECTION": 19,
    "Special Gift Collection": 20,
    "Fairy Collection": 21,
    "Dragon Collection": 22,
    "Warrior Collection A": 23,
    "Warrior Collection B": 24,
    "Fiend Collection A": 25,
    "Fiend Collection B": 26,
    "Machine Collection A": 27,
    "Machine Collection B": 28,
    "Spellcaster Collection A": 29,
    "Spellcaster Collection B": 30,
    "Zombie Collection": 31,
    "Special Monsters A": 32,
    "Special Monsters B": 33,
    "Reverse Collection": 34,
    "LP Recovery Collection": 35,
    "Special Summon Collection A": 36,
    "Special Summon Collection B": 37,
    "Special Summon Collection C": 38,
    "Equipment Collection": 39,
    "Continuous Spell/Trap A": 40,
    "Continuous Spell/Trap B": 41,
    "Quick/Counter Collection": 42,
    "Direct Damage Collection": 43,
    "Direct Attack Collection": 44,
    "Monster Destroy Collection": 45,
    "All Normal Monsters": 46,
    "All Effect Monsters": 47,
    "All Fusion Monsters": 48,
    "All Traps": 49,
    "All Spells": 50,
    "All at Random": 51,
    "LD01 All except Level 4 forbidden Unlock": 52,
    "LD02 Medium/high Level forbidden Unlock": 53,
    "LD03 ATK 1500 or more forbidden Unlock": 54,
    "LD04 Flip Effects forbidden Unlock": 55,
    "LD05 Tributes forbidden Unlock": 56,
    "LD06 Traps forbidden Unlock": 57,
    "LD07 Large Deck A Unlock": 58,
    "LD08 Large Deck B Unlock": 59,
    "LD09 Sets Forbidden Unlock": 60,
    "LD10 All except LV monsters forbidden Unlock": 61,
    "LD11 All except Fairies forbidden Unlock": 62,
    "LD12 All except Wind forbidden Unlock": 63,
    "LD13 All except monsters forbidden Unlock": 64,
    "LD14 Level 3 or below forbidden Unlock": 65,
    "LD15 DEF 1500 or less forbidden Unlock": 66,
    "LD16 Effect Monsters forbidden Unlock": 67,
    "LD17 Spells forbidden Unlock": 68,
    "LD18 Attacks forbidden Unlock": 69,
    "LD19 All except E-Hero's forbidden Unlock": 70,
    "LD20 All except Warriors forbidden Unlock": 71,
    "LD21 All except Dark forbidden Unlock": 72,
    "LD22 All limited cards forbidden Unlock": 73,
    "LD23 Refer to Mar 05 Banlist Unlock": 74,
    "LD24 Refer to Sept 04 Banlist Unlock": 75,
    "LD25 Low Life Points Unlock": 76,
    "LD26 All except Toons forbidden Unlock": 77,
    "LD27 All except Spirits forbidden Unlock": 78,
    "LD28 All except Dragons forbidden Unlock": 79,
    "LD29 All except Spellcasters forbidden Unlock": 80,
    "LD30 All except Light forbidden Unlock": 81,
    "LD31 All except Fire forbidden Unlock": 82,
    "LD32 Decks with multiples forbidden Unlock": 83,
    "LD33 Special Summons forbidden Unlock": 84,
    "LD34 Normal Summons forbidden Unlock": 85,
    "LD35 All except Zombies forbidden Unlock": 86,
    "LD36 All except Earth forbidden Unlock": 87,
    "LD37 All except Water forbidden Unlock": 88,
    "LD38 Refer to Mar 04 Banlist Unlock": 89,
    "LD39 Monsters forbidden Unlock": 90,
    "LD40 Refer to Sept 05 Banlist Unlock": 91,
    "LD41 Refer to Sept 03 Banlist Unlock": 92,
    "TD01 Battle Damage Unlock": 93,
    "TD02 Deflected Damage Unlock": 94,
    "TD03 Normal Summon Unlock": 95,
    "TD04 Ritual Summon Unlock": 96,
    "TD05 Special Summon A Unlock": 97,
    "TD06 20x Spell Unlock": 98,
    "TD07 10x Trap Unlock": 99,
    "TD08 Draw Unlock": 100,
    "TD09 Hand Destruction Unlock": 101,
    "TD10 During Opponent's Turn Unlock": 102,
    "TD11 Recover Unlock": 103,
    "TD12 Remove Monsters by Effect Unlock": 104,
    "TD13 Flip Summon Unlock": 105,
    "TD14 Special Summon B Unlock": 106,
    "TD15 Token Unlock": 107,
    "TD16 Union Unlock": 108,
    "TD17 10x Quick Spell Unlock": 109,
    "TD18 The Forbidden Unlock": 110,
    "TD19 20 Turns Unlock": 111,
    "TD20 Deck Destruction Unlock": 112,
    "TD21 Victory D. Unlock": 113,
    "TD22 The Preventers Fight Back Unlock": 114,
    "TD23 Huge Revolution Unlock": 115,
    "TD24 Victory in 5 Turns Unlock": 116,
    "TD25 Moth Grows Up Unlock": 117,
    "TD26 Magnetic Power Unlock": 118,
    "TD27 Dark Sage Unlock": 119,
    "TD28 Direct Damage Unlock": 120,
    "TD29 Destroy Monsters in Battle Unlock": 121,
    "TD30 Tribute Summon Unlock": 122,
    "TD31 Special Summon C Unlock": 123,
    "TD32 Toon Unlock": 124,
    "TD33 10x Counter Unlock": 125,
    "TD34 Destiny Board Unlock": 126,
    "TD35 Huge Damage in a Turn Unlock": 127,
    "TD36 V-Z In the House Unlock": 128,
    "TD37 Uria, Lord of Searing Flames Unlock": 129,
    "TD38 Hamon, Lord of Striking Thunder Unlock": 130,
    "TD39 Raviel, Lord of Phantasms Unlock": 131,
    "TD40 Make a Chain Unlock": 132,
    "TD41 The Gatekeeper Stands Tall Unlock": 133,
    "TD42 Serious Damage Unlock": 134,
    "TD43 Return Monsters with Effects Unlock": 135,
    "TD44 Fusion Summon Unlock": 136,
    "TD45 Big Damage at once Unlock": 137,
    "TD46 XYZ In the House Unlock": 138,
    "TD47 Spell Counter Unlock": 139,
    "TD48 Destroy Monsters with Effects Unlock": 140,
    "TD49 Plunder Unlock": 141,
    "TD50 Dark Scorpion Combination Unlock": 142,
    "Campaign Tier 1 Column 1": 143,
    "Campaign Tier 1 Column 2": 144,
    "Campaign Tier 1 Column 3": 145,
    "Campaign Tier 1 Column 4": 146,
    "Campaign Tier 1 Column 5": 147,
    "Campaign Tier 2 Column 1": 148,
    "Campaign Tier 2 Column 2": 149,
    "Campaign Tier 2 Column 3": 150,
    "Campaign Tier 2 Column 4": 151,
    "Campaign Tier 2 Column 5": 152,
    "Campaign Tier 3 Column 1": 153,
    "Campaign Tier 3 Column 2": 154,
    "Campaign Tier 3 Column 3": 155,
    "Campaign Tier 3 Column 4": 156,
    "Campaign Tier 3 Column 5": 157,
    "Campaign Tier 4 Column 1": 158,
    "Campaign Tier 4 Column 2": 159,
    "Campaign Tier 4 Column 3": 160,
    "Campaign Tier 4 Column 4": 161,
    "Campaign Tier 4 Column 5": 162,
    "Campaign Tier 5 Column 1": 163,
    "Campaign Tier 5 Column 2": 164,
    "No Banlist": 167,
    "Banlist September 2003": 168,
    "Banlist March 2004": 169,
    "Banlist September 2004": 170,
    "Banlist March 2005": 171,
    "Banlist September 2005": 172,
    "5000DP": 254,
    "Remote": 255,
}

tier_1_opponents: List[str] = [
    "Campaign Tier 1 Column 1",
    "Campaign Tier 1 Column 2",
    "Campaign Tier 1 Column 3",
    "Campaign Tier 1 Column 4",
    "Campaign Tier 1 Column 5",
]

tier_2_opponents: List[str] = [
    "Campaign Tier 2 Column 1",
    "Campaign Tier 2 Column 2",
    "Campaign Tier 2 Column 3",
    "Campaign Tier 2 Column 4",
    "Campaign Tier 2 Column 5",
]

tier_3_opponents: List[str] = [
    "Campaign Tier 3 Column 1",
    "Campaign Tier 3 Column 2",
    "Campaign Tier 3 Column 3",
    "Campaign Tier 3 Column 4",
    "Campaign Tier 3 Column 5",
]

tier_4_opponents: List[str] = [
    "Campaign Tier 4 Column 1",
    "Campaign Tier 4 Column 2",
    "Campaign Tier 4 Column 3",
    "Campaign Tier 4 Column 4",
    "Campaign Tier 4 Column 5",
]

tier_5_opponents: List[str] = [
    "Campaign Tier 5 Column 1",
    "Campaign Tier 5 Column 2",
]

Banlist_Items: List[str] = [
    "No Banlist",
    "Banlist September 2003",
    "Banlist March 2004",
    "Banlist September 2004",
    "Banlist March 2005",
    "Banlist September 2005",
]

draft_boosters: List[str] = [
    "METAL RAIDERS",
    "PHARAOH'S SERVANT",
    "PHARAONIC GUARDIAN",
    "LABYRINTH OF NIGHTMARE",
    "LEGACY OF DARKNESS",
    "MAGICIAN'S FORCE",
    "DARK CRISIS",
    "INVASION OF CHAOS",
    "RISE OF DESTINY",
    "ELEMENTAL ENERGY",
    "SHADOW OF INFINITY",
]

draft_opponents: List[str] = ["Campaign Tier 1 Column 1", "Campaign Tier 1 Column 5"]

booster_packs: List[str] = [
    "LEGEND OF B.E.W.D.",
    "METAL RAIDERS",
    "PHARAOH'S SERVANT",
    "PHARAONIC GUARDIAN",
    "SPELL RULER",
    "LABYRINTH OF NIGHTMARE",
    "LEGACY OF DARKNESS",
    "MAGICIAN'S FORCE",
    "DARK CRISIS",
    "INVASION OF CHAOS",
    "ANCIENT SANCTUARY",
    "SOUL OF THE DUELIST",
    "RISE OF DESTINY",
    "FLAMING ETERNITY",
    "THE LOST MILLENIUM",
    "CYBERNETIC REVOLUTION",
    "ELEMENTAL ENERGY",
    "SHADOW OF INFINITY",
    "GAME GIFT COLLECTION",
    "Special Gift Collection",
    "Fairy Collection",
    "Dragon Collection",
    "Warrior Collection A",
    "Warrior Collection B",
    "Fiend Collection A",
    "Fiend Collection B",
    "Machine Collection A",
    "Machine Collection B",
    "Spellcaster Collection A",
    "Spellcaster Collection B",
    "Zombie Collection",
    "Special Monsters A",
    "Special Monsters B",
    "Reverse Collection",
    "LP Recovery Collection",
    "Special Summon Collection A",
    "Special Summon Collection B",
    "Special Summon Collection C",
    "Equipment Collection",
    "Continuous Spell/Trap A",
    "Continuous Spell/Trap B",
    "Quick/Counter Collection",
    "Direct Damage Collection",
    "Direct Attack Collection",
    "Monster Destroy Collection",
]

challenges: List[str] = [
    "LD01 All except Level 4 forbidden Unlock",
    "LD02 Medium/high Level forbidden Unlock",
    "LD03 ATK 1500 or more forbidden Unlock",
    "LD04 Flip Effects forbidden Unlock",
    "LD05 Tributes forbidden Unlock",
    "LD06 Traps forbidden Unlock",
    "LD07 Large Deck A Unlock",
    "LD08 Large Deck B Unlock",
    "LD09 Sets Forbidden Unlock",
    "LD10 All except LV monsters forbidden Unlock",
    "LD11 All except Fairies forbidden Unlock",
    "LD12 All except Wind forbidden Unlock",
    "LD13 All except monsters forbidden Unlock",
    "LD14 Level 3 or below forbidden Unlock",
    "LD15 DEF 1500 or less forbidden Unlock",
    "LD16 Effect Monsters forbidden Unlock",
    "LD17 Spells forbidden Unlock",
    "LD18 Attacks forbidden Unlock",
    "LD19 All except E-Hero's forbidden Unlock",
    "LD20 All except Warriors forbidden Unlock",
    "LD21 All except Dark forbidden Unlock",
    "LD22 All limited cards forbidden Unlock",
    "LD23 Refer to Mar 05 Banlist Unlock",
    "LD24 Refer to Sept 04 Banlist Unlock",
    "LD25 Low Life Points Unlock",
    "LD26 All except Toons forbidden Unlock",
    "LD27 All except Spirits forbidden Unlock",
    "LD28 All except Dragons forbidden Unlock",
    "LD29 All except Spellcasters forbidden Unlock",
    "LD30 All except Light forbidden Unlock",
    "LD31 All except Fire forbidden Unlock",
    "LD32 Decks with multiples forbidden Unlock",
    "LD33 Special Summons forbidden Unlock",
    "LD34 Normal Summons forbidden Unlock",
    "LD35 All except Zombies forbidden Unlock",
    "LD36 All except Earth forbidden Unlock",
    "LD37 All except Water forbidden Unlock",
    "LD38 Refer to Mar 04 Banlist Unlock",
    "LD39 Monsters forbidden Unlock",
    "LD40 Refer to Sept 05 Banlist Unlock",
    "LD41 Refer to Sept 03 Banlist Unlock",
    "TD01 Battle Damage Unlock",
    "TD02 Deflected Damage Unlock",
    "TD03 Normal Summon Unlock",
    "TD04 Ritual Summon Unlock",
    "TD05 Special Summon A Unlock",
    "TD06 20x Spell Unlock",
    "TD07 10x Trap Unlock",
    "TD08 Draw Unlock",
    "TD09 Hand Destruction Unlock",
    "TD10 During Opponent's Turn Unlock",
    "TD11 Recover Unlock",
    "TD12 Remove Monsters by Effect Unlock",
    "TD13 Flip Summon Unlock",
    "TD14 Special Summon B Unlock",
    "TD15 Token Unlock",
    "TD16 Union Unlock",
    "TD17 10x Quick Spell Unlock",
    "TD18 The Forbidden Unlock",
    "TD19 20 Turns Unlock",
    "TD20 Deck Destruction Unlock",
    "TD21 Victory D. Unlock",
    "TD22 The Preventers Fight Back Unlock",
    "TD23 Huge Revolution Unlock",
    "TD24 Victory in 5 Turns Unlock",
    "TD25 Moth Grows Up Unlock",
    "TD26 Magnetic Power Unlock",
    "TD27 Dark Sage Unlock",
    "TD28 Direct Damage Unlock",
    "TD29 Destroy Monsters in Battle Unlock",
    "TD30 Tribute Summon Unlock",
    "TD31 Special Summon C Unlock",
    "TD32 Toon Unlock",
    "TD33 10x Counter Unlock",
    "TD34 Destiny Board Unlock",
    "TD35 Huge Damage in a Turn Unlock",
    "TD36 V-Z In the House Unlock",
    "TD37 Uria, Lord of Searing Flames Unlock",
    "TD38 Hamon, Lord of Striking Thunder Unlock",
    "TD39 Raviel, Lord of Phantasms Unlock",
    "TD40 Make a Chain Unlock",
    "TD41 The Gatekeeper Stands Tall Unlock",
    "TD42 Serious Damage Unlock",
    "TD43 Return Monsters with Effects Unlock",
    "TD44 Fusion Summon Unlock",
    "TD45 Big Damage at once Unlock",
    "TD46 XYZ In the House Unlock",
    "TD47 Spell Counter Unlock",
    "TD48 Destroy Monsters with Effects Unlock",
    "TD49 Plunder Unlock",
    "TD50 Dark Scorpion Combination Unlock",
]

excluded_items: List[str] = [
    "All Normal Monsters",
    "All Effect Monsters",
    "All Fusion Monsters",
    "All Traps",
    "All Spells",
    "All at Random",
    "5000DP",
    "Remote",
]

useful: List[str] = [
    "Banlist March 2004",
    "Banlist September 2004",
    "Banlist March 2005",
    "Banlist September 2005",
]

core_booster: List[str] = [
    "LEGEND OF B.E.W.D.",
    "METAL RAIDERS",
    "PHARAOH'S SERVANT",
    "PHARAONIC GUARDIAN",
    "SPELL RULER",
    "LABYRINTH OF NIGHTMARE",
    "LEGACY OF DARKNESS",
    "MAGICIAN'S FORCE",
    "DARK CRISIS",
    "INVASION OF CHAOS",
    "ANCIENT SANCTUARY",
    "SOUL OF THE DUELIST",
    "RISE OF DESTINY",
    "FLAMING ETERNITY",
    "THE LOST MILLENIUM",
    "CYBERNETIC REVOLUTION",
    "ELEMENTAL ENERGY",
    "SHADOW OF INFINITY",
]