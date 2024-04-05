from typing import Dict, List, Set, TypedDict

from BaseClasses import ItemClassification


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification

base_id = 1909000

item_table: List[ItemDict] = [
    # Rosary Beads
    {"name": "Dove Skull",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Ember of the Holy Cremation",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Silver Grape",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Uvula of Proclamation",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Hollow Pearl",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Knot of Hair",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Painted Wood Bead",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Piece of a Golden Mask",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Moss Preserved in Glass",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Frozen Olive",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Quirce's Scorched Bead",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Wicker Knot",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Perpetva's Protection",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Thorned Symbol",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Piece of a Tombstone",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Sphere of the Sacred Smoke",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Bead of Red Wax",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Little Toe made of Limestone",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Big Toe made of Limestone",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Fourth Toe made of Limestone",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Bead of Blue Wax",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Pelican Effigy",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Drop of Coagulated Ink",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Amber Eye",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Muted Bell",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Consecrated Amethyst",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Embers of a Broken Star",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Scaly Coin",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Seashell of the Inverted Spiral",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Calcified Eye of Erudition",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Weight of True Guilt",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Reliquary of the Fervent Heart",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Reliquary of the Suffering Heart",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Reliquary of the Sorrowful Heart",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Token of Appreciation",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Cloistered Ruby",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Bead of Gold Thread",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Cloistered Sapphire",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Fire Enclosed in Enamel",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Light of the Lady of the Lamp",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Scale of Burnished Alabaster",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "The Young Mason's Wheel",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Crown of Gnawed Iron",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Crimson Heart of a Miura",
        "count": 1,
        "classification": ItemClassification.useful},

    # Prayers
    {"name": "Seguiriya to your Eyes like Stars",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Debla of the Lights",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Saeta Dolorosa",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Campanillero to the Sons of the Aurora",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Lorquiana",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Zarabanda of the Safe Haven",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Taranto to my Sister",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Solea of Excommunication",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Tiento to your Thorned Hairs",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Cante Jondo of the Three Sisters",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Verdiales of the Forsaken Hamlet",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Romance to the Crimson Mist",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Zambra to the Resplendent Crown",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Aubade of the Nameless Guardian",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Cantina of the Blue Rose",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Mirabras of the Return to Port",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Tirana of the Celestial Bastion",
        "count": 1,
        "classification": ItemClassification.progression},

    # Relics
    {"name": "Blood Perpetuated in Sand",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Incorrupt Hand of the Fraternal Master",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Nail Uprooted from Dirt",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Shroud of Dreamt Sins",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Linen of Golden Thread",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Silvered Lung of Dolphos",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Three Gnarled Tongues",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Boots of Pleading",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Purified Hand of the Nun",
        "count": 1,
        "classification": ItemClassification.progression},

    # Mea Culpa Hearts
    {"name": "Smoking Heart of Incense",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of the Virtuous Pain",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of Saltpeter Blood",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of Oils",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of Cerulean Incense",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of the Holy Purge",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Molten Heart of Boiling Blood",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of the Single Tone",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Heart of the Unnamed Minstrel",
        "count": 1,
        "classification": ItemClassification.useful},
    {"name": "Brilliant Heart of Dawn",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Apodictic Heart of Mea Culpa",
        "count": 1,
        "classification": ItemClassification.progression},

    # Quest Items
    {"name": "Cord of the True Burying",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Mark of the First Refuge",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Mark of the Second Refuge",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Mark of the Third Refuge",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Tentudia's Carnal Remains",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Remains of Tentudia's Hair",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Tentudia's Skeletal Remains",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Melted Golden Coins",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Torn Bridal Ribbon",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Black Grieving Veil",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Egg of Deformity",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Hatched Egg of Deformity",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Bouquet of Rosemary",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Incense Garlic",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Thorn Upgrade",
        "count": 8,
        "classification": ItemClassification.progression},
    {"name": "Olive Seeds",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Holy Wound of Attrition",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Holy Wound of Contrition",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Holy Wound of Compunction",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Empty Bile Vessel",
        "count": 8,
        "classification": ItemClassification.progression},
    {"name": "Knot of Rosary Rope",
        "count": 6,
        "classification": ItemClassification.progression},
    {"name": "Golden Thimble Filled with Burning Oil",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key to the Chamber of the Eldest Brother",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Empty Golden Thimble",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Deformed Mask of Orestes",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Mirrored Mask of Dolphos",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Embossed Mask of Crescente",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Dried Clove",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Sooty Garlic",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Bouquet of Thyme",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Linen Cloth",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Severed Hand",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Dried Flowers bathed in Tears",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key of the Secular",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key of the Scribe",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key of the Inquisitor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key of the High Peaks",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Chalice of Inverted Verses",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Quicksilver",
        "count": 5,
        "classification": ItemClassification.progression},
    {"name": "Petrified Bell",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Verses Spun from Gold",
        "count": 4,
        "classification": ItemClassification.progression},
    {"name": "Severed Right Eye of the Traitor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Broken Left Eye of the Traitor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Incomplete Scapular",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Key Grown from Twisted Wood",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Holy Wound of Abnegation",
        "count": 1,
        "classification": ItemClassification.progression},

    # Skills
    {"name": "Combo Skill",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Charged Skill",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Ranged Skill",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Dive Skill",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Lunge Skill",
        "count": 3,
        "classification": ItemClassification.progression},
    {"name": "Dash Ability",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Wall Climb Ability",
        "count": 1,
        "classification": ItemClassification.progression},

    # Other
    {"name": "Parietal bone of Lasser, the Inquisitor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Jaw of Ashgan, the Inquisitor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Cervical vertebra of Zicher, the Brewmaster",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Clavicle of Dalhuisen, the Schoolchild",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Sternum of Vitas, the Performer",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Ribs of Sabnock, the Guardian",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Vertebra of John, the Gambler",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Scapula of Carlos, the Executioner",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Humerus of McMittens, the Nurse",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Ulna of Koke, the Troubadour",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Radius of Helzer, the Poet",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Frontal of Martinus, the Ropemaker",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Metacarpus of Hodges, the Blacksmith",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of Arthur, the Sailor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of Miriam, the Counsellor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of Brannon, the Gravedigger",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Coxal of June, the Prostitute",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Sacrum of the Dark Warlock",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Coccyx of Daniel, the Possessed",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Femur of Karpow, the Bounty Hunter",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Kneecap of Sebastien, the Puppeteer",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Tibia of Alsahli, the Mystic",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Fibula of Rysp, the Ranger",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Temporal of Joel, the Thief",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Metatarsus of Rikusyo, the Traveller",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of Zeth, the Prisoner",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of William, the Sceptic",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Phalanx of Aralcarim, the Archivist",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Occipital of Tequila, the Metalsmith",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Maxilla of Tarradax, the Cleric",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Nasal bone of Charles, the Artist",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Hyoid bone of Senex, the Beggar",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Vertebra of Lindquist, the Forger",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Trapezium of Jeremiah, the Hangman",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Trapezoid of Yeager, the Jeweller",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Capitate of Barock, the Herald",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Hamate of Vukelich, the Copyist",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Pisiform of Hernandez, the Explorer",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Triquetral of Luca, the Tailor",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Lunate of Keiya, the Butcher",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Scaphoid of Fierce, the Leper",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Anklebone of Weston, the Pilgrim",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Calcaneum of Persian, the Bandit",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Navicular of Kahnnyhoo, the Murderer",
        "count": 1,
        "classification": ItemClassification.progression},
    {"name": "Child of Moonlight",
        "count": 38,
        "classification": ItemClassification.progression},
    {"name": "Life Upgrade",
        "count": 6,
        "classification": ItemClassification.progression},
    {"name": "Fervour Upgrade",
        "count": 6,
        "classification": ItemClassification.progression},
    {"name": "Mea Culpa Upgrade",
        "count": 7,
        "classification": ItemClassification.progression},
    {"name": "Tears of Atonement (250)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (300)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (500)",
        "count": 3,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (625)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (750)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (1000)",
        "count": 4,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (1250)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (1500)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (1750)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (2000)",
        "count": 2,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (2100)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (2500)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (2600)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (3000)",
        "count": 2,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (4300)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (5000)",
        "count": 4,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (5500)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (9000)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (10000)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (11250)",
        "count": 1,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (18000)",
        "count": 5,
        "classification": ItemClassification.filler},
    {"name": "Tears of Atonement (30000)",
        "count": 1,
        "classification": ItemClassification.filler}
]

event_table: Dict[str, str] = {
    "OpenedDCGateW": "D01Z05S24",
    "OpenedDCGateE": "D01Z05S12",
    "OpenedDCLadder": "D01Z05S20",
    "OpenedWOTWCave": "D02Z01S06",
    "RodeGOTPElevator": "D02Z02S11",
    "OpenedConventLadder": "D02Z03S11",
    "BrokeJondoBellW": "D03Z02S09",
    "BrokeJondoBellE": "D03Z02S05",
    "OpenedMOMLadder": "D04Z02S06",
    "OpenedTSCGate": "D05Z02S11",
    "OpenedARLadder": "D06Z01S23",
    "BrokeBOTTCStatue": "D08Z01S02",
    "OpenedWOTHPGate": "D09Z01S05",
    "OpenedBOTSSLadder": "D17Z01S04"
}

group_table: Dict[str, Set[str]] = {
    "wounds"  : ["Holy Wound of Attrition",
                 "Holy Wound of Contrition",
                 "Holy Wound of Compunction"],

    "masks"   : ["Deformed Mask of Orestes",
                 "Mirrored Mask of Dolphos",
                 "Embossed Mask of Crescente"],

    "marks"   : ["Mark of the First Refuge",
                 "Mark of the Second Refuge",
                 "Mark of the Third Refuge"],

    "tirso"   : ["Bouquet of Rosemary",
                 "Incense Garlic",
                 "Olive Seeds",
                 "Dried Clove",
                 "Sooty Garlic",
                 "Bouquet of Thyme"],

    "tentudia": ["Tentudia's Carnal Remains",
                 "Remains of Tentudia's Hair",
                 "Tentudia's Skeletal Remains"],

    "egg"     : ["Melted Golden Coins",
                 "Torn Bridal Ribbon",
                 "Black Grieving Veil"],

    "bones"   : ["Parietal bone of Lasser, the Inquisitor",
                 "Jaw of Ashgan, the Inquisitor",
                 "Cervical vertebra of Zicher, the Brewmaster",
                 "Clavicle of Dalhuisen, the Schoolchild",
                 "Sternum of Vitas, the Performer",
                 "Ribs of Sabnock, the Guardian",
                 "Vertebra of John, the Gambler",
                 "Scapula of Carlos, the Executioner",
                 "Humerus of McMittens, the Nurse",
                 "Ulna of Koke, the Troubadour",
                 "Radius of Helzer, the Poet",
                 "Frontal of Martinus, the Ropemaker",
                 "Metacarpus of Hodges, the Blacksmith",
                 "Phalanx of Arthur, the Sailor",
                 "Phalanx of Miriam, the Counsellor",
                 "Phalanx of Brannon, the Gravedigger",
                 "Coxal of June, the Prostitute",
                 "Sacrum of the Dark Warlock",
                 "Coccyx of Daniel, the Possessed",
                 "Femur of Karpow, the Bounty Hunter",
                 "Kneecap of Sebastien, the Puppeteer",
                 "Tibia of Alsahli, the Mystic",
                 "Fibula of Rysp, the Ranger",
                 "Temporal of Joel, the Thief",
                 "Metatarsus of Rikusyo, the Traveller",
                 "Phalanx of Zeth, the Prisoner",
                 "Phalanx of William, the Sceptic",
                 "Phalanx of Aralcarim, the Archivist",
                 "Occipital of Tequila, the Metalsmith",
                 "Maxilla of Tarradax, the Cleric",
                 "Nasal bone of Charles, the Artist",
                 "Hyoid bone of Senex, the Beggar",
                 "Vertebra of Lindquist, the Forger",
                 "Trapezium of Jeremiah, the Hangman",
                 "Trapezoid of Yeager, the Jeweller",
                 "Capitate of Barock, the Herald",
                 "Hamate of Vukelich, the Copyist",
                 "Pisiform of Hernandez, the Explorer",
                 "Triquetral of Luca, the Tailor",
                 "Lunate of Keiya, the Butcher",
                 "Scaphoid of Fierce, the Leper",
                 "Anklebone of Weston, the Pilgrim",
                 "Calcaneum of Persian, the Bandit",
                 "Navicular of Kahnnyhoo, the Murderer"],

    "power"   : ["Life Upgrade",
                 "Fervour Upgrade",
                 "Empty Bile Vessel",
                 "Quicksilver"],

    "prayer"  : ["Seguiriya to your Eyes like Stars",
                 "Debla of the Lights",
                 "Saeta Dolorosa",
                 "Campanillero to the Sons of the Aurora",
                 "Lorquiana",
                 "Zarabanda of the Safe Haven",
                 "Taranto to my Sister",
                 "Solea of Excommunication",
                 "Tiento to your Thorned Hairs",
                 "Cante Jondo of the Three Sisters",
                 "Verdiales of the Forsaken Hamlet",
                 "Romance to the Crimson Mist",
                 "Zambra to the Resplendent Crown",
                 "Cantina of the Blue Rose",
                 "Mirabras of the Return to Port"]
}

tears_set: Set[str] = [
    "Tears of Atonement (500)",
    "Tears of Atonement (625)",
    "Tears of Atonement (750)",
    "Tears of Atonement (1000)",
    "Tears of Atonement (1250)",
    "Tears of Atonement (1500)",
    "Tears of Atonement (1750)",
    "Tears of Atonement (2000)",
    "Tears of Atonement (2100)",
    "Tears of Atonement (2500)",
    "Tears of Atonement (2600)",
    "Tears of Atonement (3000)",
    "Tears of Atonement (4300)",
    "Tears of Atonement (5000)",
    "Tears of Atonement (5500)",
    "Tears of Atonement (9000)",
    "Tears of Atonement (10000)",
    "Tears of Atonement (11250)",
    "Tears of Atonement (18000)",
    "Tears of Atonement (30000)"
]

reliquary_set: Set[str] = [
    "Reliquary of the Fervent Heart",
    "Reliquary of the Suffering Heart",
    "Reliquary of the Sorrowful Heart"
]

skill_set: Set[str] = [
    "Combo Skill",
    "Charged Skill",
    "Ranged Skill",
    "Dive Skill",
    "Lunge Skill"
]
