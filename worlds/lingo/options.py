from dataclasses import dataclass

from schema import And, Schema

from Options import Toggle, Choice, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool, OptionDict
from worlds.lingo.items import TRAP_ITEMS


class ShuffleDoors(Choice):
    """On "none", doors in the game will open the way they do in vanilla.
    On "panels", doors still open as in vanilla, but the panels that open the doors will be locked, and an item will be required to unlock the panels.
    On "doors", the doors themselves are locked behind items, and will open automatically without needing to solve a panel once the key is obtained."""
    display_name = "Shuffle Doors"
    option_none = 0
    option_panels = 1
    option_doors = 2


class GroupDoors(Toggle):
    """By default, door shuffle in either panels or doors mode will create individual keys for every panel or door to be locked.
    When group doors is on, some panels and doors are sorted into logical groups, which are opened together by receiving an item."""
    display_name = "Group Doors"


class ProgressiveOrangeTower(DefaultOnToggle):
    """When door shuffle is on doors mode, this setting governs the manner in which the Orange Tower floors open up.
    If off, there is an item for each floor of the tower, and each floor's item is the only one needed to access that floor.
    If on, there are six progressive items, which open up the tower from the bottom floor upward.
    """
    display_name = "Progressive Orange Tower"


class ProgressiveColorful(DefaultOnToggle):
    """When door shuffle is on in either panels or doors mode, and "Group Doors" is off, this setting governs the manner in which The Colorful opens up.
    If off, there is an item for each room of The Colorful, meaning that random rooms in the middle of the sequence can open up without giving you access to them.
    If on, there are ten progressive items, which open up the sequence from White forward."""
    display_name = "Progressive Colorful"


class LocationChecks(Choice):
    """On "normal", there will be a location check for each panel set that would ordinarily open a door, as well as for
    achievement panels and a small handful of other panels.
    On "reduced", many of the locations that are associated with opening doors are removed.
    On "insanity", every individual panel in the game is a location check."""
    display_name = "Location Checks"
    option_normal = 0
    option_reduced = 1
    option_insanity = 2


class ShuffleColors(DefaultOnToggle):
    """If on, an item is added to the pool for every puzzle color (besides White).
    You will need to unlock the requisite colors in order to be able to solve puzzles of that color."""
    display_name = "Shuffle Colors"


class ShufflePanels(Choice):
    """If on, the puzzles on each panel are randomized.
    On "rearrange", the puzzles are the same as the ones in the base game, but are placed in different areas."""
    display_name = "Shuffle Panels"
    option_none = 0
    option_rearrange = 1


class ShufflePaintings(Toggle):
    """If on, the destination, location, and appearance of the painting warps in the game will be randomized."""
    display_name = "Shuffle Paintings"


class VictoryCondition(Choice):
    """Change the victory condition.
    On "the_end", the goal is to solve THE END at the top of the tower.
    On "the_master", the goal is to solve THE MASTER at the top of the tower, after getting the number of achievements specified in the Mastery Achievements option.
    On "level_2", the goal is to solve LEVEL 2 in the second room, after solving the number of panels specified in the Level 2 Requirement option."""
    display_name = "Victory Condition"
    option_the_end = 0
    option_the_master = 1
    option_level_2 = 2


class MasteryAchievements(Range):
    """The number of achievements required to unlock THE MASTER.
    In the base game, 21 achievements are needed.
    If you include The Scientific and The Unchallenged, which are in the base game but are not counted for mastery, 23 would be required.
    If you include the custom achievement (The Wanderer), 24 would be required.
    """
    display_name = "Mastery Achievements"
    range_start = 1
    range_end = 24
    default = 21


class Level2Requirement(Range):
    """The number of panel solves required to unlock LEVEL 2.
    In the base game, 223 are needed.
    Note that this count includes ANOTHER TRY.
    When set to 1, the panel hunt is disabled, and you can access LEVEL 2 for free.
    """
    display_name = "Level 2 Requirement"
    range_start = 1
    range_end = 800
    default = 223


class EarlyColorHallways(Toggle):
    """When on, a painting warp to the color hallways area will appear in the starting room.
    This lets you avoid being trapped in the starting room for long periods of time when door shuffle is on."""
    display_name = "Early Color Hallways"


class TrapPercentage(Range):
    """Replaces junk items with traps, at the specified rate."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 20


class TrapWeights(OptionDict):
    """Specify the distribution of traps that should be placed into the pool.
    If you don't want a specific type of trap, set the weight to zero."""
    display_name = "Trap Weights"
    schema = Schema({trap_name: And(int, lambda n: n >= 0) for trap_name in TRAP_ITEMS})
    default = {trap_name: 1 for trap_name in TRAP_ITEMS}


class PuzzleSkipPercentage(Range):
    """Replaces junk items with puzzle skips, at the specified rate."""
    display_name = "Puzzle Skip Percentage"
    range_start = 0
    range_end = 100
    default = 20


class DeathLink(Toggle):
    """If on: Whenever another player on death link dies, you will be returned to the starting room."""
    display_name = "Death Link"


@dataclass
class LingoOptions(PerGameCommonOptions):
    shuffle_doors: ShuffleDoors
    group_doors: GroupDoors
    progressive_orange_tower: ProgressiveOrangeTower
    progressive_colorful: ProgressiveColorful
    location_checks: LocationChecks
    shuffle_colors: ShuffleColors
    shuffle_panels: ShufflePanels
    shuffle_paintings: ShufflePaintings
    victory_condition: VictoryCondition
    mastery_achievements: MasteryAchievements
    level_2_requirement: Level2Requirement
    early_color_hallways: EarlyColorHallways
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    puzzle_skip_percentage: PuzzleSkipPercentage
    death_link: DeathLink
    start_inventory_from_pool: StartInventoryPool
