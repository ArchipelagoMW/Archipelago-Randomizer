from BaseClasses import ItemClassification
from .poke_data import pokemon_data
filler_items = []

class ItemData:
    def __init__(self, id, classification):
        self.classification = classification
        self.id = None if id is None else id + 172000000

item_table = {
    "Master Ball": ItemData(1, ItemClassification.useful),
    "Ultra Ball": ItemData(2, ItemClassification.filler),
    "Great Ball": ItemData(3, ItemClassification.filler),
    "Poke Ball": ItemData(4, ItemClassification.filler),
    "Town Map": ItemData(5, ItemClassification.progression_skip_balancing),
    "Bicycle": ItemData(6, ItemClassification.progression),
    "Flippers": ItemData(7, ItemClassification.progression),
    "Safari Ball": ItemData(8, ItemClassification.filler),
    "Pokedex": ItemData(9, ItemClassification.filler),
    "Moon Stone": ItemData(10, ItemClassification.useful),
    "Antidote": ItemData(11, ItemClassification.filler),
    "Burn Heal": ItemData(12, ItemClassification.filler),
    "Ice Heal": ItemData(13, ItemClassification.filler),
    "Awakening": ItemData(14, ItemClassification.filler),
    "Paralyze Heal": ItemData(15, ItemClassification.filler),
    "Full Restore": ItemData(16, ItemClassification.filler),
    "Max Potion": ItemData(17, ItemClassification.filler),
    "Hyper Potion": ItemData(18, ItemClassification.filler),
    "Super Potion": ItemData(19, ItemClassification.filler),
    "Potion": ItemData(20, ItemClassification.filler),
    "Boulder Badge": ItemData(21, ItemClassification.progression),
    "Cascade Badge": ItemData(22, ItemClassification.progression),
    "Thunder Badge": ItemData(23, ItemClassification.progression),
    "Rainbow Badge": ItemData(24, ItemClassification.progression),
    "Soul Badge": ItemData(25, ItemClassification.progression),
    "Marsh Badge": ItemData(26, ItemClassification.progression),
    "Volcano Badge": ItemData(27, ItemClassification.progression),
    "Earth Badge": ItemData(28, ItemClassification.progression),
    "Escape Rope": ItemData(29, ItemClassification.filler),
    "Repel": ItemData(30, ItemClassification.filler),
    "Old Amber": ItemData(31, ItemClassification.useful),
    "Fire Stone": ItemData(32, ItemClassification.useful),
    "Thunder Stone": ItemData(33, ItemClassification.useful),
    "Water Stone": ItemData(34, ItemClassification.useful),
    "HP Up": ItemData(35, ItemClassification.filler),
    "Protein": ItemData(36, ItemClassification.filler),
    "Iron": ItemData(37, ItemClassification.filler),
    "Carbos": ItemData(38, ItemClassification.filler),
    "Calcium": ItemData(39, ItemClassification.filler),
    "Rare Candy": ItemData(40, ItemClassification.useful),
    "Dome Fossil": ItemData(41, ItemClassification.useful),
    "Helix Fossil": ItemData(42, ItemClassification.useful),
    "Secret Key": ItemData(43, ItemClassification.progression),
    "Bike Voucher": ItemData(45, ItemClassification.progression),
    "X Accuracy": ItemData(46, ItemClassification.filler),
    "Leaf Stone": ItemData(47, ItemClassification.useful),
    "Card Key": ItemData(48, ItemClassification.progression),
    "Nugget": ItemData(49, ItemClassification.filler),
    "Laptop": ItemData(50, ItemClassification.useful),
    "Poke Doll": ItemData(51, ItemClassification.filler),
    "Full Heal": ItemData(52, ItemClassification.filler),
    "Revive": ItemData(53, ItemClassification.filler),
    "Max Revive": ItemData(54, ItemClassification.filler),
    "Guard Spec": ItemData(55, ItemClassification.filler),
    "Super Repel": ItemData(56, ItemClassification.filler),
    "Max Repel": ItemData(57, ItemClassification.filler),
    "Dire Hit": ItemData(58, ItemClassification.filler),
    "Coin": ItemData(59, ItemClassification.filler),
    "Fresh Water": ItemData(60, ItemClassification.filler),
    "Soda Pop": ItemData(61, ItemClassification.filler),
    "Lemonade": ItemData(62, ItemClassification.filler),
    "S.S. Ticket": ItemData(63, ItemClassification.progression),
    "Gold Teeth": ItemData(64, ItemClassification.progression),
    "X Attack": ItemData(65, ItemClassification.filler),
    "X Defend": ItemData(66, ItemClassification.filler),
    "X Speed": ItemData(67, ItemClassification.filler),
    "X Special": ItemData(68, ItemClassification.filler),
    "Coin Case": ItemData(69, ItemClassification.progression_skip_balancing), ###
    "Oak's Parcel": ItemData(70, ItemClassification.progression),
    "Item Finder": ItemData(71, ItemClassification.progression),
    "Silph Scope": ItemData(72, ItemClassification.progression),
    "Poke Flute": ItemData(73, ItemClassification.progression),
    "Lift Key": ItemData(74, ItemClassification.progression),
    "Exp. All": ItemData(75, ItemClassification.useful),
    "Old Rod": ItemData(76, ItemClassification.progression_skip_balancing),
    "Good Rod": ItemData(77, ItemClassification.progression_skip_balancing),
    "Super Rod": ItemData(78, ItemClassification.progression_skip_balancing),
    "PP Up": ItemData(79, ItemClassification.filler),
    "Ether": ItemData(80, ItemClassification.filler),
    "Max Ether": ItemData(81, ItemClassification.filler),
    "Elixir": ItemData(82, ItemClassification.filler),
    "Max Elixir": ItemData(83, ItemClassification.filler),
    "Tea": ItemData(84, ItemClassification.progression),
    "Master Sword": ItemData(85, ItemClassification.progression),
    "Flute": ItemData(86, ItemClassification.progression),
    "Titan's Mitt": ItemData(87, ItemClassification.progression),
    "Lamp": ItemData(88, ItemClassification.progression),
    "Plant Key": ItemData(89, ItemClassification.progression),
    "Mansion Key": ItemData(90, ItemClassification.progression),
    "Hideout Key": ItemData(91, ItemClassification.progression),
    "Unknown Pass": ItemData(92, ItemClassification.progression),
    "Safari Pass": ItemData(93, ItemClassification.progression),
    "HM01 Cut": ItemData(196, ItemClassification.progression),
    "HM02 Fly": ItemData(197, ItemClassification.progression),
    "HM03 Surf": ItemData(198, ItemClassification.progression),
    "HM04 Strength": ItemData(199, ItemClassification.progression),
    "HM05 Flash": ItemData(200, ItemClassification.progression),
    "TM01 Mega Punch": ItemData(201, ItemClassification.useful),
    "TM02 Razor Wind": ItemData(202, ItemClassification.useful),
    "TM03 Swords Dance": ItemData(203, ItemClassification.useful),
    "TM04 Whirlwind": ItemData(204, ItemClassification.useful),
    "TM05 Mega Kick": ItemData(205, ItemClassification.useful),
    "TM06 Toxic": ItemData(206, ItemClassification.useful),
    "TM07 Horn Drill": ItemData(207, ItemClassification.useful),
    "TM08 Body Slam": ItemData(208, ItemClassification.useful),
    "TM09 Take Down": ItemData(209, ItemClassification.useful),
    "TM10 Double Edge": ItemData(210, ItemClassification.useful),
    "TM11 Bubble Beam": ItemData(211, ItemClassification.useful),
    "TM12 Water Gun": ItemData(212, ItemClassification.useful),
    "TM13 Ice Beam": ItemData(213, ItemClassification.useful),
    "TM14 Blizzard": ItemData(214, ItemClassification.useful),
    "TM15 Hyper Beam": ItemData(215, ItemClassification.useful),
    "TM16 Pay Day": ItemData(216, ItemClassification.useful),
    "TM17 Submission": ItemData(217, ItemClassification.useful),
    "TM18 Counter": ItemData(218, ItemClassification.useful),
    "TM19 Seismic Toss": ItemData(219, ItemClassification.useful),
    "TM20 Rage": ItemData(220, ItemClassification.useful),
    "TM21 Mega Drain": ItemData(221, ItemClassification.useful),
    "TM22 Solar Beam": ItemData(222, ItemClassification.useful),
    "TM23 Dragon Rage": ItemData(223, ItemClassification.useful),
    "TM24 Thunderbolt": ItemData(224, ItemClassification.useful),
    "TM25 Thunder": ItemData(225, ItemClassification.useful),
    "TM26 Earthquake": ItemData(226, ItemClassification.useful),
    "TM27 Fissure": ItemData(227, ItemClassification.useful),
    "TM28 Dig": ItemData(228, ItemClassification.useful),
    "TM29 Psychic": ItemData(229, ItemClassification.useful),
    "TM30 Teleport": ItemData(230, ItemClassification.useful),
    "TM31 Mimic": ItemData(231, ItemClassification.useful),
    "TM32 Double Team": ItemData(232, ItemClassification.useful),
    "TM33 Reflect": ItemData(233, ItemClassification.useful),
    "TM34 Bide": ItemData(234, ItemClassification.useful),
    "TM35 Metronome": ItemData(235, ItemClassification.useful),
    "TM36 Self Destruct": ItemData(236, ItemClassification.useful),
    "TM37 Egg Bomb": ItemData(237, ItemClassification.useful),
    "TM38 Fire Blast": ItemData(238, ItemClassification.useful),
    "TM39 Swift": ItemData(239, ItemClassification.useful),
    "TM40 Skull Bash": ItemData(240, ItemClassification.useful),
    "TM41 Soft Boiled": ItemData(241, ItemClassification.useful),
    "TM42 Dream Eater": ItemData(242, ItemClassification.useful),
    "TM43 Sky Attack": ItemData(243, ItemClassification.useful),
    "TM44 Rest": ItemData(244, ItemClassification.useful),
    "TM45 Thunder Wave": ItemData(245, ItemClassification.useful),
    "TM46 Psywave": ItemData(246, ItemClassification.useful),
    "TM47 Explosion": ItemData(247, ItemClassification.useful),
    "TM48 Rock Slide": ItemData(248, ItemClassification.useful),
    "TM49 Tri Attack": ItemData(249, ItemClassification.useful),
    "TM50 Substitute": ItemData(250, ItemClassification.useful),

    "Fuji Saved": ItemData(None, ItemClassification.progression),
    "Silph Co Liberated": ItemData(None, ItemClassification.progression),
    "Become Champion": ItemData(None, ItemClassification.progression)
}
item_table.update(
    {pokemon: ItemData(None, ItemClassification.progression) for pokemon in pokemon_data.keys()}
)
# for TM in range(0,  51):
#     item_table.append(ItemData(201 + TM, f"TM{TM}", ItemClassification.filler))
# for item in item_table:
#     print(f"\"{item.name}\": ItemData({item.id}, {item.classification})")
