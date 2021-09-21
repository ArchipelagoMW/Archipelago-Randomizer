import typing

from BaseClasses import MultiWorld
from .Options import is_option_enabled

class LocationData(typing.NamedTuple):
    region: str
    code: int
    rule: typing.Callable = lambda state: True

def get_location_table(world: MultiWorld, player: int):
    location_table: typing.Dict[str, LocationData] = {
        # PresentItemLocations
        'Yo Momma 1': LocationData('Tutorial', 1337000),
        'Yo Momma 2': LocationData('Tutorial', 1337001),
        'Starter chest 2': LocationData('Lake desolation' , 1337002),
        'Starter chest 3': LocationData('Lake desolation' , 1337003),
        'Starter chest 1': LocationData('Lake desolation' , 1337004),
        'Timespinner Wheel room': LocationData('Lake desolation' , 1337005),
        'Forget me not chest': LocationData('Upper lake desolation' , 1337006),
        'Chicken chest': LocationData('Lower lake desolation' , 1337007, lambda state: state._timespinner_has_timestop(world, player)),
        'Not so secret room': LocationData('Lower lake desolation' , 1337008, lambda state: state._timespinner_can_break_walls(world, player)),
        'Tank chest': LocationData('Lower lake desolation' , 1337009, lambda state: state._timespinner_has_timestop(world, player)),
        'Oxygen recovery room': LocationData('Upper lake desolation' , 1337010),
        'Lake secret': LocationData('Upper lake desolation' , 1337011, lambda state: state._timespinner_can_break_walls(world, player)),
        'Double jump cave floor': LocationData('Upper lake desolation' , 1337012, lambda state: state._timespinner_has_doublejump(world, player)),
        'Double jump cave platform': LocationData('Upper lake desolation' , 1337013),
        'Fire-Locked sparrow chest': LocationData('Upper lake desolation' , 1337014),
        'Crash site pedestal': LocationData('Upper lake desolation' , 1337015), # vvv TODO change into event vvv
        'Crash site chest 1': LocationData('Upper lake desolation' , 1337016, lambda state: state.can_reach('Caves of Banishment (Maw)', 'Region', player) and state.has('Gas Mask', player)),
        'Crash site chest 2': LocationData('Upper lake desolation' , 1337017, lambda state: state.can_reach('Caves of Banishment (Maw)', 'Region', player) and state.has('Gas Mask', player)),
        'Kitty Boss': LocationData('Upper lake desolation' , 1337018),
        'Basement': LocationData('Libary' , 1337019),
        'Consolation': LocationData('Libary' , 1337020),
        'Librarian': LocationData('Libary' , 1337021),
        'Reading nook chest': LocationData('Libary' , 1337022),
        'Storage room chest 1': LocationData('Libary' , 1337023, lambda state: state._timespinner_has_keycard_D(world, player)),
        'Storage room chest 2': LocationData('Libary' , 1337024, lambda state: state._timespinner_has_keycard_D(world, player)),
        'Storage room chest 3': LocationData('Libary' , 1337025, lambda state: state._timespinner_has_keycard_D(world, player)),
        'Backer room chest 5': LocationData('Libary top' , 1337026),
        'Backer room chest 4': LocationData('Libary top' , 1337027),
        'Backer room chest 3': LocationData('Libary top' , 1337028),
        'Backer room chest 2': LocationData('Libary top' , 1337029),
        'Backer room chest 1': LocationData('Libary top' , 1337030),
        'Elevator Key not required': LocationData('Varndagroth tower left' , 1337031),
        'Ye olde Timespinner': LocationData('Varndagroth tower left' , 1337032),
        'C Keycard chest': LocationData('Varndagroth tower left' , 1337033, lambda state: state._timespinner_has_keycard_C(world, player)),
        'Left air vents secret': LocationData('Varndagroth tower left' , 1337034, lambda state: state._timespinner_can_break_walls(world, player)),
        'Left elevator chest': LocationData('Varndagroth tower left' , 1337035, lambda state: state.has('Elevator Keycard', player)),
        'Spider heck room': LocationData('Varndagroth tower right (upper)' , 1337036),
        'Right elevator chest': LocationData('Varndagroth tower right (elevator)' , 1337037),
        'Elevator card chest': LocationData('Varndagroth tower right (upper)' , 1337038, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        'Air vents left': LocationData('Varndagroth tower right (upper)' , 1337039, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        'Air Vents right': LocationData('Varndagroth tower right (upper)' , 1337040, lambda state: state.has('Elevator Keycard', player) or state._timespinner_has_doublejump(world, player)),
        'Right side bottom floor': LocationData('Varndagroth tower right (lower)' , 1337041),
        'Varndagroth' : LocationData('Varndagroth tower right (elevator)' , 1337042, lambda state: state._timespinner_has_keycard_C(world, player)),
        'Varndagroth Spider hell': LocationData('Varndagroth tower right (elevator)' , 1337043, lambda state: state._timespinner_has_keycard_A(world, player)),
        'Skeleton': LocationData('Lake desolation' , 1337044, lambda state: state._timespinner_has_doublejump(world, player)), # region changed from 'Sealed Caves (Xarion)' to ease entrance logic
        'Shroom jump room': LocationData('Sealed Caves (Xarion)' , 1337045, lambda state: state._timespinner_has_timestop(world, player)),
        'Double shroom room': LocationData('Sealed Caves (Xarion)' , 1337046),
        'Mini jackpot room': LocationData('Sealed Caves (Xarion)' , 1337047, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        'Below mini jackpot room': LocationData('Sealed Caves (Xarion)' , 1337048),
        'Sealed cave secret room': LocationData('Sealed Caves (Xarion)' , 1337049, lambda state: state._timespinner_can_break_walls(world, player)),
        'Below Sealed cave secret': LocationData('Sealed Caves (Xarion)' , 1337050),
        'Last chance before Xarion': LocationData('Sealed Caves (Xarion)' , 1337051, lambda state: state._timespinner_has_doublejump(world, player)),
        'Xarion': LocationData('Sealed Caves (Xarion)' , 1337052),
        'Solo siren chest': LocationData('Sealed Caves (Sirens)' , 1337053, lambda state: state.has('Water Mask', player)),
        'Big siren room right': LocationData('Sealed Caves (Sirens)' , 1337054, lambda state: state.has('Water Mask', player)),
        'Big siren Room left': LocationData('Sealed Caves (Sirens)' , 1337055, lambda state: state.has('Water Mask', player)),
        'Room after sirens chest 2': LocationData('Sealed Caves (Sirens)' , 1337056),
        'Room after sirens chest 1': LocationData('Sealed Caves (Sirens)' , 1337057),
        'Militairy Bomber chest': LocationData('Militairy Fortress' , 1337058, lambda state: state.has('Timespinner Wheel', player) and state._timespinner_has_doublejump_of_npc(world, player)),
        'Close combat room': LocationData('Militairy Fortress' , 1337059),
        'Bridge full of soldiers': LocationData('Militairy Fortress' , 1337060),
        'Giantess Room': LocationData('Militairy Fortress' , 1337061),
        'Bridge with Giantess': LocationData('Militairy Fortress' , 1337062),
        'Military B door chest 2': LocationData('Militairy Fortress' , 1337063, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_has_keycard_B(world, player)),
        'Military B door chest 1': LocationData('Militairy Fortress' , 1337064, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_has_keycard_B(world, player)),
        'Military pedestal': LocationData('Militairy Fortress' , 1337065, lambda state: state._timespinner_has_doublejump(world, player) and (state._timespinner_has_doublejump_of_npc(world, player) or state._timespinner_has_forwarddash_doublejump(world, player))),
        'Coffee Break chest': LocationData('The lab' , 1337066),
        'Lower trash right': LocationData('The lab' , 1337067, lambda state: state._timespinner_has_doublejump(world, player)),
        'Lower trash left': LocationData('The lab' , 1337068, lambda state: state._timespinner_has_upwarddash(world, player)),
        'Single turret room': LocationData('The lab' , 1337069, lambda state: state._timespinner_has_doublejump(world, player)),
        'Trash jump room': LocationData('The lab (power off)' , 1337070),
        'Dynamo Works': LocationData('The lab (power off)' , 1337071),
        'Blob mom': LocationData('The lab (upper)' , 1337072),
        'Experiment #13': LocationData('The lab (power off)' , 1337073),
        'Download and chest room': LocationData('The lab (upper)' , 1337074),
        'Lab secret': LocationData('The lab (upper)' , 1337075, lambda state: state._timespinner_can_break_walls(world, player)),
        'Lab Spider hell': LocationData('The lab (power off)' , 1337076, lambda state: state._timespinner_has_keycard_A(world, player)),
        'Bottom': LocationData('Emperors tower' , 1337077),
        'After Courtyard Floor Secret': LocationData('Emperors tower' , 1337078, lambda state: state._timespinner_has_upwarddash(world, player) and state._timespinner_can_break_walls(world, player)),
        'After Courtyard Chest': LocationData('Emperors tower' , 1337079, lambda state: state._timespinner_has_upwarddash(world, player)),
        'Galactic Sage Room': LocationData('Emperors tower' , 1337080),
        'Bottom of Right Tower': LocationData('Emperors tower' , 1337081),
        'Wayyyy up there': LocationData('Emperors tower' , 1337082),
        'Left tower balcony': LocationData('Emperors tower' , 1337083),
        'Dad\'s Chambers chest': LocationData('Emperors tower' , 1337084),
        'Dad\'s Chambers pedestal': LocationData('Emperors tower' , 1337085),

        # PastItemLocations
        'Neliste\'s Bra': LocationData('Refugee Camp' , 1337086),
        'Refugee camp storage chest 3': LocationData('Refugee Camp' , 1337087),
        'Refugee camp storage chest 2': LocationData('Refugee Camp' , 1337088),
        'Refugee camp storage chest 1': LocationData('Refugee Camp' , 1337089),
        'Refugee camp roof': LocationData('Forest' , 1337090),
        'Bat jump chest': LocationData('Forest' , 1337091, lambda state: state._timespinner_has_doublejump_of_npc(world, player) or state._timespinner_has_forwarddash_doublejump(world, player)),
        'Green platform secret': LocationData('Forest' , 1337092, lambda state: state._timespinner_can_break_walls(world, player)),
        'Rats guarded chest': LocationData('Forest' , 1337093),
        'Waterfall chest 1': LocationData('Forest' , 1337094, lambda state: state.has('Water Mask', player)),
        'Waterfall chest 2': LocationData('Forest' , 1337095, lambda state: state.has('Water Mask', player)),
        'Batcave': LocationData('Forest' , 1337096),
        'Bridge Chest': LocationData('Forest' , 1337097),
        'Solitary bat room': LocationData('Left Side forest Caves' , 1337098),
        'Rat nest': LocationData('Upper Lake Sirine' , 1337099),
        'Double jump cave platform (past)': LocationData('Upper Lake Sirine' , 1337100, lambda state: state._timespinner_has_doublejump(world, player)),
        'Double jump cave floor (past)': LocationData('Upper Lake Sirine' , 1337101),
        'West lake serene cave secret': LocationData('Upper Lake Sirine' , 1337102, lambda state: state._timespinner_can_break_walls(world, player)),
        'Chest behind vines': LocationData('Upper Lake Sirine' , 1337103),
        'Pyramid keys room': LocationData('Upper Lake Sirine' , 1337104),
        'Deep dive': LocationData('Upper Lake Sirine' , 1337105),
        'Under the eels': LocationData('Upper Lake Sirine' , 1337106),
        'Water spikes room': LocationData('Upper Lake Sirine' , 1337107),
        'Underwater secret': LocationData('Upper Lake Sirine' , 1337108, lambda state: state._timespinner_can_break_walls(world, player)),
        'T chest': LocationData('Upper Lake Sirine' , 1337109),
        'Past the eels': LocationData('Upper Lake Sirine' , 1337110),
        'Underwater pedestal': LocationData('Upper Lake Sirine' , 1337111),
        'Mushroom double jump': LocationData('Caves of Banishment (Maw)' , 1337112, lambda state: state._timespinner_has_doublejump(world, player)),
        'Caves of banishment secret room': LocationData('Caves of Banishment (Maw)' , 1337113),
        'Below caves of banishment secret': LocationData('Caves of Banishment (Maw)' , 1337114),
        'Single shroom room': LocationData('Caves of Banishment (Maw)' , 1337115),
        'Jackpot room chest 1': LocationData('Caves of Banishment (Maw)' , 1337116, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        'Jackpot room chest 2': LocationData('Caves of Banishment (Maw)' , 1337117, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        'Jackpot room chest 3': LocationData('Caves of Banishment (Maw)' , 1337118, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        'Jackpot room chest 4': LocationData('Caves of Banishment (Maw)' , 1337119, lambda state: state._timespinner_has_forwarddash_doublejump(world, player)),
        'Banishment pedestal': LocationData('Caves of Banishment (Maw)' , 1337120),
        'Last chance before Maw': LocationData('Caves of Banishment (Maw)' , 1337121, lambda state: state._timespinner_has_doublejump(world, player)),
        'Mineshaft': LocationData('Caves of Banishment (Maw)' , 1337122, lambda state: state.has('Gas Mask', player)),
        'Wyvern room': LocationData('Caves of Banishment (Sirens)' , 1337123),
        'Above water sirens': LocationData('Caves of Banishment (Sirens)' , 1337124),
        'Underwater sirens left': LocationData('Caves of Banishment (Sirens)' , 1337125, lambda state: state.has('Water Mask', player)),
        'Underwater sirens right': LocationData('Caves of Banishment (Sirens)' , 1337126, lambda state: state.has('Water Mask', player)),
        'Water hook': LocationData('Caves of Banishment (Sirens)' , 1337127),
        'Caste Bomber chest': LocationData('Caste Ramparts' , 1337128, lambda state: state._timespinner_has_multiple_small_jumps_of_npc(world, player)),
        'Freeze the engineer': LocationData('Caste Ramparts' , 1337129, lambda state: state.has('Talaria Attachment', player) or state._timespinner_has_timestop(world, player)),
        'Giantess guarded room': LocationData('Caste Ramparts' , 1337130),
        'Knight and archer guarded room': LocationData('Caste Ramparts' , 1337131),
        'Castle pedestal': LocationData('Caste Ramparts' , 1337132),
        'Basement secret pedestal': LocationData('Caste Keep' , 1337133, lambda state: state._timespinner_can_break_walls(world, player)),
        'Break the wall': LocationData('Caste Keep' , 1337134),
        'Yas queen room': LocationData('Royal towers (lower)' , 1337135, lambda state: state._timespinner_has_pink(world, player)),
        'Basement hammer': LocationData('Caste Keep' , 1337136),
        'Omelette chest': LocationData('Caste Keep' , 1337137),
        'Just an egg': LocationData('Caste Keep' , 1337138),
        'Out of the way': LocationData('Caste Keep' , 1337139),
        'Twins': LocationData('Caste Keep' , 1337140, lambda state: state._timespinner_has_timestop(world, player)),
        'Royal guard tiny room': LocationData('Caste Keep' , 1337141, lambda state: state._timespinner_has_doublejump(world, player)),
        'Royal tower floor secret': LocationData('Royal towers (lower)' , 1337142, lambda state: state._timespinner_has_doublejump(world, player) and state._timespinner_can_break_walls(world, player)),
        'Above the gap': LocationData('Royal towers' , 1337143),
        'Under the ice mage': LocationData('Royal towers' , 1337144),
        'Next to easy struggle juggle room': LocationData('Royal towers (upper)' , 1337145),
        'Easy struggle juggle': LocationData('Royal towers (upper)' , 1337146, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        'Hard struggle juggle': LocationData('Royal towers (upper)' , 1337147, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        'No sturggle required': LocationData('Royal towers (upper)' , 1337148, lambda state: state._timespinner_has_doublejump_of_npc(world, player)),
        'Right tower freebie': LocationData('Royal towers' , 1337149),
        'Above the cide mage': LocationData('Royal towers (upper)' , 1337150),
        'Royal guard big room': LocationData('Royal towers (upper)' , 1337151),
        'Before Aelana': LocationData('Royal towers (upper)' , 1337152),
        'Statue room': LocationData('Royal towers (upper)' , 1337153, lambda state: state._timespinner_has_upwarddash(world, player)),
        'Aelana\'s pedestal': LocationData('Royal towers (upper)' , 1337154),
        'After Aelana': LocationData('Royal towers (upper)' , 1337155),

        # 1337157 - 1337170 Downloads

        # 1337171 - 1337238 Reserved

        # PyramidItemLocations
        #'Transition chest 1': LocationData('Temporal Gyre' , 1337239),
        #'Transition chest 2': LocationData('Temporal Gyre' , 1337240),
        #'Transition chest 3': LocationData('Temporal Gyre' , 1337241),
        #'Ravenlord pre fight': LocationData('Temporal Gyre' , 1337242),
        #'Ravenlord post fight': LocationData('Temporal Gyre' , 1337243),
        #'Ifrid pre fight': LocationData('Temporal Gyre' , 1337244),
        #'Ifrid post fight': LocationData('Temporal Gyre' , 1337245),
        'Why not it\'s right there': LocationData('Ancient Pyramid (left)' , 1337246),
        'Conviction guarded room': LocationData('Ancient Pyramid (left)' , 1337247),
        'Pit secret room': LocationData('Ancient Pyramid (right)' , 1337248, lambda state: state._timespinner_can_break_walls(world, player)),
        'Regret chest': LocationData('Ancient Pyramid (right)' , 1337249, lambda state: state._timespinner_can_break_walls(world, player))
    }

    downloadable_items: typing.Dict[str, LocationData] = {
        # DownloadTerminals
        'Library terminal 1': LocationData('Libary' , 1337157, lambda state: state.has('Tablet', player)),
        'Library terminal 2': LocationData('Libary' , 1337156, lambda state: state.has('Tablet', player)),
        'Library terminal 3' : LocationData('Libary' , 1337159, lambda state: state.has('Tablet', player)),
        'V terminal 1': LocationData('Libary' , 1337160, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        'V terminal 2': LocationData('Libary' , 1337161, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        'V terminal 3': LocationData('Libary' , 1337162, lambda state: state.has_all(['Tablet', 'Library Keycard V'], player)),
        'Backer room terminal': LocationData('Libary top' , 1337163, lambda state: state.has('Tablet', player)),
        'Medbay': LocationData('Varndagroth tower right (elevator)' , 1337164, lambda state: state.has('Tablet', player) and state._timespinner_has_keycard_B(world, player)),
        'Chest and download terminal': LocationData('The lab (upper)' , 1337165, lambda state: state.has('Tablet', player)),
        'Lab terminal middle': LocationData('The lab (power off)', 1337166, lambda state: state.has('Tablet', player)),
        'Sentry platform terminal': LocationData('The lab (power off)' , 1337167, lambda state: state.has('Tablet', player)),
        'Experiment 13 terminal': LocationData('The lab' , 1337168, lambda state: state.has('Tablet', player)),
        'Lab terminal left': LocationData('The lab' , 1337169, lambda state: state.has('Tablet', player)),
        'Lab terminal right': LocationData('The lab (power off)' , 1337170, lambda state: state.has('Tablet', player))
    }

    if is_option_enabled(world, player, "DownloadableItems"):
        return { **location_table, **downloadable_items }
    else:
        return location_table

starter_progression_locations = [
    'Starter chest 2',
    'Starter chest 3',
    'Starter chest 1',
    'Timespinner Wheel room'
]

events = [
    "Killed Nightmare"
]