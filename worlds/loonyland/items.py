from enum import Enum
from typing import NamedTuple

from BaseClasses import Item, ItemClassification

from worlds.loonyland.options import Badges, LongChecks, LoonylandOptions, MonsterDolls, MultipleSaves, Remix


class LoonylandItem(Item):
    """
    Item from the game Loonyland
    """

    game: str = "Loonyland"


class LLItemCat(Enum):
    ITEM = 0
    CHEAT = 1
    FILLER = 2
    TRAP = 3
    EVENT = 4
    ACCESS = 5
    DOLL = 6


class LLItem(NamedTuple):
    id: int
    category: LLItemCat
    classification: ItemClassification
    frequency: int = 1
    flags: list[str] = []

    def can_create(self, options: LoonylandOptions) -> bool:
        if (self.category == LLItemCat.CHEAT and options.badges == Badges.option_vanilla) or (
            self.category == LLItemCat.DOLL and options.dolls == MonsterDolls.option_vanilla
        ):
            return False
        if "OP" in self.flags:
            return False
        if options.remix == Remix.option_excluded and ("REMIX" in self.flags):
            return False
        if options.multisave == MultipleSaves.option_disabled and ("MULTISAVE" in self.flags):
            return False
        return True

    def in_logic(self, options: LoonylandOptions) -> bool:
        if self.category == LLItemCat.CHEAT and options.badges == Badges.option_none:
            return False
        if self.category == LLItemCat.DOLL and options.dolls == MonsterDolls.option_none:
            return False
        return True

    def modified_classification(self, options: LoonylandOptions):
        if options.long_checks == LongChecks.option_included:
            if self.category == LLItemCat.CHEAT:  # 39 badges
                return ItemClassification.progression
            if self.category == LLItemCat.ITEM:  # 100%
                return ItemClassification.progression
            if self.category == LLItemCat.DOLL:  # 100%
                return ItemClassification.progression
        if options.badges == Badges.option_none:
            if self.category == LLItemCat.ACCESS:
                return ItemClassification.filler
        if (
            "PWR" in self.flags or "PWR_BIG" in self.flags or "PWR_MAX" in self.flags
        ):  # need to be able to kill bosses, eventually an option for this
            return ItemClassification.progression

        return self.classification
