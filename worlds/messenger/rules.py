from typing import Dict, List, TYPE_CHECKING, Union

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, allow_self_locking_items, CollectionRule
from .constants import NOTES, PHOBEKINS
from .options import Logic, MessengerAccessibility

if TYPE_CHECKING:
    from . import MessengerWorld


class MessengerRules:
    player: int
    world: "MessengerWorld"
    connection_rules: Dict[str, CollectionRule]
    region_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    maximum_price: int
    required_seals: int

    def __init__(self, world: "MessengerWorld") -> None:
        self.player = world.player
        self.world = world

        # these locations are at the top of the shop tree, and the entire shop tree needs to be purchased
        maximum_price = (world.multiworld.get_location("The Shop - Demon's Bane", self.player).cost +
                         world.multiworld.get_location("The Shop - Focused Power Sense", self.player).cost)
        self.maximum_price = min(maximum_price, world.total_shards)
        self.required_seals = max(1, world.required_seals)

        # dict of connection names and requirements to traverse the exit
        self.connection_rules = {
            # from ToTHQ
            "Artificer's Portal":
                lambda state: state.has_all({"Demon King Crown", "Magic Firefly"}, self.player),
            "Shrink Down":
                lambda state: (state.has_all(NOTES, self.player) or self.has_enough_seals(state))
                              and self.has_dart(state),
            # the shop
            "Money Sink":
                lambda state: state.has("Money Wrench", self.player) and self.can_shop(state),
            # Autumn Hills
            "Autumn Hills - Portal -> Autumn Hills - Dimension Climb Shop":
                lambda state: self.has_wingsuit(state) and self.has_dart(state),
            "Autumn Hills - Hope Path Shop -> Autumn Hills - Hope Latch Checkpoint":
                self.has_dart,
            # Forlorn Temple
            "Forlorn Temple - Outside Shop -> Forlorn Temple - Entrance Shop":
                lambda state: state.has_all({"Wingsuit", *PHOBEKINS}, self.player) and self.can_dboost(state),
            # Bamboo Creek
            "Bamboo Creek - Top Left -> Forlorn Temple - Right":
                lambda state: state.multiworld.get_region("Forlorn Temple - Right", self.player).can_reach(state),
            # Howling Grotto
            "Howling Grotto - Portal -> Howling Grotto - Crushing Pits Shop":
                self.has_wingsuit,
            "Howling Grotto - Left -> Bamboo Creek - Right":
                self.has_wingsuit,
            # Searing Crags
            "Searing Crags - Rope Dart Shop -> Searing Crags - Triple Ball Spinner Checkpoint":
                self.has_vertical,
            "Searing Crags - Portal -> Searing Crags - Right":
                self.has_tabi,
            "Searing Crags - Portal -> Searing Crags - Before Final Climb Shop":
                self.has_wingsuit,
            "Searing Crags - Portal -> Searing Crags - Colossuses Shop":
                self.has_wingsuit,
            "Searing Crags - Colossuses Shop -> Searing Crags - Key of Strength Shop":
                lambda state: state.has("Power Thistle", self.player)
                              and (self.has_dart(state)
                                   or (self.has_wingsuit(state)
                                       and self.can_destroy_projectiles(state))),
            # Glacial Peak
            "Glacial Peak - Portal -> Glacial Peak - Top":
                self.has_vertical,
            "Glacial Peak - Left -> Elemental Skylands":
                lambda state: state.has("Magic Firefly", self.player) and self.has_wingsuit(state),
            "Glacial Peak - Top -> Cloud Ruins - Left":
                lambda state: self.has_vertical(state) and state.has("Ruxxtin's Amulet", self.player),
            # Cloud Ruins
            "Cloud Ruins - Spike Float Checkpoint -> Cloud Ruins - Pillar Glide Shop":
                lambda state: self.has_wingsuit(state) and (self.has_dart(state) or self.can_dboost(state)),
            "Cloud Ruins - Pillar Glide Shop -> Cloud Ruins - Ghost Pit Checkpoint":
                self.has_dart,
            # Riviere Turquoise
            "Riviere Turquoise - Waterfall Shop -> Riviere Turquoise - Flower Flight Checkpoint":
                lambda state: self.has_dart(state) or (self.has_wingsuit(state) and self.can_destroy_projectiles(state)),
            # Sunken Shrine
            "Sunken Shrine - Portal -> Sunken Shrine - Sun Path Shop":
                self.has_tabi,
            "Sunken Shrine - Portal -> Sunken Shrine - Moon Path Shop":
                self.has_tabi,
        }
        
        self.region_rules = {
            "Riviere Turquoise": lambda state: self.has_dart(state) or
                                               (self.has_wingsuit(state) and self.can_destroy_projectiles(state)),
            "Forlorn Temple": lambda state: state.has_all({"Wingsuit", *PHOBEKINS}, self.player) and self.can_dboost(state),
            "Glacial Peak": self.has_vertical,
            "Elemental Skylands": lambda state: state.has("Magic Firefly", self.player) and self.has_wingsuit(state),
            "Music Box": lambda state: (state.has_all(NOTES, self.player)
                                        or self.has_enough_seals(state)) and self.has_dart(state),
            "The Craftsman's Corner": lambda state: state.has("Money Wrench", self.player) and self.can_shop(state),
        }

        self.location_rules = {
            # ninja village
            "Ninja Village Seal - Tree House": self.has_dart,
            # autumn hills
            "Autumn Hills Seal - Spike Ball Darts": self.is_aerobatic,
            # bamboo creek
            "Bamboo Creek - Claustro": lambda state: self.has_dart(state) or self.can_dboost(state),
            # howling grotto
            "Howling Grotto Seal - Windy Saws and Balls": self.has_wingsuit,
            "Howling Grotto Seal - Crushing Pits": lambda state: self.has_wingsuit(state) and self.has_dart(state),
            "Howling Grotto - Emerald Golem": self.has_wingsuit,
            # searing crags
            "Searing Crags - Astral Tea Leaves":
                lambda state: state.can_reach("Ninja Village - Astral Seed", "Location", self.player),
            # glacial peak
            "Glacial Peak Seal - Ice Climbers": self.has_dart,
            "Glacial Peak Seal - Projectile Spike Pit": self.can_destroy_projectiles,
            # tower of time
            "Tower of Time Seal - Time Waster": self.has_dart,
            "Tower of Time Seal - Lantern Climb": lambda state: self.has_wingsuit(state) and self.has_dart(state),
            "Tower of Time Seal - Arcane Orbs": lambda state: self.has_wingsuit(state) and self.has_dart(state),
            # underworld
            "Underworld Seal - Sharp and Windy Climb": self.has_wingsuit,
            "Underworld Seal - Fireball Wave": self.is_aerobatic,
            "Underworld Seal - Rising Fanta": self.has_dart,
            # sunken shrine
            "Sunken Shrine - Key of Love": lambda state: state.has_all({"Sun Crest", "Moon Crest"}, self.player),
            # riviere turquoise
            "Riviere Turquoise Seal - Bounces and Balls": self.can_dboost,
            "Riviere Turquoise Seal - Launch of Faith": lambda state: self.can_dboost(state) or self.has_dart(state),
            # elemental skylands
            "Elemental Skylands - Key of Symbiosis": self.has_dart,
            "Elemental Skylands Seal - Air": self.has_wingsuit,
            "Elemental Skylands Seal - Water": lambda state: self.has_dart(state) and
                                                             state.has("Currents Master", self.player),
            "Elemental Skylands Seal - Fire": lambda state: self.has_dart(state) and self.can_destroy_projectiles(state),
            "Earth Mega Shard": self.has_dart,
            "Water Mega Shard": self.has_dart,
        }

    def has_wingsuit(self, state: CollectionState) -> bool:
        return state.has("Wingsuit", self.player)

    def has_dart(self, state: CollectionState) -> bool:
        return state.has("Rope Dart", self.player)

    def has_tabi(self, state: CollectionState) -> bool:
        return state.has("Lightfoot Tabi", self.player)

    def has_vertical(self, state: CollectionState) -> bool:
        return self.has_wingsuit(state) or self.has_dart(state)

    def has_enough_seals(self, state: CollectionState) -> bool:
        return state.has("Power Seal", self.player, self.required_seals)

    def can_destroy_projectiles(self, state: CollectionState) -> bool:
        return state.has("Strike of the Ninja", self.player)

    def can_dboost(self, state: CollectionState) -> bool:
        return state.has_any({"Path of Resilience", "Meditation"}, self.player) and \
            state.has("Second Wind", self.player)

    def is_aerobatic(self, state: CollectionState) -> bool:
        return self.has_wingsuit(state) and state.has("Aerobatics Warrior", self.player)

    def true(self, state: CollectionState) -> bool:
        """I know this is stupid, but it's easier to read in the dicts."""
        return True

    def can_shop(self, state: CollectionState) -> bool:
        return state.has("Shards", self.player, self.maximum_price)

    def set_messenger_rules(self) -> None:
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, self.player)
            entrance.access_rule = rule
        for loc in multiworld.get_locations(self.player):
            if loc.name in self.location_rules:
                loc.access_rule = self.location_rules[loc.name]

        multiworld.completion_condition[self.player] = lambda state: state.has("Rescue Phantom", self.player)
        # if multiworld.accessibility[self.player]:  # not locations accessibility
        #     set_self_locking_items(self.world, self.player)


class MessengerHardRules(MessengerRules):
    extra_rules: Dict[str, CollectionRule]

    def __init__(self, world: "MessengerWorld") -> None:
        super().__init__(world)

        self.region_rules.update({
            "Ninja Village": self.has_vertical,
            "Autumn Hills": self.has_vertical,
            "Catacombs": self.has_vertical,
            "Bamboo Creek": self.has_vertical,
            "Riviere Turquoise": self.true,
            "Forlorn Temple": lambda state: self.has_vertical(state) and state.has_all(PHOBEKINS, self.player),
            "Searing Crags Upper": lambda state: self.can_destroy_projectiles(state) or self.has_windmill(state)
                                                 or self.has_vertical(state),
            "Glacial Peak": lambda state: self.can_destroy_projectiles(state) or self.has_windmill(state)
                                          or self.has_vertical(state),
            "Elemental Skylands": lambda state: state.has("Magic Firefly", self.player) or
                                                self.has_windmill(state) or
                                                self.has_dart(state),
        })

        self.location_rules.update({
            "Howling Grotto Seal - Windy Saws and Balls": self.true,
            "Searing Crags Seal - Triple Ball Spinner": self.true,
            "Searing Crags Seal - Raining Rocks": lambda state: self.has_vertical(state) or self.can_destroy_projectiles(state),
            "Searing Crags Seal - Rhythm Rocks": lambda state: self.has_vertical(state) or self.can_destroy_projectiles(state),
            "Searing Crags - Power Thistle": lambda state: self.has_vertical(state) or self.can_destroy_projectiles(state),
            "Glacial Peak Seal - Ice Climbers": lambda state: self.has_vertical(state) or self.can_dboost(state),
            "Glacial Peak Seal - Projectile Spike Pit": self.true,
            "Glacial Peak Seal - Glacial Air Swag": lambda state: self.has_windmill(state) or self.has_vertical(state),
            "Glacial Peak Mega Shard": lambda state: self.has_windmill(state) or self.has_vertical(state),
            "Cloud Ruins Seal - Ghost Pit": self.true,
            "Bamboo Creek - Claustro": self.has_wingsuit,
            "Tower of Time Seal - Lantern Climb": self.has_wingsuit,
            "Elemental Skylands Seal - Water": lambda state: self.has_dart(state) or self.can_dboost(state)
                                                             or self.has_windmill(state),
            "Elemental Skylands Seal - Fire": lambda state: (self.has_dart(state) or self.can_dboost(state)
                                                             or self.has_windmill(state)) and
                                                            self.can_destroy_projectiles(state),
            "Earth Mega Shard": lambda state: self.has_dart(state) or self.can_dboost(state) or self.has_windmill(state),
            "Water Mega Shard": lambda state: self.has_dart(state) or self.can_dboost(state) or self.has_windmill(state),
        })

        self.extra_rules = {
            "Searing Crags - Key of Strength": lambda state: self.has_dart(state) or self.has_windmill(state),
            "Elemental Skylands - Key of Symbiosis": lambda state: self.has_windmill(state) or self.can_dboost(state),
            "Autumn Hills Seal - Spike Ball Darts": lambda state: self.has_dart(state) or self.has_windmill(state),
            "Underworld Seal - Fireball Wave": self.has_windmill,
        }

    def has_windmill(self, state: CollectionState) -> bool:
        return state.has("Windmill Shuriken", self.player)

    def set_messenger_rules(self) -> None:
        super().set_messenger_rules()
        for loc, rule in self.extra_rules.items():
            if not self.world.options.shuffle_shards and "Shard" in loc:
                continue
            add_rule(self.world.multiworld.get_location(loc, self.player), rule, "or")


class MessengerOOBRules(MessengerRules):
    def __init__(self, world: "MessengerWorld") -> None:
        self.world = world
        self.player = world.player

        self.required_seals = max(1, world.required_seals)
        self.region_rules = {
            "Elemental Skylands":
                lambda state: state.has_any({"Windmill Shuriken", "Wingsuit", "Rope Dart", "Magic Firefly"}, self.player),
            "Music Box": lambda state: state.has_all(set(NOTES), self.player) or self.has_enough_seals(state),
        }

        self.location_rules = {
            "Bamboo Creek - Claustro": self.has_wingsuit,
            "Searing Crags - Key of Strength": self.has_wingsuit,
            "Sunken Shrine - Key of Love": lambda state: state.has_all({"Sun Crest", "Moon Crest"}, self.player),
            "Searing Crags - Pyro": self.has_tabi,
            "Underworld - Key of Chaos": self.has_tabi,
            "Corrupted Future - Key of Courage":
                lambda state: state.has_all({"Demon King Crown", "Magic Firefly"}, self.player),
            "Autumn Hills Seal - Spike Ball Darts": self.has_dart,
            "Ninja Village Seal - Tree House": self.has_dart,
            "Underworld Seal - Fireball Wave": lambda state: state.has_any({"Wingsuit", "Windmill Shuriken"},
                                                                           self.player),
            "Tower of Time Seal - Time Waster": self.has_dart,
        }

    def set_messenger_rules(self) -> None:
        super().set_messenger_rules()
        self.world.options.accessibility.value = MessengerAccessibility.option_minimal


def set_self_locking_items(world: "MessengerWorld", player: int) -> None:
    multiworld = world.multiworld

    # locations where these placements are always valid
    allow_self_locking_items(multiworld.get_location("Searing Crags - Key of Strength", player), "Power Thistle")
    allow_self_locking_items(multiworld.get_location("Sunken Shrine - Key of Love", player), "Sun Crest", "Moon Crest")
    allow_self_locking_items(multiworld.get_location("Corrupted Future - Key of Courage", player), "Demon King Crown")
    allow_self_locking_items(multiworld.get_location("Elemental Skylands Seal - Water", player), "Currents Master")
