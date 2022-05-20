from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld

from BaseClasses import Location

SC2WOL_LOC_ID_OFFSET = 1000

class SC2WoLLocation(Location):
    game: str = "Starcraft2WoL"


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True


def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
    location_table: List[LocationData] = [
        LocationData("Liberation Day", "Liberation Day: Victory", SC2WOL_LOC_ID_OFFSET + 100),
        LocationData("Liberation Day", "Liberation Day: First Statue", SC2WOL_LOC_ID_OFFSET + 101),
        LocationData("Liberation Day", "Liberation Day: Second Statue", SC2WOL_LOC_ID_OFFSET + 102),
        LocationData("Liberation Day", "Liberation Day: Third Statue", SC2WOL_LOC_ID_OFFSET + 103),
        LocationData("Liberation Day", "Liberation Day: Fourth Statue", SC2WOL_LOC_ID_OFFSET + 104),
        LocationData("Liberation Day", "Liberation Day: Fifth Statue", SC2WOL_LOC_ID_OFFSET + 105),
        LocationData("Liberation Day", "Liberation Day: Sixth Statue", SC2WOL_LOC_ID_OFFSET + 106),
        LocationData("Liberation Day", "Beat Liberation Day", None),
        LocationData("The Outlaws", "The Outlaws: Victory", SC2WOL_LOC_ID_OFFSET + 200),
        LocationData("The Outlaws", "The Outlaws: Rebel Base", SC2WOL_LOC_ID_OFFSET + 201),
        LocationData("The Outlaws", "Beat The Outlaws", None),
        LocationData("Zero Hour", "Zero Hour: Victory", SC2WOL_LOC_ID_OFFSET + 300),
        LocationData("Zero Hour", "Zero Hour: First Group Rescued", SC2WOL_LOC_ID_OFFSET + 301),
        LocationData("Zero Hour", "Zero Hour: Second Group Rescued", SC2WOL_LOC_ID_OFFSET + 302),
        LocationData("Zero Hour", "Zero Hour: Third Group Rescued", SC2WOL_LOC_ID_OFFSET + 303),
        LocationData("Zero Hour", "Beat Zero Hour", None),
        LocationData("Evacuation", "Evacuation: Victory", SC2WOL_LOC_ID_OFFSET + 400),
        LocationData("Evacuation", "Evacuation: First Chysalis", SC2WOL_LOC_ID_OFFSET + 401),
        LocationData("Evacuation", "Evacuation: Second Chysalis", SC2WOL_LOC_ID_OFFSET + 402),
        LocationData("Evacuation", "Evacuation: Third Chysalis", SC2WOL_LOC_ID_OFFSET + 403),
        LocationData("Evacuation", "Beat Evacuation", None),
        LocationData("Outbreak", "Outbreak: Victory", SC2WOL_LOC_ID_OFFSET + 500),
        LocationData("Outbreak", "Outbreak: Left Infestor", SC2WOL_LOC_ID_OFFSET + 501),
        LocationData("Outbreak", "Outbreak: Right Infestor", SC2WOL_LOC_ID_OFFSET + 502),
        LocationData("Outbreak", "Beat Outbreak", None),
        LocationData("Safe Haven", "Safe Haven: Victory", SC2WOL_LOC_ID_OFFSET + 600),
        LocationData("Safe Haven", "Beat Safe Haven", None),
        LocationData("Haven's Fall", "Haven's Fall: Victory", SC2WOL_LOC_ID_OFFSET + 700),
        LocationData("Haven's Fall", "Beat Haven's Fall", None),
        LocationData("Smash and Grab", "Smash and Grab: Victory", SC2WOL_LOC_ID_OFFSET + 800),
        LocationData("Smash and Grab", "Smash and Grab: First Relic", SC2WOL_LOC_ID_OFFSET + 801),
        LocationData("Smash and Grab", "Smash and Grab: Second Relic", SC2WOL_LOC_ID_OFFSET + 802),
        LocationData("Smash and Grab", "Smash and Grab: Third Relic", SC2WOL_LOC_ID_OFFSET + 803),
        LocationData("Smash and Grab", "Smash and Grab: Fourth Relic", SC2WOL_LOC_ID_OFFSET + 804),
        LocationData("Smash and Grab", "Beat Smash and Grab", None),
        LocationData("The Dig", "The Dig: Victory", SC2WOL_LOC_ID_OFFSET + 900),
        LocationData("The Dig", "The Dig: Left Relic", SC2WOL_LOC_ID_OFFSET + 901),
        LocationData("The Dig", "The Dig: Right Ground Relic", SC2WOL_LOC_ID_OFFSET + 902),
        LocationData("The Dig", "The Dig: Right Cliff Relic", SC2WOL_LOC_ID_OFFSET + 903),
        LocationData("The Dig", "Beat The Dig", None),
        LocationData("The Moebius Factor", "The Moebius Factor: 3rd Data Core", SC2WOL_LOC_ID_OFFSET + 1000),
        LocationData("The Moebius Factor", "The Moebius Factor: 1st Data Core ", SC2WOL_LOC_ID_OFFSET + 1001),
        LocationData("The Moebius Factor", "The Moebius Factor: 2nd Data Core", SC2WOL_LOC_ID_OFFSET + 1002),
        LocationData("The Moebius Factor", "The Moebius Factor: South Rescue", SC2WOL_LOC_ID_OFFSET + 1003,
                     lambda state: state._sc2wol_able_to_rescue(world, player) or True),
        LocationData("The Moebius Factor", "The Moebius Factor: Wall Rescue", SC2WOL_LOC_ID_OFFSET + 1004,
                     lambda state: state._sc2wol_able_to_rescue(world, player) or True),
        LocationData("The Moebius Factor", "The Moebius Factor: Mid Rescue", SC2WOL_LOC_ID_OFFSET + 1005,
                     lambda state: state._sc2wol_able_to_rescue(world, player) or True),
        LocationData("The Moebius Factor", "The Moebius Factor: Nydus Roof Rescue", SC2WOL_LOC_ID_OFFSET + 1006,
                     lambda state: state._sc2wol_able_to_rescue(world, player) or True),
        LocationData("The Moebius Factor", "The Moebius Factor: Alive Inside Rescue", SC2WOL_LOC_ID_OFFSET + 1007,
                     lambda state: state._sc2wol_able_to_rescue(world, player) or True),
        LocationData("The Moebius Factor", "The Moebius Factor: Brutalisk", SC2WOL_LOC_ID_OFFSET + 1008),
        LocationData("The Moebius Factor", "Beat The Moebius Factor", None),
        LocationData("Supernova", "Supernova: Victory", SC2WOL_LOC_ID_OFFSET + 1100),
        LocationData("Supernova", "Supernova: West Relic", SC2WOL_LOC_ID_OFFSET + 1101),
        LocationData("Supernova", "Supernova: North Relic", SC2WOL_LOC_ID_OFFSET + 1102),
        LocationData("Supernova", "Supernova: South Relic", SC2WOL_LOC_ID_OFFSET + 1103),
        LocationData("Supernova", "Supernova: East Relic", SC2WOL_LOC_ID_OFFSET + 1104),
        LocationData("Supernova", "Beat Supernova", None),
        LocationData("Maw of the Void", "Maw of the Void: Xel'Naga Vault", SC2WOL_LOC_ID_OFFSET + 1200),
        LocationData("Maw of the Void", "Maw of the Void: Landing Zone Cleared", SC2WOL_LOC_ID_OFFSET + 1201),
        LocationData("Maw of the Void", "Maw of the Void: Expansion Prisoners", SC2WOL_LOC_ID_OFFSET + 1202),
        LocationData("Maw of the Void", "Maw of the Void: South Close Prisoners", SC2WOL_LOC_ID_OFFSET + 1203),
        LocationData("Maw of the Void", "Maw of the Void: South Far Prisoners", SC2WOL_LOC_ID_OFFSET + 1204),
        LocationData("Maw of the Void", "Maw of the Void: North Prisoners", SC2WOL_LOC_ID_OFFSET + 1205),
        LocationData("Maw of the Void", "Beat Maw of the Void", None),
        LocationData("Devil's Playground", "Devil's Playground: 8000 Minerals", SC2WOL_LOC_ID_OFFSET + 1300),
        LocationData("Devil's Playground", "Devil's Playground: Tosh's Miners", SC2WOL_LOC_ID_OFFSET + 1301),
        LocationData("Devil's Playground", "Devil's Playground: Brutalisk", SC2WOL_LOC_ID_OFFSET + 1302),
        LocationData("Devil's Playground", "Beat Devil's Playground", None),
        LocationData("Welcome to the Jungle", "Welcome to the Jungle: 7 Canisters", SC2WOL_LOC_ID_OFFSET + 1400),
        LocationData("Welcome to the Jungle", "Welcome to the Jungle: Close Relic", SC2WOL_LOC_ID_OFFSET + 1401),
        LocationData("Welcome to the Jungle", "Welcome to the Jungle: West Relic", SC2WOL_LOC_ID_OFFSET + 1402),
        LocationData("Welcome to the Jungle", "Welcome to the Jungle: North-East Relic", SC2WOL_LOC_ID_OFFSET + 1403),
        LocationData("Welcome to the Jungle", "Beat Welcome to the Jungle", None),
        LocationData("Breakout", "Breakout: Main Prison", SC2WOL_LOC_ID_OFFSET + 1500),
        LocationData("Breakout", "Breakout: Diamondback Prison", SC2WOL_LOC_ID_OFFSET + 1501),
        LocationData("Breakout", "Breakout: Siegetank Prison", SC2WOL_LOC_ID_OFFSET + 1502),
        LocationData("Breakout", "Beat Breakout", None),
        LocationData("Ghost of a Chance", "Ghost of a Chance: Psi-Indoctrinator", SC2WOL_LOC_ID_OFFSET + 1600),
        LocationData("Ghost of a Chance", "Ghost of a Chance: Terrazine Tank", SC2WOL_LOC_ID_OFFSET + 1601),
        LocationData("Ghost of a Chance", "Ghost of a Chance: Jorium Stockpile", SC2WOL_LOC_ID_OFFSET + 1602),
        LocationData("Ghost of a Chance", "Ghost of a Chance: First Island Spectres", SC2WOL_LOC_ID_OFFSET + 1603),
        LocationData("Ghost of a Chance", "Ghost of a Chance: Second Island Spectres", SC2WOL_LOC_ID_OFFSET + 1604),
        LocationData("Ghost of a Chance", "Ghost of a Chance: Third Island Spectres", SC2WOL_LOC_ID_OFFSET + 1605),
        LocationData("Ghost of a Chance", "Beat Ghost of a Chance", None),
        LocationData("The Great Train Robbery", "The Great Train Robbery: 8 Trains", SC2WOL_LOC_ID_OFFSET + 1700, lambda state: state._sc2wol_has_train_killers(world, player)),
        LocationData("The Great Train Robbery", "The Great Train Robbery: North Defiler", SC2WOL_LOC_ID_OFFSET + 1701),
        LocationData("The Great Train Robbery", "The Great Train Robbery: Mid Defiler", SC2WOL_LOC_ID_OFFSET + 1702),
        LocationData("The Great Train Robbery", "The Great Train Robbery: South Defiler", SC2WOL_LOC_ID_OFFSET + 1703),
        LocationData("The Great Train Robbery", "Beat The Great Train Robbery", None,
                     lambda state: state._sc2wol_has_train_killers(world, player)),
        LocationData("Cutthroat", "Cutthroat: Orlan's Planetary", SC2WOL_LOC_ID_OFFSET + 1800),
        LocationData("Cutthroat", "Cutthroat: Mira Han", SC2WOL_LOC_ID_OFFSET + 1801),
        LocationData("Cutthroat", "Cutthroat: North Relic", SC2WOL_LOC_ID_OFFSET + 1802),
        LocationData("Cutthroat", "Cutthroat: Mid Relic", SC2WOL_LOC_ID_OFFSET + 1803),
        LocationData("Cutthroat", "Cutthroat: Southwest Relic", SC2WOL_LOC_ID_OFFSET + 1804),
        LocationData("Cutthroat", "Beat Cutthroat", None),
        LocationData("Engine of Destruction", "Engine of Destruction: Dominion Bases", SC2WOL_LOC_ID_OFFSET + 1900,
                     lambda state: state._sc2wol_has_mobile_anti_air(world, player)),
        LocationData("Engine of Destruction", "Engine of Destruction: Odin", SC2WOL_LOC_ID_OFFSET + 1901),
        LocationData("Engine of Destruction", "Engine of Destruction: Loki", SC2WOL_LOC_ID_OFFSET + 1902,
                     lambda state: state._sc2wol_has_mobile_anti_air(world, player)),
        LocationData("Engine of Destruction", "Engine of Destruction: Lab Devourer", SC2WOL_LOC_ID_OFFSET + 1903),
        LocationData("Engine of Destruction", "Engine of Destruction: North Devourer", SC2WOL_LOC_ID_OFFSET + 1904,
                     lambda state: state._sc2wol_has_mobile_anti_air(world, player)),
        LocationData("Engine of Destruction", "Engine of Destruction: Southeast Devourer", SC2WOL_LOC_ID_OFFSET + 1905,
                     lambda state: state._sc2wol_has_mobile_anti_air(world, player)),
        LocationData("Engine of Destruction", "Beat Engine of Destruction", None,
                     lambda state: state._sc2wol_has_mobile_anti_air(world, player)),
        LocationData("Media Blitz", "Media Blitz: Full Upload", SC2WOL_LOC_ID_OFFSET + 2000),
        LocationData("Media Blitz", "Media Blitz: Tower 1", SC2WOL_LOC_ID_OFFSET + 2001),
        LocationData("Media Blitz", "Media Blitz: Tower 2", SC2WOL_LOC_ID_OFFSET + 2002),
        LocationData("Media Blitz", "Media Blitz: Tower 3", SC2WOL_LOC_ID_OFFSET + 2003),
        LocationData("Media Blitz", "Media Blitz: Science Facility", SC2WOL_LOC_ID_OFFSET + 2004),
        LocationData("Media Blitz", "Beat Media Blitz", None),
        LocationData("Piercing the Shroud", "Piercing the Shroud: Facility Escape", SC2WOL_LOC_ID_OFFSET + 2100),
        LocationData("Piercing the Shroud", "Piercing the Shroud: Holding Cell Relic", SC2WOL_LOC_ID_OFFSET + 2101),
        LocationData("Piercing the Shroud", "Piercing the Shroud: Brutalisk Relic", SC2WOL_LOC_ID_OFFSET + 2102),
        LocationData("Piercing the Shroud", "Piercing the Shroud: First Escape Relic", SC2WOL_LOC_ID_OFFSET + 2103),
        LocationData("Piercing the Shroud", "Piercing the Shroud: Second Escape Relic", SC2WOL_LOC_ID_OFFSET + 2104),
        LocationData("Piercing the Shroud", "Piercing the Shroud: Brutalisk ", SC2WOL_LOC_ID_OFFSET + 2105),
        LocationData("Piercing the Shroud", "Beat Piercing the Shroud", None),
        LocationData("Whispers of Doom", "Whispers of Doom: Void Seeker Escape", SC2WOL_LOC_ID_OFFSET + 2200),
        LocationData("Whispers of Doom", "Whispers of Doom: First Hatchery", SC2WOL_LOC_ID_OFFSET + 2201),
        LocationData("Whispers of Doom", "Whispers of Doom: Second Hatchery", SC2WOL_LOC_ID_OFFSET + 2202),
        LocationData("Whispers of Doom", "Whispers of Doom: Third Hatchery", SC2WOL_LOC_ID_OFFSET + 2203),
        LocationData("Whispers of Doom", "Beat Whispers of Doom", None),
        LocationData("A Sinister Turn", "A Sinister Turn: Preservers Freed", SC2WOL_LOC_ID_OFFSET + 2300,
                     lambda state: state._sc2wol_has_protoss_medium_units(world, player)),
        LocationData("A Sinister Turn", "A Sinister Turn: Robotics Facility", SC2WOL_LOC_ID_OFFSET + 2301),
        LocationData("A Sinister Turn", "A Sinister Turn: Dark Shrine", SC2WOL_LOC_ID_OFFSET + 2302),
        LocationData("A Sinister Turn", "A Sinister Turn: Templar Archives", SC2WOL_LOC_ID_OFFSET + 2303,
                     lambda state: state._sc2wol_has_protoss_common_units(world, player)),
        LocationData("A Sinister Turn", "Beat A Sinister Turn", None,
                     lambda state: state._sc2wol_has_protoss_medium_units(world, player)),
        LocationData("Echoes of the Future", "Echoes of the Future: Overmind", SC2WOL_LOC_ID_OFFSET + 2400),
        LocationData("Echoes of the Future", "Echoes of the Future: Close Obelisk", SC2WOL_LOC_ID_OFFSET + 2401),
        LocationData("Echoes of the Future", "Echoes of the Future: West Obelisk", SC2WOL_LOC_ID_OFFSET + 2402),
        LocationData("Echoes of the Future", "Beat Echoes of the Future", None),
        LocationData("In Utter Darkness", "In Utter Darkness: Kills", SC2WOL_LOC_ID_OFFSET + 2500),
        LocationData("In Utter Darkness", "In Utter Darkness: Protoss Archive", SC2WOL_LOC_ID_OFFSET + 2501),
        LocationData("In Utter Darkness", "In Utter Darkness: Defeat", SC2WOL_LOC_ID_OFFSET + 2502),
        LocationData("In Utter Darkness", "Beat In Utter Darkness", None),
        LocationData("Gates of Hell", "Gates of Hell: Nydus Worms", SC2WOL_LOC_ID_OFFSET + 2600),
        LocationData("Gates of Hell", "Gates of Hell: Large Army", SC2WOL_LOC_ID_OFFSET + 2601),
        LocationData("Gates of Hell", "Beat Gates of Hell", None),
        LocationData("Belly of the Beast", "Belly of the Beast: Extract", SC2WOL_LOC_ID_OFFSET + 2700),
        LocationData("Belly of the Beast", "Belly of the Beast: First Charge", SC2WOL_LOC_ID_OFFSET + 2701),
        LocationData("Belly of the Beast", "Belly of the Beast: Second Charge", SC2WOL_LOC_ID_OFFSET + 2702),
        LocationData("Belly of the Beast", "Belly of the Beast: Third Charge", SC2WOL_LOC_ID_OFFSET + 2703),
        LocationData("Belly of the Beast", "Beat Belly of the Beast", None),
        LocationData("Shatter the Sky", "Shatter the Sky: Platform Destroyed", SC2WOL_LOC_ID_OFFSET + 2800),
        LocationData("Shatter the Sky", "Shatter the Sky: Close Coolant Tower", SC2WOL_LOC_ID_OFFSET + 2801),
        LocationData("Shatter the Sky", "Shatter the Sky: Northwest Coolant Tower", SC2WOL_LOC_ID_OFFSET + 2802),
        LocationData("Shatter the Sky", "Shatter the Sky: Southeast Coolant Tower", SC2WOL_LOC_ID_OFFSET + 2803),
        LocationData("Shatter the Sky", "Shatter the Sky: Southwest Coolant Tower", SC2WOL_LOC_ID_OFFSET + 2804),
        LocationData("Shatter the Sky", "Shatter the Sky: Leviathan", SC2WOL_LOC_ID_OFFSET + 2805),
        LocationData("Shatter the Sky", "Beat Shatter the Sky", None),
        LocationData("All-In", "All-In: Victory", None)
    ]

    return tuple(location_table)

