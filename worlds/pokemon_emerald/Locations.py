from BaseClasses import Location
from .Data import get_region_data


class PokemonEmeraldLocation(Location):
    game: str = "Pokemon Emerald"
    id: int
    default_item_id: int

    def __init__(self, player: int, name: str, default_item_id: int, id: int, address: int, parent):
        super().__init__(player, name, address, parent)
        self.id = id
        self.default_item_id = default_item_id


def create_location_name_to_id_map():
    region_data = get_region_data()

    map = {}
    for region_data in region_data.values():
        for locaion_data in region_data.locations:
            map[locaion_data.name] = locaion_data.flag

    return map


def create_locations_with_tags(self, region_map, tags):
    region_data = get_region_data()
    tags = set(tags)

    for region_name, region_data in region_data.items():
        region = region_map[region_name]
        for location_data in [location for location in region_data.locations if len(tags & location.tags) > 0]:
            location = PokemonEmeraldLocation(self.player, location_data.name, location_data.default_item, location_data.flag, location_data.rom_address, region)
            region.locations.append(location)
