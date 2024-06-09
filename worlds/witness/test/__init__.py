from test.bases import WorldTestBase
from test.general import gen_steps, setup_multiworld
from test.multiworld.test_multiworlds import MultiworldTestBase
from typing import Any, ClassVar, Dict, Iterable, List, Mapping, Union

from BaseClasses import CollectionState, Item

from .. import WitnessWorld


class WitnessTestBase(WorldTestBase):
    game = "The Witness"
    player: ClassVar[int] = 1

    world: WitnessWorld

    def can_beat_game_with_items(self, items: Iterable[Item]) -> bool:
        state = CollectionState(self.multiworld)
        for item in items:
            state.collect(item)
        return state.multiworld.can_beat_game(state)

    def assert_can_beat_with_minimally(self, required_item_counts: Mapping[str, int]):
        """
        Assert that the specified mapping of items is enough to beat the game,
        and that having one less of any item would result in the game being unbeatable.
        """
        # Find the actual items
        found_items = [item for item in self.multiworld.get_items() if item.name in required_item_counts]
        actual_items = {item_name: [] for item_name in required_item_counts}
        for item in found_items:
            if len(actual_items[item.name]) < required_item_counts[item.name]:
                actual_items[item.name].append(item)

        # Assert that enough items exist in the item pool to satisfy the specified required counts
        for item_name, item_objects in actual_items.items():
            self.assertEqual(
                len(item_objects),
                required_item_counts[item_name],
                f"Couldn't find {required_item_counts[item_name]} copies of item {item_name} available in the pool, "
                f"only found {len(item_objects)}",
            )

        # assert that multiworld is beatable with the items specified
        self.assertTrue(
            self.can_beat_game_with_items(item for items in actual_items.values() for item in items),
            f"Could not beat game with items: {required_item_counts}",
        )

        # assert that one less copy of any item would result in the multiworld being unbeatable
        for item_name, item_objects in actual_items.items():
            removed_item = item_objects.pop()
            self.assertFalse(
                self.can_beat_game_with_items(item for items in actual_items.values() for item in items),
                f"Game was beatable despite having {len(item_objects)} copies of {item_name} "
                f"instead of the specified {required_item_counts[item_name]}",
            )
            item_objects.append(removed_item)


class WitnessMultiworldTestBase(MultiworldTestBase):
    options_per_world: List[Dict[str, Any]]
    common_options: Dict[str, Any] = {}

    def setUp(self):
        self.multiworld = setup_multiworld([WitnessWorld] * len(self.options_per_world), ())

        for world, options in zip(self.multiworld.worlds.values(), self.options_per_world):
            for option_name, option_value in {**self.common_options, **options}.items():
                option = getattr(world.options, option_name)
                self.assertIsNotNone(option)

                option.value = option.from_any(option_value).value

        self.assertSteps(gen_steps)

    def collect_by_name(self, item_names: Union[str, Iterable[str]], player: int) -> List[Item]:
        items = self.get_items_by_name(item_names, player)
        for item in items:
            self.multiworld.state.collect(item)
        return items

    def get_items_by_name(self, item_names: Union[str, Iterable[str]], player: int) -> List[Item]:
        if isinstance(item_names, str):
            item_names = (item_names,)
        return [item for item in self.multiworld.itempool if item.name in item_names and item.player == player]
