from typing import Dict, List, Tuple

from .Locations import (
    LocationData,
    arctic_docks,
    battle_towers,
    battle_trenches,
    castle_courtyard,
    castle_treasury,
    chimeras_keep,
    cliffs_of_desolation,
    crystal_mine,
    dagger_peak,
    desecrated_temple,
    dragons_lair,
    dungeon_of_torment,
    erupting_fissure,
    frozen_camp,
    gates_of_the_underworld,
    haunted_cemetery,
    infernal_fortress,
    lost_cave,
    plague_fiend,
    poisoned_fields,
    tower_armory,
    toxic_air_ship,
    valley_of_fire,
    venomous_spire,
    volcanic_cavern,
    yeti,
)

# Item name to ram value conversion
inv_dict: Dict[Tuple, str] = {
    (0x0, 0x6, 0x0): "Gold",
    (0x0, 0x7, 0x0): "Key",
    (0x0, 0xA, 0x0): "Level",
    (0x0, 0xD, 0x0): "Max",
    (0x0, 0x70, 0x2): "Compass",
    (0x0, 0x8, 0x10): "Lightning Potion",
    (0x0, 0x8, 0x20): "Light Potion",
    (0x0, 0x8, 0x30): "Acid Potion",
    (0x0, 0x8, 0x40): "Fire Potion",
    (0x28, 0x80, 0x4): "Acid Breath",
    (0x28, 0xF0, 0x4): "Lightning Breath",
    (0x28, 0x60, 0x4): "Fire Breath",
    (0x18, 0x70, 0x8): "Light Amulet",
    (0x18, 0x80, 0x8): "Acid Amulet",
    (0x18, 0xF0, 0x8): "Lightning Amulet",
    (0x18, 0x60, 0x8): "Fire Amulet",
    (0x14, 0xF0, 0xC): "Lightning Shield",
    (0x14, 0x60, 0xC): "Fire Shield",
    (0x10, 0xE0, 0x0): "Invisibility",
    (0x10, 0x30, 0x0): "Levitate",
    (0x10, 0x73, 0x1): "Speed Boots",
    (0x50, 0x20, 0x0): "3-Way Shot",
    (0x50, 0x60, 0x1): "5-Way Shot",
    (0x10, 0x50, 0x0): "Rapid Fire",
    (0x18, 0x40, 0x8): "Reflective Shot",
    (0x14, 0x40, 0xC): "Reflective Shield",
    (0x28, 0xB0, 0x8): "Super Shot",
    (0x10, 0xD0, 0x0): "Timestop",
    (0x10, 0x10, 0x1): "Phoenix Familiar",
    (0x10, 0x20, 0x1): "Growth",
    (0x10, 0x30, 0x1): "Shrink",
    (0x28, 0x40, 0x9): "Thunder Hammer",
    (0x11, 0xA0, 0x0): "Anti-Death Halo",
    (0x11, 0xC0, 0x0): "Invulnerability",
    (0x0, 0x1, 0x0): "Fruit",
    (0x0, 0x1, 0x0): "Meat",
    (0x0, 0x1, 0x0): "Health",
    (0x0, 0x10, 0x82): "Runestone",
    (0x0, 0x60, 0x82): "Mirror Shard",
    (0x22, 0xC0, 0x1): "Ice Axe of Untar",
    (0x22, 0xD0, 0x1): "Flame of Tarkana",
    (0x22, 0xE0, 0x1): "Scimitar of Decapitation",
    (0x22, 0xF0, 0x1): "Marker's Javelin",
    (0x22, 0x0, 0x2): "Soul Savior",
    (0x0, 0x4A, 0x80): "Mountain",
    (0x0, 0x1A, 0x80): "Castle",
    (0x0, 0x6A, 0x80): "Hell",
    (0x0, 0x7A, 0x80): "Ice",
    (0x0, 0x8A, 0x80): "Town",
    (0x0, 0x9A, 0x80): "Temple",
    (0x0, 0xDA, 0x80): "Battlefield",
    (0x0, 0xEA, 0x80): "Skorne",
    (0x0, 0xFA, 0x80): "Secret",  # I have no clue if this is correct
    (0x0, 0xC, 0x80): "Obelisk",
    (0x0, 0xA1, 0x1): "Minotaur",
    (0x0, 0xA2, 0x1): "Falconess",
    (0x0, 0xA3, 0x1): "Jackal",
    (0x0, 0xA4, 0x1): "Tigress",
    (0x0, 0xA5, 0x1): "Sumner",
}

# Character names used for slot data
characters = ["Minotaur", "Falconess", "Tigress", "Jackal", "Sumner"]

# Item ID to rom ID conversion
item_dict: Dict[int, bytes] = {
    77780000: [0x0, 0x0],
    77780001: [0x1, 0x1],
    77780002: [0x1, 0x2],
    77780003: [0x1, 0x3],
    77780004: [0x1, 0x4],
    77780005: [0x2, 0x12],
    77780006: [0x2, 0x11],
    77780007: [0x2, 0x10],
    77780008: [0x2, 0x9],
    77780009: [0x2, 0xA],
    77780010: [0x2, 0x8],
    77780011: [0x2, 0x7],
    77780012: [0x2, 0x18],
    77780013: [0x2, 0x17],
    77780014: [0x2, 0x5],
    77780015: [0x2, 0x1C],
    77780016: [0x2, 0x0],
    77780017: [0x2, 0x4],
    77780018: [0x2, 0xE],
    77780019: [0x2, 0x1A],
    77780020: [0x2, 0x2],
    77780021: [0x2, 0x16],
    77780022: [0x2, 0x3],
    77780023: [0x2, 0xC],
    77780024: [0x2, 0x13],
    77780025: [0x2, 0x14],
    77780026: [0x2, 0x15],
    77780027: [0x2, 0x19],
    77780028: [0x2, 0xD],
    77780029: [0x2, 0x6],
    77780030: [0x4, 0x1],
    77780031: [0x4, 0x3],
    77780032: [0x15, 0x1],
    77780033: [0x15, 0x2],
    77780034: [0x15, 0x3],
    77780035: [0x15, 0x4],
    77780036: [0x15, 0x5],
    77780037: [0x15, 0x6],
    77780038: [0x15, 0x7],
    77780039: [0x15, 0x8],
    77780040: [0x15, 0x9],
    77780041: [0x15, 0xA],
    77780042: [0x15, 0xB],
    77780043: [0x15, 0xC],
    77780044: [0x15, 0xD],
    77780045: [0x2B, 0x1],
    77780046: [0x2B, 0x2],
    77780047: [0x2B, 0x3],
    77780048: [0x2B, 0x4],
    77780049: [0x29, 0x1],
    77780050: [0x29, 0x2],
    77780051: [0x29, 0x3],
    77780052: [0x29, 0x4],
    77780053: [0x29, 0x5],
    77780054: [0x3, 0x2],
    77780062: [0x21, 0x1],
    77780063: [0x4, 0x2],
}

# Items that use a timer
timers = [
    "Light Amulet",
    "Acid Amulet",
    "Lightning Amulet",
    "Fire Amulet",
    "Lightning Shield",
    "Fire Shield",
    "Invisibility",
    "Levitate",
    "Speed Boots",
    "3-Way Shot",
    "5-Way Shot",
    "Rapid Fire",
    "Reflective Shot",
    "Reflective Shield",
    "Timestop",
    "Phoenix Familiar",
    "Growth",
    "Shrink",
    "Anti-Death Halo",
    "Invulnerability",
]

# Base item charge count per pickup
# Some items are bitwise
base_count: Dict[str, int] = {
    "Key": 1,
    "Lightning Potion": 1,
    "Light Potion": 1,
    "Acid Potion": 1,
    "Fire Potion": 1,
    "Acid Breath": 5,
    "Lightning Breath": 5,
    "Fire Breath": 5,
    "Light Amulet": 30,
    "Acid Amulet": 30,
    "Lightning Amulet": 30,
    "Fire Amulet": 30,
    "Lightning Shield": 10,
    "Fire Shield": 10,
    "Invisibility": 30,
    "Levitate": 30,
    "Speed Boots": 30,
    "3-Way Shot": 30,
    "5-Way Shot": 30,
    "Rapid Fire": 30,
    "Reflective Shot": 30,
    "Reflective Shield": 30,
    "Super Shot": 3,
    "Timestop": 15,
    "Phoenix Familiar": 30,
    "Growth": 30,
    "Shrink": 30,
    "Thunder Hammer": 3,
    "Anti-Death Halo": 30,
    "Invulnerability": 30,
    "Fruit": 50,
    "Meat": 100,
    "Gold": 100,
    "Runestone 1": 1,
    "Runestone 2": 2,
    "Runestone 3": 4,
    "Runestone 4": 8,
    "Runestone 5": 16,
    "Runestone 6": 32,
    "Runestone 7": 64,
    "Runestone 8": 128,
    "Runestone 9": 256,
    "Runestone 10": 512,
    "Runestone 11": 1024,
    "Runestone 12": 2048,
    "Runestone 13": 4096,
    "Dragon Mirror Shard": 1,
    "Chimera Mirror Shard": 4,
    "Plague Fiend Mirror Shard": 8,
    "Yeti Mirror Shard": 2,
    "Mountain Obelisk 1": 1,
    "Mountain Obelisk 2": 2,
    "Mountain Obelisk 3": 4,
    "Town Obelisk 1": 8,
    "Town Obelisk 2": 16,
    "Castle Obelisk 1": 32,
    "Castle Obelisk 2": 64,
    "Ice Axe of Untar": 1,
    "Flame of Tarkana": 1,
    "Scimitar of Decapitation": 1,
    "Marker's Javelin": 1,
    "Soul Savior": 1,
    "Minotaur": 1,
    "Falconess": 1,
    "Tigress": 1,
    "Jackal": 1,
    "Sumner": 1,
    "Poison Fruit": -50,
}

# Level area ID to area name conversion
levels: Dict[int, str] = {
    0x1: "Castle",
    0x2: "Mountain",
    0x7: "Town",
    0x8: "Hell",
    0x9: "Ice",
    0xF: "Boss",
    0x11: "Battlefield",
}

# Castle level ID order
castle_id = [1, 6, 3, 4, 5]

# Area ID << 4 + Level ID to raw location list conversion
level_locations: Dict[int, List[LocationData]] = {
    0x11: castle_courtyard,
    0x12: dungeon_of_torment,
    0x13: tower_armory,
    0x14: castle_treasury,
    0x15: chimeras_keep,
    0x21: valley_of_fire,
    0x22: dagger_peak,
    0x23: cliffs_of_desolation,
    0x24: lost_cave,
    0x25: volcanic_cavern,
    0x26: dragons_lair,
    0x71: poisoned_fields,
    0x72: haunted_cemetery,
    0x73: venomous_spire,
    0x74: toxic_air_ship,
    0x75: plague_fiend,
    0x81: gates_of_the_underworld,
    0x91: arctic_docks,
    0x92: frozen_camp,
    0x93: crystal_mine,
    0x94: erupting_fissure,
    0x95: yeti,
    0xF1: desecrated_temple,
    0x111: battle_trenches,
    0x112: battle_towers,
    0x113: infernal_fortress,
}

# Count of all spawners in a level
# Used for obj_read address offset calculation
# Vaules are spawner difficulty
spawners: Dict[int, List[int]] = {
    0x11: [0, 0, 0, 4, 3, 2, 0, 0, 2, 4, 2, 0, 2, 4, 0, 3, 4, 4, 3, 0, 2, 0, 0, 3, 4, 0, 2, 2, 0, 3, 0, 4, 3, 0, 0, 2, 0, 2, 2, 4, 3, 0, 3, 2, 4, 2, 2, 2, 4, 0, 4, 3, 2, 0, 4, 0, 3, 3, 4, 2, 3, 0, 0, 0, 2, 3, 4, 2, 2, 2, 2, 0, 3, 2, 0, 2, 0, 0, 3, 0, 4, 2, 2, 0, 0, 0, 3, 0, 3, 0, 3, 3, 0, 0, 4, 4, 3, 0, 2, 0, 2, 3, 0, 4, 0, 2, 2, 0, 2, 4, 0, 2, 0, 3, 4, 0, 4, 3, 2, 0, 3, 0],
    0x12: [0, 0, 0, 2, 3, 2, 0, 2, 0, 2, 3, 0, 2, 0, 2, 0, 3, 2, 0, 3, 2, 0, 3, 0, 0, 2, 0, 3, 0, 0, 4, 3, 0, 0, 0, 2, 4, 3, 2, 2, 0, 0, 0, 0, 2, 2, 0, 2, 0, 3, 4, 3, 0, 0, 2, 2, 3, 3, 3, 2, 2, 4, 4, 4],
    0x13: [0, 0, 0, 2, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 4, 4, 2, 3, 0, 0, 3, 0, 2, 0, 2, 3, 3, 2, 0, 0, 2, 3, 0, 2, 0, 4, 2, 4, 2, 2, 3, 0, 2, 0, 3, 4, 3, 0, 0, 3, 3, 3, 4, 2, 3, 4, 3, 0, 0, 3, 2, 2, 2, 0, 2, 0, 3, 2, 0, 2, 0, 4, 4, 3, 0, 4, 3, 0, 0, 2, 3, 4],
    0x14: [3, 2, 3, 0, 0, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 3, 2, 0, 3, 0, 0, 0, 2, 0, 0, 0, 3, 0, 4, 0, 0, 3, 2, 4, 3, 0, 0, 4, 3, 2, 4, 3, 4, 3, 2, 0, 2, 4, 2, 0, 3, 3, 4, 2, 0, 0, 0, 2, 2, 3, 4, 0, 3, 4, 4, 0, 2, 0, 2, 2, 0, 3, 2, 4, 0, 3, 2, 0, 0, 0, 4, 4, 0, 0, 0],
    0x15: [],
    0x21: [4, 0, 4, 2, 2, 0, 0, 2, 0, 3, 3, 0, 0, 2, 2, 0, 4, 0, 3, 2, 3, 0, 0, 2, 4, 2, 3, 2, 3, 4, 2, 3, 4],
    0x22: [0, 2, 2, 0, 2, 3, 2, 0, 3, 3, 4, 4, 4, 4, 2, 2, 3, 0, 4, 0, 0, 0, 2, 0, 2, 0, 0, 3, 3, 4, 3, 2, 4, 0, 0, 3, 0, 4, 0, 3, 0, 2, 0, 0, 2, 0, 3, 2, 4, 0, 0, 0, 3, 2, 0],
    0x23: [3, 0, 0, 2, 3, 0, 3, 2, 4, 3, 2, 0, 2, 3, 0, 3, 0, 0, 4, 2, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 4, 3, 3, 4, 0, 0, 0, 3, 0, 3, 0, 3, 0, 4, 3, 2, 2, 2, 0, 0, 4, 3, 4, 0, 2, 2, 2, 0, 2, 3, 0, 4, 2, 4, 4, 2, 0, 4, 2, 0, 2, 2, 3, 0, 2, 3, 4, 0, 0, 3, 4, 0, 0, 3, 0, 2],
    0x24: [0, 2, 3, 0, 3, 0, 0, 0, 4, 0, 2, 0, 4, 0, 3, 0, 3, 0, 3, 2, 4, 2, 0, 0, 0, 0, 0, 3, 0, 0, 4, 0, 4, 2, 2, 2, 0, 2, 2, 3, 0, 2, 0, 2, 0, 0, 2, 2, 3, 4, 0, 3, 2, 2, 0, 0, 3, 2, 3, 3, 4, 2, 3, 4, 0, 2, 3, 0, 0],
    0x25: [3, 0, 4, 0, 0, 2, 3, 0, 4, 2, 0, 2, 3, 0, 3, 0, 4, 2, 0, 2, 3, 4, 3, 2, 0, 2, 0, 2, 2, 3, 4, 3, 0, 0, 3, 0, 2, 4, 3, 0, 4, 2, 4, 3, 2, 0, 2, 0, 2, 3, 3, 0, 2, 3, 4, 2, 0, 4, 0, 0, 3, 0, 0, 2, 2, 4, 0, 3, 4, 3, 2, 3, 4, 0, 0, 0, 0, 2, 3, 3, 0, 4, 0],
    0x26: [],
    0x71: [0, 0, 2, 3, 0, 0, 2, 0, 0, 3, 4, 4, 4, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 2, 0, 0, 0, 2, 3, 3, 0, 2, 0, 3, 3, 2, 2, 0, 2, 0, 2, 3, 0, 4, 0, 3, 2, 3, 0, 2, 4, 3, 0, 4, 4, 0, 3, 0, 0, 2, 4, 3, 0, 2, 4, 0, 3, 2, 4, 2, 4, 3, 2, 0, 0, 2, 3, 0, 0, 2, 2, 3, 0, 3, 2, 0, 0, 0, 0, 2, 0, 2, 3, 2, 2, 2, 2, 0, 0, 4, 4, 2, 0, 2, 0, 2, 3, 4, 0, 2, 4, 2, 0, 2, 3, 3, 3, 0, 2, 0, 4, 0, 2, 0, 4, 4, 0, 4, 0, 0, 3, 2, 3, 0, 4, 2, 0, 0, 4, 4, 0, 3, 0, 0, 0, 0, 0, 2, 3, 0, 2, 0, 4, 2, 2, 3, 4, 0, 0, 0, 0, 3, 3],
    0x72: [0, 0, 4, 4, 4, 4, 3, 0, 4, 0, 4, 0, 3, 0, 0, 3, 0, 0, 2, 0, 0, 2, 0, 3, 0, 2, 0, 0, 2, 0, 0, 0, 3, 0, 0, 2, 2, 4, 0, 4, 0, 2, 2, 4, 2, 2, 3, 3, 3, 2, 3, 0, 4, 2, 4, 0, 4, 0, 0, 2, 0, 3, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 2, 2, 3, 4, 2, 3, 0, 3, 3, 2, 2, 0, 0, 0, 0, 0, 2, 4, 3, 0, 0, 2, 0, 3, 3, 0, 0, 2, 2, 0, 0, 2, 0, 2, 0, 2, 0, 4, 2, 4, 2, 0, 0, 0, 4, 3, 2, 0, 0, 2, 0, 3, 3, 0, 0, 3, 3, 0, 0, 2, 0, 3, 4, 3, 0, 2, 3, 0, 0, 4, 0, 0, 3, 2, 0, 2, 3, 2, 0, 0, 3],
    0x73: [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 2, 0, 2, 3, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 2, 0, 2, 0, 3, 0, 0, 0, 2, 0, 0, 3, 0, 0, 2, 4, 0, 4, 0, 3, 0, 2, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 2, 0, 3, 0, 2, 3, 2, 3, 0, 4, 2, 0, 0, 0, 4, 0, 2, 0, 2, 0, 4, 0, 4, 3, 0, 0, 0, 2, 0, 2, 2, 3, 2, 0, 3, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 3, 2, 0, 2, 0, 4, 3, 2],
    0x74: [4, 4, 0, 3, 4, 4, 4, 0, 3, 4, 4, 0, 2, 0, 0, 3, 0, 2, 0, 0, 2, 3, 0, 0, 0, 2, 0, 2, 2, 3, 2, 3, 3, 0, 2, 3, 0, 3, 0, 0, 0, 2, 0, 0, 2, 3, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 2, 0, 2, 2, 2, 0, 2, 0, 0, 2, 0, 3, 0, 0, 0, 2, 3, 2, 0, 0, 0, 3, 0, 3, 0, 0, 2, 0, 2, 0, 3, 3, 2, 0, 0, 4, 3, 2, 2, 0, 2, 3, 0, 2, 0, 2, 0, 2, 3, 0, 3, 0, 2, 2, 0, 3, 0, 4, 4],
    0x75: [],
    0x81: [4, 0, 0, 3, 2, 0, 0, 2, 0, 3, 3, 3, 0, 4, 0, 0, 3, 0, 3, 2, 0, 4, 0, 0, 4, 4, 3, 0, 2, 0, 0, 0, 0, 0, 0, 4, 3, 0, 2, 0, 2, 0, 0, 0, 4, 0, 2, 0, 3, 2, 0, 0, 4, 2, 0, 0, 2, 0, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 0, 3, 4, 3, 4, 3, 3, 4, 4, 3, 4, 3, 4, 3, 4, 3, 3, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 2, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 3, 4, 4, 4, 0, 3, 2, 0, 0, 0],
    0x91: [0, 0, 0, 0, 2, 0, 0, 3, 4, 4, 2, 0, 0, 2, 0, 4, 3, 0, 3, 4, 0, 2, 3, 4, 2, 0, 3, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 4, 2, 0, 3, 0, 2, 3, 0, 0, 2, 4, 3, 0, 3, 2, 4, 0, 2, 0, 0, 2, 3, 4, 2, 0, 0, 2, 0, 3, 2, 0, 2, 2, 0, 0, 3, 2, 0, 0, 2, 3, 0, 3, 0, 0, 2, 3, 4, 0, 0, 2, 2, 0, 3, 2, 0, 3, 0, 4, 3, 2, 4, 0, 2, 0, 2, 0, 3, 0, 0, 2, 0, 0, 4, 0, 0, 3, 0, 2, 0, 0, 0, 0, 3, 0, 4, 2, 3, 0, 2, 2, 4, 3, 2, 0, 2, 3, 0, 2, 0, 2, 3, 4, 0, 4, 2, 0, 0, 2, 0, 0, 2, 0, 2, 3, 0, 2, 0, 2, 0, 4, 3, 0, 2, 0, 0, 2, 3, 0, 2, 0, 4, 3, 2, 0, 4, 0, 0, 2, 0, 3, 0, 2, 0, 2, 0, 0, 2, 3, 2, 0, 3, 0, 4, 2, 3, 0, 2, 2, 0, 3, 0, 3, 2, 2, 0, 4, 0, 2, 0, 3, 0, 2, 0, 0, 2, 3, 2, 0, 3, 3, 2, 0, 3, 2, 2, 3, 2, 2, 0, 2, 0, 0, 2, 2, 0, 3, 2, 0, 0],
    0x92: [0, 0, 0, 3, 0, 0, 2, 0, 4, 0, 3, 4, 0, 4, 0, 0, 0, 3, 0, 0, 2, 4, 3, 0, 0, 3, 3, 4, 3, 0, 2, 0, 2, 0, 0, 3, 3, 4, 0, 0, 2, 0, 0, 2, 0, 4, 0, 2, 4, 0, 3, 2, 0, 4, 3, 0, 2, 3, 2, 0, 3, 0, 2, 4, 2, 0, 3, 0, 4, 0, 3, 0, 2, 0, 4, 3, 2, 0, 2, 0, 2, 0, 3, 0, 0, 0, 3, 0, 2, 0, 2, 0, 2, 2, 0, 2, 2, 0, 0, 2, 3, 2, 2, 4, 0, 3, 4, 0, 0, 2, 0, 0, 3, 0, 4, 0, 0, 0, 0, 0, 3, 3, 4, 0, 2, 0, 0, 2, 0, 3, 2, 0, 4, 3, 4, 2, 0, 0, 3, 0, 2, 0, 0, 3, 0, 0, 3, 2, 0, 2, 0, 3, 4, 3, 4, 2, 0, 0, 2, 4, 3, 0, 4, 2, 0, 0, 2, 3, 2, 0, 0],
    0x93: [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 4, 0, 2, 0, 2, 0, 4, 3, 0, 0, 2, 3, 0, 3, 0, 3, 4, 2, 0, 3, 4, 2, 0, 0, 2, 0, 3, 2, 4, 0, 0, 2, 0, 0, 3, 2, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2, 0, 4, 3, 2, 0, 4, 3, 0, 2, 2, 0, 0, 4, 0, 3, 0, 2, 0, 4, 3, 3, 0, 2, 3, 4, 0, 2, 2, 0, 3, 0, 2, 0, 3, 0, 2, 0, 4, 3, 2, 0, 4, 0, 2, 0, 3, 4, 2, 3, 0, 2, 0, 0, 0, 3, 4, 2, 2, 0, 3, 4, 0, 2, 0, 3, 0, 2, 3, 0, 0, 3, 2, 4, 2, 0, 0, 3, 0, 2, 0, 4, 3, 2, 0, 2, 0, 2, 0, 0, 2, 3, 2, 0, 0, 0, 3, 4, 0, 3, 0, 2, 2, 2, 2, 3, 4, 0, 4, 0, 2, 3, 0, 2, 0, 2, 3, 2, 4, 0, 0, 3, 3, 0, 2, 3, 4, 0, 2, 2, 3, 0, 0, 4, 3],
    0x94: [4, 4, 4, 3, 3, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 3, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 3, 2, 4, 4, 0, 4, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0, 2, 3, 2, 0, 2, 4, 3, 0, 0, 2, 0, 3, 0, 2, 2, 3, 0, 0, 0, 2, 0, 3, 4, 3, 2, 2, 3, 0, 3, 0, 2, 2, 0, 4, 0, 3, 0, 4, 0, 2, 0, 3, 4, 2, 0, 2, 3, 4, 0, 0, 3, 0, 0, 2, 2, 4, 0, 2, 4, 4, 2, 2, 4, 0, 0, 3, 4, 0, 2, 0, 3, 0, 2, 0, 2, 2, 3, 2, 0, 0, 4, 3, 2, 0, 2, 3, 3, 4, 0, 0, 0, 4, 0, 3, 2, 0, 3, 2, 4, 0, 2, 3, 3, 0, 3, 4, 2, 3, 0, 2, 0, 0, 4, 2, 3, 0, 3, 0, 0, 2, 2, 3, 0, 0, 3, 3, 3, 0, 2, 3, 2, 0, 2, 4, 0, 2, 0, 0, 3, 3, 0, 3, 0, 2, 0, 0, 3, 4, 0, 0, 4, 0, 2, 3, 3, 0, 2, 4, 0, 0],
    0x95: [],
    0xF1: [0, 3, 2, 2, 2, 0, 3, 4, 0, 3, 3, 0, 2, 4, 2, 2, 0, 4, 0, 0, 0, 2, 0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 2, 2, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0, 4, 4, 0, 0, 4, 2, 0, 0, 0, 3, 0, 0, 2, 0, 0, 0, 4, 0, 3, 0, 4, 3, 2, 0, 0, 2, 0],
    0x111: [0, 3, 0, 0, 4, 3, 0, 3, 2, 0, 0, 0, 0, 0, 3, 0, 0, 2, 0, 2, 2, 0, 2, 3, 0, 3, 0, 2, 0, 0, 0, 4, 3, 2, 0, 2, 0, 0, 2, 0, 2, 0, 3, 2, 2, 3, 0, 2, 0, 4, 0, 2, 0, 3, 0, 3, 4, 0, 0, 3, 0, 2, 0, 3, 0, 0, 2, 0, 3, 4, 0, 0, 4, 0, 3, 0, 2, 0, 0, 3, 0, 0, 2, 4, 2, 0, 3, 0, 0, 0, 0, 2, 4, 0, 0, 0, 2, 0, 0, 2, 0, 3, 2, 4, 3, 0, 0, 2, 0, 2, 0, 3, 3, 2, 0, 2, 0, 4, 0, 2, 0, 4, 3, 2, 0, 4, 0, 2, 0, 2, 2, 4, 0, 4, 0, 2, 3, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4, 2, 0, 0, 0, 0, 2, 3, 0, 0, 2, 3, 0, 0, 2, 2, 0, 3, 4, 0],
    0x112: [0, 3, 2, 0, 0, 2, 3, 4, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 3, 4, 2, 3, 4, 3, 2, 0, 0, 2, 0, 0, 0, 0, 4, 2, 0, 0, 0, 4, 0, 4, 0, 0, 3, 2, 0, 3, 0, 4, 0, 3, 0, 0, 0, 2, 2, 0, 2, 0, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 3, 2, 0, 0, 3, 4, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 0, 2, 4, 0, 0, 2, 0, 0, 3, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 4, 3, 0, 3, 0, 3, 2, 4, 0, 0, 2, 3, 0, 4, 3, 0, 2, 0, 2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0],
    0x113: [0, 4, 2, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0, 4, 0, 3, 0, 0, 3, 0, 3, 0, 4, 0, 0, 3, 0, 0, 2, 0, 3, 0, 0, 2, 3, 0, 0, 3, 2, 0, 0, 4, 0, 3, 0, 0, 0, 4, 0, 2, 2, 3, 0, 0, 0, 0, 3, 0, 2, 4, 3, 2, 3, 0, 2, 0, 3, 0, 0, 2, 0, 2, 0, 3, 0, 2, 0, 0, 0, 4, 0, 2, 3, 4, 3, 0, 0, 2, 0, 3, 4, 0, 3, 0, 0, 0, 2, 4, 0, 0, 2, 2, 0, 3, 2, 0, 2, 0, 0, 4, 2, 2, 0, 0, 3, 4, 4, 0, 3, 0, 2, 0, 2, 0, 2, 4, 0, 3, 0, 0, 2, 3, 3, 0, 2, 4, 0, 3, 0, 2, 0, 3, 0, 3, 0, 2, 0, 2, 4, 0, 2, 3, 0, 0, 3, 2, 0, 3, 2, 0, 0]
}

# Compressed level size in ROM
level_size = [
    0x9E0,
    0x5E0,
    0x740,
    0x8A0,
    0x90,
    0x3B0,
    0x5A0,
    0x890,
    0x670,
    0x7D0,
    0x90,
    0xCE0,
    0xA50,
    0xA30,
    0x8E0,
    0x20,
    0x760,
    0xE90,
    0xE40,
    0xE00,
    0xCD0,
    0x20,
    0x3F0,
    0xB00,
    0xA30,
    0xB30,
]

# Level address in ROM
level_address = [
    0xF939B0,
    0xF958B0,
    0xF945B0,
    0xF94EE0,
    0xF84CC0,
    0xF910B0,
    0xF915B0,
    0xF91D00,
    0xF92710,
    0xF92F40,
    0xF84B70,
    0xF84FA0,
    0xF85EB0,
    0xF86B60,
    0xF877C0,
    0xF880E0,
    0xF901C0,
    0xF884E0,
    0xF89370,
    0xF8A5F0,
    0xF8B760,
    0xF8C7C0,
    0xF90B50,
    0xF8D960,
    0xF8E6E0,
    0xF8F110,
]

# Level header address in ROM
level_header = [
    0xF9DD9C,
    0xF9E07C,
    0xF9DE54,
    0xF9DF0C,
    0xF9DFC4,
    0xF9E6E0,
    0xF9E798,
    0xF9E850,
    0xF9E908,
    0xF9E9C0,
    0xF9EA78,
    0xF9F004,
    0xF9F0BC,
    0xF9F174,
    0xF9F22C,
    0xF9F2E4,
    0xF9E1C0,
    0xF9E330,
    0xF9E3E4,
    0xF9E498,
    0xF9E54C,
    0xF9E600,
    0xF9DC2C,
    0xF9DA04,
    0xF9DABC,
    0xF9DB74,
]

# Convert area to base level
# Used for difficulty scaling
difficulty_convert: Dict[int, int] = {0x2: 0, 0x1: 10, 0x7: 20, 0x9: 30, 0xF: 35, 0x11: 40, 0x8: 45}

# Runestones required to access difficulties
# Used in Rules.py for access calculation
difficulty_lambda: Dict[int, List[int]] = {
    0x2: [0, 1, 2, 3],
    0x1: [0, 3, 4, 5],
    0x7: [0, 6, 7, 8],
    0x9: [0, 6, 7, 8],
    0xF: [0, 7, 8, 9],
    0x11: [0, 9, 10, 11],
    0x8: [0, 13, 13, 13],
}

# Area ID's with bosses in them
boss_realm = [2, 1, 7, 9]

# Area and Level ID's for boss levels
boss_level = [bytes([0x6, 0x2]), bytes([0x5, 0x9]), bytes([0x5, 0x1]), bytes([0x5, 0x7]), bytes([0x2, 0xF])]

# Area and Level ID's for mirror levels
mirror_levels = [bytes([0x6, 0x2]), bytes([0x5, 0x9]), bytes([0x5, 0x1]), bytes([0x5, 0x7])]

# Levels with obelisks in them in vanilla
# Values are index of level_locations array
level_obelisk = [5, 6, 7, 11, 12, 0, 1]

# ID's for names said by announcer
sounds = {
    0: 0x9D,
    1: 0x9E,
    2: 0xA7,
    3: 0xA5,
    5: 0x9F,
    6: 0xA1,
    7: 0xA0,
    8: 0xA2,
    9: 0xA7,
}

# ID's for colors said by announcer
colors = {
    0: 0xA3,
    1: 0xA6,
    2: 0x9C,
    3: 0xA4,
}
