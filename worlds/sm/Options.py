import typing
from Options import Choice, Range, OptionDict, Option, Toggle, DefaultOnToggle

class StartItemsRemovesFromPool(Toggle):
    displayname = "StartItems Removes From Item Pool"

class Preset(Choice):
    displayname = "Preset"
    option_newbie = 0
    option_casual = 1
    option_regular = 2
    option_veteran = 3
    option_expert = 4
    option_master = 5
    option_samus = 6
    option_Season_Races = 7
    option_SMRAT2021 = 8
    option_solution = 9
    option_custom = 10
    default = 2

class StartLocation(Choice):
    displayname = "Start Location"
    option_Ceres = 0
    option_Landing_Site = 1
    option_Gauntlet_Top = 2
    option_Green_Brinstar_Elevator = 3
    option_Big_Pink = 4
    option_Etecoons_Supers = 5
    option_Wrecked_Ship_Main = 6
    option_Firefleas_Top = 7
    option_Business_Center = 8
    option_Bubble_Mountain = 9
    option_Mama_Turtle = 10
    option_Watering_Hole = 11
    option_Aqueduct = 12
    option_Red_Brinstar_Elevator = 13
    option_Golden_Four = 14
    default = 1

class MaxDifficulty(Choice):
    displayname = "Maximum Difficulty"
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_harder = 3
    option_hardcore = 4
    option_mania = 5
    option_infinity = 6
    default = 4

class MorphPlacement(Choice):
    displayname = "Morph Placement"
    option_early = 0
    option_normal = 1
    default = 0

class SuitsRestriction(DefaultOnToggle):
    displayname = "Suits Restriction"

class StrictMinors(Toggle):
    displayname = "Strict Minors"

class MissileQty(Range):
    displayname = "Missile Quantity"
    range_start = 10
    range_end = 90
    default = 30

class SuperQty(Range):
    displayname = "Super Quantity"
    range_start = 10
    range_end = 90
    default = 20

class PowerBombQty(Range):
    displayname = "Power Bomb Quantity"
    range_start = 10
    range_end = 90
    default = 10

class MinorQty(Range):
    displayname = "Minor Quantity"
    range_start = 7
    range_end = 100
    default = 100

class EnergyQty(Choice):
    displayname = "Energy Quantity"
    option_ultra_sparse = 0
    option_sparse = 1
    option_medium = 2
    option_vanilla = 3
    default = 3

class AreaRandomization(Choice):
    displayname = "Area Randomization"
    option_off = 0
    option_light = 1
    option_on = 2
    alias_false = 0
    alias_true = 2
    default = 0

class AreaLayout(Toggle):
    displayname = "Area Layout"

class DoorsColorsRando(Toggle):
    displayname = "Doors Colors Rando"

class AllowGreyDoors(Toggle):
    displayname = "Allow Grey Doors"

class BossRandomization(Toggle):
    displayname = "Boss Randomization"

class FunCombat(Toggle):
    displayname = "Fun Combat"

class FunMovement(Toggle):
    displayname = "Fun Movement"

class FunSuits(Toggle):
    displayname = "Fun Suits"

class LayoutPatches(DefaultOnToggle):
    displayname = "Layout Patches"

class VariaTweaks(Toggle):
    displayname = "Varia Tweaks"

class NerfedCharge(Toggle):
    displayname = "Nerfed Charge"

class GravityBehaviour(Choice):
    displayname = "Gravity Behaviour"
    option_Vanilla = 0
    option_Balanced = 1
    option_Progressive = 2
    default = 1

class ElevatorsDoorsSpeed(DefaultOnToggle):
    displayname = "Elevators doors speed"

class SpinJumpRestart(Toggle):
    displayname = "Spin Jump Restart"

class InfiniteSpaceJump(Toggle):
    displayname = "Infinite Space Jump"

class RefillBeforeSave(Toggle):
    displayname = "Refill Before Save"

class Hud(Toggle):
    displayname = "Hud"

class Animals(Toggle):
    displayname = "Animals"

class NoMusic(Toggle):
    displayname = "No Music"

class RandomMusic(Toggle):
    displayname = "Random Music"

class CustomPreset(OptionDict):
    displayname = "Custom Preset"
    default = { "knows": {}, "settings": {}, "controller": {} }


sm_options: typing.Dict[str, type(Option)] = {
    "start_inventory_removes_from_pool": StartItemsRemovesFromPool,
    "preset": Preset,
    "start_location": StartLocation,
    #"majors_split": "Full",
    #"scav_num_locs": "10",
    #"scav_randomized": "off",
    #"scav_escape": "off",
    "max_difficulty": MaxDifficulty,
    #"progression_speed": "medium",
    #"progression_difficulty": "normal",
    "morph_placement": MorphPlacement,
    "suits_restriction": SuitsRestriction,
    #"hide_items": "off",
    "strict_minors": StrictMinors,
    "missile_qty": MissileQty,
    "super_qty": SuperQty,
    "power_bomb_qty": PowerBombQty,
    "minor_qty": MinorQty,
    "energy_qty": EnergyQty,
    "area_randomization": AreaRandomization,
    "area_layout": AreaLayout,
    "doors_colors_rando": DoorsColorsRando,
    "allow_grey_doors": AllowGreyDoors,
    "boss_randomization": BossRandomization,
    #"minimizer": "off",
    #"minimizer_qty": "45",
    #"minimizer_tourian": "off",
    #"escape_rando": "off",
    #"remove_escape_enemies": "off",
    "fun_combat": FunCombat,
    "fun_movement": FunMovement,
    "fun_suits": FunSuits,
    "layout_patches": LayoutPatches,
    "varia_tweaks": VariaTweaks,
    "nerfed_charge": NerfedCharge,
    "gravity_behaviour": GravityBehaviour,
    #"item_sounds": "on",
    "elevators_doors_speed": ElevatorsDoorsSpeed,
    "spin_jump_restart": SpinJumpRestart,
    #"rando_speed": "off",
    "infinite_space_jump": InfiniteSpaceJump,
    "refill_before_save": RefillBeforeSave,
    "hud": Hud,
    "animals": Animals,
    "no_music": NoMusic,
    "random_music": RandomMusic,
    "custom_preset": CustomPreset
    }
