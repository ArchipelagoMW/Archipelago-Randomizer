from BaseClasses import MultiWorld
from .Names import LocationName, ItemName
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


class LegacyLogic(LogicMixin):
    def _legacy_has_any_vendors(self, player: int) -> bool:
        return self.has_any({ItemName.blacksmith, ItemName.enchantress}, player)

    def _legacy_has_all_vendors(self, player: int) -> bool:
        return self.has_all({ItemName.blacksmith, ItemName.enchantress}, player)

    def _legacy_has_stat_upgrades(self, player: int, amount: int) -> bool:
        return self._legacy_stat_upgrade_count(player) >= amount

    def _legacy_total_stat_upgrades_count(self, player: int) -> int:
        return int(self.world.health_pool[player]) + \
               int(self.world.mana_pool[player]) + \
               int(self.world.attack_pool[player]) + \
               int(self.world.magic_damage_pool[player]) + \
               int(self.world.armor_pool[player]) + \
               int(self.world.equip_pool[player])

    def _legacy_stat_upgrade_count(self, player: int) -> int:
        return self.item_count(ItemName.health, player) + self.item_count(ItemName.mana, player) + \
               self.item_count(ItemName.attack, player) + self.item_count(ItemName.magic_damage, player) + \
               self.item_count(ItemName.armor, player) + self.item_count(ItemName.equip, player)


def set_rules(world: MultiWorld, player: int):
    # Chests
    if world.universal_chests[player]:
        for i in range(0, world.chests_per_zone[player]):
            set_rule(world.get_location(f"Chest {i + 1 + (world.chests_per_zone[player] * 1)}", player),
                     lambda state: state.has(ItemName.boss_castle, player))
            set_rule(world.get_location(f"Chest {i + 1 + (world.chests_per_zone[player] * 2)}", player),
                     lambda state: state.has(ItemName.boss_forest, player))
            set_rule(world.get_location(f"Chest {i + 1 + (world.chests_per_zone[player] * 3)}", player),
                     lambda state: state.has(ItemName.boss_tower, player))
    else:
        for i in range(0, world.chests_per_zone[player]):
            set_rule(world.get_location(f"{LocationName.garden} - Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_castle, player))
            set_rule(world.get_location(f"{LocationName.tower} - Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_forest, player))
            set_rule(world.get_location(f"{LocationName.dungeon} - Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_tower, player))

    # Fairy Chests
    if world.universal_fairy_chests[player]:
        for i in range(0, world.fairy_chests_per_zone[player]):
            set_rule(world.get_location(f"Fairy Chest {i + 1 + (world.fairy_chests_per_zone[player] * 1)}", player),
                     lambda state: state.has(ItemName.boss_castle, player))
            set_rule(world.get_location(f"Fairy Chest {i + 1 + (world.fairy_chests_per_zone[player] * 2)}", player),
                     lambda state: state.has(ItemName.boss_forest, player))
            set_rule(world.get_location(f"Fairy Chest {i + 1 + (world.fairy_chests_per_zone[player] * 3)}", player),
                     lambda state: state.has(ItemName.boss_tower, player))
    else:
        for i in range(0, world.fairy_chests_per_zone[player]):
            set_rule(world.get_location(f"{LocationName.garden} - Fairy Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_castle, player))
            set_rule(world.get_location(f"{LocationName.tower} - Fairy Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_forest, player))
            set_rule(world.get_location(f"{LocationName.dungeon} - Fairy Chest {i + 1}", player),
                     lambda state: state.has(ItemName.boss_tower, player))

    # Vendors
    if world.vendors[player] == "early":
        set_rule(world.get_location(LocationName.castle, player),
                 lambda state: state._legacy_has_all_vendors(player))
    elif world.vendors[player] == "normal":
        set_rule(world.get_location(LocationName.garden, player),
                 lambda state: state._legacy_has_any_vendors(player))
    elif world.vendors[player] == "anywhere":
        pass  # it can be anywhere, so no rule for this!

    # Architect
    if world.architect[player] == "early":
        set_rule(world.get_location(LocationName.castle, player),
                 lambda state: state.has(ItemName.architect, player))

    # Diaries
    for i in range(0, 5):
        set_rule(world.get_location(f"Diary {i + 6}", player),
                 lambda state: state.has(ItemName.boss_castle, player))
        set_rule(world.get_location(f"Diary {i + 11}", player),
                 lambda state: state.has(ItemName.boss_forest, player))
        set_rule(world.get_location(f"Diary {i + 16}", player),
                 lambda state: state.has(ItemName.boss_tower, player))
        set_rule(world.get_location(f"Diary {i + 21}", player),
                 lambda state: state.has(ItemName.boss_dungeon, player))

    # Scale each manor location.
    set_rule(world.get_location(LocationName.manor_left_wing_window, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_left_wing_roof, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_right_wing_window, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_right_wing_roof, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_left_big_base, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_right_big_base, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_left_tree1, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_left_tree2, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_right_tree, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.manor_left_big_upper1, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_big_upper2, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_big_windows, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_big_roof, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_far_base, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_far_roof, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_left_extension, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_right_big_upper, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_right_big_roof, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_right_extension, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.manor_right_high_base, player),
             lambda state: state.has(ItemName.boss_tower, player))
    set_rule(world.get_location(LocationName.manor_right_high_upper, player),
             lambda state: state.has(ItemName.boss_tower, player))
    set_rule(world.get_location(LocationName.manor_right_high_tower, player),
             lambda state: state.has(ItemName.boss_tower, player))
    set_rule(world.get_location(LocationName.manor_observatory_base, player),
             lambda state: state.has(ItemName.boss_tower, player))
    set_rule(world.get_location(LocationName.manor_observatory_scope, player),
             lambda state: state.has(ItemName.boss_tower, player))

    # Standard Zone Progression
    set_rule(world.get_location(LocationName.garden, player),
             lambda state: state._legacy_has_stat_upgrades(player, 0.125 * state._legacy_total_stat_upgrades_count(player)) and
                           state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.tower, player),
             lambda state: state._legacy_has_stat_upgrades(player, 0.3125 * state._legacy_total_stat_upgrades_count(player)) and
                           state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.dungeon, player),
             lambda state: state._legacy_has_stat_upgrades(player, 0.5 * state._legacy_total_stat_upgrades_count(player)) and
                           state.has(ItemName.boss_tower, player))

    # Bosses
    set_rule(world.get_location(LocationName.boss_castle, player),
             lambda state: state.has(ItemName.boss_castle, player))
    set_rule(world.get_location(LocationName.boss_forest, player),
             lambda state: state.has(ItemName.boss_forest, player))
    set_rule(world.get_location(LocationName.boss_tower, player),
             lambda state: state.has(ItemName.boss_tower, player))
    set_rule(world.get_location(LocationName.boss_dungeon, player),
             lambda state: state.has(ItemName.boss_dungeon, player))
    set_rule(world.get_location(LocationName.fountain, player),
             lambda state: state._legacy_has_stat_upgrades(player, 0.625 * state._legacy_total_stat_upgrades_count(player)) and
                           state.has(ItemName.boss_dungeon, player))

    world.completion_condition[player] = lambda state: state.has(ItemName.boss_fountain, player)
