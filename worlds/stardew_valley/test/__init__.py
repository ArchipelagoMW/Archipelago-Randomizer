import os
from argparse import Namespace
from typing import Dict, FrozenSet, Tuple, Any, ClassVar

from BaseClasses import MultiWorld
from test.TestBase import WorldTestBase
from test.general import gen_steps
from .. import StardewValleyWorld, options
from ...AutoWorld import call_all


class SVTestBase(WorldTestBase):
    game = "Stardew Valley"
    world: StardewValleyWorld
    player: ClassVar[int] = 1
    skip_long_tests: bool = True

    def world_setup(self, *args, **kwargs):
        super().world_setup(*args, **kwargs)
        long_tests_key = "long"
        if long_tests_key in os.environ:
            self.skip_long_tests = not bool(os.environ[long_tests_key])
        if self.constructed:
            self.world = self.multiworld.worlds[self.player]  # noqa

    @property
    def run_default_tests(self) -> bool:
        # world_setup is overridden, so it'd always run default tests when importing SVTestBase
        is_not_stardew_test = type(self) is not SVTestBase
        should_run_default_tests = is_not_stardew_test and super().run_default_tests
        return should_run_default_tests

    def allsanity_options(self):
        allsanity = {
            options.Goal.internal_name: options.Goal.option_perfection,
            options.BundleRandomization.internal_name: options.BundleRandomization.option_shuffled,
            options.BundlePrice.internal_name: options.BundlePrice.option_expensive,
            options.SeasonRandomization.internal_name: options.SeasonRandomization.option_randomized,
            options.SeedShuffle.internal_name: options.SeedShuffle.option_shuffled,
            options.BackpackProgression.internal_name: options.BackpackProgression.option_progressive,
            options.ToolProgression.internal_name: options.ToolProgression.option_progressive,
            options.SkillProgression.internal_name: options.SkillProgression.option_progressive,
            options.BuildingProgression.internal_name: options.BuildingProgression.option_progressive,
            options.FestivalLocations.internal_name: options.FestivalLocations.option_hard,
            options.TheMinesElevatorsProgression.internal_name: options.TheMinesElevatorsProgression.option_progressive,
            options.ArcadeMachineLocations.internal_name: options.ArcadeMachineLocations.option_full_shuffling,
            options.SpecialOrderLocations.internal_name: options.SpecialOrderLocations.option_board_qi,
            options.HelpWantedLocations.internal_name: 56,
            options.Fishsanity.internal_name: options.Fishsanity.option_all,
            options.Museumsanity.internal_name: options.Museumsanity.option_all,
            options.Friendsanity.internal_name: options.Friendsanity.option_all,
            options.NumberOfPlayerBuffs.internal_name: 12,
            options.ExcludeGingerIsland.internal_name: options.ExcludeGingerIsland.option_false,
            options.TrapItems.internal_name: options.TrapItems.option_nightmare,
        }
        return allsanity

pre_generated_worlds = {}


# Mostly a copy of test.general.setup_solo_multiworld, I just don't want to change the core.
def setup_solo_multiworld(test_options=None, seed=None,
                          _cache: Dict[FrozenSet[Tuple[str, Any]], MultiWorld] = {}) -> MultiWorld:  # noqa
    if test_options is None:
        test_options = {}

    # Yes I reuse the worlds generated between tests, its speeds the execution by a couple seconds
    frozen_options = frozenset(test_options.items())
    if frozen_options in _cache:
        return _cache[frozen_options]

    multiworld = MultiWorld(1)
    multiworld.game[1] = StardewValleyWorld.game
    multiworld.player_name = {1: "Tester"}
    multiworld.set_seed(seed)
    # print(f"Seed: {multiworld.seed}") # Uncomment to print the seed for every test
    args = Namespace()
    for name, option in StardewValleyWorld.option_definitions.items():
        value = option(test_options[name]) if name in test_options else option.from_any(option.default)
        setattr(args, name, {1: value})
    multiworld.set_options(args)
    multiworld.set_default_common_options()
    for step in gen_steps:
        call_all(multiworld, step)

    _cache[frozen_options] = multiworld

    return multiworld
