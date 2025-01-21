from typing import Dict, Callable

from BaseClasses import Item, ItemClassification as IClass
from .data.strings import GOALS, ITEMS, OTHER


def is_mam_achievement_included(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.progression if achievements and (not goal == GOALS.vanilla) else IClass.useful


def is_achievements_included(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.progression if achievements else IClass.useful


def is_goal_efficiency_iii(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.progression if goal == GOALS.efficiency_iii else IClass.useful


def always_progression(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.progression


def always_useful(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.useful


def always_filler(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.filler


def always_trap(goal: str, achievements: bool, early_useful: str) -> IClass:
    return IClass.trap


# Routing buildings are not needed to complete the game, but building factories without balancers and tunnels
# would be unreasonably complicated and time-consuming.
# Some buildings are not needed to complete the game, but are "logically needed" for the "MAM" achievement.

buildings_processing: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.cutter: always_progression,
    ITEMS.cutter_quad: always_progression,
    ITEMS.rotator: always_progression,
    ITEMS.rotator_ccw: always_progression,
    ITEMS.rotator_180: always_progression,
    ITEMS.stacker: always_progression,
    ITEMS.painter: always_progression,
    ITEMS.painter_double: always_progression,
    ITEMS.painter_quad: always_progression,
    ITEMS.color_mixer: always_progression,
}

buildings_routing: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.balancer: always_progression,
    ITEMS.comp_merger: always_progression,
    ITEMS.comp_splitter: always_progression,
    ITEMS.tunnel: always_progression,
    ITEMS.tunnel_tier_ii: is_mam_achievement_included,
}

buildings_other: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.trash: always_progression,
    ITEMS.extractor_chain: always_useful
}

buildings_top_row: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.belt_reader: is_mam_achievement_included,
    ITEMS.storage: is_achievements_included,
    ITEMS.switch: always_progression,
    ITEMS.item_filter: is_mam_achievement_included,
    ITEMS.display: always_useful
}

buildings_wires: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.wires: always_progression,
    ITEMS.const_signal: always_progression,
    ITEMS.logic_gates: is_mam_achievement_included,
    ITEMS.virtual_proc: is_mam_achievement_included
}

gameplay_unlocks: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.blueprints: is_achievements_included
}

upgrades: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.upgrade_big_belt: is_goal_efficiency_iii,
    ITEMS.upgrade_big_miner: always_useful,
    ITEMS.upgrade_big_proc: always_useful,
    ITEMS.upgrade_big_paint: always_useful,
    ITEMS.upgrade_small_belt: always_filler,
    ITEMS.upgrade_small_miner: always_filler,
    ITEMS.upgrade_small_proc: always_filler,
    ITEMS.upgrade_small_paint: always_filler
}

bundles: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.bundle_blueprint: always_filler,
    ITEMS.bundle_level: always_filler,
    ITEMS.bundle_upgrade: always_filler
}

standard_traps: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.trap_locked: always_trap,
    ITEMS.trap_throttled: always_trap,
    ITEMS.trap_malfunction: always_trap
}

random_draining_trap: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.trap_draining_inv: always_trap
}

split_draining_traps: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.trap_draining_blueprint: always_trap,
    ITEMS.trap_draining_level: always_trap,
    ITEMS.trap_draining_upgrade: always_trap
}

belt_and_extractor: Dict[str, Callable[[str, bool, str], IClass]] = {
    ITEMS.belt: always_progression,
    ITEMS.extractor: always_progression
}

item_table: Dict[str, Callable[[str, bool, str], IClass]] = {
    **buildings_processing,
    **buildings_routing,
    **buildings_other,
    **buildings_top_row,
    **buildings_wires,
    **gameplay_unlocks,
    **upgrades,
    **bundles,
    **standard_traps,
    **random_draining_trap,
    **split_draining_traps,
    **belt_and_extractor
}

big_upgrades = [
    ITEMS.upgrade_big_belt,
    ITEMS.upgrade_big_miner,
    ITEMS.upgrade_big_proc,
    ITEMS.upgrade_big_paint
]

small_upgrades = [
    ITEMS.upgrade_small_belt,
    ITEMS.upgrade_small_miner,
    ITEMS.upgrade_small_proc,
    ITEMS.upgrade_small_paint
]


def trap(random: float, split_draining: bool) -> str:
    """Returns a random trap item."""
    random_value = (len(standard_traps)+1)*random
    if random_value >= 1:
        return list(standard_traps.keys())[int(random_value)-1]
    else:
        return ITEMS.trap_draining_inv \
            if not split_draining else list(split_draining_traps.keys())[int(random_value*3)]


def filler(random: float) -> str:
    """Returns a random filler item."""
    if random < 0.16:  # These float values are intentionally just estimates of 1/6 and 2/3
        return big_upgrades[int(random*4/0.16)]
    elif random < 0.66:
        return small_upgrades[int((random-0.16)*4/0.5)]  # Yes, I want this calculation to be written that way
    else:
        return list(bundles.keys())[int((random-0.66)*len(bundles)/0.34)]


item_descriptions = {  # TODO replace keys with global strings
    "Balancer": "A routing building, that can merge two belts into one, split a belt in two, " +
                "or balance the items of two belts",
    "Tunnel": "A routing building consisting of two parts, that allows for gaps in belts",
    "Compact Merger": "A small routing building, that merges two belts into one",
    "Tunnel Tier II": "A routing building consisting of two parts, that allows for even longer gaps in belts",
    "Compact Splitter": "A small routing building, that splits a belt in two",
    "Cutter": "A processing building, that cuts shapes vertically in two halves",
    "Rotator": "A processing building, that rotates shapes 90 degrees clockwise",
    "Painter": "A processing building, that paints shapes in a given color",
    "Rotator (CCW)": "A processing building, that rotates shapes 90 degrees counter-clockwise",
    "Color Mixer": "A processing building, that mixes two colors together to create a new one",
    "Stacker": "A processing building, that combines two shapes with missing parts or puts one on top of the other",
    "Quad Cutter": "A processing building, that cuts shapes in four quarter parts",
    "Double Painter": "A processing building, that paints two shapes in a given color",
    "Rotator (180°)": "A processing building, that rotates shapes 180 degrees",
    "Quad Painter": "A processing building, that paint each quarter of a shape in another given color and requires " +
                    "wire inputs for each color to work",
    "Trash": "A building, that destroys unused shapes",
    "Chaining Extractor": "An upgrade to extractors, that can increase the output without balancers or mergers",
    "Belt Reader": "A wired building, that shows the average amount of items passing through per second",
    "Storage": "A building, that stores up to 5000 of a certain shape",
    "Switch": "A building, that sends a constant boolean signal",
    "Item Filter": "A wired building, that filters items based on wire input",
    "Display": "A wired building, that displays a shape or color based on wire input",
    "Wires": "The main building of the wires layer, that carries signals between other buildings",
    "Constant Signal": "A building on the wires layer, that sends a constant shape, color, or boolean signal",
    "Logic Gates": "Multiple buildings on the wires layer, that perform logical operations on wire signals",
    "Virtual Processing": "Multiple buildings on the wires layer, that process wire signals like processor buildings",
    "Blueprints": "A game mechanic, that allows copy-pasting multiple buildings at once",
    "Big Belt Upgrade": "An upgrade, that adds 1 to the speed multiplier of belts, distributors, and tunnels",
    "Big Miner Upgrade": "An upgrade, that adds 1 to the speed multiplier of extractors",
    "Big Processors Upgrade": "An upgrade, that adds 1 to the speed multiplier of cutters, rotators, and stackers",
    "Big Painting Upgrade": "An upgrade, that adds 1 to the speed multiplier of painters and color mixers",
    "Small Belt Upgrade": "An upgrade, that adds 0.1 to the speed multiplier of belts, distributors, and tunnels",
    "Small Miner Upgrade": "An upgrade, that adds 0.1 to the speed multiplier of extractors",
    "Small Processors Upgrade": "An upgrade, that adds 0.1 to the speed multiplier of cutters, rotators, and stackers",
    "Small Painting Upgrade": "An upgrade, that adds 0.1 to the speed multiplier of painters and color mixers",
    "Blueprint Shapes Bundle": "A bundle with 1000 blueprint shapes, instantly delivered to the hub",
    "Level Shapes Bundle": "A bundle with some shapes needed for the current level, " +
                           "instantly delivered to the hub",
    "Upgrade Shapes Bundle": "A bundle with some shapes needed for a random upgrade, " +
                           "instantly delivered to the hub",
    "Inventory Draining Trap": "Randomly drains either blueprint shapes, current level requirement shapes, " +
                               "or random upgrade requirement shapes, by half",
    "Blueprint Shapes Draining Trap": "Drains the stored blueprint shapes by half",
    "Level Shapes Draining Trap": "Drains the current level requirement shapes by half",
    "Upgrade Shapes Draining Trap": "Drains a random upgrade requirement shape by half",
    "Locked Building Trap": "Locks a random building from being placed for 15-60 seconds",
    "Throttled Building Trap": "Halves the speed of a random building for 15-60 seconds",
    "Malfunctioning Trap": "Makes a random building process items incorrectly for 15-60 seconds",
    "Belt": "One of the most important buildings in the game, that transports your shapes and colors from one " +
            "place to another",
    "Extractor": "One of the most important buildings in the game, that extracts shapes from those randomly " +
                 "generated patches"
}


class ShapezItem(Item):
    game = OTHER.game_name
