from BaseClasses import CollectionState
from worlds.generic.Rules import add_item_rule, add_rule


def have_light_source(state: CollectionState, player: int) -> bool:
    return state.has("Lantern", player) or (state.has("Stick", player) and state.has("Boots", player))


def have_bombs(state: CollectionState, player: int) -> bool:
    return state.has("Bombs", player)
    # or werewolf badge when badges are added


def have_all_orbs(state: CollectionState, player: int) -> bool:
    return state.has("Orb", player, 4)


def have_all_bats(state: CollectionState, player: int) -> bool:
    return state.has("Bat Statue", player, 4)


def have_all_vamps(state: CollectionState, player: int) -> bool:
    return state.has("Vamp Statue", player, 8)


def have_special_weapon_damage(state: CollectionState, player: int) -> bool:
    return (
        state.has_any(("Bombs", "Shock Wand", "Cactus", "Boomerang", "Whoopee", "Hot Pants"), player)
    )


def have_special_weapon_bullet(state: CollectionState, player: int) -> bool:
    return (
        state.has_any(("Bombs", "Ice Spear", "Cactus", "Boomerang", "Whoopee", "Hot Pants"), player)
    )


# return lambda state: True slingshot counts

def have_special_weapon_range_damage(state: CollectionState, player: int) -> bool:
    return (
        state.has_any(("Bombs", "Shock Wand", "Cactus", "Boomerang"), player)
    )
    # return lambda state: True slingshot counts


def have_special_weapon_through_walls(state: CollectionState, player: int) -> bool:
    return (
        state.has_any(("Bombs", "Shock Wand", "Whoopee"), player)
        # state.has("Hot Pants")
    )


def can_cleanse_crypts(state: CollectionState, player: int) -> bool:
    return (have_light_source(state, player) and can_enter_zombiton(state, player) and have_special_weapon_range_damage(
        state, player))


# these will get removed in favor of region access reqs eventually
def can_enter_zombiton(state: CollectionState, player: int) -> bool:
    return state.has("Boots", player)


def can_enter_rocky_cliffs(state: CollectionState, player: int) -> bool:
    return state.has("Big Gem", player)


def can_enter_vampy(state: CollectionState, player: int) -> bool:
    return can_enter_rocky_cliffs(state, player) and have_light_source(state, player)


def can_enter_vampy_ii(state: CollectionState, player: int) -> bool:
    return can_enter_vampy(state, player) and state.has("Skull Key", player)


def can_enter_vampy_iii(state: CollectionState, player: int) -> bool:
    return can_enter_vampy_ii(state, player) and state.has("Bat Key", player)


def can_enter_vampy_iv(state: CollectionState, player: int) -> bool:
    return can_enter_vampy_iii(state, player) and state.has("Pumpkin Key", player)

def set_rules(multiworld, world, player):

    access_rules = {
        "Slurpy Swamp Mud - Swamp Mud Path": lambda state: state.has("Boots", player),
        #"Halloween Hill - Bog Beast Home": lambda state: True,
        "Rocky Cliffs - Rocky Cliffs below Upper Caverns": lambda state: can_enter_rocky_cliffs(state, player),
        "Slurpy Swamp Mud - Sapling Shrine": lambda state: state.has("Boots", player),
        #"Halloween Hill - Terror Glade": lambda state: True,
        "Halloween Hill - Rocky Cliffs Vine": lambda state: state.has("Fertilizer", player),
        "Rocky Cliffs - Rocky Cliffs Grand Pharoh": lambda state: can_enter_rocky_cliffs(state, player),
        "Rocky Cliffs - Rocky Cliffs Rock Corner": lambda state: can_enter_rocky_cliffs(state, player) and have_bombs(state, player),
        #"Halloween Hill - Mushroom outside town": lambda state: True,
        #"Halloween Hill - North of UG Passage": lambda state: True,
        #"Halloween Hill - Top left mushroom spot": lambda state: True,
        #"Halloween Hill - NE of UG Passage": lambda state: True,
        #"Halloween Hill - East Woods": lambda state: True,
        "Rocky Cliffs - Rocky Cliffs Ledge": lambda state: can_enter_rocky_cliffs(state, player),
        "Rocky Cliffs - Rocky Cliffs Peak": lambda state: can_enter_rocky_cliffs(state, player),
        #"Halloween Hill - Cat Tree": lambda state: True,
        "The Witch's Cabin Front - Bedroom": lambda state: have_light_source(state, player),
        #"The Witch's Cabin Back - Backroom": lambda state: True,
        #"Bonita's Cabin - Barrel Maze": lambda state: True,
        "The Bog Pit - Top Door": lambda state: state.has("Skull Key", player),
        #"The Bog Pit - Post Room": lambda state: True,
        #"The Bog Pit - Window Drip": lambda state: True,
        #"The Bog Pit - Green room": lambda state: True,
        "The Bog Pit - Arena": lambda state: True,
        "The Bog Pit - Kill Wall": lambda state: True,
        "Underground Tunnel Top - Swampdog Door": lambda state: state.has("Pumpkin Key", player),
        "Underground Tunnel Top - Scribble Wall": lambda state: have_special_weapon_bullet(state, player),
        "Underground Tunnel Top - Tiny Passage": lambda state: True,
        "Underground Tunnel Top - fire frogs": lambda state: True,
        "Underground Tunnel Mud - Torch Island": lambda state: state.has("Boots", player),
        "Underground Tunnel Top - Small Room": lambda state: True,
        "Swamp Gas Cavern Front - Scratch Wall": lambda state: state.has("Boots", player) and have_special_weapon_bullet(state, player),
        "Swamp Gas Cavern Front - Bat Mound": lambda state: state.has("Boots", player) and state.has("Bat Key", player),
        "Swamp Gas Cavern Back - Stair room": lambda state: state.has("Boots", player),
        "Swamp Gas Cavern Front - Rock Prison": lambda state: state.has("Boots", player) and have_bombs(state, player),
        "A Tiny Cabin - Tiny Cabin": lambda state: state.has("Skull Key", player),
        "A Cabin Seer - Bedside ": lambda state: can_enter_zombiton(state, player),
        "Dusty Crypt - Pumpkin Door": lambda state: have_light_source(state, player) and state.has("Pumpkin Key", player),
        "Dusty Crypt - Maze": lambda state: have_light_source(state, player),
        "Musty Crypt - Big Closed Room": lambda state: have_light_source(state, player) and can_enter_zombiton(state, player) and have_special_weapon_bullet(state, player),
        "Rusty Crypt - Spike Vine": lambda state: have_light_source(state, player) and state.has("Fertilizer", player),
        "Rusty Crypt - Boulders": lambda state: have_light_source(state, player),
        "A Messy Cabin - Barrel Mess": lambda state: can_enter_zombiton(state, player),
        "Under The Lake - Lightning Rod Secret": lambda state: have_light_source(state, player) and have_all_orbs(state, player),
        "Under The Lake - Bat Door": lambda state: have_light_source(state, player) and have_all_orbs(state, player) and state.has("Bat Key", player),
        "Deeper Under The Lake - SE corner": lambda state: have_light_source(state, player) and have_all_orbs(state, player),
        "Deeper Under The Lake - Rhombus": lambda state: have_light_source(state, player) and have_all_orbs(state, player),
        "Frankenjulie's Laboratory - Boss Reward": lambda state: have_light_source(state, player) and have_all_orbs(state, player),
        "Haunted Tower - Barracks": lambda state: state.has("Ghost Potion", player) and state.has("Bat Key", player),
        "Haunted Tower, Floor 2 - Top Left": lambda state: state.has("Ghost Potion", player),
        "Haunted Tower Roof - Boss Reward": lambda state: state.has("Ghost Potion", player),
        "Haunted Basement - DoorDoorDoorDoorDoorDoor": lambda state: state.has("Ghost Potion", player) and have_light_source(state, player) and state.has("Bat Key", player) and state.has("Skull Key", player) and state.has("Pumpkin Key", player),
        "Abandoned Mines - Shaft": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "The Shrine Of Bombulus - Bombulus": lambda state: can_enter_rocky_cliffs(state, player),
        "A Gloomy Cavern - Lockpick": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "Happy Stick Woods - Happy Stick Hidden": lambda state: state.has("Happy Stick", player),
        "Happy Stick Woods - Happy Stick Reward": lambda state: state.has("Happy Stick", player),
        "The Wolf Den - Wolf Top Left": lambda state: have_light_source(state, player) and state.has("Silver Sling", player),
        "The Wolf Den - Pumpkin Door": lambda state: have_light_source(state, player) and state.has("Silver Sling", player) and state.has("Pumpkin Key", player),
        "The Wolf Den - Grow Room": lambda state: have_light_source(state, player) and state.has("Silver Sling", player) and state.has("Fertilizer", player),
        "Upper Creepy Caverns - The Three ombres": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "Under the Ravine - Left Vine": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player) and state.has("Fertilizer", player),
        "Under the Ravine - Right Vine": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player) and state.has("Fertilizer", player),
        "Creepy Caverns Middle - M Pharoh bat Room": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player) and state.has("Bat Key", player),
        "Creepy Caverns Right - E 2 blue Pharos": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "Creepy Caverns Middle - M GARGOYLE ROOM": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "Castle Vampy - Vampire Guard": lambda state: can_enter_vampy(state, player),
        "Castle Vampy - maze top left": lambda state: can_enter_vampy(state, player),
        "Castle Vampy - Top Right Gauntlet": lambda state: can_enter_vampy(state, player),
        "Castle Vampy - Bat Closet": lambda state: can_enter_vampy(state, player),
        "Castle Vampy II Main - Candle Room": lambda state: can_enter_vampy_ii(state, player),
        "Castle Vampy II Main - Top Right Top": lambda state: can_enter_vampy_ii(state, player),
        "Castle Vampy II Main - Bottom Right Middle": lambda state: can_enter_vampy_ii(state, player),
        "Castle Vampy II Main - Bat room": lambda state: can_enter_vampy_ii(state, player) and have_special_weapon_bullet(state, player),
        "Cabin In The Woods - Gold Skull": lambda state: True,
        "Castle Vampy III Main - Middle": lambda state: can_enter_vampy_iii(state, player),
        "Castle Vampy III Main - Behind the Pews": lambda state: can_enter_vampy_iii(state, player),
        "Castle Vampy III Main - AMBUSH!": lambda state: can_enter_vampy_iii(state, player),
        "Castle Vampy III Main - Halloween": lambda state: can_enter_vampy_iii(state, player),
        "Castle Vampy III Main - So many bats": lambda state: can_enter_vampy_iii(state, player),
        "Castle Vampy IV Main - Right Path": lambda state: can_enter_vampy_iv(state, player),
        "Castle Vampy IV Main - Left Path": lambda state: can_enter_vampy_iv(state, player),
        "Castle Vampy IV Main - Ballroom Right": lambda state: can_enter_vampy_iv(state, player) and state.has("Ghost Potion", player) and state.has("Silver Sling", player),
        "Castle Vampy IV Main - Right Secret Wall": lambda state: can_enter_vampy_iv(state, player),
        "Castle Vampy IV Main - Ballroom Left": lambda state: can_enter_vampy_iv(state, player) and state.has("Ghost Potion", player) and state.has("Silver Sling", player),
        "Castle Vampy Roof NW - Gutsy the Elder": lambda state: can_enter_vampy(state, player) and have_all_bats(state, player) and have_special_weapon_damage(state, player),
        "Castle Vampy Roof NE - Stoney the Elder": lambda state: can_enter_vampy(state, player) and have_all_bats(state, player),
        "Castle Vampy Roof SW - Drippy the Elder": lambda state: can_enter_vampy(state, player) and have_all_bats(state, player),
        "Castle Vampy Roof SE - Toasty the Elder": lambda state: can_enter_vampy(state, player) and have_all_bats(state, player),
        "The Heart Of Terror - Bonkula": lambda state: can_enter_vampy_iv(state, player) and have_all_vamps(state, player),
        "A Hidey-Hole - Bat Door": lambda state: state.has("Bat Key", player),
        #"A Hidey-Hole - Pebbles": lambda state: True,
        "Swampdog Lair - Entrance": lambda state: state.has("Boots", player),
        "Swampdog Lair - End": lambda state: state.has("Boots", player) and have_light_source(state, player) and state.has("Fertilizer", player),
        "The Witch's Cabin Front - Ghostbusting": lambda state: state.has("Big Gem", player) and state.has("Doom Daisy", player) and state.has("Mushroom", player, 10),
        "A Cabin Larry - Hairy Larry": lambda state: have_light_source(state, player) and state.has("Silver Sling", player) and state.has("Boots", player) ,
        "Halloween Hill - Scaredy Cat": lambda state: state.has("Cat", player),
        "Halloween Hill - Silver Bullet": lambda state: state.has("Silver", player) and can_cleanse_crypts(state, player),
        "Halloween Hill - Smashing Pumpkins": lambda state: can_cleanse_crypts(state, player),
        "Halloween Hill - Sticky Shoes": lambda state: True,
        "A Cabin Collector - The Collection": lambda state: state.has("Silver Sling", player) and state.has("Ghost Potion", player) and can_enter_vampy(state, player),
        "A Gloomy Cavern - The Rescue": lambda state: have_light_source(state, player) and can_enter_rocky_cliffs(state, player),
        "A Cabin Trees - Tree Trimming": lambda state: True,
        "The Witch's Cabin Front - Witch Mushrooms": lambda state: state.has("Mushroom", player, 10),
        "Halloween Hill - Zombie Stomp": lambda state: can_cleanse_crypts(state, player),
        "The Evilizer - Save Halloween Hill": lambda state: True
        }
    for loc in multiworld.get_locations(player):
        if loc.name in access_rules:
            add_rule(loc, access_rules[loc.name])

