"""
Defines Region for The Witness, assigns locations to them,
and connects them with the proper requirements
"""
from logging import warning
from typing import FrozenSet, Dict, Set

from BaseClasses import Entrance, Region, Location
from worlds.AutoWorld import World
from .static_logic import StaticWitnessLogic
from .Options import get_option_value
from Utils import KeyedDefaultDict
from .locations import WitnessPlayerLocations, StaticWitnessLocations
from .player_logic import WitnessPlayerLogic


class WitnessRegions:
    """Class that defines Witness Regions"""

    locat = None
    logic = None

    def make_lambda(self, panel_hex_to_solve_set: FrozenSet[FrozenSet[str]], world: World, player: int,
                    player_logic: WitnessPlayerLogic):
        """
        Lambdas are made in a for loop, so the values have to be captured
        This function is for that purpose
        """

        return lambda state: state._witness_can_solve_panels(
            panel_hex_to_solve_set, world, player, player_logic, self.locat
        )

    def entity_requires_region(self, entity: str, region: str, player_logic: WitnessPlayerLogic):
        if all(region in requirement for requirement in player_logic.REQUIREMENTS_BY_HEX[entity]):
            return True
        if entity in StaticWitnessLogic.ENTITIES_BY_HEX and StaticWitnessLogic.ENTITIES_BY_HEX[entity]["region"]:
            return StaticWitnessLogic.ENTITIES_BY_HEX[entity]["region"]["name"] == region
        return False

    def connect_if_possible(self, world: World, source: str, target: str, player_logic: WitnessPlayerLogic,
                            panel_hex_to_solve_set: FrozenSet[FrozenSet[str]], backwards: bool = False):
        """
        connect two regions and set the corresponding requirement
        """

        # Remove any possibilities where being in the target region would be required anyway.
        for subset in panel_hex_to_solve_set:
            if any(
                self.entity_requires_region(entity, target, player_logic)
                or not player_logic.REQUIREMENTS_BY_HEX[entity]
                for entity in subset
            ):
                panel_hex_to_solve_set = panel_hex_to_solve_set - {subset}

        # If there is no way to actually use this connection, don't even bother making it.
        if not panel_hex_to_solve_set:
            return

        source_region = self.region_cache[source]
        target_region = self.region_cache[target]

        backwards = " Backwards" if backwards else ""

        connection = Entrance(
            world.player,
            source + " to " + target + backwards,
            source_region
        )

        connection.access_rule = self.make_lambda(panel_hex_to_solve_set, world, world.player, player_logic)

        source_region.exits.append(connection)
        connection.connect(target_region)

        # Register any necessary indirect connections

        entities = {entity for sub in panel_hex_to_solve_set for entity in sub}
        mentioned_regions = {
                                single_unlock
                                for entity in entities
                                for requirement in player_logic.REQUIREMENTS_BY_HEX[entity]
                                for single_unlock in requirement
                                if single_unlock in StaticWitnessLogic.ALL_REGIONS_BY_NAME
                                and single_unlock != source
        }

        for dependent_region in mentioned_regions:
            world.multiworld.register_indirect_condition(self.region_cache[dependent_region], connection)

    def create_regions(self, world: World, player_logic: WitnessPlayerLogic):
        """
        Creates all the regions for The Witness
        """
        from . import create_region

        difficulty = get_option_value(world, "puzzle_randomization")

        if difficulty == 1:
            reference_logic = StaticWitnessLogic.sigma_expert
        elif difficulty == 0:
            reference_logic = StaticWitnessLogic.sigma_normal
        else:
            reference_logic = StaticWitnessLogic.vanilla

        all_locations = set()

        for region_name, region in reference_logic.ALL_REGIONS_BY_NAME.items():
            locations_for_this_region = [
                reference_logic.ENTITIES_BY_HEX[panel]["checkName"] for panel in region["panels"]
                if reference_logic.ENTITIES_BY_HEX[panel]["checkName"] in self.locat.CHECK_LOCATION_TABLE
            ]
            locations_for_this_region += [
                StaticWitnessLocations.get_event_name(panel) for panel in region["panels"]
                if StaticWitnessLocations.get_event_name(panel) in self.locat.EVENT_LOCATION_TABLE
            ]

            all_locations = all_locations | set(locations_for_this_region)

            new_region = create_region(world, region_name, self.locat, locations_for_this_region)
            self.region_cache[region_name] = new_region
            self.location_cache.update({location.name: location for location in new_region.locations})

            world.multiworld.regions.append(new_region)

        for region_name, region in reference_logic.ALL_REGIONS_BY_NAME.items():
            for connection in player_logic.CONNECTIONS_BY_REGION_NAME[region_name]:
                if connection[1] == frozenset({frozenset(["TrueOneWay"])}):
                    self.connect_if_possible(world, region_name, connection[0], player_logic, frozenset({frozenset()}))
                    continue

                self.connect_if_possible(world, region_name, connection[0], player_logic, connection[1])
                self.connect_if_possible(world, connection[0], region_name, player_logic, connection[1])

        return self.location_cache

    def __init__(self, locat: WitnessPlayerLocations, world: World):
        self.locat = locat
        player_name = world.multiworld.get_player_name(world.player)

        def get_uncached_region(key: str) -> Region:
            warning(f"Region \"{key}\" was not cached in {player_name}'s Witness world. Violet pls fix this.")
            return world.multiworld.get_region(key, world.player)

        def get_uncached_location(key: str) -> Location:
            warning(f"Location \"{key}\" was not cached in {player_name}'s Witness world. Violet pls fix this.")
            return world.multiworld.get_location(key, world.player)

        self.region_cache: KeyedDefaultDict[str, Region] = KeyedDefaultDict(
            get_uncached_region
        )
        self.location_cache: Dict[str, Location] = KeyedDefaultDict(
            get_uncached_location
        )
