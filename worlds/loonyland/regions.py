from typing import NamedTuple

from BaseClasses import Region

from worlds.loonyland.options import Badges, LoonylandOptions


class LoonylandRegion(Region):
    game = "Loonyland"


class LLRegion(NamedTuple):
    real: bool
    map: str = ""
    flags: list[str] = []

    def can_create(self, options: LoonylandOptions) -> bool:
        if options.badges == Badges.option_none and "MODE" in self.flags:
            return False
        return True
