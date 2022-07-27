import logging
from typing import Optional

from BaseClasses import Boss
from Fill import FillError


def BossFactory(boss: str, player: int) -> Optional[Boss]:
    if boss in boss_table:
        enemizer_name, defeat_rule = boss_table[boss]
        return Boss(boss, enemizer_name, defeat_rule, player)
    raise Exception('Unknown Boss: %s', boss)


def ArmosKnightsDefeatRule(state, player: int):
    # Magic amounts are probably a bit overkill
    return (
            state.has_melee_weapon(player) or
            state.can_shoot_arrows(player) or
            (state.has('Cane of Somaria', player) and state.can_extend_magic(player, 10)) or
            (state.has('Cane of Byrna', player) and state.can_extend_magic(player, 16)) or
            (state.has('Ice Rod', player) and state.can_extend_magic(player, 32)) or
            (state.has('Fire Rod', player) and state.can_extend_magic(player, 32)) or
            state.has('Blue Boomerang', player) or
            state.has('Red Boomerang', player))


def LanmolasDefeatRule(state, player: int):
    return (
            state.has_melee_weapon(player) or
            state.has('Fire Rod', player) or
            state.has('Ice Rod', player) or
            state.has('Cane of Somaria', player) or
            state.has('Cane of Byrna', player) or
            state.can_shoot_arrows(player))


def MoldormDefeatRule(state, player: int):
    return state.has_melee_weapon(player)


def HelmasaurKingDefeatRule(state, player: int):
    # TODO: technically possible with the hammer
    return state.has_sword(player) or state.can_shoot_arrows(player)


def ArrghusDefeatRule(state, player: int):
    if not state.has('Hookshot', player):
        return False
    # TODO: ideally we would have a check for bow and silvers, which combined with the
    # hookshot is enough. This is not coded yet because the silvers that only work in pyramid feature
    # makes this complicated
    if state.has_melee_weapon(player):
        return True

    return ((state.has('Fire Rod', player) and (state.can_shoot_arrows(player) or state.can_extend_magic(player,
                                                                                                         12))) or  # assuming mostly gitting two puff with one shot
            (state.has('Ice Rod', player) and (state.can_shoot_arrows(player) or state.can_extend_magic(player, 16))))


def MothulaDefeatRule(state, player: int):
    return (
            state.has_melee_weapon(player) or
            (state.has('Fire Rod', player) and state.can_extend_magic(player, 10)) or
            # TODO: Not sure how much (if any) extend magic is needed for these two, since they only apply
            # to non-vanilla locations, so are harder to test, so sticking with what VT has for now:
            (state.has('Cane of Somaria', player) and state.can_extend_magic(player, 16)) or
            (state.has('Cane of Byrna', player) and state.can_extend_magic(player, 16)) or
            state.can_get_good_bee(player)
    )


def BlindDefeatRule(state, player: int):
    return state.has_melee_weapon(player) or state.has('Cane of Somaria', player) or state.has('Cane of Byrna', player)


def KholdstareDefeatRule(state, player: int):
    return (
            (
                    state.has('Fire Rod', player) or
                    (
                            state.has('Bombos', player) and
                            (state.has_sword(player) or state.world.swordless[player])
                    )
            ) and
            (
                    state.has_melee_weapon(player) or
                    (state.has('Fire Rod', player) and state.can_extend_magic(player, 20)) or
                    (
                            state.has('Fire Rod', player) and
                            state.has('Bombos', player) and
                            state.world.swordless[player] and
                            state.can_extend_magic(player, 16)
                    )
            )
    )


def VitreousDefeatRule(state, player: int):
    return state.can_shoot_arrows(player) or state.has_melee_weapon(player)


def TrinexxDefeatRule(state, player: int):
    if not (state.has('Fire Rod', player) and state.has('Ice Rod', player)):
        return False
    return state.has('Hammer', player) or state.has('Tempered Sword', player) or state.has('Golden Sword', player) or \
           (state.has('Master Sword', player) and state.can_extend_magic(player, 16)) or \
           (state.has_sword(player) and state.can_extend_magic(player, 32))


def AgahnimDefeatRule(state, player: int):
    return state.has_sword(player) or state.has('Hammer', player) or state.has('Bug Catching Net', player)


def GanonDefeatRule(state, player: int):
    if state.world.swordless[player]:
        return state.has('Hammer', player) and \
               state.has_fire_source(player) and \
               state.has('Silver Bow', player) and \
               state.can_shoot_arrows(player)

    can_hurt = state.has_beam_sword(player)
    common = can_hurt and state.has_fire_source(player)
    # silverless ganon may be needed in anything higher than no glitches
    if state.world.logic[player] != 0:
        # need to light torch a sufficient amount of times
        return common and (state.has('Tempered Sword', player) or state.has('Golden Sword', player) or (
                state.has('Silver Bow', player) and state.can_shoot_arrows(player)) or
                           state.has('Lamp', player) or state.can_extend_magic(player, 12))

    else:
        return common and state.has('Silver Bow', player) and state.can_shoot_arrows(player)


boss_table = {
    'Armos Knights': ('Armos', ArmosKnightsDefeatRule),
    'Lanmolas': ('Lanmola', LanmolasDefeatRule),
    'Moldorm': ('Moldorm', MoldormDefeatRule),
    'Helmasaur King': ('Helmasaur', HelmasaurKingDefeatRule),
    'Arrghus': ('Arrghus', ArrghusDefeatRule),
    'Mothula': ('Mothula', MothulaDefeatRule),
    'Blind': ('Blind', BlindDefeatRule),
    'Kholdstare': ('Kholdstare', KholdstareDefeatRule),
    'Vitreous': ('Vitreous', VitreousDefeatRule),
    'Trinexx': ('Trinexx', TrinexxDefeatRule),
    'Agahnim': ('Agahnim', AgahnimDefeatRule),
    'Agahnim2': ('Agahnim2', AgahnimDefeatRule)
}

boss_location_table = [
        ('Ganons Tower', 'top'),
        ('Tower of Hera', None),
        ('Skull Woods', None),
        ('Ganons Tower', 'middle'),
        ('Eastern Palace', None),
        ('Desert Palace', None),
        ('Palace of Darkness', None),
        ('Swamp Palace', None),
        ('Thieves Town', None),
        ('Ice Palace', None),
        ('Misery Mire', None),
        ('Turtle Rock', None),
        ('Ganons Tower', 'bottom'),
    ]


def can_place_boss(boss: str, dungeon_name: str, level: Optional[str] = None) -> bool:
    # blacklist approach
    if boss in {"Agahnim", "Agahnim2", "Ganon"}:
        return False

    if dungeon_name == 'Ganons Tower':
        if level == 'top':
            if boss in {"Armos Knights", "Arrghus", "Blind", "Trinexx", "Lanmolas"}:
                return False
        elif level == 'middle':
            if boss == "Blind":
                return False

    elif dungeon_name == 'Tower of Hera':
        if boss in {"Armos Knights", "Arrghus", "Blind", "Trinexx", "Lanmolas"}:
            return False

    elif dungeon_name == 'Skull Woods':
        if boss == "Trinexx":
            return False

    return True

restrictive_boss_locations = {}
for location in boss_location_table:
    restrictive_boss_locations[location] = not all(can_place_boss(boss, *location)
                                               for boss in boss_table if not boss.startswith("Agahnim"))

def place_boss(world, player: int, boss: str, location: str, level: Optional[str]):
    if location == 'Ganons Tower' and world.mode[player] == 'inverted':
        location = 'Inverted Ganons Tower'
    logging.debug('Placing boss %s at %s', boss, location + (' (' + level + ')' if level else ''))
    world.get_dungeon(location, player).bosses[level] = BossFactory(boss, player)

def format_boss_location(location, level):
    return location + (' (' + level + ')' if level else '')

def place_bosses(world, player: int):
    if world.boss_shuffle[player] == 'none':
        return
    # Most to least restrictive order
    boss_locations = boss_location_table.copy()
    world.random.shuffle(boss_locations)
    boss_locations.sort(key= lambda location: -int(restrictive_boss_locations[location]))

    all_bosses = sorted(boss_table.keys())  # sorted to be deterministic on older pythons
    placeable_bosses = [boss for boss in all_bosses if boss not in ['Agahnim', 'Agahnim2', 'Ganon']]

    shuffle_mode = world.boss_shuffle[player]
    already_placed_bosses = []
    if ";" in shuffle_mode:
        bosses = shuffle_mode.split(";")
        shuffle_mode = bosses.pop()
        for boss in bosses:
            if "-" in boss:
                loc, boss = boss.split("-")
                boss = boss.title()
                level = None
                if loc.split(" ")[-1] in {"top", "middle", "bottom"}:
                    # split off level
                    loc = loc.split(" ")
                    level = loc[-1]
                    loc = " ".join(loc[:-1])
                loc = loc.title().replace("Of", "of")
                if can_place_boss(boss, loc, level) and (loc, level) in boss_locations:
                    place_boss(world, player, boss, loc, level)
                    already_placed_bosses.append(boss)
                    boss_locations.remove((loc, level))
                else:
                    raise Exception(f"Cannot place {boss} at {format_boss_location(loc, level)} for player {player}.")
            else:
                boss = boss.title()
                boss_locations, already_placed_bosses = place_where_possible(world, player, boss, boss_locations)

    if shuffle_mode == "none":
        return  # vanilla bosses come pre-placed

    if shuffle_mode in ["basic", "full"]:
        if world.boss_shuffle[player] == "basic":  # vanilla bosses shuffled
            bosses = placeable_bosses + ['Armos Knights', 'Lanmolas', 'Moldorm']
        else:  # all bosses present, the three duplicates chosen at random
            bosses = placeable_bosses + world.random.sample(placeable_bosses, 3)

        # there is probably a better way to do this
        while already_placed_bosses:
            # remove already manually placed bosses, to prevent for example triple Lanmolas
            boss = already_placed_bosses.pop()
            if boss in bosses:
                bosses.remove(boss)
            # there may be more bosses than locations at this point, depending on manual placement

        logging.debug('Bosses chosen %s', bosses)

        world.random.shuffle(bosses)
        for loc, level in boss_locations:
            for _ in range(len(bosses)):
                boss = bosses.pop()
                if can_place_boss(boss, loc, level):
                    break
                # put the boss back in queue
                bosses.insert(0, boss)  # this would be faster with deque,
                # but the deque size is small enough that it should not matter

            else:
                raise FillError(f'Could not place boss for location {format_boss_location(loc, level)}')

            place_boss(world, player, boss, loc, level)

    elif shuffle_mode == "chaos":  # all bosses chosen at random
        for loc, level in boss_locations:
            try:
                boss = world.random.choice(
                    [b for b in placeable_bosses if can_place_boss(b, loc, level)])
            except IndexError:
                raise FillError(f'Could not place boss for location {format_boss_location(loc, level)}')
            else:
                place_boss(world, player, boss, loc, level)

    elif shuffle_mode == "singularity":
        primary_boss = world.random.choice(placeable_bosses)
        remaining_boss_locations, _ = place_where_possible(world, player, primary_boss, boss_locations)
        if remaining_boss_locations:
            # pick a boss to go into the remaining locations
            remaining_boss = world.random.choice([boss for boss in placeable_bosses if all(
                can_place_boss(boss, loc, level) for loc, level in remaining_boss_locations)])
            remaining_boss_locations, _ = place_where_possible(world, player, remaining_boss, remaining_boss_locations)
            if remaining_boss_locations:
                raise Exception("Unfilled boss locations!")
    else:
        raise FillError(f"Could not find boss shuffle mode {shuffle_mode}")


def place_where_possible(world, player: int, boss: str, boss_locations):
    remainder = []
    placed_bosses = []
    for loc, level in boss_locations:
        # place that boss where it can go
        if can_place_boss(boss, loc, level):
            place_boss(world, player, boss, loc, level)
            placed_bosses.append(boss)
        else:
            remainder.append((loc, level))
    return remainder, placed_bosses
