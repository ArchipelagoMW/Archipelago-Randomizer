from typing import Dict, Optional, TYPE_CHECKING

from BaseClasses import Entrance, ItemClassification, Region
from .datatypes import EntranceType, Room, RoomAndDoor
from .items import LingoItem
from .locations import LingoLocation
from .options import SunwarpAccess
from .player_logic import AccessRequirements, LingoPlayerLogic, PlayerLocation
from .rules import lingo_can_do_pilgrimage, lingo_can_use_entrance, make_location_lambda
from .static_logic import ALL_ROOMS, PAINTINGS

if TYPE_CHECKING:
    from . import LingoWorld


def create_region(room: Room, world: "LingoWorld", player_logic: LingoPlayerLogic) -> Region:
    new_region = Region(room.name, world.player, world.multiworld)
    for location in player_logic.locations_by_room.get(room.name, {}):
        new_location = LingoLocation(world.player, location.name, location.code, new_region)
        new_location.access_rule = make_location_lambda(location, world, player_logic)
        new_region.locations.append(new_location)
        if location.name in player_logic.event_loc_to_item:
            event_name = player_logic.event_loc_to_item[location.name]
            event_item = LingoItem(event_name, ItemClassification.progression, None, world.player)
            new_location.place_locked_item(event_item)

    return new_region


def create_pilgrimage_region(room: Room, part: int, world: "LingoWorld", player_logic: LingoPlayerLogic) -> Region:
    new_region = Region(f"{room.name} (Pilgrimage Part {part})", world.player, world.multiworld)

    if player_logic.sunwarp_entrances[part] == room.name:
        access_reqs: AccessRequirements = AccessRequirements()
        if world.options.sunwarp_access >= SunwarpAccess.option_unlock:
            access_reqs.doors.add(RoomAndDoor("Sunwarps", f"{part+1} Sunwarp"))

        event_name = f"{part+1} Sunwarp Reached"
        new_location = LingoLocation(world.player, event_name, None, new_region)
        new_location.access_rule = make_location_lambda(PlayerLocation(event_name, None, access_reqs), world,
                                                        player_logic)
        new_location.place_locked_item(LingoItem(event_name, ItemClassification.progression, None, world.player))
        new_region.locations.append(new_location)

    return new_region


def is_acceptable_pilgrimage_entrance(entrance_type: EntranceType, world: "LingoWorld") -> bool:
    if entrance_type == EntranceType.SUNWARP or entrance_type == EntranceType.WARP:
        return False
    
    if entrance_type == EntranceType.PAINTING and not world.options.pilgrimage_allows_paintings:
        return False
    
    if entrance_type == EntranceType.CROSSROADS_ROOF_ACCESS and not world.options.pilgrimage_allows_roof_access:
        return False
    
    return True


def connect_entrance(regions: Dict[str, Region], source_region: Region, target_region: Region, description: str,
                     door: Optional[RoomAndDoor], entrance_type: EntranceType, pilgrimage: bool, world: "LingoWorld",
                     player_logic: LingoPlayerLogic):
    if description in world.multiworld.regions.entrance_cache[world.player]:
        description += f" ({entrance_type.name})"

    connection = Entrance(world.player, description, source_region)
    connection.access_rule = lambda state: lingo_can_use_entrance(state, target_region.name, door, world, player_logic)

    source_region.exits.append(connection)
    connection.connect(target_region)

    if door is not None:
        effective_room = target_region.name if door.room is None else door.room
        if door.door not in player_logic.item_by_door.get(effective_room, {}):
            for region in player_logic.calculate_door_requirements(effective_room, door.door, world).rooms:
                world.multiworld.register_indirect_condition(regions[region], connection)
    
    if not pilgrimage and world.options.enable_pilgrimage and is_acceptable_pilgrimage_entrance(entrance_type, world):
        for part in range(1, 6):
            pilgrimage_descriptor = f" (Pilgrimage Part {part})"
            if source_region.name == "Menu":
                pilgrim_source_region = source_region
            else:
                pilgrim_source_region = regions[f"{source_region.name}{pilgrimage_descriptor}"]
            pilgrim_target_region = regions[f"{target_region.name}{pilgrimage_descriptor}"]

            effective_door = door
            if effective_door is not None:
                effective_room = target_region.name if door.room is None else door.room
                effective_door = RoomAndDoor(effective_room, door.door)

            connect_entrance(regions, pilgrim_source_region, pilgrim_target_region,
                             f"{description}{pilgrimage_descriptor}", effective_door, entrance_type, True, world,
                             player_logic)


def connect_painting(regions: Dict[str, Region], warp_enter: str, warp_exit: str, world: "LingoWorld",
                     player_logic: LingoPlayerLogic) -> None:
    source_painting = PAINTINGS[warp_enter]
    target_painting = PAINTINGS[warp_exit]

    target_region = regions[target_painting.room]
    source_region = regions[source_painting.room]

    entrance_name = f"{source_painting.room} to {target_painting.room} ({source_painting.id} Painting)"
    connect_entrance(regions, source_region, target_region, entrance_name, source_painting.required_door,
                     EntranceType.PAINTING, False, world, player_logic)


def create_regions(world: "LingoWorld", player_logic: LingoPlayerLogic) -> None:
    regions = {
        "Menu": Region("Menu", world.player, world.multiworld)
    }

    painting_shuffle = world.options.shuffle_paintings
    early_color_hallways = world.options.early_color_hallways

    # Instantiate all rooms as regions with their locations first.
    for room in ALL_ROOMS:
        regions[room.name] = create_region(room, world, player_logic)

        if world.options.enable_pilgrimage:
            for part in range(1, 6):
                pilgrimage_region = create_pilgrimage_region(room, part, world, player_logic)
                regions[pilgrimage_region.name] = pilgrimage_region

    # Connect all created regions now that they exist.
    for room in ALL_ROOMS:
        for entrance in room.entrances:
            # Don't use the vanilla painting connections if we are shuffling paintings.
            if entrance.type == EntranceType.PAINTING and painting_shuffle:
                continue

            # Don't connect sunwarps if sunwarps are disabled or if we're shuffling sunwarps.
            if entrance.type == EntranceType.SUNWARP and (world.options.sunwarp_access == SunwarpAccess.option_disabled
                                                          or world.options.shuffle_sunwarps):
                continue

            entrance_name = f"{entrance.room} to {room.name}"
            if entrance.door is not None:
                if entrance.door.room is not None:
                    entrance_name += f" (through {entrance.door.room} - {entrance.door.door})"
                else:
                    entrance_name += f" (through {room.name} - {entrance.door.door})"

            effective_door = entrance.door
            if entrance.type == EntranceType.SUNWARP and world.options.sunwarp_access == SunwarpAccess.option_normal:
                effective_door = None

            connect_entrance(regions, regions[entrance.room], regions[room.name], entrance_name, effective_door,
                             entrance.type, False, world, player_logic)

    if world.options.enable_pilgrimage:
        # Create connections from Menu for the beginning of each pilgrimage segment.
        for i in range(0, 5):
            regions["Menu"].connect(regions[f"{player_logic.sunwarp_exits[i]} (Pilgrimage Part {i+1})"],
                                    f"Pilgrimage Part {i+1}")

        # Create the actual pilgrimage.
        regions[player_logic.sunwarp_entrances[0]].connect(regions["Pilgrim Antechamber"], "Pilgrimage",
                                                           lambda state: lingo_can_do_pilgrimage(state, world,
                                                                                                 player_logic))
    else:
        connect_entrance(regions, regions["Starting Room"], regions["Pilgrim Antechamber"], "Sun Painting",
                         RoomAndDoor("Pilgrim Antechamber", "Sun Painting"), EntranceType.PAINTING, False, world,
                         player_logic)

    if early_color_hallways:
        connect_entrance(regions, regions["Starting Room"], regions["Outside The Undeterred"], "Early Color Hallways",
                         None, EntranceType.PAINTING, False, world, player_logic)

    if painting_shuffle:
        for warp_enter, warp_exit in player_logic.painting_mapping.items():
            connect_painting(regions, warp_enter, warp_exit, world, player_logic)

    if world.options.shuffle_sunwarps:
        for i in range(0, 6):
            if world.options.sunwarp_access == SunwarpAccess.option_normal:
                effective_door = None
            else:
                effective_door = RoomAndDoor("Sunwarps", f"{i + 1} Sunwarp")

            source_region = regions[player_logic.sunwarp_entrances[i]]
            target_region = regions[player_logic.sunwarp_exits[i]]

            entrance_name = f"{source_region.name} to {target_region.name} ({i + 1} Sunwarp)"
            connect_entrance(regions, source_region, target_region, entrance_name, effective_door, EntranceType.SUNWARP,
                             False, world, player_logic)

    world.multiworld.regions += regions.values()
