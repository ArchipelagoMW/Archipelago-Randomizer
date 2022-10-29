from typing import TextIO
import os
import logging

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from Fill import fill_restrictive, FillError, sweep_from_pool
from ..AutoWorld import World, WebWorld
from ..generic.Rules import add_item_rule
from .items import item_table, item_groups
from .locations import location_data, PokemonRBLocation
from .regions import create_regions
from .logic import PokemonLogic
from .options import pokemon_rb_options
from .rom_addresses import rom_addresses
from .text import encode_text
from .rom import generate_output, get_base_rom_bytes, get_base_rom_path, process_pokemon_data, process_wild_pokemon,\
    process_static_pokemon
from .rules import set_rules

import worlds.pokemon_rb.poke_data as poke_data


class PokemonWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pokemon Red and Blue with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Alchav"]
    )]


class PokemonRedBlueWorld(World):
    """Pokémon Red and Pokémon Blue are the original monster-collecting turn-based RPGs.  Explore the Kanto region with
    your Pokémon, catch more than 150 unique creatures, earn badges from the region's Gym Leaders, and challenge the
    Elite Four to become the champion!"""
    # -MuffinJets#4559
    game = "Pokemon Red and Blue"
    option_definitions = pokemon_rb_options
    remote_items = False
    data_version = 1
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {location.name: location.address for location in location_data if location.type == "Item"}
    item_name_groups = item_groups

    web = PokemonWebWorld()

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.fly_map = None
        self.fly_map_code = None
        self.extra_badges = {}
        self.type_chart = None
        self.local_poke_data = None
        self.learnsets = None
        self.trainer_name = None
        self.rival_name = None

    @classmethod
    def stage_assert_generate(cls, world):
        versions = set()
        for player in world.player_ids:
            if world.worlds[player].game == "Pokemon Red and Blue":
                versions.add(world.game_version[player].current_key)
        for version in versions:
            if not os.path.exists(get_base_rom_path(version)):
                raise FileNotFoundError(get_base_rom_path(version))

    def generate_early(self):
        def encode_name(name, t):
            try:
                if len(encode_text(name)) > 7:
                    raise IndexError(f"{t} name too long for player {self.world.player_name[self.player]}. Must be 7 characters or fewer.")
                return encode_text(name, length=8, whitespace="@", safety=True)
            except KeyError as e:
                raise KeyError(f"Invalid character(s) in {t} name for player {self.world.player_name[self.player]}") from e
        self.trainer_name = encode_name(self.world.trainer_name[self.player].value, "Player")
        self.rival_name = encode_name(self.world.rival_name[self.player].value, "Rival")

        if len(self.world.player_name[self.player].encode()) > 16:
            raise Exception(f"Player name too long for {self.world.get_player_name(self.player)}. Player name cannot exceed 16 bytes for Pokémon Red and Blue.")

        if self.world.badges_needed_for_hm_moves[self.player].value >= 2:
            badges_to_add = ["Marsh Badge", "Volcano Badge", "Earth Badge"]
            if self.world.badges_needed_for_hm_moves[self.player].value == 3:
                badges = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Marsh Badge",
                          "Soul Badge", "Volcano Badge", "Earth Badge"]
                self.world.random.shuffle(badges)
                badges_to_add += [badges.pop(), badges.pop()]
            hm_moves = ["Cut", "Fly", "Surf", "Strength", "Flash"]
            self.world.random.shuffle(hm_moves)
            self.extra_badges = {}
            for badge in badges_to_add:
                self.extra_badges[hm_moves.pop()] = badge

        process_pokemon_data(self)

    def create_items(self) -> None:
        start_inventory = self.world.start_inventory[self.player].value.copy()
        locations = [location for location in location_data if location.type == "Item"]
        item_pool = []
        for location in locations:
            if "Hidden" in location.name and not self.world.randomize_hidden_items[self.player].value:
                continue
            if "Rock Tunnel B1F" in location.region and not self.world.extra_key_items[self.player].value:
                continue
            if location.name == "Celadon City - Mansion Lady" and not self.world.tea[self.player].value:
                continue
            if location.original_item in self.world.start_inventory[self.player].value and \
                    location.original_item in item_groups["Unique"]:
                start_inventory[location.original_item] -= 1
                item = self.create_filler()
            else:
                item = self.create_item(location.original_item)
            if location.event:
                self.world.get_location(location.name, self.player).place_locked_item(item)
            elif ("Badge" not in item.name or self.world.badgesanity[self.player].value) and \
                    (item.name != "Oak's Parcel" or self.world.old_man[self.player].value != 1):
                item_pool.append(item)
        self.world.random.shuffle(item_pool)

        self.world.itempool += item_pool

    def generate_basic(self) -> None:

        process_wild_pokemon(self)
        process_static_pokemon(self)

        if self.world.old_man[self.player].value == 1:
            item = self.create_item("Oak's Parcel")
            locations = []
            for location in self.world.get_locations():
                if location.player == self.player and location.item is None and location.can_reach(self.world.state) \
                        and location.item_rule(item):
                    locations.append(location)
            self.world.random.choice(locations).place_locked_item(item)

        if not self.world.badgesanity[self.player].value:
            self.world.non_local_items[self.player].value -= self.item_name_groups["Badges"]
            for i in range(5):
                try:
                    badges = []
                    badgelocs = []
                    for badge in ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge",
                                  "Marsh Badge", "Volcano Badge", "Earth Badge"]:
                        badges.append(self.create_item(badge))
                    for loc in ["Pewter Gym - Brock 1", "Cerulean Gym - Misty 1", "Vermilion Gym - Lt. Surge 1",
                                "Celadon Gym - Erika 1", "Fuchsia Gym - Koga 1", "Saffron Gym - Sabrina 1",
                                "Cinnabar Gym - Blaine 1", "Viridian Gym - Giovanni 1"]:
                        badgelocs.append(self.world.get_location(loc, self.player))
                    state = self.world.get_all_state(False)
                    self.world.random.shuffle(badges)
                    self.world.random.shuffle(badgelocs)
                    fill_restrictive(self.world, state, badgelocs.copy(), badges, True, True)
                except FillError:
                    for location in badgelocs:
                        location.item = None
                    continue
                break
            else:
                raise FillError(f"Failed to place badges for player {self.player}")

        locs = [self.world.get_location("Fossil - Choice A", self.player),
                self.world.get_location("Fossil - Choice B", self.player)]
        for loc in locs:
            add_item_rule(loc, lambda i: i.advancement or i.name in self.item_name_groups["Unique"]
                                         or i.name == "Master Ball")

        loc = self.world.get_location("Pallet Town - Player's PC", self.player)
        if loc.item is None:
            locs.append(loc)

        for loc in locs:
            unplaced_items = []
            if loc.name in self.world.priority_locations[self.player].value:
                add_item_rule(loc, lambda i: i.advancement)
            for item in reversed(self.world.itempool):
                if item.player == self.player and loc.item_rule(item):
                    self.world.itempool.remove(item)
                    state = sweep_from_pool(self.world.state, self.world.itempool + unplaced_items)
                    if state.can_reach(loc, "Location", self.player):
                        loc.place_locked_item(item)
                        break
                    else:
                        unplaced_items.append(item)
            self.world.itempool += unplaced_items

        intervene = False
        test_state = self.world.get_all_state(False)
        if not test_state.pokemon_rb_can_surf(self.player) or not test_state.pokemon_rb_can_strength(self.player):
            intervene = True
        elif self.world.accessibility[self.player].current_key != "minimal":
            if not test_state.pokemon_rb_can_cut(self.player) or not test_state.pokemon_rb_can_flash(self.player):
                intervene = True
        if intervene:
            # the way this is handled will be improved significantly in the future when I add options to
            # let you choose the exact weights for HM compatibility
            logging.warning(
                f"HM-compatible Pokémon possibly missing, placing Mew on Route 1 for player {self.player}")
            loc = self.world.get_location("Route 1 - Wild Pokemon - 1", self.player)
            loc.item = self.create_item("Mew")

    def create_regions(self):
        if self.world.free_fly_location[self.player].value:
            if self.world.old_man[self.player].value == 0:
                fly_map_code = self.world.random.randint(1, 9)
            else:
                fly_map_code = self.world.random.randint(5, 9)
                if fly_map_code == 5:
                    fly_map_code = 4
            if fly_map_code == 9:
                fly_map_code = 10
        else:
            fly_map_code = 0
        self.fly_map = ["Pallet Town", "Viridian City", "Pewter City", "Cerulean City", "Lavender Town",
                        "Vermilion City", "Celadon City", "Fuchsia City", "Cinnabar Island", "Indigo Plateau",
                        "Saffron City"][fly_map_code]
        self.fly_map_code = fly_map_code
        create_regions(self.world, self.player)
        self.world.completion_condition[self.player] = lambda state, player=self.player: state.has("Become Champion", player=player)

    def set_rules(self):
        set_rules(self.world, self.player)

    def create_item(self, name: str) -> Item:
        return PokemonRBItem(name, self.player)

    def generate_output(self, output_directory: str):
        generate_output(self, output_directory)

    def write_spoiler_header(self, spoiler_handle: TextIO):
        if self.world.free_fly_location[self.player].value:
            spoiler_handle.write('Fly unlocks:                     %s\n' % self.fly_map)
        if self.extra_badges:
            for hm_move, badge in self.extra_badges.items():
                spoiler_handle.write(hm_move + " enabled by: " + (" " * 20)[:20 - len(hm_move)] + badge + "\n")

    def write_spoiler(self, spoiler_handle):
        if self.world.randomize_type_matchup_types[self.player].value or \
                self.world.randomize_type_matchup_type_effectiveness[self.player].value:
            spoiler_handle.write(f"\n\nType matchups ({self.world.player_name[self.player]}):\n\n")
            for matchup in self.type_chart:
                spoiler_handle.write(f"{matchup[0]} deals {matchup[2] * 10}% damage to {matchup[1]}\n")

    def get_filler_item_name(self) -> str:
        return self.world.random.choice([item for item in item_table if item_table[item].classification in
                                         [ItemClassification.filler, ItemClassification.trap] and item not in
                                         item_groups["Vending Machine Drinks"]])

    def fill_slot_data(self) -> dict:
        # for trackers
        return {
            "second_fossil_check_condition": self.world.second_fossil_check_condition[self.player].value,
            "require_item_finder": self.world.require_item_finder[self.player].value,
            "randomize_hidden_items": self.world.randomize_hidden_items[self.player].value,
            "badges_needed_for_hm_moves": self.world.badges_needed_for_hm_moves[self.player].value,
            "oaks_aide_rt_2": self.world.oaks_aide_rt_2[self.player].value,
            "oaks_aide_rt_11": self.world.oaks_aide_rt_11[self.player].value,
            "oaks_aide_rt_15": self.world.oaks_aide_rt_15[self.player].value,
            "extra_key_items": self.world.extra_key_items[self.player].value,
            "extra_strength_boulders": self.world.extra_strength_boulders[self.player].value,
            "tea": self.world.tea[self.player].value,
            "old_man": self.world.old_man[self.player].value,
            "elite_four_condition": self.world.elite_four_condition[self.player].value,
            "victory_road_condition": self.world.victory_road_condition[self.player].value,
            "viridian_gym_condition": self.world.viridian_gym_condition[self.player].value,
            "free_fly_map": self.fly_map_code,
            "extra_badges": self.extra_badges
        }


class PokemonRBItem(Item):
    game = "Pokemon Red and Blue"
    type = None

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(PokemonRBItem, self).__init__(
            name,
            item_data.classification,
            item_data.id, player
        )
