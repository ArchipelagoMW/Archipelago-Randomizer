from typing import Dict, Callable, Optional, Tuple, Union, TYPE_CHECKING

from BaseClasses import CollectionState, MultiWorld, Location, Region, Entrance
from .Options import Accessibility, Goal
from .Constants import NOTES, PHOBEKINS
from ..generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from . import MessengerWorld
else:
    MessengerWorld = object


class MessengerRules:
    player: int

    def __init__(self, player: int):
        self.player = player

        self.region_rules: Dict[str, Callable] = {
            "Ninja Village": self.has_wingsuit,
            "Autumn Hills": self.has_wingsuit,
            "Catacombs": self.has_wingsuit,
            "Bamboo Creek": self.has_wingsuit,
            "Searing Crags Upper": self.has_vertical,
            "Cloud Ruins": lambda state: self.has_wingsuit(state) and state.has("Ruxxtin's Amulet", player),
            "Underworld": self.has_tabi,
            "Forlorn Temple": lambda state: state.has_all(PHOBEKINS, player) and self.has_wingsuit(state),
            "Glacial Peak": self.has_vertical,
            "Elemental Skylands": lambda state: state.has("Fairy Bottle", player),
            "Music Box": lambda state: state.has_all(NOTES, player)
        }

        self.location_rules: Dict[str, Callable] = {
            # ninja village
            "Ninja Village Seal - Tree House": self.has_dart,
            # autumn hills
            "Key of Hope": self.has_dart,
            # howling grotto
            "Howling Grotto Seal - Windy Saws and Balls": self.has_wingsuit,
            "Howling Grotto Seal - Crushing Pits": lambda state: self.has_wingsuit(state) and self.has_dart(state),
            # searing crags
            "Key of Strength": lambda state: state.has("Power Thistle", player),
            # glacial peak
            "Glacial Peak Seal - Ice Climbers": self.has_dart,
            "Glacial Peak Seal - Projectile Spike Pit": self.has_vertical,
            "Glacial Peak Seal - Glacial Air Swag": self.has_vertical,
            # tower of time
            "Tower of Time Seal - Time Waster Seal": self.has_dart,
            "Tower of Time Seal - Lantern Climb": self.has_wingsuit,
            "Tower of Time Seal - Arcane Orbs": lambda state: self.has_wingsuit(state) and self.has_dart(state),
            # underworld
            "Underworld Seal - Sharp and Windy Climb": self.has_wingsuit,
            "Underworld Seal - Fireball Wave": self.has_wingsuit,
            "Underworld Seal - Rising Fanta": self.has_dart,
            # sunken shrine
            "Sun Crest": self.has_tabi,
            "Moon Crest": self.has_tabi,
            "Key of Love": lambda state: state.has_all({"Sun Crest", "Moon Crest"}, player),
            "Sunken Shrine Seal - Waterfall Paradise": self.has_tabi,
            "Sunken Shrine Seal - Tabi Gauntlet": self.has_tabi,
            # riviere turquoise
            "Fairy Bottle": self.has_vertical,
            "Riviere Turquoise Seal - Flower Power": self.has_vertical,
            # elemental skylands
            "Key of Symbiosis": self.has_dart,
            "Elemental Skylands Seal - Air": self.has_wingsuit,
            "Elemental Skylands Seal - Water": self.has_dart,
            "Elemental Skylands Seal - Fire": self.has_dart,
            # corrupted future
            "Key of Courage": lambda state: state.has_all({"Demon King Crown", "Fairy Bottle"}, player),
            # the shop
            "Shop Chest": self.has_enough_seals
        }

    def has_wingsuit(self, state: CollectionState) -> bool:
        return state.has("Wingsuit", self.player)

    def has_dart(self, state: CollectionState) -> bool:
        return state.has("Rope Dart", self.player)

    def has_tabi(self, state: CollectionState) -> bool:
        return state.has("Ninja Tabi", self.player)

    def has_vertical(self, state: CollectionState) -> bool:
        return self.has_wingsuit(state) or self.has_dart(state)

    def has_enough_seals(self, state: CollectionState) -> bool:
        required_seals = state.multiworld.worlds[self.player].required_seals
        return state.has("Power Seal", self.player, required_seals)


def set_rules(world: MessengerWorld) -> None:
    multiworld = world.multiworld
    player = world.player

    for region in multiworld.get_regions(player):
        if region.name in world.rules.region_rules:
            for entrance in region.entrances:
                entrance.access_rule = world.rules.region_rules[region.name]
        for loc in region.locations:
            if loc.name in world.rules.location_rules:
                loc.access_rule = world.rules.location_rules[loc.name]
    if multiworld.goal[player] == Goal.option_power_seal_hunt:
        set_rule(multiworld.get_entrance("Tower HQ -> Music Box", player),
                 lambda state: state.has("Shop Chest", player))

    if multiworld.enable_logic[player]:
        multiworld.completion_condition[player] = lambda state: state.has("Rescue Phantom", player)
    else:
        multiworld.accessibility[player].value = Accessibility.option_minimal
    if multiworld.accessibility[player] > Accessibility.option_locations:
        set_self_locking_items(multiworld, player)


def location_item_name(state: CollectionState, location: str, player: int) -> Optional[Tuple[str, int]]:
    location = state.multiworld.get_location(location, player)
    if location.item is None:
        return None
    return location.item.name, location.item.player


def allow_self_locking_items(spot: Union[Location, Region], *item_names: str) -> None:
    """
    Sets rules on the supplied spot, such that the supplied item_name(s) can possibly be placed there.
    :param spot: Location or Region that the item(s) are allowed to be placed in
    :param item_names: item name or names that are allowed to be placed in the Location or Region
    """
    player = spot.player

    def set_always_allow(location: Location, rule: Callable) -> None:
        location.always_allow = rule

    def add_allowed_rules(area: Union[Location, Entrance], location: Location) -> None:
        for item_name in item_names:
            add_rule(area, lambda state, item_name=item_name:
                     location_item_name(state, location.name, player) == (item_name, player), "or")
            set_always_allow(location, lambda state, item, item_name=item_name:
                             item.name == item_name and item.player == player)

    if isinstance(spot, Region):
        for entrance in spot.entrances:
            for location in spot.locations:
                add_allowed_rules(entrance, location)
    else:
        add_allowed_rules(spot, spot)


def set_self_locking_items(multiworld: MultiWorld, player: int) -> None:
    # do the ones for seal shuffle on and off first
    allow_self_locking_items(multiworld.get_location("Key of Strength", player), "Power Thistle")
    allow_self_locking_items(multiworld.get_location("Key of Love", player), "Sun Crest", "Moon Crest")
    allow_self_locking_items(multiworld.get_location("Key of Courage", player), "Demon King Crown")

    # add these locations when seals aren't shuffled
    if not multiworld.shuffle_seals[player]:
        allow_self_locking_items(multiworld.get_region("Cloud Ruins", player), "Ruxxtin's Amulet")
        allow_self_locking_items(multiworld.get_region("Forlorn Temple", player), PHOBEKINS)
