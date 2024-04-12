import hashlib
import logging
from typing import Dict, Any, TYPE_CHECKING, Optional, Sequence, Tuple, ClassVar

from BaseClasses import Tutorial, ItemClassification, MultiWorld, Item
from worlds.AutoWorld import World, WebWorld
from .Names import dr_wily
from .Items import (item_table, item_names, MM2Item, filler_item_table, filler_item_weights, robot_master_weapon_table,
                    stage_access_table, item_item_table, lookup_item_to_id)
from .Locations import (location_table, MM2Location, mm2_regions, MM2Region,
                        energy_pickups, etank_1ups, lookup_location_to_id)
from .Rom import (get_base_rom_bytes, get_base_rom_path, RomData, patch_rom, extract_mm2, MM2ProcedurePatch,
                  MM2LCHASH, PROTEUSHASH, MM2VCHASH, MM2NESHASH)
from .Options import MM2Options
from .Client import MegaMan2Client
from .Rules import set_rules, weapon_damage, robot_masters, weapons_to_name, minimum_weakness_requirement
import os
import threading
import base64
import settings
logger = logging.getLogger("Mega Man 2")

if TYPE_CHECKING:
    from BaseClasses import CollectionState


class MM2Settings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the MM2 EN rom"""
        description = "Mega Man 2 ROM File"
        copy_to: Optional[str] = "Mega Man 2 (USA).nes"
        md5s = [MM2NESHASH, MM2VCHASH, MM2LCHASH, PROTEUSHASH]

        def browse(self: settings.T,
                   filetypes: Optional[Sequence[Tuple[str, Sequence[str]]]] = None,
                   **kwargs: Any) -> Optional[settings.T]:
            if not filetypes:
                from Utils import is_windows
                file_types = [("NES", [".nes"]), ("Program", [".exe"] if is_windows else [""])]
                return super().browse(file_types, **kwargs)
            else:
                return super().browse(filetypes, **kwargs)

        @classmethod
        def validate(cls, path: str) -> None:
            """Try to open and validate file against hashes"""
            with open(path, "rb", buffering=0) as f:
                try:
                    cls._validate_stream_hashes(f)
                    base_rom_bytes = f.read()
                    basemd5 = hashlib.md5()
                    basemd5.update(base_rom_bytes)
                    if basemd5.hexdigest() == PROTEUSHASH:
                        # we need special behavior here
                        cls.copy_to = None
                except ValueError:
                    raise ValueError(f"File hash does not match for {path}")

    rom_file: RomFile = RomFile(RomFile.copy_to)


class MM2WebWorld(WebWorld):
    theme = "partyTime"
    tutorials = [

        Tutorial(
           "Multiworld Setup Guide",
           "A guide to setting up the Mega Man 2 randomizer connected to an Archipelago Multiworld.",
           "English",
           "setup_en.md",
           "setup/en",
           ["Silvris"]
        )
    ]


class MM2World(World):
    """
    In the year 200X, following his prior defeat by Mega Man, the evil Dr. Wily has returned to take over the world with
    his own group of Robot Masters. Mega Man once again sets out to defeat the eight Robot Masters and stop Dr. Wily.

    """

    game = "Mega Man 2"
    settings: ClassVar[MM2Settings]
    options_dataclass = MM2Options
    options: MM2Options
    item_name_to_id = lookup_item_to_id
    location_name_to_id = lookup_location_to_id
    item_name_groups = item_names
    web = MM2WebWorld()
    rom_name: bytearray

    def __init__(self, world: MultiWorld, player: int):
        self.rom_name = bytearray()
        self.rom_name_available_event = threading.Event()
        super().__init__(world, player)
        self.weapon_damage = weapon_damage.copy()

    def create_regions(self) -> None:
        menu = MM2Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for region in mm2_regions:
            stage = MM2Region(region, self.player, self.multiworld)
            required_items = mm2_regions[region][0]
            locations = mm2_regions[region][1]
            prev_stage = mm2_regions[region][2]
            if prev_stage is None:
                menu.connect(stage, f"To {region}",
                             lambda state, items=required_items: state.has_all(items, self.player))
            else:
                old_stage = self.multiworld.get_region(prev_stage, self.player)
                old_stage.connect(stage, f"To {region}",
                                  lambda state, items=required_items: state.has_all(items, self.player))
            stage.add_locations(locations)
            for location in stage.get_locations():
                if location.address is None and location.name is not dr_wily:
                    location.place_locked_item(MM2Item(location.name, ItemClassification.progression,
                                                       None, self.player))
            if self.options.consumables:
                if region in etank_1ups:
                    stage.add_locations(etank_1ups[region], MM2Location)
                if self.options.consumables == self.options.consumables.option_all:
                    if region in energy_pickups:
                        stage.add_locations(energy_pickups[region], MM2Location)
            self.multiworld.regions.append(stage)

    def create_item(self, name: str, force_non_progression: bool = False) -> MM2Item:
        item = item_table[name]
        classification = ItemClassification.filler
        if item.progression and not force_non_progression:
            classification = ItemClassification.progression_skip_balancing \
                if item.skip_balancing else ItemClassification.progression
        return MM2Item(name, classification, item.code, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choices(list(filler_item_weights.keys()),
                                              weights=list(filler_item_weights.values()))[0]

    def create_items(self) -> None:
        itempool = []
        # grab first robot master
        robot_master = self.item_id_to_name[0x880101 + self.options.starting_robot_master.value]
        self.multiworld.push_precollected(self.create_item(robot_master))
        itempool.extend([self.create_item(name) for name in stage_access_table.keys()
                         if name != robot_master])
        itempool.extend([self.create_item(name) for name in robot_master_weapon_table.keys()])
        itempool.extend([self.create_item(name) for name in item_item_table.keys()])
        total_checks = 24
        if self.options.consumables:
            total_checks += 20
            if self.options.consumables == self.options.consumables.option_all:
                total_checks += 27
        remaining = total_checks - len(itempool)
        itempool.extend([self.create_item(name)
                         for name in self.multiworld.random.choices(list(filler_item_weights.keys()),
                                                                    weights=list(filler_item_weights.values()),
                                                                    k=remaining)])
        self.multiworld.itempool += itempool

    set_rules = set_rules

    def generate_early(self) -> None:
        if (not self.options.yoku_jumps
            and self.options.starting_robot_master.current_key == "heat_man") or \
                (not self.options.enable_lasers
                 and self.options.starting_robot_master.current_key == "quick_man"):
            robot_master_pool = [1, 2, 3, 5, 6, 7, ]
            if self.options.yoku_jumps:
                robot_master_pool.append(0)
            if self.options.enable_lasers:
                robot_master_pool.append(4)
            self.options.starting_robot_master.value = self.random.choice(robot_master_pool)
            logger.warning(
                f"Incompatible starting Robot Master, changing to "
                f"{self.options.starting_robot_master.current_key.replace('_', ' ').title()}")

    def generate_basic(self) -> None:
        goal_location = self.multiworld.get_location(dr_wily, self.player)
        goal_location.place_locked_item(MM2Item("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def generate_output(self, output_directory: str) -> None:
        try:
            patch = MM2ProcedurePatch()
            patch_rom(self, patch)

            self.rom_name = patch.name

            patch.write(os.path.join(output_directory,
                                     f"{self.multiworld.get_out_file_name_base(self.player)}{patch.patch_file_ending}"))
        except Exception:
            raise
        finally:
            self.rom_name_available_event.set()  # make sure threading continues and errors are collected

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "death_link": self.options.death_link.value,
            "weapon_damage": self.weapon_damage
        }

    def interpret_slot_data(self, slot_data: Dict[str, Any]) -> Dict[str, Any]:
        local_weapon = {int(key): value for key, value in slot_data["weapon_damage"].items()}
        return {"weapon_damage": local_weapon}

    def modify_multidata(self, multidata: Dict[str, Any]) -> None:
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change and item.name in self.item_name_groups["Weapons"]:
            # need to evaluate robot master access
            weapon = next((wp for wp in weapons_to_name if weapons_to_name[wp] == item.name), None)
            if weapon:
                for rbm in robot_masters:
                    if self.weapon_damage[weapon][rbm] >= minimum_weakness_requirement[weapon]:
                        state.prog_items[self.player][robot_masters[rbm]] = 1
        return change

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().remove(state, item)
        if change and item.name in self.item_name_groups["Weapons"]:
            removed_weapon = next((weapons_to_name[weapon] == item.name for weapon in weapons_to_name), None)
            received_weapons = {weapon for weapon in weapons_to_name
                                if weapons_to_name[weapon] in state.prog_items[self.player]}
            if removed_weapon:
                for rbm in robot_masters:
                    if self.weapon_damage[removed_weapon][rbm] > 0 and not any(self.weapon_damage[wp][rbm] >
                                                                               minimum_weakness_requirement[wp]
                                                                               for wp in received_weapons):
                        state.prog_items[self.player][robot_masters[rbm]] = 0
        return change
