from typing import Dict, Any
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Items import item_table, group_table
from .Locations import location_table
from .Rules import create_rules
from .Options import short_hike_options

class ShortHikeWeb(WebWorld):
    theme = "ocean"

base_loc_id = 81000
base_item_id = 82000
class ShortHikeWorld(World):
    """
    A Short Hike is a relaxing adventure set on the islands of Hawk Peak. Fly and climb using Claire's wings and Golden Feathers
    to make your way up to the summit. Along the way you'll meet other hikers, discover hidden treasures,
    and take in the beautiful world around you.
    """

    game: str = "A Short Hike"
    web = ShortHikeWeb()
    data_version = 2

    item_name_to_id = {item["name"]: item["id"] for item in item_table}
    location_name_to_id = {loc["name"]: loc["id"] for loc in location_table}
    location_name_to_game_id = {loc["name"]: loc["inGameId"] for loc in location_table}
    location_name_to_chest_angle = {loc["name"]: loc["chestAngle"] for loc in location_table}

    item_name_groups = group_table
    option_definitions = short_hike_options

    required_client_version = (0, 1, 9)

    def __init__(self, multiworld, player):
        super(ShortHikeWorld, self).__init__(multiworld, player)

    def set_rules(self):
        create_rules()

    def create_item(self, name: str) -> "ShortHikeItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_item_id - 1

        return ShortHikeItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return ShortHikeItem(event, ItemClassification.progression_skip_balancing, None, self.player)

    def create_items(self) -> None:
        for item in item_table:
            count = item["count"]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    self.multiworld.itempool.append(self.create_item(item["name"]))
 
        junk = 0
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        main_region = Region("Hawk Peak", self.player, self.multiworld)

        for loc in self.location_name_to_id.keys():
            main_region.locations.append(ShortHikeLocation(self.player, loc, self.location_name_to_id[loc], main_region))

        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)

    def set_rules(self):
        create_rules(self, location_table)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        locations: Dict[int, Any] = {}

        world = self.multiworld
        player = self.player

        for loc in world.get_filled_locations(player):
            if loc.item.code == None:
                continue
            else:
                data = {
                    "ap_id": loc.address,
                    "item_name": loc.item.name,
                    "player_name": world.player_name[loc.item.player],
                    "type": int(loc.item.classification),
                    "chest_angle": self.location_name_to_chest_angle[loc.name],
                }

                locations[self.location_name_to_game_id[loc.name]] = data

        settings = {
            "goal": world.goal[player].value,
            "showGoldenChests": bool(world.show_golden_chests[player].value),
            "skipCutscenes": bool(world.skip_cutscenes[player].value),
        }
    
        slot_data = {
            "locations": locations,
            "settings": settings,
        }
    
        return slot_data


class ShortHikeItem(Item):
    game: str = "A Short Hike"


class ShortHikeLocation(Location):
    game: str = "A Short Hike"