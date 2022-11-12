from typing import Dict, Set
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification, RegionType
from worlds.generic.Rules import set_rule
from ..AutoWorld import World, WebWorld
from .Items import item_table, group_table, tears_set
from .Locations import location_table
from .Exits import region_exit_table, exit_lookup_table
from .Rules import rules
from .Options import blasphemous_options


class BlasphemousWeb(WebWorld):
    theme = ""
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Blasphemous randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["TRPG"]
    )]


class BlasphemousWorld(World):
    """
    description
    """

    game: str = "Blasphemous"
    web = BlasphemousWeb()
    base_id = 1909000
    data_version: 0

    item_name_to_id = {item["name"]: (1909000 + item_table.index(item)) for item in item_table}
    location_name_to_id = {loc["name"]: (1909000 + location_table.index(loc)) for loc in location_table}
    item_name_groups = group_table
    option_definitions = blasphemous_options


    def set_rules(self):
        rules(self)


    def create_item(self, name: str) -> "BlasphemousItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - self.base_id

        return BlasphemousItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return BlasphemousItem(event, ItemClassification.progression_skip_balancing, None, self.player)


    def add_item(self, name: str, classification: ItemClassification, code: int) -> "Item":
        return BlasphemousItem(name, classification, code, self.player)


    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(tears_set)

    
    def generate_basic(self):
        pool = []

        for item in item_table:
            id = self.base_id + item_table.index(item)
            for i in range(item["count"]):
                pool.append(self.add_item(item["name"], item["classification"], id))

        while len(self.multiworld.get_locations()) > len(pool):
            pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += pool


    def create_regions(self) -> None:
        
        type = RegionType.Generic
        player = self.player
        world = self.multiworld

        region_table: Dict[str, Region] = {
            "menu"    : Region("Menu", type, 
                            "Menu", player, world),
            "albero"  : Region("Albero", type, 
                            "Albero", player, world),
            "attots"  : Region("All the Tears of the Sea", type, 
                            "All the Tears of the Sea", player, world),
            "ar"      : Region("Archcathedral Rooftops", type, 
                            "Archcathedral Rooftops", player, world),
            "bottc"   : Region("Bridge of the Three Cavalries", type, 
                            "Bridge of the Three Cavalries", player, world),
            "botss"   : Region("Brotherhood of the Silent Sorrow", type, 
                            "Brotherhood of the Silent Sorrow", player, world),
            "coolotcv": Region("Convent of Our Lady of the Charred Visage", type, 
                            "Convent of Our Lady of the Charred Visage", player, world),
            "dohh"    : Region("Deambulatory of His Holiness", type, 
                            "Deambulatory of His Holiness", player, world),
            "dc"      : Region("Desecrated Cistern", type, 
                            "Desecrated Cistern", player, world),
            "eos"     : Region("Echoes of Salt", type, 
                            "Echoes of Salt", player, world),
            "ft"      : Region("Ferrous Tree", type,
                            "Ferrous Tree", player, world),
            "gotp"    : Region("Graveyard of the Peaks", type, 
                            "Graveyard of the Peaks", player, world),
            "ga"      : Region("Grievance Ascends", type, 
                            "Grievance Ascends", player, world),
            "hotd"    : Region("Hall of the Dawning", type, 
                            "Hall of the Dawning", player, world),
            "jondo"   : Region("Jondo", type, 
                            "Jondo", player, world),
            "kottw"   : Region("Knot of the Three Words", type, 
                            "Knot of the Three Words", player, world),
            "lotnw"   : Region("Library of the Negated Words", type, 
                            "Library of the Negated Words", player, world),
            "md"      : Region("Mercy Dreams", type, 
                            "Mercy Dreams", player, world),
            "mom"     : Region("Mother of Mothers", type, 
                            "Mother of Mothers", player, world),
            "moted"   : Region("Mountains of the Endless Dusk", type, 
                            "Mountains of the Endless Dusk", player, world),
            "mah"     : Region("Mourning and Havoc", type, 
                            "Mourning and Havoc", player, world),
            "potss"   : Region("Patio of the Silent Steps", type, 
                            "Patio of the Silent Steps", player, world),
            "petrous" : Region("Petrous", type, 
                            "Petrous", player, world),
            "thl"     : Region("The Holy Line", type, 
                            "The Holy Line", player, world),
            "trpots"  : Region("The Resting Place of the Sister", type, 
                            "The Resting Place of the Sister", player, world),
            "tsc"     : Region("The Sleeping Canvases", type, 
                            "The Sleeping Canvases", player, world),
            "wothp"   : Region("Wall of the Holy Prohibitions", type, 
                            "Wall of the Holy Prohibitions", player, world),
            "wotbc"   : Region("Wasteland of the Buried Churches", type, 
                            "Wasteland of the Buried Churches", player, world),
            "wotw"    : Region("Where Olive Trees Wither", type, 
                            "Where Olive Trees Wither", player, world),
            "dungeon" : Region("Dungeons", type,
                            "Dungeons", player, world)
        }

        for rname, reg in region_table.items():
            world.regions.append(reg)

            for ename, exits in region_exit_table.items():
                if ename == rname:
                    for i in exits:
                        ent = Entrance(player, i, reg)
                        reg.exits.append(ent)

                        for e, r in exit_lookup_table.items():
                            if i == e:
                                ent.connect(region_table[r])

        for loc in location_table:
            id = self.base_id + location_table.index(loc)
            region_table[loc["region"]].locations\
                .append(BlasphemousLocation(self.player, loc["name"], id, region_table[loc["region"]]))


class BlasphemousItem(Item):
    game: str = "Blasphemous"


class BlasphemousLocation(Location):
    game: str = "Blasphemous"