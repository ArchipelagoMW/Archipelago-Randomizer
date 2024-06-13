from typing import Any, Dict

from .Options import Architect, GoldGainMultiplier, Vendors

rl_options_presets: Dict[str, Dict[str, Any]] = {
    # Example preset using only literal values.
    "Unknown Fate": {
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
        "allow_default_names":      True,
        "death_link":               "random",
    },
    # A preset I actually use, using some literal values and some from the option itself.
    "Limited Potential": {
        "progression_balancing":    0,
        "fairy_chests_per_zone":    2,
        "starting_class":           "random",
        "chests_per_zone":          30,
        "vendors":                  Vendors.option_normal,
        "architect":                Architect.option_disabled,
        "gold_gain_multiplier":     GoldGainMultiplier.option_half,
        "number_of_children":       2,
        "free_diary_on_generation": False,
        "health_pool":              10,
        "mana_pool":                10,
        "attack_pool":              10,
        "magic_damage_pool":        10,
        "armor_pool":               5,
        "equip_pool":               10,
        "crit_chance_pool":         5,
        "crit_damage_pool":         5,
    }
}
