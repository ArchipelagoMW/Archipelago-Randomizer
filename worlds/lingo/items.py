from typing import Dict, NamedTuple, Optional, List
from BaseClasses import Item, MultiWorld
from .Options import get_option_value
from .static_logic import StaticLingoLogic


class ItemData(NamedTuple):
    """
    ItemData for an item in Lingo
    """
    code: Optional[int]
    progression: bool
    trap: bool
    mode: Optional[str]
    event: bool
    door_ids: List[str]
    painting_ids: List[str]

    def should_include(self, world: MultiWorld, player: int) -> bool:
        if self.mode == "colors":
            return get_option_value(world, player, "shuffle_colors") > 0
        elif self.mode == "doors":
            return get_option_value(world, player, "shuffle_doors") > 0
        elif self.mode == "orange tower":
            # door shuffle is on and tower isn't progressive
            return get_option_value(world, player, "shuffle_doors") > 0\
                and not get_option_value(world, player, "progressive_orange_tower")
        elif self.mode == "complex door":
            return get_option_value(world, player, "shuffle_doors") == 2  # complex doors
        elif self.mode == "door group":
            return get_option_value(world, player, "shuffle_doors") == 1  # simple doors
        elif self.mode == "special":
            return False
        else:
            return True


class LingoItem(Item):
    """
    Item from the game Lingo
    """
    game: str = "Lingo"


class StaticLingoItems:
    """
    Defines the items that can be included in a Lingo world
    """

    base_id: int = 0

    ALL_ITEM_TABLE: Dict[str, ItemData] = {}

    def create_item(self, name: str, event: bool, progression: bool, trap: bool, mode: Optional[str] = None,
                    door_ids: Optional[List[str]] = None, painting_ids: Optional[List[str]] = None):
        new_id = None if event is True else self.base_id + len(self.ALL_ITEM_TABLE)
        new_item = ItemData(new_id, progression, trap, mode, event, [] if door_ids is None else door_ids,
                            [] if painting_ids is None else painting_ids)
        self.ALL_ITEM_TABLE[name] = new_item

    def __init__(self, base_id: int):
        self.base_id = base_id

        for color in ["Black", "Red", "Blue", "Yellow", "Green", "Orange", "Gray", "Brown", "Purple"]:
            self.create_item(color, False, True, False, "colors")

        door_groups: Dict[str, List[str]] = {}
        for room_name, doors in StaticLingoLogic.DOORS_BY_ROOM.items():
            for door_name, door in doors.items():
                if door.skip_item is True or door.event is True:
                    continue

                if room_name == "Orange Tower":
                    door_mode = "orange tower"
                elif door.group is None:
                    door_mode = "doors"
                else:
                    door_mode = "complex door"
                    door_groups.setdefault(door.group, []).extend(door.door_ids)

                if room_name in StaticLingoLogic.PROGRESSION_BY_ROOM\
                        and door_name in StaticLingoLogic.PROGRESSION_BY_ROOM[room_name]:
                    door_mode = "special"

                self.create_item(door.item_name, False, not door.junk_item, False, door_mode, door.door_ids,
                                 door.painting_ids)

        for group, group_door_ids in door_groups.items():
            self.create_item(group, False, True, False, "door group", group_door_ids, [])

        self.create_item("Progressive Orange Tower", False, True, False, "special")
        self.create_item("Nothing", False, False, False)
        self.create_item("Slowness Trap", False, False, True)
        self.create_item("Iceland Trap", False, False, True)

        for item_name in StaticLingoLogic.PROGRESSIVE_ITEMS:
            self.create_item(item_name, False, True, False, "special")
