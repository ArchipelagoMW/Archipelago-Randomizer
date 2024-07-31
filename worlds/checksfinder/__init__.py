from BaseClasses import Region, Entrance, Tutorial, ItemClassification
from .Items import ChecksFinderItem, item_table
from .Locations import ChecksFinderLocation, advancement_table
from Options import OptionError, PerGameCommonOptions
from .Rules import set_rules, set_completion_rules
from worlds.AutoWorld import World, WebWorld

client_version = 7


class ChecksFinderWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago ChecksFinder software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Mewlif"]
    )]


class ChecksFinderWorld(World):
    """
    ChecksFinder is a game where you avoid mines and find checks inside the board
    with the mines! You win when you get all your items and beat the board!
    """
    game = "ChecksFinder"
    options_dataclass = PerGameCommonOptions
    web = ChecksFinderWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in advancement_table.items()}

    def _get_checksfinder_data(self):
        return {
            'world_seed': self.random.getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.player_name,
            'player_id': self.player,
            'client_version': client_version,
            'race': self.multiworld.is_race,
        }

    def generate_early(self):
        if not self.player_name.isascii():
            raise OptionError(f"{self.player_name}'s name must be only ASCII characters.")

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        board = Region("Board", self.player, self.multiworld)
        board.locations += [ChecksFinderLocation(self.player, loc_name, loc_data.id, board)
                            for loc_name, loc_data in advancement_table.items()]

        connection = Entrance(self.player, "New Board", menu)
        menu.exits.append(connection)
        connection.connect(board)
        self.multiworld.regions += [menu, board]

    def create_items(self):
        # Generate item pool
        itempool = []
        # Add the map width and height stuff
        itempool += ["Map Width"] * (10-5)
        itempool += ["Map Height"] * (10-5)
        # Add the map bombs
        itempool += ["Map Bombs"] * (20-5)
        # Convert itempool into real items
        itempool = [self.create_item(item) for item in itempool]

        self.multiworld.itempool += itempool

    def set_rules(self):
        set_rules(self.multiworld, self.player)
        set_completion_rules(self.multiworld, self.player)

    def fill_slot_data(self):
        slot_data = self._get_checksfinder_data()
        return slot_data

    def create_item(self, name: str) -> ChecksFinderItem:
        item_data = item_table[name]
        item = ChecksFinderItem(name, ItemClassification.progression, item_data.code, self.player)
        return item
