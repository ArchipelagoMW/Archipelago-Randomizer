# Copyright (c) 2022 FelicitusNeko
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from BaseClasses import Item


class MeritousItem(Item):
    game: str = "Meritous"


offset = 0

item_table = {
    "Nothing": offset + 0,
    "Reflect Shield upgrade": offset + 1,
    "Circuit Charge upgrade": offset + 2,
    "Circuit Refill upgrade": offset + 3,
    "Map": offset + 4,
    "Shield Boost": offset + 5,
    "Crystal Efficiency": offset + 6,
    "Circuit Booster": offset + 7,
    "Metabolism": offset + 8,
    "Dodge Enhancer": offset + 9,
    "Ethereal Monocle": offset + 10,
    "Crystal Gatherer": offset + 11,
    "PSI Key 1": offset + 12,
    "PSI Key 2": offset + 13,
    "PSI Key 3": offset + 14,
    "Cursed Seal": offset + 15,
    "Agate Knife": offset + 16,
    "Evolution Trap": offset + 17,
    "Crystals x500": offset + 18,
    "Crystals x1000": offset + 19,
    "Crystals x2000": offset + 20
}
