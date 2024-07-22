from typing import Dict, TYPE_CHECKING
from collections.abc import Callable
from BaseClasses import CollectionState
from worlds.generic.Rules import forbid_item

if TYPE_CHECKING:
    from . import ShiversWorld


def water_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Lobby", player) or
            (state.can_reach_region("Janitor Closet", player) and cloth_capturable(state, player))) \
        and state.has_all({"Water Pot Bottom", "Water Pot Top", "Water Pot Bottom DUPE", "Water Pot Top DUPE"}, player)


def wax_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Library", player) or state.can_reach_region("Anansi", player)) \
        and state.has_all({"Wax Pot Bottom", "Wax Pot Top", "Wax Pot Bottom DUPE", "Wax Pot Top DUPE"}, player)


def ash_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Office", player) or state.can_reach_region("Burial", player)) \
        and state.has_all({"Ash Pot Bottom", "Ash Pot Top", "Ash Pot Bottom DUPE", "Ash Pot Top DUPE"}, player)


def oil_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Prehistoric", player) or state.can_reach_region("Tar River", player)) \
        and state.has_all({"Oil Pot Bottom", "Oil Pot Top", "Oil Pot Bottom DUPE", "Oil Pot Top DUPE"}, player)


def cloth_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Egypt", player) or state.can_reach_region("Burial", player) or
            state.can_reach_region("Janitor Closet", player)) \
        and state.has_all({"Cloth Pot Bottom", "Cloth Pot Top", "Cloth Pot Bottom DUPE", "Cloth Pot Top DUPE"}, player)


def wood_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Workshop", player) or state.can_reach_region("Blue Maze", player) or
            state.can_reach_region("Gods Room", player) or state.can_reach_region("Pegasus", player)) \
        and state.has_all({"Wood Pot Bottom", "Wood Pot Top", "Wood Pot Bottom DUPE", "Wood Pot Top DUPE"}, player)


def crystal_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Lobby", player) or state.can_reach_region("Ocean", player)) \
        and state.has_all(
            {"Crystal Pot Bottom", "Crystal Pot Top", "Crystal Pot Bottom DUPE", "Crystal Pot Top DUPE"}, player)


def sand_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Greenhouse", player) or state.can_reach_region("Ocean", player)) \
        and state.has_all({"Sand Pot Bottom", "Sand Pot Top", "Sand Pot Bottom DUPE", "Sand Pot Top DUPE"}, player)


def metal_capturable(state: CollectionState, player: int) -> bool:
    return (state.can_reach_region("Projector Room", player) or
            state.can_reach_region("Prehistoric", player) or state.can_reach_region("Bedroom", player)) \
        and state.has_all({"Metal Pot Bottom", "Metal Pot Top", "Metal Pot Bottom DUPE", "Metal Pot Top DUPE"}, player)


def lightning_capturable(state: CollectionState, world: "ShiversWorld", player: int) -> bool:
    return (first_nine_ixupi_capturable or world.options.early_lightning) \
        and state.can_reach_region("Generator", player) \
        and state.has_all(
            {"Lightning Pot Bottom", "Lightning Pot Top", "Lightning Pot Bottom DUPE", "Lightning Pot Top DUPE"}, player)


def beths_body_available(state: CollectionState, world: "ShiversWorld", player: int) -> bool:
    return (first_nine_ixupi_capturable(state, player) or world.options.early_beth) \
        and state.can_reach_region("Generator", player)


def first_nine_ixupi_capturable(state: CollectionState, player: int) -> bool:
    return water_capturable(state, player) and wax_capturable(state, player) \
        and ash_capturable(state, player) and oil_capturable(state, player) \
        and cloth_capturable(state, player) and wood_capturable(state, player) \
        and crystal_capturable(state, player) and sand_capturable(state, player) \
        and metal_capturable(state, player)


# def all_skull_dials_available(state: CollectionState, player: int) -> bool:
#     return state.can_reach_region("Prehistoric", player) and state.can_reach_region("Tar River", player) \
#         and state.can_reach_region("Egypt", player) and state.can_reach_region("Burial", player) \
#         and state.can_reach_region("Gods Room", player) and state.can_reach_region("Werewolf", player)


def all_skull_dials_set(state: CollectionState, player: int) -> bool:
    return state.has("Set Skull Dial: Prehistoric", player) \
        and state.has("Set Skull Dial: Tar River", player) \
        and state.has("Set Skull Dial: Egypt", player) \
        and state.has("Set Skull Dial: Burial", player) \
        and state.has("Set Skull Dial: Gods Room", player) \
        and state.has("Set Skull Dial: Werewolf", player)


def completion_condition(state: CollectionState, player: int) -> bool:
    return state.has("Victory", player)


def get_rules_lookup(world: "ShiversWorld", player: int):
    rules_lookup: Dict[str, Dict[str, Callable[[CollectionState], bool]]] = {
        "entrances": {
            "To Office Elevator From Underground Blue Tunnels": lambda state: state.has("Key for Office Elevator", player),
            "To Office Elevator From Office": lambda state: state.has("Key for Office Elevator", player),
            "To Bedroom Elevator From Office": lambda state: state.has("Use Bedroom Elevator", player),
            "To Office From Bedroom Elevator": lambda state: state.has_all({"Key for Bedroom Elevator", "Crawling"}, player),
            "To Three Floor Elevator From Maintenance Tunnels": lambda state: state.has("Key for Three Floor Elevator", player),
            "To Three Floor Elevator From Blue Maze Bottom": lambda state: state.has("Key for Three Floor Elevator", player),
            "To Three Floor Elevator From Blue Maze Top": lambda state: state.has("Key for Three Floor Elevator", player),
            "To Workshop": lambda state: state.has("Key for Workshop", player),
            "To Lobby From Office": lambda state: state.has("Key for Office", player),
            "To Office From Lobby": lambda state: state.has("Key for Office", player),
            "To Library From Lobby": lambda state: state.has("Key for Library", player),
            "To Lobby From Library": lambda state: state.has("Key for Library", player),
            "To Prehistoric From Lobby": lambda state: state.has("Key for Prehistoric Room", player),
            "To Lobby From Prehistoric": lambda state: state.has("Key for Prehistoric Room", player),
            "To Greenhouse": lambda state: state.has("Key for Greenhouse", player),
            "To Ocean From Prehistoric": lambda state: state.has("Key for Ocean Room", player),
            "To Prehistoric From Ocean": lambda state: state.has("Key for Ocean Room", player),
            "To Projector Room": lambda state: state.has("Key for Projector Room", player),
            "To Generator": lambda state: state.has("Key for Generator Room", player),
            "To Lobby From Egypt": lambda state: state.has("Key for Egypt Room", player),
            "To Egypt From Lobby": lambda state: state.has("Key for Egypt Room", player),
            "To Janitor Closet": lambda state: state.has("Key for Janitor Closet", player),
            "To Shaman From Burial": lambda state: state.has("Key for Shaman Room", player),
            "To Burial From Shaman": lambda state: state.has("Key for Shaman Room", player),
            "To Inventions From UFO": lambda state: state.has("Key for UFO Room", player),
            "To UFO From Inventions": lambda state: state.has("Key for UFO Room", player),
            "To Torture From Inventions": lambda state: state.has("Key for Torture Room", player),
            "To Inventions From Torture": lambda state: state.has("Key for Torture Room", player),
            "To Torture": lambda state: state.has("Key for Puzzle Room", player),
            "To Puzzle Room Mastermind From Torture": lambda state: state.has("Key for Puzzle Room", player),
            "To Bedroom": lambda state: state.has("Key for Bedroom", player),
            "To Underground Lake From Underground Tunnels": lambda state: state.has("Key for Underground Lake", player),
            "To Underground Tunnels From Underground Lake": lambda state: state.has("Key for Underground Lake", player),
            "To Outside From Lobby": lambda state: state.has("Key for Front Door", player),
            "To Lobby From Outside": lambda state: state.has("Key for Front Door", player),
            "To Maintenance Tunnels From Theater Back Hallway": lambda state: state.has("Crawling", player),
            "To Blue Maze From Egypt": lambda state: state.has("Crawling", player),
            "To Egypt From Blue Maze": lambda state: state.has("Crawling", player),
            "To Lobby From Tar River": lambda state: state.has("Crawling", player) and oil_capturable(state, player),
            "To Tar River From Lobby": lambda state: state.has("Crawling", player) and oil_capturable(state, player) and state.can_reach_region("Tar River", player),
            "To Burial From Egypt": lambda state: state.can_reach_region("Egypt", player),
            "To Gods Room From Anansi": lambda state: state.can_reach_region("Gods Room", player),
            "To Slide Room": lambda state: all_skull_dials_set(state, player),
            "To Lobby From Slide Room": lambda state: beths_body_available(state, world, player)
        },
        "locations_required": {
            "Puzzle Solved Anansi Musicbox": lambda state: state.has("Set Jukebox", player),
            "Storage: Clock Tower": lambda state: state.has("Set Clock Chains", player),
            "Storage: Anansi Musicbox": lambda state: state.has("Set Jukebox", player),
            "Storage: Janitor Closet": lambda state: cloth_capturable(state, player),
            "Storage: Tar River": lambda state: oil_capturable(state, player),
            "Storage: Theater": lambda state: state.can_reach_region("Projector Room", player),
            "Storage: Slide": lambda state: beths_body_available(state, world, player) and state.can_reach_region("Slide Room", player),
            "Ixupi Captured Water": lambda state: water_capturable(state, player),
            "Ixupi Captured Wax": lambda state: wax_capturable(state, player),
            "Ixupi Captured Ash": lambda state: ash_capturable(state, player),
            "Ixupi Captured Oil": lambda state: oil_capturable(state, player),
            "Ixupi Captured Cloth": lambda state: cloth_capturable(state, player),
            "Ixupi Captured Wood": lambda state: wood_capturable(state, player),
            "Ixupi Captured Crystal": lambda state: crystal_capturable(state, player),
            "Ixupi Captured Sand": lambda state: sand_capturable(state, player),
            "Ixupi Captured Metal": lambda state: metal_capturable(state, player),
            "Final Riddle: Planets Aligned": lambda state: state.can_reach_region("Fortune Teller", player),
            "Final Riddle: Norse God Stone Message": lambda state: state.can_reach_region("Fortune Teller", player) and state.can_reach_region("UFO", player),
            "Final Riddle: Beth's Body Page 17": lambda state: beths_body_available(state, world, player),
            "Final Riddle: Guillotine Dropped": lambda state: beths_body_available(state, world, player),
            "Puzzle Solved Skull Dial Door": lambda state: all_skull_dials_set(state, player),
            "Set Jukebox": lambda state: state.can_reach_region("Clock Tower", player),
            "Victory": lambda state: first_nine_ixupi_capturable(state, player) and lightning_capturable(state, world, player),
            },
        "locations_puzzle_hints": {
            "Puzzle Solved Clock Tower Door": lambda state: state.can_reach_region("Three Floor Elevator", player),
            "Puzzle Solved Clock Chains": lambda state: state.has("Read Professor Windlenot's Diary", player),
            "Set Clock Chains": lambda state: state.has("Read Professor Windlenot's Diary", player),
            "Puzzle Solved Shaman Drums": lambda state: state.can_reach_region("Clock Tower", player),
            "Puzzle Solved Red Door": lambda state: state.can_reach_region("Maintenance Tunnels", player),
            "Puzzle Solved UFO Symbols": lambda state: state.can_reach_region("Library", player),
            "Puzzle Solved Maze Door": lambda state: state.can_reach_region("Projector Room", player),
            "Puzzle Solved Theater Door": lambda state: state.can_reach_region("Underground Lake", player),
            "Puzzle Solved Columns of RA": lambda state: state.can_reach_region("Underground Lake", player),
            "Final Riddle: Guillotine Dropped": lambda state: beths_body_available(state, world, player) and state.can_reach_region("Underground Lake", player)
            },
        "elevators": {
            "Puzzle Solved Office Elevator": lambda state: (state.can_reach_region("Underground Lake", player) or state.can_reach_region("Office", player))
                                                                  and state.has("Key for Office Elevator", player),
            "Puzzle Solved Bedroom Elevator": lambda state: state.has_all({"Key for Bedroom Elevator", "Crawling"}, player),
            "Use Bedroom Elevator": lambda state: state.has_all({"Key for Bedroom Elevator", "Crawling"}, player),
            "Puzzle Solved Three Floor Elevator": lambda state: (state.can_reach_region("Maintenance Tunnels", player) or state.can_reach_region("Blue Maze", player))
                                                                  and state.has("Key for Three Floor Elevator", player)
            },
        "lightning": {
            "Ixupi Captured Lightning": lambda state: lightning_capturable(state, world, player)
        }
    }
    return rules_lookup


def set_rules(world: "ShiversWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    rules_lookup = get_rules_lookup(world, player)
    # Set required entrance rules
    for entrance_name, rule in rules_lookup["entrances"].items():
        multiworld.get_entrance(entrance_name, player).access_rule = rule

    # Set required location rules
    for location_name, rule in rules_lookup["locations_required"].items():
        multiworld.get_location(location_name, player).access_rule = rule

    # Set option location rules
    if world.options.puzzle_hints_required.value:
        for location_name, rule in rules_lookup["locations_puzzle_hints"].items():
            multiworld.get_location(location_name, player).access_rule = rule

        # Adding these seem to cause a lot of failures even though the make sense logically
        # multiworld.get_entrance("To Theater From Lobby", player).access_rule = lambda state: state.can_reach_region("Underground Lake", player)
        # multiworld.get_entrance("To Clock Tower Staircase From Theater Back Hallway", player).access_rule = lambda state: state.can_reach_region("Three Floor Elevator", player)
        # multiworld.get_entrance("To Gods Room", player).access_rule = lambda state: state.can_reach_region("Clock Tower", player)
        # multiworld.get_entrance("To Anansi From Gods Room", player).access_rule = lambda state: state.can_reach_region("Maintenance Tunnels", player)
        # multiworld.get_entrance("To Maze From Maze Staircase", player).access_rule = lambda state: state.can_reach_region("Projector Room", player)
    if world.options.elevators_stay_solved.value:
        for location_name, rule in rules_lookup["elevators"].items():
            multiworld.get_location(location_name, player).access_rule = rule
    if world.options.early_lightning.value:
        for location_name, rule in rules_lookup["lightning"].items():
            multiworld.get_location(location_name, player).access_rule = rule

    # Register indirect conditions
    multiworld.register_indirect_condition(world.get_region("Burial"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Egypt"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Gods Room"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Prehistoric"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Tar River"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Werewolf"), world.get_entrance("To Slide Room"))
    multiworld.register_indirect_condition(world.get_region("Prehistoric"), world.get_entrance("To Tar River From Lobby"))

    # forbid cloth in janitor closet and oil in tar river
    forbid_item(multiworld.get_location("Storage: Janitor Closet", player), "Cloth Pot Bottom DUPE", player)
    forbid_item(multiworld.get_location("Storage: Janitor Closet", player), "Cloth Pot Top DUPE", player)
    forbid_item(multiworld.get_location("Storage: Tar River", player), "Oil Pot Bottom DUPE", player)
    forbid_item(multiworld.get_location("Storage: Tar River", player), "Oil Pot Top DUPE", player)

    # Filler Item Forbids
    forbid_item(multiworld.get_location("Puzzle Solved Lyre", player), "Easier Lyre", player)
    forbid_item(multiworld.get_location("Ixupi Captured Water", player), "Water Always Available in Lobby", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wax", player), "Wax Always Available in Library", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wax", player), "Wax Always Available in Anansi Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wax", player), "Wax Always Available in Shaman Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Ash", player), "Ash Always Available in Office", player)
    forbid_item(multiworld.get_location("Ixupi Captured Ash", player), "Ash Always Available in Burial Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Oil", player), "Oil Always Available in Prehistoric Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Cloth", player), "Cloth Always Available in Egypt", player)
    forbid_item(multiworld.get_location("Ixupi Captured Cloth", player), "Cloth Always Available in Burial Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wood", player), "Wood Always Available in Workshop", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wood", player), "Wood Always Available in Blue Maze", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wood", player), "Wood Always Available in Pegasus Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Wood", player), "Wood Always Available in Gods Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Crystal", player), "Crystal Always Available in Lobby", player)
    forbid_item(multiworld.get_location("Ixupi Captured Crystal", player), "Crystal Always Available in Ocean", player)
    forbid_item(multiworld.get_location("Ixupi Captured Sand", player), "Sand Always Available in Plants Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Sand", player), "Sand Always Available in Ocean", player)
    forbid_item(multiworld.get_location("Ixupi Captured Metal", player), "Metal Always Available in Projector Room", player)
    forbid_item(multiworld.get_location("Ixupi Captured Metal", player), "Metal Always Available in Bedroom", player)
    forbid_item(multiworld.get_location("Ixupi Captured Metal", player), "Metal Always Available in Prehistoric", player)

    # Set completion condition
    multiworld.completion_condition[player] = lambda state: completion_condition(state, player)
