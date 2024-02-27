from enum import Enum
from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from .options import ShuffleDoors, SunwarpAccess
from .static_logic import DOORS_BY_ROOM, PROGRESSION_BY_ROOM, PROGRESSIVE_ITEMS, get_door_group_item_id, \
    get_door_item_id, get_progressive_item_id, get_special_item_id

if TYPE_CHECKING:
    from . import LingoWorld


class ItemType(Enum):
    NORMAL = 1
    COLOR = 2


class ItemData(NamedTuple):
    """
    ItemData for an item in Lingo
    """
    code: int
    classification: ItemClassification
    type: ItemType
    door_ids: List[str]
    painting_ids: List[str]


class LingoItem(Item):
    """
    Item from the game Lingo
    """
    game: str = "Lingo"


ALL_ITEM_TABLE: Dict[str, ItemData] = {}


def load_item_data():
    global ALL_ITEM_TABLE

    for color in ["Black", "Red", "Blue", "Yellow", "Green", "Orange", "Gray", "Brown", "Purple"]:
        ALL_ITEM_TABLE[color] = ItemData(get_special_item_id(color), ItemClassification.progression,
                                         ItemType.COLOR, [], [])

    door_groups: Dict[str, List[str]] = {}
    for room_name, doors in DOORS_BY_ROOM.items():
        for door_name, door in doors.items():
            if door.skip_item is True or door.event is True:
                continue

            if door.group is not None:
                door_groups.setdefault(door.group, []).extend(door.door_ids)

            ALL_ITEM_TABLE[door.item_name] = \
                ItemData(get_door_item_id(room_name, door_name),
                         ItemClassification.filler if door.junk_item else ItemClassification.progression,
                         ItemType.NORMAL, door.door_ids, door.painting_ids)

    for group, group_door_ids in door_groups.items():
        ALL_ITEM_TABLE[group] = ItemData(get_door_group_item_id(group),
                                         ItemClassification.progression, ItemType.NORMAL, group_door_ids, [])

    special_items: Dict[str, ItemClassification] = {
        ":)":                        ItemClassification.filler,
        "The Feeling of Being Lost": ItemClassification.filler,
        "Wanderlust":                ItemClassification.filler,
        "Empty White Hallways":      ItemClassification.filler,
        "Slowness Trap":             ItemClassification.trap,
        "Iceland Trap":              ItemClassification.trap,
        "Atbash Trap":               ItemClassification.trap,
        "Puzzle Skip":               ItemClassification.useful,
    }

    for item_name, classification in special_items.items():
        ALL_ITEM_TABLE[item_name] = ItemData(get_special_item_id(item_name), classification,
                                             ItemType.NORMAL, [], [])

    for item_name in PROGRESSIVE_ITEMS:
        ALL_ITEM_TABLE[item_name] = ItemData(get_progressive_item_id(item_name),
                                             ItemClassification.progression, ItemType.NORMAL, [], [])


# Initialize the item data at module scope.
load_item_data()
