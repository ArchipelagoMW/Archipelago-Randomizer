import os
import typing
import math

from BaseClasses import Item, MultiWorld
from .Items import SA2BItem, ItemData, item_table, upgrades_table
from .Locations import SA2BLocation, all_locations, setup_locations
from .Options import sa2b_options
from .Regions import create_regions, shuffleable_regions, connect_regions, LevelGate, gate_0_whitelist_regions, gate_0_blacklist_regions
from .Rules import set_rules
from .Names import ItemName
from ..AutoWorld import World
import Patch


class SA2BWorld(World):
    """
    J.R.R. Tolkien's The Lord of the Rings, Vol. 1 is an SNES Action-RPG brought to you by the minds that would
    eventually bring you the original Fallout. Embark on Frodo's legendary journey to destroy the One Ring and 
    rid Middle-Earth of the shadow of the Dark Lord Sauron forever.
    """
    game: str = "Sonic Adventure 2 Battle"
    options = sa2b_options
    topology_present = False
    data_version = 0

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = all_locations

    music_map: typing.Dict[int, int]
    emblems_for_cannons_core: int
    region_emblem_map: typing.Dict[int, int]

    def _get_slot_data(self):
        return {
            "MusicMap":                             self.music_map,
            "MusicShuffle":                         self.world.MusicShuffle[self.player],
            "DeathLink":                            self.world.DeathLink[self.player],
            "IncludeMissions":                      self.world.IncludeMissions[self.player],
            "EmblemPercentageForCannonsCore":       self.world.EmblemPercentageForCannonsCore[self.player],
            "NumberOfLevelGates":                   self.world.NumberOfLevelGates[self.player],
            "LevelGateDistribution":                self.world.LevelGateDistribution[self.player],
            "EmblemsForCannonsCore":                self.emblems_for_cannons_core,
            "RegionEmblemMap":                      self.region_emblem_map,
        }

    def _create_items(self, name: str):
        data = item_table[name]
        return [self.create_item(name)] * data.quantity

    def get_required_client_version(self) -> typing.Tuple[int, int, int]:
        return max((0, 2, 5), super(SA2BWorld, self).get_required_client_version())

    def fill_slot_data(self) -> dict:
        slot_data = self._get_slot_data()
        slot_data["MusicMap"] = self.music_map
        for option_name in sa2b_options:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = option.value

        return slot_data

    def check_for_impossible_shuffle(self, shuffled_levels: typing.List[int], gate_0_range: int, world: MultiWorld):
        blacklist_level_count = 0

        for i in range(gate_0_range):
            if shuffled_levels[i] in gate_0_blacklist_regions:
                blacklist_level_count += 1

        if blacklist_level_count == gate_0_range:
            index_to_swap = world.random.randint(0, gate_0_range)
            for i in range(len(shuffled_levels)):
                if shuffled_levels[i] in gate_0_whitelist_regions:
                    shuffled_levels[i], shuffled_levels[index_to_swap] = shuffled_levels[index_to_swap], shuffled_levels[i]
                    break

    def get_levels_per_gate(self, world: MultiWorld, player) -> list:
        return list()

    def generate_basic(self):
        itempool: typing.List[SA2BItem] = []

        # First Missions
        total_required_locations = 31

        # Mission Locations
        total_required_locations *= self.world.IncludeMissions[self.player]

        # Upgrades
        total_required_locations += 28

        # Fill item pool with all required items
        for item in {**upgrades_table}:
            itempool += self._create_items(item)

        total_emblem_count = total_required_locations - len(itempool)

        itempool += [self.create_item(ItemName.emblem)] * total_emblem_count

        self.world.itempool += itempool

        self.emblems_for_cannons_core = math.floor(total_emblem_count * (self.world.EmblemPercentageForCannonsCore[self.player] / 100.0))

        shuffled_region_list = list(range(30))
        emblem_requirement_list = list()
        self.world.random.shuffle(shuffled_region_list)
        levels_per_gate = 30 / (self.world.NumberOfLevelGates[self.player] + 1)

        self.check_for_impossible_shuffle(shuffled_region_list, math.ceil(levels_per_gate), self.world)
        levels_added_to_gate = 0
        total_levels_added = 0
        current_gate = 0
        gates = list()
        gates.append(LevelGate(0))
        for i in range(30):
            gates[current_gate].gate_levels.append(shuffled_region_list[i])
            emblem_requirement_list.append(current_gate)
            levels_added_to_gate += 1
            total_levels_added += 1
            if levels_added_to_gate >= levels_per_gate:
                current_gate += 1
                if current_gate > self.world.NumberOfLevelGates[self.player]:
                    current_gate = self.world.NumberOfLevelGates[self.player];
                else:
                    print(total_emblem_count * math.pow(total_levels_added / 30.0, 2.0))
                    gates.append(LevelGate(max(math.floor(total_emblem_count * math.pow(total_levels_added / 30.0, 2.0)), current_gate)))
                levels_added_to_gate = 0

        self.region_emblem_map = dict(zip(shuffled_region_list, emblem_requirement_list))

        connect_regions(self.world, self.player, gates, self.emblems_for_cannons_core)

        if self.world.MusicShuffle[self.player] == "levels":
            musiclist_o = list(range(0, 47))
            musiclist_s = musiclist_o.copy()
            self.world.random.shuffle(musiclist_s)
            self.music_map = dict(zip(musiclist_o, musiclist_s))
        elif self.world.MusicShuffle[self.player] == "full":
            musiclist_o = list(range(0, 78))
            musiclist_s = musiclist_o.copy()
            self.world.random.shuffle(musiclist_s)
            self.music_map = dict(zip(musiclist_o, musiclist_s))
        else:
            self.music_map = dict()

    def create_regions(self):
        location_table = setup_locations(self.world, self.player)
        create_regions(self.world, self.player, location_table)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        created_item = SA2BItem(name, data.progression, data.code, self.player)
        if name == ItemName.emblem:
            created_item.skip_in_prog_balancing = True
        return created_item

    def set_rules(self):
        set_rules(self.world, self.player)
