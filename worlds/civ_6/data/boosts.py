from dataclasses import dataclass
from typing import List

from ..ItemData import CivVIBoostData


boosts: List[CivVIBoostData] = [
    CivVIBoostData("BOOST_TECH_SAILING", "ERA_ANCIENT", [], 0, "DEFAULT"),
    CivVIBoostData(
        "BOOST_TECH_ASTROLOGY",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_IRRIGATION",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ARCHERY",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_WRITING",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MASONRY",
        "ERA_ANCIENT",
        ["TECH_MINING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_BRONZE_WORKING",
        "ERA_ANCIENT",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_THE_WHEEL",
        "ERA_ANCIENT",
        ["TECH_MINING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_CELESTIAL_NAVIGATION",
        "ERA_CLASSICAL",
        ["TECH_SAILING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_CURRENCY",
        "ERA_CLASSICAL",
        ["CIVIC_FOREIGN_TRADE"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_HORSEBACK_RIDING",
        "ERA_CLASSICAL",
        ["TECH_ANIMAL_HUSBANDRY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_IRON_WORKING",
        "ERA_CLASSICAL",
        ["TECH_MINING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SHIPBUILDING",
        "ERA_CLASSICAL",
        ["TECH_SAILING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MATHEMATICS",
        "ERA_CLASSICAL",
        [
            "TECH_CURRENCY",
            "TECH_BRONZE_WORKING",
            "TECH_CELESTIAL_NAVIGATION",
            "TECH_WRITING",
            "TECH_APPRENTICESHIP",
            "TECH_FLIGHT",
            "CIVIC_GAMES_RECREATION",
            "CIVIC_DRAMA_POETRY",
        ],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_CONSTRUCTION",
        "ERA_CLASSICAL",
        ["TECH_THE_WHEEL"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ENGINEERING",
        "ERA_CLASSICAL",
        ["TECH_MASONRY"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_MILITARY_TACTICS",
        "ERA_MEDIEVAL",
        ["TECH_BRONZE_WORKING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_APPRENTICESHIP",
        "ERA_MEDIEVAL",
        ["TECH_MINING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MACHINERY",
        "ERA_MEDIEVAL",
        ["TECH_ARCHERY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_EDUCATION",
        "ERA_MEDIEVAL",
        ["TECH_WRITING"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_STIRRUPS",
        "ERA_MEDIEVAL",
        ["CIVIC_FEUDALISM"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MILITARY_ENGINEERING",
        "ERA_MEDIEVAL",
        ["TECH_ENGINEERING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_CASTLES",
        "ERA_MEDIEVAL",
        [
            "CIVIC_DIVINE_RIGHT",
            "CIVIC_EXPLORATION",
            "CIVIC_REFORMED_CHURCH",
            "CIVIC_SUFFRAGE",
            "CIVIC_TOTALITARIANISM",
            "CIVIC_CLASS_STRUGGLE",
            "CIVIC_DIGITAL_DEMOCRACY",
            "CIVIC_CORPORATE_LIBERTARIANISM",
            "CIVIC_SYNTHETIC_TECHNOCRACY",
        ],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_CARTOGRAPHY",
        "ERA_RENAISSANCE",
        ["TECH_CELESTIAL_NAVIGATION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MASS_PRODUCTION",
        "ERA_RENAISSANCE",
        ["TECH_CONSTRUCTION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_BANKING",
        "ERA_RENAISSANCE",
        ["CIVIC_GUILDS"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_GUNPOWDER",
        "ERA_RENAISSANCE",
        ["TECH_BRONZE_WORKING", "TECH_MILITARY_ENGINEERING"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_PRINTING",
        "ERA_RENAISSANCE",
        ["TECH_WRITING", "TECH_EDUCATION"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SQUARE_RIGGING",
        "ERA_RENAISSANCE",
        ["TECH_GUNPOWDER"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ASTRONOMY",
        "ERA_RENAISSANCE",
        ["TECH_EDUCATION"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_METAL_CASTING",
        "ERA_RENAISSANCE",
        ["TECH_MACHINERY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SIEGE_TACTICS",
        "ERA_RENAISSANCE",
        ["TECH_MILITARY_ENGINEERING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_INDUSTRIALIZATION",
        "ERA_INDUSTRIAL",
        ["TECH_APPRENTICESHIP"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SCIENTIFIC_THEORY",
        "ERA_INDUSTRIAL",
        ["CIVIC_THE_ENLIGHTENMENT"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_BALLISTICS",
        "ERA_INDUSTRIAL",
        ["TECH_SIEGE_TACTICS", "TECH_MILITARY_ENGINEERING"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_MILITARY_SCIENCE",
        "ERA_INDUSTRIAL",
        ["TECH_STIRRUPS"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_STEAM_POWER",
        "ERA_INDUSTRIAL",
        ["TECH_MASS_PRODUCTION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SANITATION",
        "ERA_INDUSTRIAL",
        ["CIVIC_URBANIZATION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ECONOMICS",
        "ERA_INDUSTRIAL",
        ["TECH_CURRENCY", "TECH_BANKING"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_RIFLING",
        "ERA_INDUSTRIAL",
        ["TECH_MINING", "TECH_MILITARY_ENGINEERING"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_FLIGHT",
        "ERA_MODERN",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_REPLACEABLE_PARTS",
        "ERA_MODERN",
        ["TECH_MILITARY_SCIENCE"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_STEEL",
        "ERA_MODERN",
        ["TECH_MINING", "TECH_STEAM_POWER", "TECH_INDUSTRIALIZATION"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ELECTRICITY",
        "ERA_MODERN",
        ["CIVIC_MERCANTILISM", "TECH_CELESTIAL_NAVIGATION"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_RADIO",
        "ERA_MODERN",
        ["CIVIC_CONSERVATION"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_CHEMISTRY",
        "ERA_MODERN",
        ["CIVIC_CIVIL_SERVICE"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_COMBUSTION",
        "ERA_MODERN",
        ["CIVIC_NATURAL_HISTORY", "CIVIC_HUMANISM"],
        2,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_ADVANCED_FLIGHT",
        "ERA_ATOMIC",
        ["TECH_FLIGHT"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_ROCKETRY",
        "ERA_ATOMIC",
        ["CIVIC_DIPLOMATIC_SERVICE"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_ADVANCED_BALLISTICS",
        "ERA_ATOMIC",
        [
            "TECH_ELECTRICITY",
            "TECH_REFINING",
            "TECH_APPRENTICESHIP",
            "TECH_INDUSTRIALIZATION",
        ],
        4,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_COMBINED_ARMS",
        "ERA_ATOMIC",
        ["CIVIC_MOBILIZATION", "CIVIC_NATIONALISM"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_PLASTICS",
        "ERA_ATOMIC",
        ["TECH_REFINING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_COMPUTERS",
        "ERA_ATOMIC",
        [
            "CIVIC_SUFFRAGE",
            "CIVIC_TOTALITARIANISM",
            "CIVIC_CLASS_STRUGGLE",
            "CIVIC_DIGITAL_DEMOCRACY",
            "CIVIC_CORPORATE_LIBERTARIANISM",
            "CIVIC_SYNTHETIC_TECHNOCRACY",
        ],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_NUCLEAR_FISSION",
        "ERA_ATOMIC",
        ["CIVIC_DIPLOMATIC_SERVICE"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_SYNTHETIC_MATERIALS",
        "ERA_ATOMIC",
        ["TECH_FLIGHT"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_TELECOMMUNICATIONS",
        "ERA_INFORMATION",
        ["CIVIC_DIPLOMATIC_SERVICE"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_SATELLITES",
        "ERA_INFORMATION",
        ["CIVIC_DRAMA_POETRY", "CIVIC_HUMANISM", "TECH_RADIO"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_GUIDANCE_SYSTEMS",
        "ERA_INFORMATION",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_LASERS",
        "ERA_INFORMATION",
        ["TECH_COMPUTERS"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_COMPOSITES",
        "ERA_INFORMATION",
        ["TECH_COMBUSTION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_STEALTH_TECHNOLOGY",
        "ERA_INFORMATION",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_ROBOTICS",
        "ERA_INFORMATION",
        ["CIVIC_GLOBALIZATION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_NANOTECHNOLOGY",
        "ERA_INFORMATION",
        ["TECH_MINING", "TECH_RADIO"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_NUCLEAR_FUSION",
        "ERA_INFORMATION",
        [
            "TECH_APPRENTICESHIP",
            "TECH_INDUSTRIALIZATION",
            "TECH_ELECTRICITY",
            "TECH_NUCLEAR_FISSION",
        ],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_BUTTRESS",
        "ERA_MEDIEVAL",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_REFINING",
        "ERA_MODERN",
        ["TECH_INDUSTRIALIZATION", "TECH_MINING", "TECH_APPRENTICESHIP"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_TECH_SEASTEADS",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_ADVANCED_AI",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_ADVANCED_POWER_CELLS",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_CYBERNETICS",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_SMART_MATERIALS",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_PREDICTIVE_SYSTEMS",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_TECH_OFFWORLD_MISSION",
        "ERA_FUTURE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CRAFTSMANSHIP",
        "ERA_ANCIENT",
        [
            "TECH_IRRIGATION",
            "TECH_MINING",
            "TECH_CONSTRUCTION",
            "TECH_ANIMAL_HUSBANDRY",
            "TECH_SAILING",
        ],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_FOREIGN_TRADE",
        "ERA_ANCIENT",
        ["TECH_CARTOGRAPHY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MILITARY_TRADITION",
        "ERA_ANCIENT",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_STATE_WORKFORCE",
        "ERA_ANCIENT",
        [
            "TECH_CURRENCY",
            "TECH_BRONZE_WORKING",
            "TECH_CELESTIAL_NAVIGATION",
            "TECH_WRITING",
            "TECH_APPRENTICESHIP",
            "TECH_FLIGHT",
            "CIVIC_GAMES_RECREATION",
            "CIVIC_DRAMA_POETRY",
        ],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_EARLY_EMPIRE",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MYSTICISM",
        "ERA_ANCIENT",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_GAMES_RECREATION",
        "ERA_CLASSICAL",
        ["TECH_CONSTRUCTION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_POLITICAL_PHILOSOPHY",
        "ERA_CLASSICAL",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_DRAMA_POETRY",
        "ERA_CLASSICAL",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MILITARY_TRAINING",
        "ERA_CLASSICAL",
        ["TECH_BRONZE_WORKING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_DEFENSIVE_TACTICS",
        "ERA_CLASSICAL",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_RECORDED_HISTORY",
        "ERA_CLASSICAL",
        ["TECH_WRITING"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_THEOLOGY",
        "ERA_CLASSICAL",
        ["TECH_ASTROLOGY"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_NAVAL_TRADITION",
        "ERA_MEDIEVAL",
        ["TECH_SHIPBUILDING"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_FEUDALISM",
        "ERA_MEDIEVAL",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CIVIL_SERVICE",
        "ERA_MEDIEVAL",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MERCENARIES",
        "ERA_MEDIEVAL",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MEDIEVAL_FAIRES",
        "ERA_MEDIEVAL",
        ["CIVIC_FOREIGN_TRADE", "TECH_CURRENCY"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_GUILDS",
        "ERA_MEDIEVAL",
        ["TECH_CURRENCY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_DIVINE_RIGHT",
        "ERA_MEDIEVAL",
        ["CIVIC_THEOLOGY", "TECH_ASTROLOGY"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_EXPLORATION",
        "ERA_RENAISSANCE",
        ["TECH_CARTOGRAPHY", "TECH_CELESTIAL_NAVIGATION"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_HUMANISM",
        "ERA_RENAISSANCE",
        ["CIVIC_DRAMA_POETRY"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_DIPLOMATIC_SERVICE",
        "ERA_RENAISSANCE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_REFORMED_CHURCH",
        "ERA_RENAISSANCE",
        ["TECH_ASTROLOGY"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MERCANTILISM",
        "ERA_RENAISSANCE",
        ["TECH_CURRENCY"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_THE_ENLIGHTENMENT",
        "ERA_RENAISSANCE",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_COLONIALISM",
        "ERA_INDUSTRIAL",
        ["TECH_ASTRONOMY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CIVIL_ENGINEERING",
        "ERA_INDUSTRIAL",
        [
            "TECH_CURRENCY",
            "TECH_BRONZE_WORKING",
            "TECH_CELESTIAL_NAVIGATION",
            "TECH_WRITING",
            "TECH_APPRENTICESHIP",
            "TECH_FLIGHT",
            "CIVIC_GAMES_RECREATION",
            "CIVIC_DRAMA_POETRY",
        ],
        8,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_NATIONALISM",
        "ERA_INDUSTRIAL",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_OPERA_BALLET",
        "ERA_INDUSTRIAL",
        ["CIVIC_HUMANISM", "CIVIC_DRAMA_POETRY"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_NATURAL_HISTORY",
        "ERA_INDUSTRIAL",
        ["CIVIC_HUMANISM", "CIVIC_DRAMA_POETRY"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_SCORCHED_EARTH",
        "ERA_INDUSTRIAL",
        ["TECH_BALLISTICS"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_URBANIZATION",
        "ERA_INDUSTRIAL",
        [],
        0,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CONSERVATION",
        "ERA_MODERN",
        ["CIVIC_URBANIZATION"],
        1,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CAPITALISM",
        "ERA_MODERN",
        ["TECH_CURRENCY", "TECH_BANKING", "TECH_ECONOMICS"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_NUCLEAR_PROGRAM",
        "ERA_MODERN",
        ["TECH_WRITING", "TECH_EDUCATION", "TECH_CHEMISTRY"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MASS_MEDIA",
        "ERA_MODERN",
        ["TECH_RADIO"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_MOBILIZATION",
        "ERA_MODERN",
        ["CIVIC_NATIONALISM"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_SUFFRAGE",
        "ERA_MODERN",
        ["TECH_SANITATION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_TOTALITARIANISM",
        "ERA_MODERN",
        [
            "TECH_BRONZE_WORKING",
            "TECH_MILITARY_ENGINEERING",
            "TECH_MILITARY_SCIENCE",
        ],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CLASS_STRUGGLE",
        "ERA_MODERN",
        ["TECH_APPRENTICESHIP", "TECH_INDUSTRIALIZATION"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_COLD_WAR",
        "ERA_ATOMIC",
        ["TECH_NUCLEAR_FISSION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_PROFESSIONAL_SPORTS",
        "ERA_ATOMIC",
        ["CIVIC_GAMES_RECREATION"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_CULTURAL_HERITAGE",
        "ERA_ATOMIC",
        [],
        0,
        "EXCLUDED",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_RAPID_DEPLOYMENT",
        "ERA_ATOMIC",
        ["TECH_FLIGHT", "TECH_CARTOGRAPHY", "TECH_SHIPBUILDING"],
        3,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_SPACE_RACE",
        "ERA_ATOMIC",
        ["TECH_ROCKETRY"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_GLOBALIZATION",
        "ERA_INFORMATION",
        ["TECH_FLIGHT", "TECH_ADVANCED_FLIGHT"],
        2,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_SOCIAL_MEDIA",
        "ERA_INFORMATION",
        ["TECH_TELECOMMUNICATIONS"],
        1,
        "DEFAULT",
    ),
    CivVIBoostData(
        "BOOST_CIVIC_ENVIRONMENTALISM",
        "ERA_INFORMATION",
        ["TECH_SATELLITES"],
        1,
        "DEFAULT",
    ),
]
