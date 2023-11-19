from typing import Dict, List, NamedTuple, Optional, Set, TYPE_CHECKING

from .items import ALL_ITEM_TABLE
from .locations import ALL_LOCATION_TABLE, LocationClassification
from .options import LocationChecks, ShuffleDoors, VictoryCondition
from .static_logic import DOORS_BY_ROOM, Door, PAINTINGS, PAINTINGS_BY_ROOM, PAINTING_ENTRANCES, PAINTING_EXITS, \
    PANELS_BY_ROOM, PROGRESSION_BY_ROOM, REQUIRED_PAINTING_ROOMS, REQUIRED_PAINTING_WHEN_NO_DOORS_ROOMS, RoomAndDoor, \
    RoomAndPanel
from .testing import LingoTestOptions

if TYPE_CHECKING:
    from . import LingoWorld


class AccessRequirements:
    rooms: Set[str]
    doors: Set[RoomAndDoor]
    colors: Set[str]

    def __init__(self):
        self.rooms = set()
        self.doors = set()
        self.colors = set()

    def merge(self, other: "AccessRequirements"):
        self.rooms |= other.rooms
        self.doors |= other.doors
        self.colors |= other.colors

    def __str__(self):
        return f"AccessRequirements(rooms={self.rooms}, doors={self.doors}, colors={self.colors})"


class PlayerLocation(NamedTuple):
    name: str
    code: Optional[int] = None
    access: AccessRequirements = ()
    counting_panels: int = 0


class LingoPlayerLogic:
    """
    Defines logic after a player's options have been applied
    """

    ITEM_BY_DOOR: Dict[str, Dict[str, str]]

    LOCATIONS_BY_ROOM: Dict[str, List[PlayerLocation]]
    REAL_LOCATIONS: List[str]

    EVENT_LOC_TO_ITEM: Dict[str, str]
    REAL_ITEMS: List[str]

    VICTORY_CONDITION: str
    MASTERY_LOCATION: str
    LEVEL_2_LOCATION: str

    PAINTING_MAPPING: Dict[str, str]

    FORCED_GOOD_ITEM: str

    PANEL_REQS: Dict[str, Dict[str, AccessRequirements]]
    DOOR_REQS: Dict[str, Dict[str, AccessRequirements]]

    def add_location(self, room: str, name: str, code: Optional[int], panels: List[RoomAndPanel]):
        """
        Creates a location. This function determines the access requirements for the location by combining and
        flattening the requirements for each of the given panels.
        """
        access_reqs = AccessRequirements()
        for panel in panels:
            if panel.room is not None and panel.room != room:
                access_reqs.rooms.add(panel.room)

            panel_room = room if panel.room is None else panel.room
            sub_access_reqs = self.calculate_panel_requirements(panel_room, panel.panel)
            access_reqs.merge(sub_access_reqs)

        self.LOCATIONS_BY_ROOM.setdefault(room, []).append(PlayerLocation(name, code, access_reqs, 0))

    def set_door_item(self, room: str, door: str, item: str):
        self.ITEM_BY_DOOR.setdefault(room, {})[door] = item

    def handle_non_grouped_door(self, room_name: str, door_data: Door, world: "LingoWorld"):
        if room_name in PROGRESSION_BY_ROOM and door_data.name in PROGRESSION_BY_ROOM[room_name]:
            if room_name == "Orange Tower" and not world.options.progressive_orange_tower:
                self.set_door_item(room_name, door_data.name, door_data.item_name)
            else:
                progressive_item_name = PROGRESSION_BY_ROOM[room_name][door_data.name].item_name
                self.set_door_item(room_name, door_data.name, progressive_item_name)
                self.REAL_ITEMS.append(progressive_item_name)
        else:
            self.set_door_item(room_name, door_data.name, door_data.item_name)

    def __init__(self, world: "LingoWorld"):
        self.ITEM_BY_DOOR = {}
        self.LOCATIONS_BY_ROOM = {}
        self.REAL_LOCATIONS = []
        self.EVENT_LOC_TO_ITEM = {}
        self.REAL_ITEMS = []
        self.VICTORY_CONDITION = ""
        self.MASTERY_LOCATION = ""
        self.LEVEL_2_LOCATION = ""
        self.PAINTING_MAPPING = {}
        self.FORCED_GOOD_ITEM = ""
        self.PANEL_REQS = {}
        self.DOOR_REQS = {}

        door_shuffle = world.options.shuffle_doors
        color_shuffle = world.options.shuffle_colors
        painting_shuffle = world.options.shuffle_paintings
        location_checks = world.options.location_checks
        victory_condition = world.options.victory_condition
        early_color_hallways = world.options.early_color_hallways

        if location_checks == LocationChecks.option_reduced and door_shuffle != ShuffleDoors.option_none:
            raise Exception("You cannot have reduced location checks when door shuffle is on, because there would not "
                            "be enough locations for all of the door items.")

        # Create an event for every door, representing whether that door has been opened. Also create event items for
        # doors that are event-only.
        for room_name, room_data in DOORS_BY_ROOM.items():
            for door_name, door_data in room_data.items():
                if door_shuffle == ShuffleDoors.option_none:
                    itemloc_name = f"{room_name} - {door_name} (Opened)"
                    self.add_location(room_name, itemloc_name, None, door_data.panels)
                    self.EVENT_LOC_TO_ITEM[itemloc_name] = itemloc_name
                    self.set_door_item(room_name, door_name, itemloc_name)
                else:
                    # This line is duplicated from StaticLingoItems
                    if door_data.skip_item is False and door_data.event is False:
                        if door_data.group is not None and door_shuffle == ShuffleDoors.option_simple:
                            # Grouped doors are handled differently if shuffle doors is on simple.
                            self.set_door_item(room_name, door_name, door_data.group)
                        else:
                            self.handle_non_grouped_door(room_name, door_data, world)

                if door_data.event:
                    event_item_name = f"{door_data.item_name} (Opened)"
                    self.add_location(room_name, door_data.item_name, None, door_data.panels)
                    self.EVENT_LOC_TO_ITEM[door_data.item_name] = event_item_name
                    self.set_door_item(room_name, door_name, event_item_name)

        # Create events for each achievement panel, so that we can determine when THE MASTER is accessible.
        for room_name, room_data in PANELS_BY_ROOM.items():
            for panel_name, panel_data in room_data.items():
                if panel_data.achievement:
                    event_name = f"{room_name} - {panel_name} (Achieved)"
                    self.add_location(room_name, event_name, None, [RoomAndPanel(room_name, panel_name)])
                    self.EVENT_LOC_TO_ITEM[event_name] = "Mastery Achievement"

        # Handle the victory condition. Victory conditions other than the chosen one become regular checks, so we need
        # to prevent the actual victory condition from becoming a check.
        self.MASTERY_LOCATION = "Orange Tower Seventh Floor - THE MASTER"
        self.LEVEL_2_LOCATION = "N/A"

        if victory_condition == VictoryCondition.option_the_end:
            self.VICTORY_CONDITION = "Orange Tower Seventh Floor - THE END"
            self.add_location("Orange Tower Seventh Floor", "The End (Solved)", None, [])
            self.EVENT_LOC_TO_ITEM["The End (Solved)"] = "Victory"
        elif victory_condition == VictoryCondition.option_the_master:
            self.VICTORY_CONDITION = "Orange Tower Seventh Floor - THE MASTER"
            self.MASTERY_LOCATION = "Orange Tower Seventh Floor - Mastery Achievements"

            self.add_location("Orange Tower Seventh Floor", self.MASTERY_LOCATION, None, [])
            self.EVENT_LOC_TO_ITEM[self.MASTERY_LOCATION] = "Victory"
        elif victory_condition == VictoryCondition.option_level_2:
            self.VICTORY_CONDITION = "Second Room - LEVEL 2"
            self.LEVEL_2_LOCATION = "Second Room - Unlock Level 2"

            self.add_location("Second Room", self.LEVEL_2_LOCATION, None, [RoomAndPanel("Second Room", "LEVEL 2")])
            self.EVENT_LOC_TO_ITEM[self.LEVEL_2_LOCATION] = "Victory"

            self.create_panel_hunt_events(world)

        # Instantiate all real locations.
        location_classification = LocationClassification.normal
        if location_checks == LocationChecks.option_reduced:
            location_classification = LocationClassification.reduced
        elif location_checks == LocationChecks.option_insanity:
            location_classification = LocationClassification.insanity

        for location_name, location_data in ALL_LOCATION_TABLE.items():
            if location_name != self.VICTORY_CONDITION:
                if location_classification not in location_data.classification:
                    continue

                self.add_location(location_data.room, location_name, location_data.code, location_data.panels)
                self.REAL_LOCATIONS.append(location_name)

        # Instantiate all real items.
        for name, item in ALL_ITEM_TABLE.items():
            if item.should_include(world):
                self.REAL_ITEMS.append(name)

        # Create the paintings mapping, if painting shuffle is on.
        if painting_shuffle:
            # Shuffle paintings until we get something workable.
            workable_paintings = False
            for i in range(0, 20):
                workable_paintings = self.randomize_paintings(world)
                if workable_paintings:
                    break

            if not workable_paintings:
                raise Exception("This Lingo world was unable to generate a workable painting mapping after 20 "
                                "iterations. This is very unlikely to happen on its own, and probably indicates some "
                                "kind of logic error.")

        if door_shuffle != ShuffleDoors.option_none and location_classification != LocationClassification.insanity \
                and not early_color_hallways and LingoTestOptions.disable_forced_good_item is False:
            # If shuffle doors is on, force a useful item onto the HI panel. This may not necessarily get you out of BK,
            # but the goal is to allow you to reach at least one more check. The non-painting ones are hardcoded right
            # now. We only allow the entrance to the Pilgrim Room if color shuffle is off, because otherwise there are
            # no extra checks in there. We only include the entrance to the Rhyme Room when color shuffle is off and
            # door shuffle is on simple, because otherwise there are no extra checks in there.
            good_item_options: List[str] = ["Starting Room - Back Right Door", "Second Room - Exit Door"]

            if not color_shuffle:
                good_item_options.append("Pilgrim Room - Sun Painting")

            if door_shuffle == ShuffleDoors.option_simple:
                good_item_options += ["Welcome Back Doors"]

                if not color_shuffle:
                    good_item_options.append("Rhyme Room Doors")
            else:
                good_item_options += ["Welcome Back Area - Shortcut to Starting Room"]

            for painting_obj in PAINTINGS_BY_ROOM["Starting Room"]:
                if not painting_obj.enter_only or painting_obj.required_door is None:
                    continue

                # If painting shuffle is on, we only want to consider paintings that actually go somewhere.
                if painting_shuffle and painting_obj.id not in self.PAINTING_MAPPING.keys():
                    continue

                pdoor = DOORS_BY_ROOM[painting_obj.required_door.room][painting_obj.required_door.door]
                good_item_options.append(pdoor.item_name)

            # Copied from The Witness -- remove any plandoed items from the possible good items set.
            for v in world.multiworld.plando_items[world.player]:
                if v.get("from_pool", True):
                    for item_key in {"item", "items"}:
                        if item_key in v:
                            if type(v[item_key]) is str:
                                if v[item_key] in good_item_options:
                                    good_item_options.remove(v[item_key])
                            elif type(v[item_key]) is dict:
                                for item, weight in v[item_key].items():
                                    if weight and item in good_item_options:
                                        good_item_options.remove(item)
                            else:
                                # Other type of iterable
                                for item in v[item_key]:
                                    if item in good_item_options:
                                        good_item_options.remove(item)

            if len(good_item_options) > 0:
                self.FORCED_GOOD_ITEM = world.random.choice(good_item_options)
                self.REAL_ITEMS.remove(self.FORCED_GOOD_ITEM)
                self.REAL_LOCATIONS.remove("Second Room - Good Luck")

    def randomize_paintings(self, world: "LingoWorld") -> bool:
        self.PAINTING_MAPPING.clear()

        door_shuffle = world.options.shuffle_doors

        # First, assign mappings to the required-exit paintings. We ensure that req-blocked paintings do not lead to
        # required paintings.
        req_exits = []
        required_painting_rooms = REQUIRED_PAINTING_ROOMS
        if door_shuffle == ShuffleDoors.option_none:
            required_painting_rooms += REQUIRED_PAINTING_WHEN_NO_DOORS_ROOMS
            req_exits = [painting_id for painting_id, painting in PAINTINGS.items() if painting.required_when_no_doors]
            req_enterable = [painting_id for painting_id, painting in PAINTINGS.items()
                             if not painting.exit_only and not painting.disable and not painting.req_blocked and
                             not painting.req_blocked_when_no_doors and painting.room not in required_painting_rooms]
        else:
            req_enterable = [painting_id for painting_id, painting in PAINTINGS.items()
                             if not painting.exit_only and not painting.disable and not painting.req_blocked and
                             painting.room not in required_painting_rooms]
        req_exits += [painting_id for painting_id, painting in PAINTINGS.items()
                      if painting.exit_only and painting.required]
        req_entrances = world.random.sample(req_enterable, len(req_exits))

        self.PAINTING_MAPPING = dict(zip(req_entrances, req_exits))

        # Next, determine the rest of the exit paintings.
        exitable = [painting_id for painting_id, painting in PAINTINGS.items()
                    if not painting.enter_only and not painting.disable and painting_id not in req_exits and
                    painting_id not in req_entrances]
        nonreq_exits = world.random.sample(exitable, PAINTING_EXITS - len(req_exits))
        chosen_exits = req_exits + nonreq_exits

        # Determine the rest of the entrance paintings.
        enterable = [painting_id for painting_id, painting in PAINTINGS.items()
                     if not painting.exit_only and not painting.disable and painting_id not in chosen_exits and
                     painting_id not in req_entrances]
        chosen_entrances = world.random.sample(enterable, PAINTING_ENTRANCES - len(req_entrances))

        # Assign one entrance to each non-required exit, to ensure that the total number of exits is achieved.
        for warp_exit in nonreq_exits:
            warp_enter = world.random.choice(chosen_entrances)
            chosen_entrances.remove(warp_enter)
            self.PAINTING_MAPPING[warp_enter] = warp_exit

        # Assign each of the remaining entrances to any required or non-required exit.
        for warp_enter in chosen_entrances:
            warp_exit = world.random.choice(chosen_exits)
            self.PAINTING_MAPPING[warp_enter] = warp_exit

        # The Eye Wall painting is unique in that it is both double-sided and also enter only (because it moves).
        # There is only one eligible double-sided exit painting, which is the vanilla exit for this warp. If the
        # exit painting is an entrance in the shuffle, we will disable the Eye Wall painting. Otherwise, Eye Wall
        # is forced to point to the vanilla exit.
        if "eye_painting_2" not in self.PAINTING_MAPPING.keys():
            self.PAINTING_MAPPING["eye_painting"] = "eye_painting_2"

        # Just for sanity's sake, ensure that all required painting rooms are accessed.
        for painting_id, painting in PAINTINGS.items():
            if painting_id not in self.PAINTING_MAPPING.values() \
                    and (painting.required or (painting.required_when_no_doors and
                                               door_shuffle == ShuffleDoors.option_none)):
                return False

        return True

    def calculate_panel_requirements(self, room: str, panel: str):
        """
        Calculate and return the access requirements for solving a given panel. The goal is to eliminate recursion in
        the access rule function by collecting the rooms, doors, and colors needed by this panel and any panel required
        by this panel. Memoization is used so that no panel is evaluated more than once.
        """
        if panel not in self.PANEL_REQS.setdefault(room, {}):
            access_reqs = AccessRequirements()
            panel_object = PANELS_BY_ROOM[room][panel]

            for req_room in panel_object.required_rooms:
                access_reqs.rooms.add(req_room)

            for req_door in panel_object.required_doors:
                door_object = DOORS_BY_ROOM[room if req_door.room is None else req_door.room][req_door.door]
                if door_object.event:
                    sub_access_reqs = self.calculate_door_requirements(
                        room if req_door.room is None else req_door.room, req_door.door)
                    access_reqs.merge(sub_access_reqs)
                else:
                    access_reqs.doors.add(RoomAndDoor(room if req_door.room is None else req_door.room, req_door.door))

            for color in panel_object.colors:
                access_reqs.colors.add(color)

            for req_panel in panel_object.required_panels:
                if req_panel.room is not None and req_panel.room != room:
                    access_reqs.rooms.add(req_panel.room)

                sub_access_reqs = self.calculate_panel_requirements(room if req_panel.room is None else req_panel.room,
                                                                    req_panel.panel)
                access_reqs.merge(sub_access_reqs)

            self.PANEL_REQS[room][panel] = access_reqs

        return self.PANEL_REQS[room][panel]

    def calculate_door_requirements(self, room: str, door: str):
        """
        Similar to calculate_panel_requirements, but for event doors.
        """
        if door not in self.DOOR_REQS.setdefault(room, {}):
            access_reqs = AccessRequirements()
            door_object = DOORS_BY_ROOM[room][door]

            for req_panel in door_object.panels:
                if req_panel.room is not None and req_panel.room != room:
                    access_reqs.rooms.add(req_panel.room)

                sub_access_reqs = self.calculate_panel_requirements(room if req_panel.room is None else req_panel.room,
                                                                    req_panel.panel)
                access_reqs.merge(sub_access_reqs)

            self.DOOR_REQS[room][door] = access_reqs

        return self.DOOR_REQS[room][door]

    def create_panel_hunt_events(self, world: "LingoWorld"):
        """
        Creates the event locations/items used for determining access to the LEVEL 2 panel. Instead of creating an event
        for every single counting panel in the game, we try to coalesce panels with identical access rules into the same
        event. Right now, this means the following:

        When color shuffle is off, panels in a room with no extra access requirements (room, door, or other panel) are
        all coalesced into one event.

        When color shuffle is on, single-colored panels (including white) in a room are combined into one event per
        color. Multicolored panels and panels with any extra access requirements are not coalesced, and will each
        receive their own event.
        """
        for room_name, room_data in PANELS_BY_ROOM.items():
            unhindered_panels_by_color: dict[Optional[str], int] = {}

            for panel_name, panel_data in room_data.items():
                # We won't count non-counting panels.
                if panel_data.non_counting:
                    continue

                # We won't coalesce any panels that have requirements beyond colors. To simplify things for now, we will
                # only coalesce single-color panels. Chains/stacks/combo puzzles will be separate.
                if len(panel_data.required_panels) > 0 or len(panel_data.required_doors) > 0\
                        or len(panel_data.required_rooms) > 0\
                        or (world.options.shuffle_colors and len(panel_data.colors) > 1):
                    event_name = f"{room_name} - {panel_name} (Counted)"
                    self.EVENT_LOC_TO_ITEM[event_name] = "Counting Panel Solved"
                    self.LOCATIONS_BY_ROOM.setdefault(room_name, []).append(
                        PlayerLocation(event_name, None, self.calculate_panel_requirements(room_name, panel_name), 1))
                else:
                    if len(panel_data.colors) == 0 or not world.options.shuffle_colors:
                        color = None
                    else:
                        color = panel_data.colors[0]

                    unhindered_panels_by_color[color] = unhindered_panels_by_color.get(color, 0) + 1

            for color, panel_count in unhindered_panels_by_color.items():
                access_reqs = AccessRequirements()
                if color is None:
                    event_name = f"{room_name} - {panel_count} White Panels (Counted)"
                else:
                    event_name = f"{room_name} - {panel_count} {color.capitalize()} Panels (Counted)"
                    access_reqs.colors.add(color)

                self.LOCATIONS_BY_ROOM.setdefault(room_name, []).append(PlayerLocation(event_name, None, access_reqs,
                                                                                       panel_count))
                self.EVENT_LOC_TO_ITEM[event_name] = "Counting Panels Solved"
