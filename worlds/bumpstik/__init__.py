# Copyright (c) 2022 FelicitusNeko
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Items import BumpStikItem, item_table
from .Locations import location_table
from .Regions import create_regions
from ..AutoWorld import World, WebWorld
from ..generic.Rules import forbid_item


class BumpStikWeb(WebWorld):
    tutorials = [Tutorial(
        "Bumper Stickers Setup Tutorial",
        "A guide to setting up the Archipelago Bumper Stickers software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["KewlioMZX"]
    )]
    theme = "stone"
    bug_report_page = "https://github.com/FelicitusNeko/FlixelBumpStik/issues"


class BumpStikWorld(World):
    """
        Bumper Stickers is a match-three puzzle game unlike any you've probably seen.
        Launch Bumpers onto the field, and match them in sets of three of the same color.
        How long can you go without getting Jammed?
    """

    game = "Bumper Stickers"
    web = BumpStikWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table
    #item_name_groups = item_groups

    data_version = 0

    required_client_version = (0, 3, 5)

    # option_definitions = bumpstik_options

    def __init__(self, world: MultiWorld, player: int):
        super(BumpStikWorld, self).__init__(world, player)

    def create_item(self, name: str) -> Item:
        return BumpStikItem(name, ItemClassification.filler, item_table[name], self.player)

    def create_event(self, event: str) -> Item:
        return BumpStikItem(event, ItemClassification.filler, None, self.player)

    def _create_item_in_quantities(self, name: str, qty: int) -> [Item]:
        return [self.create_item(name) for _ in range(0, qty)]

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_regions(self):
        create_regions(self.world, self.player)

    def create_items(self):
        frequencies = [0, 0, 0, 0, 0, 4, 5, 25, 33]
        item_pool = []

        for i, name in enumerate(item_table):
            if i < len(frequencies):
                item_pool += self._create_item_in_quantities(
                    name, frequencies[i])

        item_delta = len(location_table) - len(item_pool) - 1
        if item_delta > 0:
            item_pool += self._create_item_in_quantities(self.get_filler_item_name(), item_delta)

        self.world.itempool += item_pool

    def set_rules(self):
        forbid_item(self.world.get_location("Bonus Booster 5", self.player),
                    "Booster Bumper", self.player)

    def generate_basic(self):
        self.world.get_location("Level 5 - Cleared all Hazards", self.player).place_locked_item(
            self.create_item(self.get_filler_item_name()))

        self.world.completion_condition[self.player] = \
            lambda state: state.has("Booster Bumper", self.player, 5) and \
                          state.has("Treasure Bumper", self.player, 32)
