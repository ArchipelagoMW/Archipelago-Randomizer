from typing import Dict, List, Set, Any
from collections import Counter
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Items import base_id, item_table, group_table, tears_set, reliquary_set
from .Locations import location_table
from .Rooms import room_table, door_table
from .Rules import rules
from worlds.generic.Rules import set_rule, add_rule
from .Options import blasphemous_options
from .Vanilla import unrandomized_dict, junk_locations, thorn_set, skill_dict


class BlasphemousWeb(WebWorld):
    theme = "stone"
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
    Blasphemous is a challenging Metroidvania set in the cursed land of Cvstodia. Play as the Penitent One, trapped
    in an endless cycle of death and rebirth, and free the world from it's terrible fate in your quest to break
    your eternal damnation!
    """

    game: str = "Blasphemous"
    web = BlasphemousWeb()
    data_version = 1

    item_name_to_id = {item["name"]: (base_id + index) for index, item in enumerate(item_table)}
    location_name_to_id = {loc["name"]: (base_id + index) for index, loc in enumerate(location_table)}
    location_name_to_game_id = {loc["name"]: loc["game_id"] for loc in location_table}

    item_name_groups = group_table
    option_definitions = blasphemous_options


    #def set_rules(self):
        #rules(self)


    def create_item(self, name: str) -> "BlasphemousItem":
        item_id: int = self.item_name_to_id[name]
        id = item_id - base_id

        return BlasphemousItem(name, item_table[id]["classification"], item_id, player=self.player)


    def create_event(self, event: str):
        return BlasphemousItem(event, ItemClassification.progression_skip_balancing, None, self.player)


    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(tears_set)


    def generate_early(self):
        world = self.multiworld
        player = self.player

        if not world.dash_shuffle[player]:
            world.start_inventory[player].value["Dash"] = 1

        if not world.wall_climb_shuffle[player]:
            world.start_inventory[player].value["Wall Climb"] = 1

        if world.skip_long_quests[player]:
            for loc in junk_locations:
                world.exclude_locations[player].value.add(loc)


    def create_items(self):
        world = self.multiworld
        player = self.player

        removed: int = 0
        to_remove: List[str] = [
            "Tears of Atonement (250)",
            "Tears of Atonement (300)",
            "Tears of Atonement (500)",
            "Tears of Atonement (500)",
            "Tears of Atonement (500)"
        ]

        placed_items = []

        placed_items.extend(unrandomized_dict.values())

        if world.thorn_shuffle[player] == 2:
            for i in range(8):
                placed_items.append("Thorn Upgrade")

        if world.dash_shuffle[player]:
            placed_items.append(to_remove[removed])
            removed += 1

        if world.wall_climb_shuffle[player]:
            placed_items.append(to_remove[removed])
            removed += 1

        if not world.reliquary_shuffle[player]:
            placed_items.extend(reliquary_set)
        elif world.reliquary_shuffle[player]:
            for i in range(3):
                placed_items.append(to_remove[removed])
                removed += 1

        if world.start_wheel[player]:
            placed_items.append("The Young Mason's Wheel")

        if not world.skill_randomizer[player]:
            placed_items.extend(skill_dict.values())

        counter = Counter(placed_items)

        pool = []

        for item in item_table:
            if not world.dash_shuffle[player] and item["name"] == "Dash":
                continue
            if not world.wall_climb_shuffle[player] and item["name"] == "Wall Climb":
                continue
            if not world.boots_of_pleading[player] and item["name"] == "Boots of Pleading":
                continue
            if not world.purified_hand[player] and item["name"] == "Purified Hand of the Nun":
                continue

            count = item["count"] - counter[item["name"]]
            
            if count <= 0:
                continue
            else:
                for i in range(count):
                    pool.append(self.create_item(item["name"]))

        world.itempool += pool


    def pre_fill(self):
        self.place_items_from_dict(unrandomized_dict)

        if self.multiworld.thorn_shuffle[self.player] == 2:
            self.place_items_from_set(thorn_set, "Thorn Upgrade")

        if self.multiworld.start_wheel[self.player]:
            self.multiworld.get_location("BotSS: Beginning gift", self.player)\
                .place_locked_item(self.create_item("The Young Mason's Wheel"))

        if not self.multiworld.skill_randomizer[self.player]:
            self.place_items_from_dict(skill_dict)

        if self.multiworld.thorn_shuffle[self.player] == 1:
            self.multiworld.local_items[self.player].value.add("Thorn Upgrade")
        

    def place_items_from_set(self, location_set: Set[str], name: str):
        for loc in location_set:
            self.multiworld.get_location(loc, self.player)\
                .place_locked_item(self.create_item(name))

    
    def place_items_from_dict(self, option_dict: Dict[str, str]):
        for loc, item in option_dict.items():
            self.multiworld.get_location(loc, self.player)\
                .place_locked_item(self.create_item(item))


    def create_regions(self) -> None:
        player = self.player
        world = self.multiworld
        
        menu = Region("Menu", player, world)
        misc = Region("Misc", player, world)

        world.regions.append(menu)
        world.regions.append(misc)

        for room in room_table:
            reg = Region(room, player, world)
            world.regions.append(reg)

        ent = Entrance(player, "Misc", world.get_region("D17Z01S01", player))
        ent.connect(misc)
        world.get_region("D17Z01S01", player).exits.append(ent)

        ent2 = Entrance(player, "New Game", menu)
        ent2.connect(world.get_region("D17Z01S01", player))
        menu.exits.append(ent2)

        if not world.door_randomizer[player]:
            for door in door_table:
                if door.get("OriginalDoor") is None:
                    continue
                else:
                    parent: Region = self.get_room_from_door(door["Id"])
                    target: Region = self.get_room_from_door(door["OriginalDoor"])
                    exit = Entrance(player, door["Id"], parent)

                    exit.connect(target)
                    parent.exits.append(exit)

        for door in door_table:
            if door.get("RequiredDoors") is not None:
                for d in door["RequiredDoors"]:
                    #print(d, self.get_connected_door(d))
                    connection = self.get_connected_door(d)
                    add_rule(world.get_entrance(door["Id"], player), lambda state: state.can_reach(connection), "or")
                add_rule(world.get_entrance(door["Id"], player), lambda state: state.can_reach(self.get_connected_door(door["Id"])), "or")

        for loc in location_table:
            if not world.boots_of_pleading[player] and loc["name"] == "BotSS: 2nd meeting with Redento":
                continue
            if not world.purified_hand[player] and loc["name"] == "MoM: Western room ledge":
                continue

            reg: Region = world.get_region(loc["room"], player)

            id = base_id + location_table.index(loc)
            reg.locations.append(BlasphemousLocation(player, loc["name"], id, reg))
        
        victory = Location(player, "His Holiness Escribar", None, world.get_region("D07Z01S03", player))
        victory.place_locked_item(self.create_event("Victory"))
        world.get_region("D07Z01S03", player).locations.append(victory)

        if world.ending[self.player].value == 1:
            set_rule(victory, lambda state: state.has("Thorn Upgrade", player, 8))
        elif world.ending[self.player].value == 2:
            set_rule(victory, lambda state: state.has("Thorn Upgrade", player, 8) and \
                state.has("Holy Wound of Abnegation", player))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)
        

    def get_room_from_door(self, door: str) -> Region:
        return self.multiworld.get_region(door.split("[")[0], self.player)

    
    def get_connected_door(self, door: str) -> Entrance:
        player = self.player
        world = self.multiworld

        target: str

        try: 
            world.get_entrance(door, player)
        except KeyError:
            parent = self.get_room_from_door(door)
            for r in world.get_regions(player):
                for e in r.exits:
                    if e.connected_region == parent:
                        target = e.name
        else:
            parent = world.get_entrance(door, player)
            for e in parent.connected_region.exits:
                if e.connected_region == parent.parent_region:
                    target = e.name

        return world.get_entrance(target, player)

    
    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}
        locations = []

        world = self.multiworld
        player = self.player
        thorns: bool = True

        if world.thorn_shuffle[player].value == 2:
            thorns = False

        for loc in world.get_filled_locations(player):
            if loc.name == "His Holiness Escribar":
                continue
            else:
                data = {
                    "id": self.location_name_to_game_id[loc.name],
                    "ap_id": loc.address,
                    "name": loc.item.name,
                    "player_name": world.player_name[loc.item.player]
                }

                locations.append(data)

        config = {
            "LogicDifficulty": world.difficulty[player].value,
            "StartingLocation": 0,
            "VersionCreated": "AP",
            
            "UnlockTeleportation": bool(world.prie_dieu_warp[player].value),
            "AllowHints": bool(world.corpse_hints[player].value),
            "AllowPenitence": bool(world.penitence[player].value),
            
            "ShuffleReliquaries": bool(world.reliquary_shuffle[player].value),
            "ShuffleBootsOfPleading": bool(world.boots_of_pleading[player].value),
            "ShufflePurifiedHand": bool(world.purified_hand[player].value),
            "ShuffleDash": bool(world.dash_shuffle[player].value),
            "ShuffleWallClimb": bool(world.wall_climb_shuffle[player].value),
            
            "ShuffleSwordSkills": bool(world.skill_randomizer[player].value),
            "ShuffleThorns": thorns,
            "JunkLongQuests": bool(world.skip_long_quests[player].value),
            "StartWithWheel": bool(world.start_wheel[player].value),

            "EnemyShuffleType": world.enemy_randomizer[player].value,
            "MaintainClass": bool(world.enemy_groups[player].value),
            "AreaScaling": bool(world.enemy_scaling[player].value),

            "BossShuffleType": 0,
            "DoorShuffleType": 0
        }
    
        slot_data = {
            "locations": locations,
            "cfg": config,
            "ending": world.ending[self.player].value,
            "death_link": bool(world.death_link[self.player].value)
        }
    
        return slot_data


class BlasphemousItem(Item):
    game: str = "Blasphemous"


class BlasphemousLocation(Location):
    game: str = "Blasphemous"