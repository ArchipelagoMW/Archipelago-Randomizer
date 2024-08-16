from typing import Dict, List, Any, Tuple, TypedDict, ClassVar, Union, Set
from logging import warning
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld, CollectionState
from .items import (item_name_to_id, item_table, item_name_groups, fool_tiers, filler_items, slot_data_item_names,
                    combat_items)
from .locations import location_table, location_name_groups, location_name_to_id, hexagon_locations
from .rules import set_location_rules, set_region_rules, randomize_ability_unlocks, gold_hexagon
from .er_rules import set_er_location_rules
from .regions import tunic_regions
from .er_scripts import create_er_regions, verify_plando_directions
from .er_data import portal_mapping, RegionInfo, tunic_er_regions
from .options import (TunicOptions, EntranceRando, tunic_option_groups, tunic_option_presets, TunicPlandoConnections,
                      LaurelsLocation, LogicRules, LaurelsZips, IceGrappling, LadderStorage, EntranceLayout)
from .combat_logic import area_data, CombatState
from worlds.AutoWorld import WebWorld, World
from Options import PlandoConnection, OptionError
from decimal import Decimal, ROUND_HALF_UP
from settings import Group, Bool


class TunicSettings(Group):
    class DisableLocalSpoiler(Bool):
        """Disallows the TUNIC client from creating a local spoiler log."""

    disable_local_spoiler: Union[DisableLocalSpoiler, bool] = False


class TunicWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the TUNIC Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["SilentDestroyer"]
        )
    ]
    theme = "grassFlowers"
    game = "TUNIC"
    option_groups = tunic_option_groups
    options_presets = tunic_option_presets


class TunicItem(Item):
    game: str = "TUNIC"


class TunicLocation(Location):
    game: str = "TUNIC"


class SeedGroup(TypedDict):
    laurels_zips: bool  # laurels_zips value
    ice_grappling: int  # ice_grappling value
    ladder_storage: int  # ls value
    laurels_at_10_fairies: bool  # laurels location value
    entrance_layout: int  # entrance layout value
    has_decoupled_enabled: bool  # for checking that players don't have conflicting options
    plando: List[PlandoConnection]  # consolidated plando connections for the seed group


class TunicWorld(World):
    """
    Explore a land filled with lost legends, ancient powers, and ferocious monsters in TUNIC, an isometric action game
    about a small fox on a big adventure. Stranded on a mysterious beach, armed with only your own curiosity, you will
    confront colossal beasts, collect strange and powerful items, and unravel long-lost secrets. Be brave, tiny fox!
    """
    game = "TUNIC"
    web = TunicWeb()

    options: TunicOptions
    options_dataclass = TunicOptions
    settings: ClassVar[TunicSettings]
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    ability_unlocks: Dict[str, int]
    slot_data_items: List[TunicItem]
    tunic_portal_pairs: Dict[str, str]
    er_portal_hints: Dict[int, str]
    seed_groups: Dict[str, SeedGroup] = {}
    used_shop_numbers: Set[int]
    er_regions: Dict[str, RegionInfo]  # absolutely needed so outlet regions work

    def generate_early(self) -> None:
        self.er_regions = tunic_er_regions.copy()
        if self.options.plando_connections:
            for index, cxn in enumerate(self.options.plando_connections):
                # flip any that are pointing to exit to point to entrance so that I don't have to deal with it
                if self.options.decoupled and cxn.direction == "exit":
                    replacement = PlandoConnection(cxn.exit, cxn.entrance, "entrance", cxn.percentage)
                    self.options.plando_connections.value.remove(cxn)
                    self.options.plando_connections.value.insert(index, replacement)
                # if decoupled is off, just convert these to both
                if not self.options.decoupled and cxn.direction != "both":
                    replacement = PlandoConnection(cxn.entrance, cxn.exit, "both", cxn.percentage)
                    self.options.plando_connections.value.remove(cxn)
                    self.options.plando_connections.value.insert(index, replacement)
                # if decoupled is on and you plando'd an entrance to itself but left the direction as both
                if self.options.decoupled and cxn.direction == "both" and cxn.entrance == cxn.exit:
                    replacement = PlandoConnection(cxn.entrance, cxn.exit, "entrance")
                    self.options.plando_connections.value.remove(cxn)
                    self.options.plando_connections.value.insert(index, replacement)
              
                if (self.options.entrance_layout == EntranceLayout.option_direction_pairs
                        and not verify_plando_directions(cxn)):
                    raise OptionError(f"TUNIC: Player {self.player_name} has invalid plando connections. "
                                      f"They have Direction Pairs enabled and the connection "
                                      f"{cxn.entrance} --> {cxn.exit} does not abide by this option.")

        # Universal tracker stuff, shouldn't do anything in standard gen
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "TUNIC" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["TUNIC"]
                self.options.start_with_sword.value = passthrough["start_with_sword"]
                self.options.keys_behind_bosses.value = passthrough["keys_behind_bosses"]
                self.options.sword_progression.value = passthrough["sword_progression"]
                self.options.ability_shuffling.value = passthrough["ability_shuffling"]
                self.options.laurels_zips.value = passthrough["laurels_zips"]
                self.options.ice_grappling.value = passthrough["ice_grappling"]
                self.options.ladder_storage.value = passthrough["ladder_storage"]
                self.options.ladder_storage_without_items = passthrough["ladder_storage_without_items"]
                self.options.lanternless.value = passthrough["lanternless"]
                self.options.maskless.value = passthrough["maskless"]
                self.options.hexagon_quest.value = passthrough["hexagon_quest"]
                self.options.entrance_rando.value = passthrough["entrance_rando"]
                self.options.shuffle_ladders.value = passthrough["shuffle_ladders"]
                self.options.entrance_layout.value = EntranceLayout.option_standard
                self.options.decoupled = passthrough["decoupled"]
                self.options.laurels_location.value = LaurelsLocation.option_anywhere
                self.options.combat_logic.value = passthrough["combat_logic"]

    @classmethod
    def stage_generate_early(cls, multiworld: MultiWorld) -> None:
        tunic_worlds: Tuple[TunicWorld] = multiworld.get_game_worlds("TUNIC")
        for tunic in tunic_worlds:
            # setting up state combat logic stuff, see has_combat_reqs for its use
            # and this is magic so pycharm doesn't like it, unfortunately
            if tunic.options.combat_logic:
                multiworld.state.tunic_need_to_reset_combat_from_collect[tunic.player] = False
                multiworld.state.tunic_need_to_reset_combat_from_remove[tunic.player] = False
                multiworld.state.tunic_area_combat_state[tunic.player] = {}
                for area_name in area_data.keys():
                    multiworld.state.tunic_area_combat_state[tunic.player][area_name] = CombatState.unchecked

            # if it's one of the options, then it isn't a custom seed group
            if tunic.options.entrance_rando.value in EntranceRando.options.values():
                continue
            group = tunic.options.entrance_rando.value
            # if this is the first world in the group, set the rules equal to its rules
            if group not in cls.seed_groups:
                cls.seed_groups[group] = \
                    SeedGroup(laurels_zips=bool(tunic.options.laurels_zips),
                              ice_grappling=tunic.options.ice_grappling.value,
                              ladder_storage=tunic.options.ladder_storage.value,
                              laurels_at_10_fairies=tunic.options.laurels_location == LaurelsLocation.option_10_fairies,
                              entrance_layout=tunic.options.entrance_layout.value,
                              has_decoupled_enabled=bool(tunic.options.decoupled),
                              plando=tunic.options.plando_connections.value.copy())
                continue
            # I feel that syncing this one is worse than erroring out
            if bool(tunic.options.decoupled) != cls.seed_groups[group]["has_decoupled_enabled"]:
                raise OptionError(f"TUNIC: All players in the seed group {group} must "
                                  f"have Decoupled either enabled or disabled.")
            # off is more restrictive
            if not tunic.options.laurels_zips:
                cls.seed_groups[group]["laurels_zips"] = False
            # lower value is more restrictive
            if tunic.options.ice_grappling < cls.seed_groups[group]["ice_grappling"]:
                cls.seed_groups[group]["ice_grappling"] = tunic.options.ice_grappling.value
            # lower value is more restrictive
            if tunic.options.ladder_storage.value < cls.seed_groups[group]["ladder_storage"]:
                cls.seed_groups[group]["ladder_storage"] = tunic.options.ladder_storage.value
            # laurels at 10 fairies changes logic for secret gathering place placement
            if tunic.options.laurels_location == 3:
                cls.seed_groups[group]["laurels_at_10_fairies"] = True
            # fixed shop and direction pairs override standard, but conflict with each other
            if tunic.options.entrance_layout:
                if cls.seed_groups[group]["entrance_layout"] == EntranceLayout.option_standard:
                    cls.seed_groups[group]["entrance_layout"] = tunic.options.entrance_layout.value
                elif cls.seed_groups[group]["entrance_layout"] != tunic.options.entrance_layout.value:
                    raise OptionError(f"TUNIC: Conflict between seed group {group}'s Entrance Layout options. "
                                      f"Seed group cannot have both Fixed Shop and Direction Pairs enabled.")
            if tunic.options.plando_connections:
                # loop through the connections in the player's yaml
                for index, player_cxn in enumerate(tunic.options.plando_connections):
                    new_cxn = True
                    for group_cxn in cls.seed_groups[group]["plando"]:
                        # verify that it abides by direction pairs if enabled
                        if (cls.seed_groups[group]["entrance_layout"] == EntranceLayout.option_direction_pairs
                                and not verify_plando_directions(player_cxn)):
                            player_dir = "<->" if player_cxn.direction == "both" else "-->"
                            raise Exception(f"TUNIC: Conflict between Entrance Layout option and Plando Connection: "
                                            f"{player_cxn.entrance} {player_dir} {player_cxn.exit}")
                        # check if this pair is the same as a pair in the group already
                        if ((player_cxn.entrance == group_cxn.entrance and player_cxn.exit == group_cxn.exit)
                            or (player_cxn.entrance == group_cxn.exit and player_cxn.exit == group_cxn.entrance
                                and "both" in [player_cxn.direction, group_cxn.direction])):
                            new_cxn = False
                            # if the group's was one-way and the player's was two-way, we replace the group's now
                            if player_cxn.direction == "both" and group_cxn.direction == "entrance":
                                cls.seed_groups[group]["plando"].remove(group_cxn)
                                cls.seed_groups[group]["plando"].insert(index, player_cxn)
                            break
                        is_mismatched = (
                            player_cxn.entrance == group_cxn.entrance and player_cxn.exit != group_cxn.exit
                            or player_cxn.exit == group_cxn.exit and player_cxn.entrance != group_cxn.entrance
                        )
                        if not tunic.options.decoupled:
                            is_mismatched = is_mismatched or (
                                player_cxn.entrance == group_cxn.exit and player_cxn.exit != group_cxn.entrance
                                or player_cxn.exit == group_cxn.entrance and player_cxn.entrance != group_cxn.exit
                            )
                        if is_mismatched:
                            group_dir = "<->" if group_cxn.direction == "both" else "-->"
                            player_dir = "<->" if player_cxn.direction == "both" else "-->"
                            raise OptionError(f"TUNIC: Conflict between seed group {group}'s plando "
                                              f"connection {group_cxn.entrance} {group_dir} {group_cxn.exit} and "
                                              f"{tunic.player_name}'s plando connection "
                                              f"{player_cxn.entrance} {player_dir} {player_cxn.exit}")
                    if new_cxn:
                        cls.seed_groups[group]["plando"].append(player_cxn)

    def create_item(self, name: str, classification: ItemClassification = None) -> TunicItem:
        item_data = item_table[name]
        # if item_data.combat_ic is None, it'll take item_data.classification instead
        itemclass: ItemClassification = ((item_data.combat_ic if self.options.combat_logic else None)
                                         or item_data.classification)
        return TunicItem(name, classification or itemclass, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        tunic_items: List[TunicItem] = []
        self.slot_data_items = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        for money_fool in fool_tiers[self.options.fool_traps]:
            items_to_create["Fool Trap"] += items_to_create[money_fool]
            items_to_create[money_fool] = 0

        if self.options.start_with_sword:
            self.multiworld.push_precollected(self.create_item("Sword"))

        if self.options.sword_progression:
            items_to_create["Stick"] = 0
            items_to_create["Sword"] = 0
        else:
            items_to_create["Sword Upgrade"] = 0

        if self.options.laurels_location:
            laurels = self.create_item("Hero's Laurels")
            if self.options.laurels_location == "6_coins":
                self.get_location("Coins in the Well - 6 Coins").place_locked_item(laurels)
            elif self.options.laurels_location == "10_coins":
                self.get_location("Coins in the Well - 10 Coins").place_locked_item(laurels)
            elif self.options.laurels_location == "10_fairies":
                self.get_location("Secret Gathering Place - 10 Fairy Reward").place_locked_item(laurels)
            items_to_create["Hero's Laurels"] = 0

        if self.options.keys_behind_bosses:
            for rgb_hexagon, location in hexagon_locations.items():
                hex_item = self.create_item(gold_hexagon if self.options.hexagon_quest else rgb_hexagon)
                self.get_location(location).place_locked_item(hex_item)
                items_to_create[rgb_hexagon] = 0
            items_to_create[gold_hexagon] -= 3

        # Filler items in the item pool
        available_filler: List[str] = [filler for filler in items_to_create if items_to_create[filler] > 0 and
                                       item_table[filler].classification == ItemClassification.filler]

        # Remove filler to make room for other items
        def remove_filler(amount: int) -> None:
            for _ in range(amount):
                if not available_filler:
                    fill = "Fool Trap"
                else:
                    fill = self.random.choice(available_filler)
                if items_to_create[fill] == 0:
                    raise Exception("No filler items left to accommodate options selected. Turn down fool trap amount.")
                items_to_create[fill] -= 1
                if items_to_create[fill] == 0:
                    available_filler.remove(fill)

        if self.options.shuffle_ladders:
            ladder_count = 0
            for item_name, item_data in item_table.items():
                if item_data.item_group == "Ladders":
                    items_to_create[item_name] = 1
                    ladder_count += 1
            remove_filler(ladder_count)

        if self.options.hexagon_quest:
            # Calculate number of hexagons in item pool
            hexagon_goal = self.options.hexagon_goal
            extra_hexagons = self.options.extra_hexagon_percentage
            items_to_create[gold_hexagon] += int((Decimal(100 + extra_hexagons) / 100 * hexagon_goal).to_integral_value(rounding=ROUND_HALF_UP))

            # Replace pages and normal hexagons with filler
            for replaced_item in list(filter(lambda item: "Pages" in item or item in hexagon_locations, items_to_create)):
                filler_name = self.get_filler_item_name()
                items_to_create[filler_name] += items_to_create[replaced_item]
                if items_to_create[filler_name] >= 1 and filler_name not in available_filler:
                    available_filler.append(filler_name)
                items_to_create[replaced_item] = 0

            remove_filler(items_to_create[gold_hexagon])

            for hero_relic in item_name_groups["Hero Relics"]:
                tunic_items.append(self.create_item(hero_relic, ItemClassification.useful))
                items_to_create[hero_relic] = 0

        if not self.options.ability_shuffling:
            for page in item_name_groups["Abilities"]:
                if items_to_create[page] > 0:
                    tunic_items.append(self.create_item(page, ItemClassification.useful))
                    items_to_create[page] = 0

        if self.options.maskless:
            tunic_items.append(self.create_item("Scavenger Mask", ItemClassification.useful))
            items_to_create["Scavenger Mask"] = 0

        if self.options.lanternless:
            tunic_items.append(self.create_item("Lantern", ItemClassification.useful))
            items_to_create["Lantern"] = 0

        for item, quantity in items_to_create.items():
            for _ in range(quantity):
                tunic_items.append(self.create_item(item))

        for tunic_item in tunic_items:
            if tunic_item.name in slot_data_item_names:
                self.slot_data_items.append(tunic_item)

        self.multiworld.itempool += tunic_items

    def create_regions(self) -> None:
        self.tunic_portal_pairs = {}
        self.er_portal_hints = {}
        self.ability_unlocks = randomize_ability_unlocks(self.random, self.options)

        # stuff for universal tracker support, can be ignored for standard gen
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "TUNIC" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["TUNIC"]
                self.ability_unlocks["Pages 24-25 (Prayer)"] = passthrough["Hexagon Quest Prayer"]
                self.ability_unlocks["Pages 42-43 (Holy Cross)"] = passthrough["Hexagon Quest Holy Cross"]
                self.ability_unlocks["Pages 52-53 (Icebolt)"] = passthrough["Hexagon Quest Icebolt"]

        # Ladders and Combat Logic uses ER rules with vanilla connections for easier maintenance
        if self.options.entrance_rando or self.options.shuffle_ladders or self.options.combat_logic:
            portal_pairs = create_er_regions(self)
            if self.options.entrance_rando:
                # these get interpreted by the game to tell it which entrances to connect
                for portal1, portal2 in portal_pairs.items():
                    self.tunic_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()
        else:
            # uses the original rules, easier to navigate and reference
            for region_name in tunic_regions:
                region = Region(region_name, self.player, self.multiworld)
                self.multiworld.regions.append(region)

            for region_name, exits in tunic_regions.items():
                region = self.get_region(region_name)
                region.add_exits(exits)

            for location_name, location_id in self.location_name_to_id.items():
                region = self.get_region(location_table[location_name].region)
                location = TunicLocation(self.player, location_name, location_id, region)
                region.locations.append(location)

            victory_region = self.get_region("Spirit Arena")
            victory_location = TunicLocation(self.player, "The Heir", None, victory_region)
            victory_location.place_locked_item(TunicItem("Victory", ItemClassification.progression, None, self.player))
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
            victory_region.locations.append(victory_location)

    def set_rules(self) -> None:
        # same reason as in create_regions, could probably be put into create_regions
        if self.options.entrance_rando or self.options.shuffle_ladders or self.options.combat_logic:
            set_er_location_rules(self)
        else:
            set_region_rules(self)
            set_location_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    # cache whether you can get through combat logic areas
    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and self.options.combat_logic and item.name in combat_items:
            state.tunic_need_to_reset_combat_from_collect[self.player] = True
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and self.options.combat_logic and item.name in combat_items:
            state.tunic_need_to_reset_combat_from_remove[self.player] = True
        return change

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        if self.options.entrance_rando:
            hint_data.update({self.player: {}})
            # all state seems to have efficient paths
            all_state = self.multiworld.get_all_state(True)
            all_state.update_reachable_regions(self.player)
            paths = all_state.path
            portal_names = {portal.name for portal in portal_mapping}.union({f"Shop Portal {i + 1}" for i in range(500)})
            for location in self.multiworld.get_locations(self.player):
                # skipping event locations
                if not location.address:
                    continue
                path_to_loc = []
                previous_name = "placeholder"
                try:
                    name, connection = paths[location.parent_region]
                except KeyError:
                    # logic bug, proceed with warning since it takes a long time to update AP
                    warning(f"{location.name} is not logically accessible for {self.player_name}. "
                            "Creating entrance hint Inaccessible. Please report this to the TUNIC rando devs.")
                    hint_text = "Inaccessible"
                else:
                    while connection != ("Menu", None):
                        name, connection = connection
                        # for LS entrances, we just want to give the portal name
                        if "(LS)" in name:
                            name = name.split(" (LS) ", 1)[0]
                        # was getting some cases like Library Grave -> Library Grave -> other place
                        if name in portal_names and name != previous_name:
                            previous_name = name
                            path_to_loc.append(name)
                    hint_text = " -> ".join(reversed(path_to_loc))

                if hint_text:
                    hint_data[self.player][location.address] = hint_text

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "seed": self.random.randint(0, 2147483647),
            "start_with_sword": self.options.start_with_sword.value,
            "keys_behind_bosses": self.options.keys_behind_bosses.value,
            "sword_progression": self.options.sword_progression.value,
            "ability_shuffling": self.options.ability_shuffling.value,
            "hexagon_quest": self.options.hexagon_quest.value,
            "fool_traps": self.options.fool_traps.value,
            "laurels_zips": self.options.laurels_zips.value,
            "ice_grappling": self.options.ice_grappling.value,
            "ladder_storage": self.options.ladder_storage.value,
            "ladder_storage_without_items": self.options.ladder_storage_without_items.value,
            "lanternless": self.options.lanternless.value,
            "maskless": self.options.maskless.value,
            "entrance_rando": int(bool(self.options.entrance_rando.value)),
            "decoupled": self.options.decoupled.value if self.options.entrance_rando else 0,
            "shuffle_ladders": self.options.shuffle_ladders.value,
            "combat_logic": self.options.combat_logic.value,
            "Hexagon Quest Prayer": self.ability_unlocks["Pages 24-25 (Prayer)"],
            "Hexagon Quest Holy Cross": self.ability_unlocks["Pages 42-43 (Holy Cross)"],
            "Hexagon Quest Icebolt": self.ability_unlocks["Pages 52-53 (Icebolt)"],
            "Hexagon Quest Goal": self.options.hexagon_goal.value,
            "Entrance Rando": self.tunic_portal_pairs,
            "disable_local_spoiler": int(self.settings.disable_local_spoiler or self.multiworld.is_race),
        }

        for tunic_item in filter(lambda item: item.location is not None and item.code is not None, self.slot_data_items):
            if tunic_item.name not in slot_data:
                slot_data[tunic_item.name] = []
            if tunic_item.name == gold_hexagon and len(slot_data[gold_hexagon]) >= 6:
                continue
            slot_data[tunic_item.name].extend([tunic_item.location.name, tunic_item.location.player])

        for start_item in self.options.start_inventory_from_pool:
            if start_item in slot_data_item_names:
                if start_item not in slot_data:
                    slot_data[start_item] = []
                for _ in range(self.options.start_inventory_from_pool[start_item]):
                    slot_data[start_item].extend(["Your Pocket", self.player])

        for plando_item in self.multiworld.plando_items[self.player]:
            if plando_item["from_pool"]:
                items_to_find = set()
                for item_type in [key for key in ["item", "items"] if key in plando_item]:
                    for item in plando_item[item_type]:
                        items_to_find.add(item)
                for item in items_to_find:
                    if item in slot_data_item_names:
                        slot_data[item] = []
                        for item_location in self.multiworld.find_item_locations(item, self.player):
                            slot_data[item].extend([item_location.name, item_location.player])

        return slot_data

    # for the universal tracker, doesn't get called in standard gen
    # docs: https://github.com/FarisTheAncient/Archipelago/blob/tracker/worlds/tracker/docs/re-gen-passthrough.md
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        # we are using re_gen_passthrough over modifying the world here due to complexities with ER
        return slot_data
