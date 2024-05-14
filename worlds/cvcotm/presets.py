from typing import Any, Dict

from Options import Accessibility, ProgressionBalancing
from .options import IgnoreCleansing, AutoRun, DSSPatch, AlwaysAllowSpeedDash, BreakIronMaidens, BuffRangedFamiliars,\
    BuffSubWeapons, BuffShooterStrength, ItemDropRandomization, HalveDSSCardsPlaced, Countdown, SubWeaponShuffle,\
    DisableBattleArenaMPDrain, RequireAllBosses, EarlyDouble, DeathLink, CompletionGoal

all_random_options = {
    "progression_balancing":         "random",
    "accessibility":                 "random",
    "ignore_cleansing":              "random",
    "auto_run":                      "random",
    "dss_patch":                     "random",
    "always_allow_speed_dash":       "random",
    "break_iron_maidens":            "random",
    "required_last_keys":            "random",
    "available_last_keys":           "random",
    "buff_ranged_familiars":         "random",
    "buff_sub_weapons":              "random",
    "buff_shooter_strength":         "random",
    "item_drop_randomization":       "random",
    "halve_dss_cards_placed":        "random",
    "countdown":                     "random",
    "sub_weapon_shuffle":            "random",
    "disable_battle_arena_mp_drain": "random",
    "require_all_bosses":            "random",
    "early_double":                  "random",
    "death_link":                    "random",
    "completion_goal":               "random",
}

beginner_mode_options = {
    "progression_balancing":         ProgressionBalancing.default,
    "accessibility":                 Accessibility.option_items,
    "ignore_cleansing":              IgnoreCleansing.option_false,
    "auto_run":                      AutoRun.option_true,
    "dss_patch":                     DSSPatch.option_true,
    "always_allow_speed_dash":       AlwaysAllowSpeedDash.option_true,
    "break_iron_maidens":            BreakIronMaidens.option_true,
    "required_last_keys":            3,
    "available_last_keys":           6,
    "buff_ranged_familiars":         BuffRangedFamiliars.option_true,
    "buff_sub_weapons":              BuffSubWeapons.option_true,
    "buff_shooter_strength":         BuffShooterStrength.option_true,
    "item_drop_randomization":       ItemDropRandomization.option_normal,
    "halve_dss_cards_placed":        HalveDSSCardsPlaced.option_false,
    "countdown":                     Countdown.option_majors,
    "sub_weapon_shuffle":            SubWeaponShuffle.option_false,
    "disable_battle_arena_mp_drain": DisableBattleArenaMPDrain.option_true,
    "require_all_bosses":            RequireAllBosses.option_false,
    "early_double":                  EarlyDouble.option_true,
    "death_link":                    DeathLink.option_off,
    "completion_goal":               CompletionGoal.option_dracula,
}

standard_competitive_2022_options = {
    "progression_balancing":         ProgressionBalancing.default,
    "accessibility":                 Accessibility.option_items,
    "ignore_cleansing":              IgnoreCleansing.option_false,
    "auto_run":                      AutoRun.option_false,
    "dss_patch":                     DSSPatch.option_true,
    "always_allow_speed_dash":       AlwaysAllowSpeedDash.option_true,
    "break_iron_maidens":            BreakIronMaidens.option_true,
    "required_last_keys":            3,
    "available_last_keys":           5,
    "buff_ranged_familiars":         BuffRangedFamiliars.option_true,
    "buff_sub_weapons":              BuffSubWeapons.option_true,
    "buff_shooter_strength":         BuffShooterStrength.option_false,
    "item_drop_randomization":       ItemDropRandomization.option_normal,
    "halve_dss_cards_placed":        HalveDSSCardsPlaced.option_true,
    "countdown":                     Countdown.option_majors,
    "sub_weapon_shuffle":            SubWeaponShuffle.option_true,
    "disable_battle_arena_mp_drain": DisableBattleArenaMPDrain.option_false,
    "require_all_bosses":            RequireAllBosses.option_false,
    "early_double":                  EarlyDouble.option_false,
    "death_link":                    DeathLink.option_off,
    "completion_goal":               CompletionGoal.option_dracula,
}

randomania_2023_options = {
    "progression_balancing":         ProgressionBalancing.default,
    "accessibility":                 Accessibility.option_items,
    "ignore_cleansing":              IgnoreCleansing.option_false,
    "auto_run":                      AutoRun.option_false,
    "dss_patch":                     DSSPatch.option_true,
    "always_allow_speed_dash":       AlwaysAllowSpeedDash.option_true,
    "break_iron_maidens":            BreakIronMaidens.option_false,
    "required_last_keys":            3,
    "available_last_keys":           5,
    "buff_ranged_familiars":         BuffRangedFamiliars.option_true,
    "buff_sub_weapons":              BuffSubWeapons.option_true,
    "buff_shooter_strength":         BuffShooterStrength.option_false,
    "item_drop_randomization":       ItemDropRandomization.option_normal,
    "halve_dss_cards_placed":        HalveDSSCardsPlaced.option_false,
    "countdown":                     Countdown.option_majors,
    "sub_weapon_shuffle":            SubWeaponShuffle.option_true,
    "disable_battle_arena_mp_drain": DisableBattleArenaMPDrain.option_false,
    "require_all_bosses":            RequireAllBosses.option_false,
    "early_double":                  EarlyDouble.option_false,
    "death_link":                    DeathLink.option_off,
    "completion_goal":               CompletionGoal.option_dracula,
}

competitive_all_bosses_options = {
    "progression_balancing":         ProgressionBalancing.default,
    "accessibility":                 Accessibility.option_items,
    "ignore_cleansing":              IgnoreCleansing.option_false,
    "auto_run":                      AutoRun.option_false,
    "dss_patch":                     DSSPatch.option_true,
    "always_allow_speed_dash":       AlwaysAllowSpeedDash.option_true,
    "break_iron_maidens":            BreakIronMaidens.option_false,
    "required_last_keys":            8,
    "available_last_keys":           8,
    "buff_ranged_familiars":         BuffRangedFamiliars.option_true,
    "buff_sub_weapons":              BuffSubWeapons.option_true,
    "buff_shooter_strength":         BuffShooterStrength.option_false,
    "item_drop_randomization":       ItemDropRandomization.option_hard,
    "halve_dss_cards_placed":        HalveDSSCardsPlaced.option_true,
    "countdown":                     Countdown.option_none,
    "sub_weapon_shuffle":            SubWeaponShuffle.option_true,
    "disable_battle_arena_mp_drain": DisableBattleArenaMPDrain.option_false,
    "require_all_bosses":            RequireAllBosses.option_true,
    "early_double":                  EarlyDouble.option_false,
    "death_link":                    DeathLink.option_off,
    "completion_goal":               CompletionGoal.option_dracula,
}

hardcore_mode_options = {
    "progression_balancing":         0,
    "accessibility":                 Accessibility.option_locations,
    "ignore_cleansing":              IgnoreCleansing.option_true,
    "auto_run":                      AutoRun.option_false,
    "dss_patch":                     DSSPatch.option_true,
    "always_allow_speed_dash":       AlwaysAllowSpeedDash.option_false,
    "break_iron_maidens":            BreakIronMaidens.option_false,
    "required_last_keys":            9,
    "available_last_keys":           9,
    "buff_ranged_familiars":         BuffRangedFamiliars.option_false,
    "buff_sub_weapons":              BuffSubWeapons.option_false,
    "buff_shooter_strength":         BuffShooterStrength.option_false,
    "item_drop_randomization":       ItemDropRandomization.option_hard,
    "halve_dss_cards_placed":        HalveDSSCardsPlaced.option_true,
    "countdown":                     Countdown.option_none,
    "sub_weapon_shuffle":            SubWeaponShuffle.option_true,
    "disable_battle_arena_mp_drain": DisableBattleArenaMPDrain.option_false,
    "require_all_bosses":            RequireAllBosses.option_false,
    "early_double":                  EarlyDouble.option_false,
    "death_link":                    DeathLink.option_on,
    "completion_goal":               CompletionGoal.option_battle_arena_and_dracula,
}

cvcotm_options_presets: Dict[str, Dict[str, Any]] = {
    "All Random": all_random_options,
    "Beginner Mode": beginner_mode_options,
    "Standard Competitive 2022": standard_competitive_2022_options,
    "Randomania 2023": randomania_2023_options,
    "Competitive All Bosses": competitive_all_bosses_options,
    "Hardcore Mode": hardcore_mode_options,
}
