# items
# listing individual groups first for easy lookup
NOTES = [
    "Key of Hope",
    "Key of Chaos",
    "Key of Courage",
    "Key of Love",
    "Key of Strength",
    "Key of Symbiosis"
]

PROG_ITEMS = [
    "Wingsuit",
    "Rope Dart",
    "Ninja Tabi",
    "Power Thistle",
    "Demon King Crown",
    "Ruxxtin Amulet",
    "Fairy Bottle",
    "Sun Crest",
    "Moon Crest",
]

PHOBEKINS = [
    "Necro",
    "Pyro",
    "Claustro",
    "Acro"
]

USEFUL_ITEMS = [
    "Windmill Shuriken"
]

JUNK = [
    "Time Shard",  # currently just send in quantity of 1. Need to engineer a way to send this in quantities.
    "Candle",
    "Seashell",
]

# item_name_to_id needs to be deterministic and match upstream
ALL_ITEMS = [
    *NOTES,
    "Windmill Shuriken",
    "Wingsuit",
    "Rope Dart",
    "Ninja Tabi",
    "Candle",
    "Seashell",
    "Power Thistle",
    "Demon King Crown",
    "Ruxxtin Amulet",
    "Fairy Bottle",
    "Sun Crest",
    "Moon Crest",
    *PHOBEKINS,
    "Time Shard"  # there's 45 separate instances of this in the client lookup, but hopefully we don't care?
]

# locations
# the names of these don't actually matter, but using the upstream's names for now
# order must be exactly the same as upstream
ALWAYS_LOCATIONS = [
    "Seashell",
    "Ninja Tabi",
    "Rope Dart",
    "Wingsuit",
    "Key of Love",
    "Key of Courage",
    "Key of Chaos",
    "Sun Crest",
    "Moon Crest",
    "Pyro",
    "Acro",
    "Necro",
    "Ruxxtin's Amulet",
    "Candle",
    "Claustro",
    "Climbing Claws",
    "Demon King Crown",
    "Key of Symbiosis",
    "Key of Strength",
    "Power Thistle",
    "Fairy Bottle",
    "Key of Hope"
]

SEALS = [
    "Ninja Village Seal - Tree House",

    "Autumn Hills Seal - Trip Saws",
    "Autumn Hills Seal - Double Swing Saws",
    "Autumn Hills Seal - Spike Ball Swing",
    "Autumn Hills Seal - Spike Ball Darts",

    "Catacombs Seal - Triple Spike Crushers",
    "Catacombs Seal - Crusher Gauntlet",
    "Catacombs Seal - Dirty Pond",

    "Bamboo Creek Seal - Spike Crushers and Doors",
    "Bamboo Creek Seal - Spike Ball Pits",
    "Bamboo Creek Seal - Spike Crushers and Doors v2",

    "Howling Grotto Seal - Windy Saws and Balls",
    "Howling Grotto Seal - Crushing Pits",
    "Howling Grotto Seal - Breezy Crushers",

    "Quillshroom Marsh Seal - Spikey Window",
    "Quillshroom Marsh Seal - Sand Trap",
    "Quillshroom Marsh Seal - Do the Spike Wave",

    "Searing Crags Seal - Triple Ball Spinner",
    "Searing Crags Seal - Raining Rocks",
    "Searing Crags Seal - Rythym Rocks",

    "Glacial Peak Seal - Ice Climbers",
    "Glacial Peak Seal - Projectile Spike Pit",
    "Glacial Peak Seal - Glacial Air Swag",

    "Tower of Time Seal - Time Waster Seal",
    "Tower of Time Seal - Lantern Climb",
    "Tower of Time Seal - Arcane Orbs",

    "Cloud Ruins Seal - Ghost Pit",
    "Cloud Ruins Seal - Toothbrush Alley",
    "Cloud Ruins Seal - Saw Pit",
    "Cloud Ruins Seal - Money Farm Room",

    "Underworld Seal - Sharp and Windy Climb",
    "Underworld Seal - Spike Wall",
    "Underworld Seal - Fireball Wave",
    "Underworld Seal - Rising Fanta",

    "Forlorn Temple Seal - Rocket Maze",
    "Forlorn Temple Seal - Rocket Sunset",

    "Sunken Shrine Seal - Ultra Lifeguard",
    "Sunken Shrine Seal - Waterfall Paradise",
    "Sunken Shrine Seal - Tabi Gauntlet",

    "Riviere Turquoise Seal - Bounces and Balls",
    "Riviere Turquoise Seal - Launch of Faith",
    "Riviere Turquoise Seal - Flower Power",

    "Elemental Skylands Seal - Air Seal",
    "Elemental Skylands Seal - Water Seal",
    "Elemental Skylands Seal - Fire Seal"
]
