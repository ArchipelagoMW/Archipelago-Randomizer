from typing import Protocol

from BaseClasses import Region, Entrance
from . import vanilla_data, mods
from .entrance_rando import create_player_randomization_flag, create_entrance_rando_target
from .model import ConnectionData, RegionData
from ..content import StardewContent
from ..content.vanilla.ginger_island import ginger_island_content_pack
from ..options import StardewValleyOptions


class RegionFactory(Protocol):
    def __call__(self, name: str) -> Region:
        raise NotImplementedError


def create_regions(region_factory: RegionFactory, world_options: StardewValleyOptions, content: StardewContent) \
        -> tuple[dict[str, Region], dict[str, Entrance]]:
    connection_data_by_name, region_data_by_name = create_connections_and_regions(content.registered_packs)

    regions_by_name: dict[str: Region] = {
        region_name: region_factory(region_name)
        for region_name in region_data_by_name
    }

    entrances_by_name: dict[str: Entrance] = {}

    # Not really a mask... :thinking:
    randomization_flag = create_player_randomization_flag(world_options.entrance_randomization, content)

    for region_name, region_data in region_data_by_name.items():
        origin_region = regions_by_name[region_name]

        for exit_name in region_data.exits:
            connection_data = connection_data_by_name[exit_name]
            destination_region = regions_by_name[connection_data.destination]

            if connection_data.is_eligible_for_randomization(randomization_flag):
                create_entrance_rando_target(origin_region, destination_region, connection_data)
            else:
                origin_region.connect(destination_region, connection_data.name)

    return regions_by_name, entrances_by_name


def create_connections_and_regions(active_content_packs: set[str]) -> tuple[dict[str, ConnectionData], dict[str, RegionData]]:
    regions_by_name = create_all_regions(active_content_packs)
    connections_by_name = create_all_connections(active_content_packs)

    return connections_by_name, regions_by_name


def create_vanilla_regions(active_content_packs: set[str]) -> dict[str, RegionData]:
    if ginger_island_content_pack.name in active_content_packs:
        return {**vanilla_data.regions_with_ginger_island_by_name}
    else:
        return {**vanilla_data.regions_without_ginger_island_by_name}


def create_all_regions(active_content_packs: set[str]) -> dict[str, RegionData]:
    current_regions_by_name = create_vanilla_regions(active_content_packs)
    mods.modify_regions_for_mods(current_regions_by_name, active_content_packs)
    return current_regions_by_name


def create_vanilla_connections(active_content_packs: set[str]) -> dict[str, ConnectionData]:
    if ginger_island_content_pack.name in active_content_packs:
        return {**vanilla_data.connections_with_ginger_island_by_name}
    else:
        return {**vanilla_data.connections_without_ginger_island_by_name}


def create_all_connections(active_content_packs: set[str]) -> dict[str, ConnectionData]:
    connections = create_vanilla_connections(active_content_packs)
    mods.modify_connections_for_mods(connections, active_content_packs)
    return connections
