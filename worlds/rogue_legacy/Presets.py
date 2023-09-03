from typing import Any

from .Options import *

rl_option_presets: Dict[str, Dict[str, Any]] = {
    "All Random": {
        "progression_balancing":    "random",
        "accessibility":            "random",
        "starting_gender":          "random",
        "starting_class":           "random",
        "new_game_plus":            "random",
        "fairy_chests_per_zone":    "random",
        "chests_per_zone":          "random",
        "universal_fairy_chests":   "random",
        "universal_chests":         "random",
        "vendors":                  "random",
        "architect":                "random",
        "architect_fee":            "random",
        "disable_charon":           "random",
        "require_purchasing":       "random",
        "progressive_blueprints":   "random",
        "gold_gain_multiplier":     "random",
        "number_of_children":       "random",
        "free_diary_on_generation": "random",
        "khidr":                    "random",
        "alexander":                "random",
        "leon":                     "random",
        "herodotus":                "random",
        "health_pool":              "random",
        "mana_pool":                "random",
        "attack_pool":              "random",
        "magic_damage_pool":        "random",
        "armor_pool":               "random",
        "equip_pool":               "random",
        "crit_chance_pool":         "random",
        "crit_damage_pool":         "random",
        "allow_default_names":      "random",
        "death_link":               "random",
    },
    "Limited Resources": {
        "progression_balancing":    0,
        "fairy_chests_per_zone":    2,
        "chests_per_zone":          30,
        "vendors":                  "normal",
        "architect":                "disabled",
        "gold_gain_multiplier":     "half",
        "number_of_children":       2,
        "free_diary_on_generation": False,
        "health_pool":              10,
        "mana_pool":                10,
        "attack_pool":              10,
        "magic_damage_pool":        10,
        "armor_pool":               5,
        "equip_pool":               10,
        "crit_chance_pool":         0,
        "crit_damage_pool":         0,
    }
}
