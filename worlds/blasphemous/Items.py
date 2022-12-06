from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List, Set


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


item_table: List[ItemDict] = [
    # Rosary Beads
    {'name': "Dove Skull",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Ember of the Holy Cremation",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Silver Grape",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Uvula of Proclamation",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Hollow Pearl",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Knot of Hair",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Painted Wood Bead",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Piece of a Golden Mask",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Moss Preserved in Glass",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Frozen Olive",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Quirce's Scorched Bead",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Wicker Knot",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Perpetva's Protection",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Thorned Symbol",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Piece of a Tombstone",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Sphere of the Sacred Smoke",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Bead of Red Wax",
        'count': 3,
        'classification': ItemClassification.progression},
    {'name': "Little Toe made of Limestone",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Big Toe made of Limestone",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Fourth Toe made of Limestone",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Bead of Blue Wax",
        'count': 3,
        'classification': ItemClassification.progression},
    {'name': "Pelican Effigy",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Drop of Coagulated Ink",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Amber Eye",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Muted Bell",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Consecrated Amethyst",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Embers of a Broken Star",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Scaly Coin",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Seashell of the Inverted Spiral",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Calcified Eye of Erudition",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Weight of True Guilt",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Reliquary of the Fervent Heart",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Reliquary of the Suffering Heart",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Reliquary of the Sorrowful Heart",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Token of Appreciation",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Cloistered Ruby",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Bead of Gold Thread",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Cloistered Sapphire",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Fire Enclosed in Enamel",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Light of the Lady of the Lamp",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Scale of Burnished Alabaster",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "The Young Mason's Wheel",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Crown of Gnawed Iron",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Crimson Heart of a Miura",
        'count': 1,
        'classification': ItemClassification.useful},

    # Prayers
    {'name': "Seguiriya to your Eyes like Stars",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Debla of the Lights",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Saeta Dolorosa",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Campanillero to the Sons of the Aurora",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Lorquiana",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Zarabanda of the Safe Haven",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Taranto to my Sister",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Solea of Excommunication",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Tiento to your Thorned Hairs",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Cante Jondo of the Three Sisters",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Verdiales of the Forsaken Hamlet",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Romance to the Crimson Mist",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Zambra to the Resplendent Crown",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Aubade of the Nameless Guardian",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Cantina of the Blue Rose",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Mirabras of the Return to Port",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Tirana of the Celestial Bastion",
        'count': 1,
        'classification': ItemClassification.progression},

    # Relics
    {'name': "Blood Perpetuated in Sand",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Incorrupt Hand of the Fraternal Master",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Nail Uprooted from Dirt",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Shroud of Dreamt Sins",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Linen of Golden Thread",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Silvered Lung of Dolphos",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Three Gnarled Tongues",
        'count': 1,
        'classification': ItemClassification.progression},

    # Mea Culpa Hearts
    {'name': "Smoking Heart of Incense",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of the Virtuous Pain",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of Saltpeter Blood",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of Oils",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of Cerulean Incense",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of the Holy Purge",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Molten Heart of Boiling Blood",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of the Single Tone",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Heart of the Unnamed Minstrel",
        'count': 1,
        'classification': ItemClassification.useful},
    {'name': "Brilliant Heart of Dawn",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Apodictic Heart of Mea Culpa",
        'count': 1,
        'classification': ItemClassification.progression},

    # Quest Items
    {'name': "Cord of the True Burying",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Mark of the First Refuge",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Mark of the Second Refuge",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Mark of the Third Refuge",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Tentudia's Carnal Remains",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Remains of Tentudia's Hair",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Tentudia's Skeletal Remains",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Melted Golden Coins",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Torn Bridal Ribbon",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Black Grieving Veil",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Egg of Deformity",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Hatched Egg of Deformity",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Bouquet of Rosemary",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Incense Garlic",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Thorn Upgrade",
        'count': 8,
        'classification': ItemClassification.progression},
    {'name': "Olive Seeds",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Holy Wound of Attrition",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Holy Wound of Contrition",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Holy Wound of Compunction",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Empty Bile Vessel",
        'count': 8,
        'classification': ItemClassification.progression},
    {'name': "Knot of Rosary Rope",
        'count': 6,
        'classification': ItemClassification.progression},
    {'name': "Golden Thimble Filled with Burning Oil",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key to the Chamber of the Eldest Brother",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Empty Golden Thimble",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Deformed Mask of Orestes",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Mirrored Mask of Dolphos",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Embossed Mask of Crescente",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Dried Clove",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Sooty Garlic",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Bouquet of Thyme",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Linen Cloth",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Severed Hand",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Dried Flowers bathed in Tears",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key of the Secular",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key of the Scribe",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key of the Inquisitor",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key of the High Peaks",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Chalice of Inverted Verses",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Quicksilver",
        'count': 5,
        'classification': ItemClassification.useful},
    {'name': "Petrified Bell",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Verses Spun from Gold",
        'count': 4,
        'classification': ItemClassification.progression},
    {'name': "Severed Right Eye of the Traitor",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Broken Left Eye of the Traitor",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Incomplete Scapular",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Key Grown from Twisted Wood",
        'count': 1,
        'classification': ItemClassification.progression},
    {'name': "Holy Wound of Abnegation",
        'count': 1,
        'classification': ItemClassification.progression},

    # Other
    {'name': "Ossuary Remains",
        'count': 44,
        'classification': ItemClassification.progression},
    {'name': "Child of Moonlight",
        'count': 38,
        'classification': ItemClassification.progression},
    {'name': "Life Upgrade",
        'count': 6,
        'classification': ItemClassification.progression},
    {'name': "Fervour Upgrade",
        'count': 6,
        'classification': ItemClassification.progression},
    {'name': "Mea Culpa Upgrade",
        'count': 7,
        'classification': ItemClassification.progression},
    {'name': "Tears of Atonement (500)",
        'count': 2,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (625)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (750)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (1000)",
        'count': 4,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (1250)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (1500)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (1750)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (2000)",
        'count': 2,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (2100)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (2500)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (2600)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (3000)",
        'count': 2,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (4300)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (5000)",
        'count': 4,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (5500)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (9000)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (10000)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (11250)",
        'count': 1,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (18000)",
        'count': 5,
        'classification': ItemClassification.filler},
    {'name': "Tears of Atonement (30000)",
        'count': 1,
        'classification': ItemClassification.filler},
]

group_table: Dict[str, Set[str]] = {
    "wounds"  : ["Holy Wound of Attrition",
                 "Holy Wound of Contrition",
                 "Holy Wound of Compunction"],

    "masks"   : ["Deformed Mask of Orestes",
                 "Mirrored Mask of Dolphos",
                 "Embossed Mask of Crescente"],

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
                 "Aubade of the Nameless Guardian",
                 "Cantina of the Blue Rose",
                 "Mirabras of the Return to Port",
                 "Tirana of the Celestial Bastion"]
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