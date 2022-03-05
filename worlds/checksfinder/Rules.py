from ..generic.Rules import set_rule, add_rule
from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin


# Sets rules on entrances and advancements that are always applied
def set_rules(world: MultiWorld, player: int):
    return True


# Sets rules on completion condition
def set_completion_rules(world: MultiWorld, player: int):

    width_req = world.max_width[player]-5
    height_req = world.max_height[player]-5
    bomb_req = world.max_bombs[player]-5
    completion_requirements = lambda state: \
        state.has("Map Width", player, width_req) and \
        state.has("Map Height", player, height_req) and \
        state.has("Map Bombs", player, bomb_req)
    world.completion_condition[player] = lambda state: completion_requirements(state)
