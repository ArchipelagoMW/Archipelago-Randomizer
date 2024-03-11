from BaseClasses import CollectionState
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import YIWorld


class BossReqs:
    player: int


    def __init__(self, world: "YIWorld") -> None:
        self.player = world.player
        self.castle_unlock = world.options.castle_open_condition.value
        self.boss_unlock = world.options.castle_clear_condition.value

    def castle_access(self, state: CollectionState,) -> bool:
        return state.has('Boss Clear', self.player, self.castle_unlock)

    def castle_clear(self, state: CollectionState,) -> bool:
        return state.has('Boss Clear', self.player, self.boss_unlock)
