from . import SVTestBase
from .. import options


class TestCropsanityRules(SVTestBase):
    options = {
        options.Cropsanity.internal_name: options.Cropsanity.option_enabled
    }

    def test_need_greenhouse_for_cactus(self):
        self.assert_cannot_reach_location("Harvest Cactus Fruit")

        self.multiworld.state.collect(self.create_item("Cactus Seeds"))
        self.multiworld.state.collect(self.create_item("Shipping Bin"))
        self.multiworld.state.collect(self.create_item("Desert Obelisk"))
        self.assert_cannot_reach_location("Harvest Cactus Fruit")

        self.multiworld.state.collect(self.create_item("Greenhouse"))
        self.assert_can_reach_location("Harvest Cactus Fruit")
