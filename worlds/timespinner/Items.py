import typing

class ItemData(typing.NamedTuple):
    category: str
    code: int
    count: int
    progression: bool

# A lot of items arent normally dropped by the randomizer but they can be enabled if desired
item_table: dict[str, ItemData] = {
    'Eternal Crown': ItemData('Enquipment', 1337000, 1, False),
    #'Security Visor': ItemData('Enquipment', 1337001, 1, False),
    #'Engineer Goggles': ItemData('Enquipment', 1337002, 1, False),
    #'Leather Helmet': ItemData('Enquipment', 1337003, 1, False),
    #'Copper Helmet': ItemData('Enquipment', 1337004, 1, False),
    'Pointy Hat': ItemData('Enquipment', 1337005, 1, False),
    #'Dragoon Helmet': ItemData('Enquipment', 1337006, 1, False),
    'Buckle Hat': ItemData('Enquipment', 1337007, 1, False),
    #'Advisor Hat': ItemData('Enquipment', 1337008, 1, False),
    'Librarian Hat': ItemData('Enquipment', 1337009, 1, False),
    #'Combat Helmet': ItemData('Enquipment', 1337010, 1, False),
    'Captain\'s Cap': ItemData('Enquipment', 1337011, 1, False),
    'Lab Glasses': ItemData('Enquipment', 1337012, 1, False),
    'Empire Crown': ItemData('Enquipment', 1337013, 1, False),
    'Viletian Crown': ItemData('Enquipment', 1337014, 1, False),
    #'Sunglasses': ItemData('Enquipment', 1337015, 1, False),
    'Old Coat': ItemData('Enquipment', 1337016, 1, False),
    #'Trendy Jacket': ItemData('Enquipment', 1337017, 1, False),
    #'Security Vest': ItemData('Enquipment', 1337018, 1, False),
    #'Leather Jerkin': ItemData('Enquipment', 1337019, 1, False),
    #'Copper Breastplate': ItemData('Enquipment', 1337020, 1, False),
    'Traveler\'s Cloak': ItemData('Enquipment', 1337021, 1, False),
    #'Dragoon Armor': ItemData('Enquipment', 1337022, 1, False),
    'Midnight Cloak': ItemData('Enquipment', 1337023, 1, False),
    #'Advisor Robe': ItemData('Enquipment', 1337024, 1, False),
    'Librarian Robe': ItemData('Enquipment', 1337025, 1, False),
    #'Military Armor': ItemData('Enquipment', 1337026, 1, False),
    'Captain\'s Uniform': ItemData('Enquipment', 1337027, 1, False),
    'Lab Coat': ItemData('Enquipment', 1337028, 1, False),
    'Empress Robe': ItemData('Enquipment', 1337029, 1, False),
    'Princess Dress': ItemData('Enquipment', 1337030, 1, False),
    'Eternal Coat': ItemData('Enquipment', 1337031, 1, False),
    #'Synthetic Plume': ItemData('Enquipment', 1337032, 1, False),
    #'Cheveur Plume': ItemData('Enquipment', 1337033, 1, False),
    'Metal Wristband': ItemData('Enquipment', 1337034, 1, False),
    #'Nymph Hairband': ItemData('Enquipment', 1337035, 1, False),
    #'Mother o\' Pearl': ItemData('Enquipment', 1337036, 1, False),
    'Bird Statue': ItemData('Enquipment', 1337037, 1, False),
    #'Chaos Stole': ItemData('Enquipment', 1337038, 1, False),
    'Pendulum': ItemData('Enquipment', 1337039, 1, False),
    #'Chaos Horn': ItemData('Enquipment', 1337040, 1, False),
    'Filigree Clasp': ItemData('Enquipment', 1337041, 1, False),
    #'Azure Stole': ItemData('Enquipment', 1337042, 1, False),
    #'Ancient Coin': ItemData('Enquipment', 1337043, 1, False),
    #'Shiny Rock': ItemData('Enquipment', 1337044, 1, False),
    'Galaxy Earrings': ItemData('Enquipment', 1337045, 1, False),
    'Selen\'s Bangle': ItemData('Enquipment', 1337046, 1, False),
    'Glass Pumpkin': ItemData('Enquipment', 1337047, 1, False),
    'Gilded Egg': ItemData('Enquipment', 1337048, 1, False),
    'Meyef': ItemData('Familiar', 1337049, 1, False),
    'Griffin': ItemData('Familiar', 1337050, 1, False),
    'Merchant Crow': ItemData('Familiar', 1337051, 1, False),
    'Kobo': ItemData('Familiar', 1337052, 1, False),
    'Sprite': ItemData('Familiar', 1337053, 1, False),
    'Demon': ItemData('Familiar', 1337054, 1, False),
    'Potion': ItemData('UseItem', 1337055, 1, False),
    'Ether': ItemData('UseItem', 1337056, 1, False),
    'Sand Vial': ItemData('UseItem', 1337057, 1, False),
    'Hi-Potion': ItemData('UseItem', 1337058, 1, False),
    'Hi-Ether': ItemData('UseItem', 1337059, 1, False),
    'Sand Bottle': ItemData('UseItem', 1337060, 1, False),
    'Berry Pick-Mi-Up': ItemData('UseItem', 1337061, 1, False),
    'Berry Pick-Mi-Up+': ItemData('UseItem', 1337062, 1, False),
    'Mind Refresh': ItemData('UseItem', 1337063, 1, False),
    'Mind Refresh ULTRA': ItemData('UseItem', 1337064, 1, False),
    'Antidote': ItemData('UseItem', 1337065, 1, False),
    'Chaos Rose': ItemData('UseItem', 1337066, 1, False),
    'Warp Shard': ItemData('UseItem', 1337067, 1, False),
    #'Dream Wisp': ItemData('UseItem', 1337068, 1, False),
    #'PlaceHolderItem1': ItemData('UseItem', 1337069, 1, False),
    #'Lachiemi Sun': ItemData('UseItem', 1337070, 1, False),
    'Jerky': ItemData('UseItem', 1337071, 1, False),
    #'Biscuit': ItemData('UseItem', 1337072, 1, False),
    #'Fried Cheveur': ItemData('UseItem', 1337073, 1, False),
    #'Sautéed Wyvern Tail': ItemData('UseItem', 1337074, 1, False),
    #'Unagi Roll': ItemData('UseItem', 1337075, 1, False),
    #'Cheveur au Vin': ItemData('UseItem', 1337076, 1, False),
    #'Royal Casserole': ItemData('UseItem', 1337077, 1, False),
    'Spaghetti': ItemData('UseItem', 1337078, 1, False),
    #'Plump Maggot': ItemData('UseItem', 1337079, 1, False),
    #'Orange Juice': ItemData('UseItem', 1337080, 1, False),
    'Filigree Tea': ItemData('UseItem', 1337081, 1, False),
    #'Empress Cake': ItemData('UseItem', 1337082, 1, False),
    #'Rotten Tail': ItemData('UseItem', 1337083, 1, False),
    #'Alchemy Tools': ItemData('UseItem', 1337084, 1, False),
    'Galaxy Stone': ItemData('UseItem', 1337085, 1, False),
    #1337086 Used interally
    #'Essence Crystal': ItemData('UseItem', 1337087, 1, False),
    #'Gold Ring': ItemData('UseItem', 1337088, 1, False),
    #'Gold Necklace': ItemData('UseItem', 1337089, 1, False),
    'Herb': ItemData('UseItem', 1337090, 1, False),
    'Mushroom': ItemData('UseItem', 1337091, 1, False),
    #'Plasma Crystal': ItemData('UseItem', 1337092, 1, False),
    'Plasma IV Bag': ItemData('UseItem', 1337093, 1, False),
    #'Cheveur Drumstick': ItemData('UseItem', 1337094, 1, False),
    #'Wyvern Tail': ItemData('UseItem', 1337095, 1, False),
    #'Eel Meat': ItemData('UseItem', 1337096, 1, False),
    #'Cheveux Breast': ItemData('UseItem', 1337097, 1, False),
    'Food Synthesizer': ItemData('UseItem', 1337098, 1, False),
    'Cheveux Feather': ItemData('UseItem', 1337099, 1, False),
    'Siren Ink': ItemData('UseItem', 1337100, 1, False),
    'Plasma Core': ItemData('UseItem', 1337101, 1, False),
    #'Silver Ore': ItemData('UseItem', 1337102, 1, False),
    #'Historical Documents': ItemData('UseItem', 1337103, 1, False),
    #'MapReveal 0': ItemData('UseItem', 1337104, 1, False),
    #'MapReveal 1': ItemData('UseItem', 1337105, 1, False),
    #'MapReveal 2': ItemData('UseItem', 1337106, 1, False),
    'Timespinner Wheel': ItemData('Relic', 1337107, 1, True),
    'Timespinner Spindle': ItemData('Relic', 1337108, 1, True),
    'Timespinner Gear 1': ItemData('Relic', 1337109, 1, True),
    'Timespinner Gear 2': ItemData('Relic', 1337110, 1, True),
    'Timespinner Gear 3': ItemData('Relic', 1337111, 1, True),
    'Twin Pyramid Key': ItemData('Relic', 1337112, 1, True),
    'Celestial Sash': ItemData('Relic', 1337113, 1, True),
    'Succubus Hairpin': ItemData('Relic', 1337114, 1, True),
    'Talaria Attachment': ItemData('Relic', 1337115, 1, True),
    'Water Mask': ItemData('Relic', 1337116, 1, True),
    'Gas Mask': ItemData('Relic', 1337117, 1, True),
    'Soul Scanner': ItemData('Relic', 1337118, 1, False),
    'Security Keycard A': ItemData('Relic', 1337119, 1, True),
    'Security Keycard B': ItemData('Relic', 1337120, 1, True),
    'Security Keycard C': ItemData('Relic', 1337121, 1, True),
    'Security Keycard D': ItemData('Relic', 1337122, 1, True),
    'Library Keycard V': ItemData('Relic', 1337123, 1, True),
    'Tablet': ItemData('Relic', 1337124, 1, True),
    'Elevator Keycard': ItemData('Relic', 1337125, 1, True),
    'Jewelry Box': ItemData('Relic', 1337126, 1, False),
    'Goddess Brooch': ItemData('Relic', 1337127, 1, False),
    'Wyrm Brooch': ItemData('Relic', 1337128, 1, False), 	
    'Greed Brooch': ItemData('Relic', 1337129, 1, False),
    'Eternal Brooch': ItemData('Relic', 1337130, 1, False),
    'Blue Orb': ItemData('Orb Melee', 1337131, 1, False),
    'Blade Orb': ItemData('Orb Melee', 1337132, 1, False),
    'Fire Orb': ItemData('Orb Melee', 1337133, 1, True),
    'Plasma Orb': ItemData('Orb Melee', 1337134, 1, True),
    'Iron Orb': ItemData('Orb Melee', 1337135, 1, False),
    'Ice Orb': ItemData('Orb Melee', 1337136, 1, False),
    'Wind Orb': ItemData('Orb Melee', 1337137, 1, False),
    'Gun Orb': ItemData('Orb Melee', 1337138, 1, False),
    'Umbra Orb': ItemData('Orb Melee', 1337139, 1, False),
    'Empire Orb': ItemData('Orb Melee', 1337140, 1, False),
    'Eye Orb': ItemData('Orb Melee', 1337141, 1, False),
    'Blood Orb': ItemData('Orb Melee', 1337142, 1, False),
    'Forbidden Tome': ItemData('Orb Melee', 1337143, 1, False),
    'Shattered Orb': ItemData('Orb Melee', 1337144, 1, False),
    'Nether Orb': ItemData('Orb Melee', 1337145, 1, False),
    'Radiant Orb': ItemData('Orb Melee', 1337146, 1, False),
    'Aura Blast': ItemData('Orb Spell', 1337147, 1, False),
    'Colossal Blade': ItemData('Orb Spell', 1337148, 1, False),
    'Infernal Flames': ItemData('Orb Spell', 1337149, 1, True),
    'Plasma Geyser': ItemData('Orb Spell', 1337150, 1, True),
    'Colossal Hammer': ItemData('Orb Spell', 1337151, 1, False),
    'Frozen Spires': ItemData('Orb Spell', 1337152, 1, False),
    'Storm Eye': ItemData('Orb Spell', 1337153, 1, False),
    'Arm Cannon': ItemData('Orb Spell', 1337154, 1, False),
    'Dark Flames': ItemData('Orb Spell', 1337155, 1, False),
    'Aura Serpent': ItemData('Orb Spell', 1337156, 1, False),
    'Chaos Blades': ItemData('Orb Spell', 1337157, 1, False),
    'Crimson Vortex': ItemData('Orb Spell', 1337158, 1, False),
    'Djinn Inferno': ItemData('Orb Spell', 1337159, 1, True),
    'Bombardment': ItemData('Orb Spell', 1337160, 1, False),
    'Corruption': ItemData('Orb Spell', 1337161, 1, False),
    'Lightwall': ItemData('Orb Spell', 1337162, 1, True),
    'Bleak Ring': ItemData('Orb Passive', 1337163, 1, False),
    'Scythe Ring': ItemData('Orb Passive', 1337164, 1, False),
    'Pyro Ring': ItemData('Orb Passive', 1337165, 1, True),
    'Royal Ring': ItemData('Orb Passive', 1337166, 1, True),
    'Shield Ring': ItemData('Orb Passive', 1337167, 1, False),
    'Icicle Ring': ItemData('Orb Passive', 1337168, 1, False),
    'Tailwind Ring': ItemData('Orb Passive', 1337169, 1, False),
    'Economizer Ring': ItemData('Orb Passive', 1337170, 1, False),
    'Dusk Ring': ItemData('Orb Passive', 1337171, 1, False),
    'Star of Lachiem': ItemData('Orb Passive', 1337172, 1, False),
    'Oculus Ring': ItemData('Orb Passive', 1337173, 1, True),
    'Sanguine Ring': ItemData('Orb Passive', 1337174, 1, False),
    'Sun Ring': ItemData('Orb Passive', 1337175, 1, False),
    'Silence Ring': ItemData('Orb Passive', 1337176, 1, False),
    'Shadow Seal': ItemData('Orb Passive', 1337177, 1, False),
    'Hope Ring': ItemData('Orb Passive', 1337178, 1, False),
    'Max HP': ItemData('Stat', 1337179, 12, False),
    'Max Aura': ItemData('Stat', 1337180, 13, False),
    # 1337181 - 1337248 Reserved
    'MaxSand': ItemData('Stat', 1337249, 14, False)
}

starter_melee_weapons = [
    'Blue Orb',
    'Blade Orb',
    'Fire Orb',
    'Iron Orb',
    'Ice Orb',
    'Wind Orb',
    'Gun Orb',
    'Umbra Orb',
    'Empire Orb',
    'Eye Orb',
    'Blood Orb',
    'Forbidden Tome',
    'Shattered Orb',
    'Nether Orb',
    'Radiant Orb'
]

starter_spells = [
    'Colossal Blade',
    'Infernal Flames',
    'Plasma Geyser',
    'Colossal Hammer',
    'Frozen Spires',
    'Storm Eye',
    'Arm Cannon',
    'Dark Flames',
    'Aura Serpent',
    'Chaos Blades',
    'Crimson Vortex',
    'Djinn Inferno',
    'Bombardment',
    'Corruption'
]

# weighted
starter_progression_items = [
    'Talaria Attachment',
    'Talaria Attachment',
    'Succubus Hairpin',
    'Succubus Hairpin',
    'Timespinner Wheel',
    'Timespinner Wheel',
    'Twin Pyramid Key',
    'Celestial Sash',
    'Lightwall'
]

filler_items = [
    'Potion',
    'Ether',
    'Hi-Potion',
    'Hi-Ether',
    'Sand Vial',
    'Sand Bottle',
    'Berry Pick-Mi-Up',
    'Berry Pick-Mi-Up+',
    'Mind Refresh',
    'Mind Refresh ULTRA',
    'Antidote',
    'Chaos Rose'
]