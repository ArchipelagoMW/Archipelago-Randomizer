"""
Author: Louis M
Date: Thu, 18 Apr 2024 18:45:56 +0000
Description: Base class for the Aquaria randomizer unit tests
"""


from test.bases import WorldTestBase

# Every location accessible after the home water.
after_home_water_locations = [
    "Sun Crystal",
    "Home Water, Transturtle",
    "Open Water top left area, bulb under the rock in the right path",
    "Open Water top left area, bulb under the rock in the left path",
    "Open Water top left area, bulb to the right of the save crystal",
    "Open Water top right area, bulb in the small path before Mithalas",
    "Open Water top right area, bulb in the path from the left entrance",
    "Open Water top right area, bulb in the clearing close to the bottom exit",
    "Open Water top right area, bulb in the big clearing close to the save crystal",
    "Open Water top right area, bulb in the big clearing to the top exit",
    "Open Water top right area, first urn in the Mithalas exit",
    "Open Water top right area, second urn in the Mithalas exit",
    "Open Water top right area, third urn in the Mithalas exit",
    "Open Water top right area, bulb in the turtle room",
    "Open Water top right area, Transturtle",
    "Open Water bottom left area, bulb behind the chomper fish",
    "Open Water bottom left area, bulb inside the lowest fish pass",
    "Open Water skeleton path, bulb close to the right exit",
    "Open Water skeleton path, bulb behind the chomper fish",
    "Open Water skeleton path, King Skull",
    "Arnassi Ruins, bulb in the right part",
    "Arnassi Ruins, bulb in the left part",
    "Arnassi Ruins, bulb in the center part",
    "Arnassi Ruins, Song Plant Spore",
    "Arnassi Ruins, Arnassi Armor",
    "Arnassi Ruins, Arnassi Statue",
    "Arnassi Ruins, Transturtle",
    "Arnassi Ruins, Crab Armor",
    "Simon Says area, Transturtle",
    "Mithalas City, first bulb in the left city part",
    "Mithalas City, second bulb in the left city part",
    "Mithalas City, bulb in the right part",
    "Mithalas City, bulb at the top of the city",
    "Mithalas City, first bulb in a broken home",
    "Mithalas City, second bulb in a broken home",
    "Mithalas City, bulb in the bottom left part",
    "Mithalas City, first bulb in one of the homes",
    "Mithalas City, second bulb in one of the homes",
    "Mithalas City, first urn in one of the homes",
    "Mithalas City, second urn in one of the homes",
    "Mithalas City, first urn in the city reserve",
    "Mithalas City, second urn in the city reserve",
    "Mithalas City, third urn in the city reserve",
    "Mithalas City, first bulb at the end of the top path",
    "Mithalas City, second bulb at the end of the top path",
    "Mithalas City, bulb in the top path",
    "Mithalas City, Mithalas Pot",
    "Mithalas City, urn in the Castle flower tube entrance",
    "Mithalas City, Doll",
    "Mithalas City, urn inside a home fish pass",
    "Mithalas City Castle, bulb in the flesh hole",
    "Mithalas City Castle, Blue banner",
    "Mithalas City Castle, urn in the bedroom",
    "Mithalas City Castle, first urn of the single lamp path",
    "Mithalas City Castle, second urn of the single lamp path",
    "Mithalas City Castle, urn in the bottom room",
    "Mithalas City Castle, first urn on the entrance path",
    "Mithalas City Castle, second urn on the entrance path",
    "Mithalas City Castle, beating the Priests",
    "Mithalas City Castle, Trident Head",
    "Mithalas Cathedral, first urn in the top right room",
    "Mithalas Cathedral, second urn in the top right room",
    "Mithalas Cathedral, third urn in the top right room",
    "Mithalas Cathedral, urn in the flesh room with fleas",
    "Mithalas Cathedral, first urn in the bottom right path",
    "Mithalas Cathedral, second urn in the bottom right path",
    "Mithalas Cathedral, urn behind the flesh vein",
    "Mithalas Cathedral, urn in the top left eyes boss room",
    "Mithalas Cathedral, first urn in the path behind the flesh vein",
    "Mithalas Cathedral, second urn in the path behind the flesh vein",
    "Mithalas Cathedral, third urn in the path behind the flesh vein",
    "Mithalas Cathedral, fourth urn in the top right room",
    "Mithalas Cathedral, Mithalan Dress",
    "Mithalas Cathedral right area, urn below the left entrance",
    "Cathedral Underground, bulb in the center part",
    "Cathedral Underground, first bulb in the top left part",
    "Cathedral Underground, second bulb in the top left part",
    "Cathedral Underground, third bulb in the top left part",
    "Cathedral Underground, bulb close to the save crystal",
    "Cathedral Underground, bulb in the bottom right path",
    "Cathedral boss area, beating Mithalan God",
    "Kelp Forest top left area, bulb in the bottom left clearing",
    "Kelp Forest top left area, bulb in the path down from the top left clearing",
    "Kelp Forest top left area, bulb in the top left clearing",
    "Kelp Forest top left area, Jelly Egg",
    "Kelp Forest top left area, bulb close to the Verse Egg",
    "Kelp Forest top left area, Verse Egg",
    "Kelp Forest top right area, bulb under the rock in the right path",
    "Kelp Forest top right area, bulb at the left of the center clearing",
    "Kelp Forest top right area, bulb in the left path's big room",
    "Kelp Forest top right area, bulb in the left path's small room",
    "Kelp Forest top right area, bulb at the top of the center clearing",
    "Kelp Forest top right area, Black Pearl",
    "Kelp Forest top right area, bulb in the top fish pass",
    "Kelp Forest bottom left area, bulb close to the spirit crystals",
    "Kelp Forest bottom left area, Walker baby",
    "Kelp Forest bottom left area, Transturtle",
    "Kelp Forest bottom right area, Odd Container",
    "Kelp Forest boss area, beating Drunian God",
    "Kelp Forest boss room, bulb at the bottom of the area",
    "Kelp Forest bottom left area, Fish Cave puzzle",
    "Kelp Forest sprite cave, bulb inside the fish pass",
    "Kelp Forest sprite cave, bulb in the second room",
    "Kelp Forest sprite cave, Seed Bag",
    "Mermog cave, bulb in the left part of the cave",
    "Mermog cave, Piranha Egg",
    "The Veil top left area, In Li's cave",
    "The Veil top left area, bulb under the rock in the top right path",
    "The Veil top left area, bulb hidden behind the blocking rock",
    "The Veil top left area, Transturtle",
    "The Veil top left area, bulb inside the fish pass",
    "Turtle cave, Turtle Egg",
    "Turtle cave, bulb in Bubble Cliff",
    "Turtle cave, Urchin Costume",
    "The Veil top right area, bulb in the middle of the wall jump cliff",
    "The Veil top right area, Golden Starfish",
    "The Veil top right area, bulb at the top of the waterfall",
    "The Veil top right area, Transturtle",
    "The Veil bottom area, bulb in the left path",
    "The Veil bottom area, bulb in the spirit path",
    "The Veil bottom area, Verse Egg",
    "The Veil bottom area, Stone Head",
    "Octopus Cave, Dumbo Egg",
    "Octopus Cave, bulb in the path below the Octopus Cave path",
    "Bubble Cave, bulb in the left cave wall",
    "Bubble Cave, bulb in the right cave wall (behind the ice crystal)",
    "Bubble Cave, Verse Egg",
    "Sun Temple, bulb in the top left part",
    "Sun Temple, bulb in the top right part",
    "Sun Temple, bulb at the top of the high dark room",
    "Sun Temple, Golden Gear",
    "Sun Temple, first bulb of the temple",
    "Sun Temple, bulb on the left part",
    "Sun Temple, bulb in the hidden room of the right part",
    "Sun Temple, Sun Key",
    "Sun Worm path, first path bulb",
    "Sun Worm path, second path bulb",
    "Sun Worm path, first cliff bulb",
    "Sun Worm path, second cliff bulb",
    "Sun Temple boss area, beating Sun God",
    "Abyss left area, bulb in hidden path room",
    "Abyss left area, bulb in the right part",
    "Abyss left area, Glowing Seed",
    "Abyss left area, Glowing Plant",
    "Abyss left area, bulb in the bottom fish pass",
    "Abyss right area, bulb behind the rock in the whale room",
    "Abyss right area, bulb in the middle path",
    "Abyss right area, bulb behind the rock in the middle path",
    "Abyss right area, bulb in the left green room",
    "Abyss right area, Transturtle",
    "Ice Cave, bulb in the room to the right",
    "Ice Cave, first bulb in the top exit room",
    "Ice Cave, second bulb in the top exit room",
    "Ice Cave, third bulb in the top exit room",
    "Ice Cave, bulb in the left room",
    "King Jellyfish Cave, bulb in the right path from King Jelly",
    "King Jellyfish Cave, Jellyfish Costume",
    "The Whale, Verse Egg",
    "Sunken City right area, crate close to the save crystal",
    "Sunken City right area, crate in the left bottom room",
    "Sunken City left area, crate in the little pipe room",
    "Sunken City left area, crate close to the save crystal",
    "Sunken City left area, crate before the bedroom",
    "Sunken City left area, Girl Costume",
    "Sunken City, bulb on top of the boss area",
    "The Body center area, breaking Li's cage",
    "The Body center area, bulb on the main path blocking tube",
    "The Body left area, first bulb in the top face room",
    "The Body left area, second bulb in the top face room",
    "The Body left area, bulb below the water stream",
    "The Body left area, bulb in the top path to the top face room",
    "The Body left area, bulb in the bottom face room",
    "The Body right area, bulb in the top face room",
    "The Body right area, bulb in the top path to the bottom face room",
    "The Body right area, bulb in the bottom face room",
    "The Body bottom area, bulb in the Jelly Zap room",
    "The Body bottom area, bulb in the nautilus room",
    "The Body bottom area, Mutant Costume",
    "Final Boss area, first bulb in the turtle room",
    "Final Boss area, second bulb in the turtle room",
    "Final Boss area, third bulb in the turtle room",
    "Final Boss area, Transturtle",
    "Final Boss area, bulb in the boss third form room",
    "Simon Says area, beating Simon Says",
    "Beating Fallen God",
    "Beating Mithalan God",
    "Beating Drunian God",
    "Beating Sun God",
    "Beating the Golem",
    "Beating Nautilus Prime",
    "Beating Blaster Peg Prime",
    "Beating Mergog",
    "Beating Mithalan priests",
    "Beating Octopus Prime",
    "Beating Crabbius Maximus",
    "Beating Mantis Shrimp Prime",
    "Beating King Jellyfish God Prime",
    "First secret",
    "Second secret",
    "Third secret",
    "Sunken City cleared",
    "Objective complete",
]

class AquariaTestBase(WorldTestBase):
    """Base class for Aquaria unit tests"""
    game = "Aquaria"
