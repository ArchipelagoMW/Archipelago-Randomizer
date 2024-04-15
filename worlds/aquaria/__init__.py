"""
Author: Louis M
Date: Fri, 15 Mar 2024 18:41:40 +0000
Description: Main module for Aquaria game multiworld randomizer
"""

from typing import List, Dict, ClassVar, Any
from ..AutoWorld import World, WebWorld
from BaseClasses import Tutorial, MultiWorld, ItemClassification, LocationProgressType
from .Items import item_table, AquariaItem, ItemType, ItemGroup
from .Locations import location_table
from .Options import AquariaOptions
from .Regions import AquariaRegions


class AquariaWeb(WebWorld):
    """
    Class used to generate the Aquaria Game Web pages (setup, tutorial, etc.)
    """
    theme = "ocean"

    bug_report_page = "https://github.com/tioui/Aquaria_Randomizer/issues"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Aquaria for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Tioui"]
    )

    setup_fr = Tutorial(
        "Guide de configuration Multimonde",
        "Un guide pour configurer Aquaria MultiWorld",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Tioui"]
    )

    tutorials = [setup, setup_fr]


class AquariaWorld(World):
    """
    Aquaria is a side-scrolling action-adventure game. It follows Naija, an
    aquatic humanoid woman, as she explores the underwater world of Aquaria.
    Along her journey, she learns about the history of the world she inhabits
    as well as her own past. The gameplay focuses on a combination of swimming,
    singing, and combat, through which Naija can interact with the world. Her
    songs can move items, affect plants and animals, and change her physical
    appearance into other forms that have different abilities, like firing
    projectiles at hostile creatures, or passing through barriers inaccessible
    to her in her natural form.
    From: https://en.wikipedia.org/wiki/Aquaria_(video_game)
    """

    game: str = "Aquaria"
    "The name of the game"

    topology_present = True
    "show path to required location checks in spoiler"

    web: WebWorld = AquariaWeb()
    "The web page generation informations"

    item_name_to_id: ClassVar[Dict[str, int]] =\
        {name: data[0] for name, data in item_table.items()}
    "The name and associated ID of each item of the world"

    item_name_groups = {
        "Damage": {"Energy form", "Nature form", "Beast form",
                   "Li and Li song", "Baby nautilus", "Baby piranha",
                   "Baby blaster"},
        "Light": {"Sun form", "Baby dumbo"}
    }
    """Grouping item make it easier to find them"""

    location_name_to_id = location_table
    "The name and associated ID of each location of the world"

    base_id = 698000
    "The starting ID of the items and locations of the world"

    ingredients_substitution: List[int]
    "Used to randomize ingredient drop"

    options_dataclass = AquariaOptions
    "Used to manage world options"

    options: AquariaOptions
    "Every options of the world"

    regions: AquariaRegions
    "Used to manage Regions"

    exclude: List[str]

    def __init__(self, world: MultiWorld, player: int):
        """Initialisation of the Aquaria World"""
        super(AquariaWorld, self).__init__(world, player)
        self.regions = AquariaRegions(world, player)
        self.ingredients_substitution = []
        self.exclude = []

    def create_regions(self) -> None:
        """
        Create every Region in `regions`
        """
        self.regions.add_regions_to_world()
        self.regions.connect_regions()

    def create_item(self, name: str) -> AquariaItem:
        """
        Create an AquariaItem using `name' as item name.
        """
        result: AquariaItem
        try:
            data = item_table[name]
            classification: ItemClassification = ItemClassification.useful
            if data[2] == ItemType.JUNK:
                classification = ItemClassification.filler
            elif data[2] == ItemType.PROGRESSION:
                classification = ItemClassification.progression
            result = AquariaItem(name, classification, data[0], self.player)
        except BaseException:
            raise Exception('The item ' + name + ' is not valid.')

        return result

    def __pre_fill_item(self, item_name: str, location_name: str, precollected) -> None:
        """Pre-assign an item to a location"""
        if item_name not in precollected:
            self.exclude.append(item_name)
            data = item_table[item_name]
            item = AquariaItem(item_name, ItemClassification.useful, data[0], self.player)
            self.multiworld.get_location(location_name, self.player).place_locked_item(item)

    def get_filler_item_name(self):
        """Getting a random ingredient item as filler"""
        ingredients = []
        for name, data in item_table.items():
            if data[3] == ItemGroup.INGREDIENT:
                ingredients.append(name)
        filler_item_name = self.random.choice(ingredients)
        return filler_item_name

    def create_items(self) -> None:
        """Create every item in the world"""
        precollected = [item.name for item in self.multiworld.precollected_items[self.player]]
        if self.options.turtle_randomizer.value > 0:
            if self.options.turtle_randomizer.value == 2:
                self.__pre_fill_item("Transturtle Final Boss", "Final boss area, Transturtle", precollected)
        else:
            self.__pre_fill_item("Transturtle Veil top left", "The veil top left area, Transturtle", precollected)
            self.__pre_fill_item("Transturtle Veil top right", "The veil top right area, Transturtle", precollected)
            self.__pre_fill_item("Transturtle Open Water top left", "Open water top right area, Transturtle",
                                 precollected)
            self.__pre_fill_item("Transturtle Forest bottom left", "Kelp Forest bottom left area, Transturtle",
                                 precollected)
            self.__pre_fill_item("Transturtle Home water", "Home water, Transturtle", precollected)
            self.__pre_fill_item("Transturtle Abyss right", "Abyss right area, Transturtle", precollected)
            self.__pre_fill_item("Transturtle Final Boss", "Final boss area, Transturtle", precollected)
            # The last two are inverted because in the original game, they are special turtle that communicate directly
            self.__pre_fill_item("Transturtle Simon says", "Arnassi Ruins, Transturtle", precollected)
            self.__pre_fill_item("Transturtle Arnassi ruins", "Simon says area, Transturtle", precollected)
        for name, data in item_table.items():
            if name in precollected:
                precollected.remove(name)
                self.multiworld.itempool.append(self.create_item(self.get_filler_item_name()))
            else:
                if name not in self.exclude:
                    for i in range(data[1]):
                        item = self.create_item(name)
                        self.multiworld.itempool.append(item)


    def __excluded_hard_or_hidden_location(self) -> None:
        self.multiworld.get_location("Energy temple boss area, Fallen god tooth", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Cathedral boss area, beating Mithalan God", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Kelp forest boss area, beating Drunian God", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Sun temple boss area, beating Sun God", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Sunken city, bulb on the top of the boss area (boiler room)",
                                     self.player).progress_type = LocationProgressType.EXCLUDED
        self.multiworld.get_location("Home water, Nautilus Egg", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Energy temple blaster room, Blaster egg", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Mithalas castle, beating the priests", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Mermog cave, Piranha Egg", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Octopus cave, Dumbo Egg", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("King Jellyfish cave, bulb in the right path from King Jelly",
                                     self.player).progress_type = LocationProgressType.EXCLUDED
        self.multiworld.get_location("King Jellyfish cave, Jellyfish Costume",
                                     self.player).progress_type = LocationProgressType.EXCLUDED
        self.multiworld.get_location("Final boss area, bulb in the boss second form room",
                                     self.player).progress_type = LocationProgressType.EXCLUDED
        self.multiworld.get_location("Sun Worm path, first cliff bulb", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Sun Worm path, second cliff bulb", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("The veil top right area, bulb in the top of the water fall",
                                     self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Bubble cave, bulb in the left cave wall", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Bubble cave, bulb in the right cave wall (behind the ice cristal)",
                                     self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Bubble cave, Verse egg", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Kelp Forest bottom left area, bulb close to the spirit cristals",
                                     self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Kelp forest bottom left area, Walker baby",
                                     self.player).progress_type = LocationProgressType.EXCLUDED
        self.multiworld.get_location("Sun temple, Sun key", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("The body bottom area, Mutant Costume", self.player).progress_type = (
            LocationProgressType.EXCLUDED)
        self.multiworld.get_location("Sun temple, bulb in the hidden room of the right part",
                                     self.player).progress_type = LocationProgressType.EXCLUDED

    def set_rules(self) -> None:
        """
        Launched when the Multiworld generator is ready to generate rules
        """
        self.regions.add_event_locations()
        self.regions.adjusting_rules(self.options)
        if self.options.exclude_hard_or_hidden_locations:
            self.__excluded_hard_or_hidden_location()

        self.multiworld.completion_condition[self.player] = lambda \
            state: state.has("Victory", self.player)

        # for debugging purposes, you may want to visualize the layout of your world.
        # Uncomment the following code to write a PlantUML diagram to the file
        # "aquaria_world.puml" that can help you see whether your regions and locations
        # are connected and placed as desired
        # from Utils import visualize_regions
        # visualize_regions(self.multiworld.get_region("Menu", self.player), "aquaria_world.puml")

    def generate_basic(self) -> None:
        """
        Player-specific randomization that does not affect logic.
        Used to fill then `ingredients_substitution` list
        """
        simple_ingredients_substitution = [i for i in range(27)]
        if self.options.ingredient_randomizer.value > 0:
            if self.options.ingredient_randomizer.value == 1:
                simple_ingredients_substitution.pop(-1)
                simple_ingredients_substitution.pop(-1)
                simple_ingredients_substitution.pop(-1)
            self.random.shuffle(simple_ingredients_substitution)
            if self.options.ingredient_randomizer.value == 1:
                simple_ingredients_substitution.extend([24, 25, 26])
        dishes_substitution = [i for i in range(27, 76)]
        if self.options.dish_randomizer:
            self.random.shuffle(dishes_substitution)
        self.ingredients_substitution.clear()
        self.ingredients_substitution.extend(simple_ingredients_substitution)
        self.ingredients_substitution.extend(dishes_substitution)

    def fill_slot_data(self) -> Dict[str, Any]:
        aquarian_translation = False
        if self.options.aquarian_translation:
            aquarian_translation = True
        skip_first_vision = False
        if self.options.skip_first_vision:
            skip_first_vision = True
        return {"ingredientReplacement": self.ingredients_substitution,
                "aquarianTranslate": aquarian_translation,
                "secret_needed": self.options.objective.value > 0,
                "minibosses_to_kill": self.options.mini_bosses_to_beat.value,
                "bigbosses_to_kill": self.options.big_bosses_to_beat.value,
                "skip_first_vision": skip_first_vision,
                }
