from worlds.AutoWorld import World, CollectionState
from worlds.generic.Rules import add_rule, set_rule
from .Locations import location_table, tihs_locations, zipline_unlocks, is_location_valid, contract_locations, \
    shop_locations
from .Types import HatType, ChapterIndex
from BaseClasses import Location, Entrance, Region
import typing


act_connections = {
    "Mafia Town - Act 2": ["Mafia Town - Act 1"],
    "Mafia Town - Act 3": ["Mafia Town - Act 1"],
    "Mafia Town - Act 4": ["Mafia Town - Act 2", "Mafia Town - Act 3"],
    "Mafia Town - Act 6": ["Mafia Town - Act 4"],
    "Mafia Town - Act 7": ["Mafia Town - Act 4"],
    "Mafia Town - Act 5": ["Mafia Town - Act 6", "Mafia Town - Act 7"],

    "Battle of the Birds - Act 2": ["Battle of the Birds - Act 1"],
    "Battle of the Birds - Act 3": ["Battle of the Birds - Act 1"],
    "Battle of the Birds - Act 4": ["Battle of the Birds - Act 2", "Battle of the Birds - Act 3"],
    "Battle of the Birds - Act 5": ["Battle of the Birds - Act 2", "Battle of the Birds - Act 3"],
    "Battle of the Birds - Finale A": ["Battle of the Birds - Act 4", "Battle of the Birds - Act 5"],
    "Battle of the Birds - Finale B": ["Battle of the Birds - Finale A"],

    "Subcon Forest - Finale": ["Subcon Forest - Act 1", "Subcon Forest - Act 2",
                               "Subcon Forest - Act 3", "Subcon Forest - Act 4",
                               "Subcon Forest - Act 5"],

    "The Arctic Cruise - Act 2":  ["The Arctic Cruise - Act 1"],
    "The Arctic Cruise - Finale": ["The Arctic Cruise - Act 2"],
}


def can_use_hat(state: CollectionState, world: World, hat: HatType) -> bool:
    return state.count("Yarn", world.player) >= get_hat_cost(world, hat)


def get_hat_cost(world: World, hat: HatType) -> int:
    cost: int = 0
    for h in world.get_hat_craft_order():
        cost += world.get_hat_yarn_costs().get(h)
        if h == hat:
            break

    return cost


def can_sdj(state: CollectionState, world: World):
    return can_use_hat(state, world, HatType.SPRINT)


def can_use_hookshot(state: CollectionState, world: World):
    return state.has("Hookshot Badge", world.player)


def has_relic_combo(state: CollectionState, world: World, relic: str) -> bool:
    return state.has_group(relic, world.player, len(world.item_name_groups[relic]))


def get_relic_count(state: CollectionState, world: World, relic: str) -> int:
    return state.count_group(relic, world.player)


def can_hit_bells(state: CollectionState, world: World):
    if world.multiworld.UmbrellaLogic[world.player].value == 0:
        return True

    return state.has("Umbrella", world.player) or can_use_hat(state, world, HatType.BREWING)


# Only use for rifts
def can_clear_act(state: CollectionState, world: World, act_entrance: str) -> bool:
    entrance: Entrance = world.multiworld.get_entrance(act_entrance, world.player)
    if not state.can_reach(entrance.connected_region, player=world.player):
        return False

    if "Free Roam" in entrance.connected_region.name:
        return True

    name: str = format("Act Completion (%s)" % entrance.connected_region.name)
    return world.multiworld.get_location(name, world.player).access_rule(state)


def can_clear_alpine(state: CollectionState, world: World) -> bool:
    return state.has("Birdhouse Cleared", world.player) and state.has("Lava Cake Cleared", world.player) \
            and state.has("Windmill Cleared", world.player) and state.has("Twilight Bell Cleared", world.player)


def can_clear_metro(state: CollectionState, world: World) -> bool:
    return state.has("Nyakuza Intro Cleared", world.player) \
           and state.has("Yellow Overpass Station Cleared", world.player) \
           and state.has("Yellow Overpass Manhole Cleared", world.player) \
           and state.has("Green Clean Station Cleared", world.player) \
           and state.has("Green Clean Manhole Cleared", world.player) \
           and state.has("Bluefin Tunnel Cleared", world.player) \
           and state.has("Pink Paw Station Cleared", world.player) \
           and state.has("Pink Paw Manhole Cleared", world.player)


def set_rules(world: World):
    dlc1: bool = bool(world.multiworld.EnableDLC1[world.player].value > 0)
    dlc2: bool = bool(world.multiworld.EnableDLC2[world.player].value > 0)

    # First, chapter access
    starting_chapter = ChapterIndex(world.multiworld.StartingChapter[world.player].value)
    world.set_chapter_cost(starting_chapter, 0)

    # Chapter costs increase progressively. Randomly decide the chapter order, except for Finale
    chapter_list: typing.List[ChapterIndex] = [ChapterIndex.MAFIA, ChapterIndex.BIRDS,
                                               ChapterIndex.SUBCON, ChapterIndex.ALPINE]

    final_chapter = ChapterIndex.FINALE
    if world.multiworld.EndGoal[world.player].value == 2:
        final_chapter = ChapterIndex.METRO
        chapter_list.append(ChapterIndex.FINALE)

    if dlc1:
        chapter_list.append(ChapterIndex.CRUISE)

    if dlc2 and final_chapter is not ChapterIndex.METRO:
        chapter_list.append(ChapterIndex.METRO)

    chapter_list.remove(starting_chapter)
    world.multiworld.random.shuffle(chapter_list)

    if starting_chapter is not ChapterIndex.ALPINE and (dlc1 or dlc2):
        index1: int = 69
        index2: int = 69
        lowest_index: int
        chapter_list.remove(ChapterIndex.ALPINE)

        if dlc1:
            index1 = chapter_list.index(ChapterIndex.CRUISE)

        if dlc2 and final_chapter is not ChapterIndex.METRO:
            index2 = chapter_list.index(ChapterIndex.METRO)

        lowest_index = min(index1, index2)
        if lowest_index == 0:
            pos = 0
        else:
            pos = world.multiworld.random.randint(0, lowest_index)

        chapter_list.insert(pos, ChapterIndex.ALPINE)

    lowest_cost: int = world.multiworld.LowestChapterCost[world.player].value
    highest_cost: int = world.multiworld.HighestChapterCost[world.player].value

    cost_increment: int = world.multiworld.ChapterCostIncrement[world.player].value
    min_difference: int = world.multiworld.ChapterCostMinDifference[world.player].value
    last_cost: int = 0
    cost: int
    loop_count: int = 0

    for chapter in chapter_list:
        min_range: int = lowest_cost + (cost_increment * loop_count)
        if min_range >= highest_cost:
            min_range = highest_cost-1

        value: int = world.multiworld.random.randint(min_range, min(highest_cost,
                                                                    max(lowest_cost, last_cost + cost_increment)))

        cost = world.multiworld.random.randint(value, min(value + cost_increment, highest_cost))
        if loop_count >= 1:
            if last_cost + min_difference > cost:
                cost = last_cost + min_difference

        cost = min(cost, highest_cost)
        world.set_chapter_cost(chapter, cost)
        last_cost = cost
        loop_count += 1

    world.set_chapter_cost(final_chapter, world.multiworld.random.randint(
                                                        world.multiworld.FinalChapterMinCost[world.player].value,
                                                        world.multiworld.FinalChapterMaxCost[world.player].value))

    add_rule(world.multiworld.get_entrance("Telescope -> Mafia Town", world.player),
             lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.MAFIA)))

    add_rule(world.multiworld.get_entrance("Telescope -> Battle of the Birds", world.player),
             lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.BIRDS)))

    add_rule(world.multiworld.get_entrance("Telescope -> Subcon Forest", world.player),
             lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.SUBCON)))

    add_rule(world.multiworld.get_entrance("Telescope -> Alpine Skyline", world.player),
             lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.ALPINE)))

    add_rule(world.multiworld.get_entrance("Telescope -> Time's End", world.player),
             lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.FINALE))
             and can_use_hat(state, world, HatType.BREWING) and can_use_hat(state, world, HatType.DWELLER))

    if dlc1:
        add_rule(world.multiworld.get_entrance("Telescope -> The Arctic Cruise", world.player),
                 lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.ALPINE))
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.CRUISE)))

    if dlc2:
        add_rule(world.multiworld.get_entrance("Telescope -> Nyakuza Metro", world.player),
                 lambda state: state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.ALPINE))
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.METRO))
                 and can_use_hat(state, world, HatType.DWELLER) and can_use_hat(state, world, HatType.ICE))

    if world.multiworld.ActRandomizer[world.player].value == 0:
        set_default_rift_rules(world)

    location: Location
    for (key, data) in location_table.items():
        if not is_location_valid(world, key):
            continue

        if key in contract_locations.keys():
            continue

        location = world.multiworld.get_location(key, world.player)

        # Not all locations in Alpine can be reached from The Illness has Spread
        # as many of the ziplines are blocked off
        if data.region == "Alpine Skyline Area":
            if key not in tihs_locations:
                add_rule(location, lambda state: state.can_reach("Alpine Free Roam", "Region", world.player), "and")
            else:
                add_rule(location, lambda state: can_use_hookshot(state, world))

        if data.region == "The Birdhouse" or data.region == "The Lava Cake" \
           or data.region == "The Windmill" or data.region == "The Twilight Bell":
            add_rule(location, lambda state: state.can_reach("Alpine Free Roam", "Region", world.player), "and")

        for hat in data.required_hats:
            if hat is not HatType.NONE:
                add_rule(location, lambda state, hat=hat: can_use_hat(state, world, hat))

        if data.hookshot:
            add_rule(location, lambda state: can_use_hookshot(state, world))

        if data.umbrella and world.multiworld.UmbrellaLogic[world.player].value > 0:
            add_rule(location, lambda state: state.has("Umbrella", world.player))

        if data.paintings > 0 and world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(location, lambda state, paintings=data.paintings:
                     state.count("Progressive Painting Unlock", world.player) >= paintings)

        if data.dweller_bell > 0:
            if data.dweller_bell == 1:  # Required to be hit regardless of Dweller Mask
                add_rule(location, lambda state: can_hit_bells(state, world))
            else:  # Can bypass with Dweller Mask
                add_rule(location, lambda state: can_hit_bells(state, world) or can_use_hat(state, world, HatType.DWELLER))

    set_specific_rules(world)

    if world.multiworld.LogicDifficulty[world.player].value >= 1:
        world.multiworld.SDJLogic[world.player].value = 1

    if world.multiworld.SDJLogic[world.player].value > 0:
        set_sdj_rules(world)

    if world.multiworld.ShuffleAlpineZiplines[world.player].value > 0:
        set_alps_zipline_rules(world)

    for (key, acts) in act_connections.items():
        if "Arctic Cruise" in key and not dlc1:
            continue

        i: int = 1
        entrance: Entrance = world.multiworld.get_entrance(key, world.player)
        region: Region = entrance.connected_region
        access_rules: typing.List[typing.Callable[[CollectionState], bool]] = []
        entrance.parent_region.exits.remove(entrance)
        del entrance.parent_region

        # Entrances to this act that we have to set access_rules on
        entrances: typing.List[Entrance] = []

        for act in acts:
            act_entrance: Entrance = world.multiworld.get_entrance(act, world.player)
            access_rules.append(act_entrance.access_rule)
            required_region = act_entrance.connected_region
            name: str = format("%s: Connection %i" % (key, i))
            new_entrance: Entrance = connect_regions(required_region, region, name, world.player)
            entrances.append(new_entrance)

            # Copy access rules from act completions
            if "Free Roam" not in required_region.name:
                rule: typing.Callable[[CollectionState], bool]
                name = format("Act Completion (%s)" % required_region.name)
                rule = world.multiworld.get_location(name, world.player).access_rule
                access_rules.append(rule)

            i += 1

        for e in entrances:
            for rules in access_rules:
                add_rule(e, rules)

    for entrance in world.multiworld.get_region("Alpine Free Roam", world.player).entrances:
        add_rule(entrance, lambda state: can_use_hookshot(state, world))
        if world.multiworld.UmbrellaLogic[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Umbrella", world.player))

    if world.multiworld.EndGoal[world.player].value == 1:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Time Piece Cluster", world.player)
    elif world.multiworld.EndGoal[world.player].value == 2:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Rush Hour Cleared", world.player)


def set_specific_rules(world: World):
    dlc1: bool = bool(world.multiworld.EnableDLC1[world.player].value > 0)

    add_rule(world.multiworld.get_entrance("Alpine Skyline - Finale", world.player),
             lambda state: can_clear_alpine(state, world))

    add_rule(world.multiworld.get_location("Mafia Boss Shop Item", world.player),
             lambda state: state.has("Time Piece", world.player, 12)
             and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.BIRDS)))

    add_rule(world.multiworld.get_location("Spaceship - Rumbi Abuse", world.player),
             lambda state: state.has("Time Piece", world.player, 4))

    # Normal logic
    if world.multiworld.LogicDifficulty[world.player].value == 0:
        add_rule(world.multiworld.get_entrance("-> The Birdhouse", world.player),
                 lambda state: can_use_hat(state, world, HatType.BREWING))

        add_rule(world.multiworld.get_location("Alpine Skyline - Yellow Band Hills", world.player),
                 lambda state: can_use_hat(state, world, HatType.BREWING))

        if dlc1:
            add_rule(world.multiworld.get_location("Act Completion (Time Rift - Deep Sea)", world.player),
                     lambda state: can_use_hat(state, world, HatType.DWELLER))

            add_rule(world.multiworld.get_location("Rock the Boat - Post Captain Rescue", world.player),
                     lambda state: can_use_hat(state, world, HatType.ICE))

            add_rule(world.multiworld.get_location("Act Completion (Rock the Boat)", world.player),
                     lambda state: can_use_hat(state, world, HatType.ICE))

    # Hard logic, includes SDJ stuff
    if world.multiworld.LogicDifficulty[world.player].value >= 1:
        add_rule(world.multiworld.get_location("Act Completion (Time Rift - The Twilight Bell)", world.player),
                 lambda state: can_use_hat(state, world, HatType.SPRINT)
                 and state.has("Scooter Badge", world.player), "or")

    # Expert logic
    if world.multiworld.LogicDifficulty[world.player].value >= 2:
        set_rule(world.multiworld.get_location("Alpine Skyline - The Twilight Path", world.player), lambda state: True)
    else:
        add_rule(world.multiworld.get_entrance("-> The Twilight Bell", world.player),
                 lambda state: can_use_hat(state, world, HatType.DWELLER))

    add_rule(world.multiworld.get_location("Mafia Town - Behind HQ Chest", world.player),
             lambda state: state.can_reach("Act Completion (Heating Up Mafia Town)", "Location", world.player)
             or state.can_reach("Down with the Mafia!", "Region", world.player)
             or state.can_reach("Cheating the Race", "Region", world.player)
             or state.can_reach("The Golden Vault", "Region", world.player))

    # Old guys don't appear in SCFOS
    add_rule(world.multiworld.get_location("Mafia Town - Old Man (Steel Beams)", world.player),
             lambda state: state.can_reach("Welcome to Mafia Town", "Region", world.player)
             or state.can_reach("Barrel Battle", "Region", world.player)
             or state.can_reach("Cheating the Race", "Region", world.player)
             or state.can_reach("The Golden Vault", "Region", world.player)
             or state.can_reach("Down with the Mafia!", "Region", world.player))

    add_rule(world.multiworld.get_location("Mafia Town - Old Man (Seaside Spaghetti)", world.player),
             lambda state: state.can_reach("Welcome to Mafia Town", "Region", world.player)
             or state.can_reach("Barrel Battle", "Region", world.player)
             or state.can_reach("Cheating the Race", "Region", world.player)
             or state.can_reach("The Golden Vault", "Region", world.player)
             or state.can_reach("Down with the Mafia!", "Region", world.player))

    # Only available outside She Came from Outer Space
    add_rule(world.multiworld.get_location("Mafia Town - Mafia Geek Platform", world.player),
             lambda state: state.can_reach("Welcome to Mafia Town", "Region", world.player)
             or state.can_reach("Barrel Battle", "Region", world.player)
             or state.can_reach("Down with the Mafia!", "Region", world.player)
             or state.can_reach("Cheating the Race", "Region", world.player)
             or state.can_reach("Heating Up Mafia Town", "Region", world.player)
             or state.can_reach("The Golden Vault", "Region", world.player))

    # Only available outside Down with the Mafia! (for some reason)
    add_rule(world.multiworld.get_location("Mafia Town - On Scaffolding", world.player),
             lambda state: state.can_reach("Welcome to Mafia Town", "Region", world.player)
             or state.can_reach("Barrel Battle", "Region", world.player)
             or state.can_reach("She Came from Outer Space", "Region", world.player)
             or state.can_reach("Cheating the Race", "Region", world.player)
             or state.can_reach("Heating Up Mafia Town", "Region", world.player)
             or state.can_reach("The Golden Vault", "Region", world.player))

    # For some reason, the brewing crate is removed in HUMT
    add_rule(world.multiworld.get_location("Mafia Town - Secret Cave", world.player),
             lambda state: state.has("HUMT Access", world.player), "or")

    # Can bounce across the lava to get this without Hookshot (need to die though)
    add_rule(world.multiworld.get_location("Mafia Town - Above Boats", world.player),
             lambda state: state.has("HUMT Access", world.player), "or")

    set_rule(world.multiworld.get_location("Act Completion (Cheating the Race)", world.player),
             lambda state: can_use_hat(state, world, HatType.TIME_STOP)
             or world.multiworld.CTRWithSprint[world.player].value > 0 and can_use_hat(state, world, HatType.SPRINT))

    set_rule(world.multiworld.get_location("Subcon Forest - Boss Arena Chest", world.player),
             lambda state: state.can_reach("Toilet of Doom", "Region", world.player)
             and (world.multiworld.ShuffleSubconPaintings[world.player].value == 0
             or state.has("Progressive Painting Unlock", world.player, 1))
             or state.can_reach("Your Contract has Expired", "Region", world.player))

    if world.multiworld.UmbrellaLogic[world.player].value > 0:
        add_rule(world.multiworld.get_location("Act Completion (Toilet of Doom)", world.player),
                 lambda state: state.has("Umbrella", world.player) or can_use_hat(state, world, HatType.BREWING))

    set_rule(world.multiworld.get_location("Act Completion (Time Rift - Village)", world.player),
             lambda state: can_use_hat(state, world, HatType.BREWING) or state.has("Umbrella", world.player)
             or can_use_hat(state, world, HatType.DWELLER))

    add_rule(world.multiworld.get_entrance("Subcon Forest - Act 2", world.player),
             lambda state: state.has("Snatcher's Contract - The Subcon Well", world.player))

    add_rule(world.multiworld.get_entrance("Subcon Forest - Act 3", world.player),
             lambda state: state.has("Snatcher's Contract - Toilet of Doom", world.player))

    add_rule(world.multiworld.get_entrance("Subcon Forest - Act 4", world.player),
             lambda state: state.has("Snatcher's Contract - Queen Vanessa's Manor", world.player))

    add_rule(world.multiworld.get_entrance("Subcon Forest - Act 5", world.player),
             lambda state: state.has("Snatcher's Contract - Mail Delivery Service", world.player))

    if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
        for key in contract_locations:
            if key == "Snatcher's Contract - The Subcon Well":
                continue
            
            add_rule(world.multiworld.get_location(key, world.player),
                     lambda state: state.has("Progressive Painting Unlock", world.player, 1))

    add_rule(world.multiworld.get_location("Alpine Skyline - Mystifying Time Mesa: Zipline", world.player),
             lambda state: can_use_hat(state, world, HatType.SPRINT) or can_use_hat(state, world, HatType.TIME_STOP))

    if world.multiworld.EnableDLC1[world.player].value > 0:
        add_rule(world.multiworld.get_entrance("Cruise Ship Entrance BV", world.player),
                 lambda state: can_use_hookshot(state, world))

        # This particular item isn't present in Act 3 for some reason, yes in vanilla too
        add_rule(world.multiworld.get_location("The Arctic Cruise - Toilet", world.player),
                 lambda state: state.can_reach("Bon Voyage!", "Region", world.player)
                 or state.can_reach("Ship Shape", "Region", world.player))

    if world.multiworld.EnableDLC2[world.player].value > 0:
        add_rule(world.multiworld.get_entrance("-> Bluefin Tunnel", world.player),
                 lambda state: state.has("Metro Ticket - Green", world.player)
                 or state.has("Metro Ticket - Blue", world.player))

        add_rule(world.multiworld.get_entrance("-> Pink Paw Station", world.player),
                 lambda state: state.has("Metro Ticket - Pink", world.player)
                 or state.has("Metro Ticket - Yellow", world.player) and state.has("Metro Ticket - Blue", world.player))

        add_rule(world.multiworld.get_entrance("Nyakuza Metro - Finale", world.player),
                 lambda state: can_clear_metro(state, world))

        add_rule(world.multiworld.get_location("Act Completion (Rush Hour)", world.player),
                 lambda state: state.has("Metro Ticket - Yellow", world.player)
                 and state.has("Metro Ticket - Blue", world.player)
                 and state.has("Metro Ticket - Pink", world.player))

        for key in shop_locations.keys():
            if "Green Clean Station Thug B" in key and is_location_valid(world, key):
                add_rule(world.multiworld.get_location(key, world.player),
                         lambda state: state.has("Metro Ticket - Yellow", world.player), "or")


def set_sdj_rules(world: World):
    add_rule(world.multiworld.get_location("Subcon Forest - Long Tree Climb Chest", world.player),
             lambda state: can_sdj(state, world)
             and (world.multiworld.ShuffleSubconPaintings[world.player].value == 0
             or state.count("Progressive Painting Unlock", world.player) >= 2), "or")

    add_rule(world.multiworld.get_location("Subcon Forest - Green and Purple Dweller Rocks", world.player),
             lambda state: can_sdj(state, world)
             and (world.multiworld.ShuffleSubconPaintings[world.player].value == 0
             or state.count("Progressive Painting Unlock", world.player) >= 3), "or")

    add_rule(world.multiworld.get_location("Alpine Skyline - The Birdhouse: Dweller Platforms Relic", world.player),
             lambda state: can_sdj(state, world), "or")

    add_rule(world.multiworld.get_location("Act Completion (Time Rift - Gallery)", world.player),
             lambda state: can_sdj(state, world), "or")

    add_rule(world.multiworld.get_location("Act Completion (Time Rift - Curly Tail Trail)", world.player),
             lambda state: can_sdj(state, world), "or")


def set_alps_zipline_rules(world: World):
    add_rule(world.multiworld.get_entrance("-> The Birdhouse", world.player),
             lambda state: state.has("Zipline Unlock - The Birdhouse Path", world.player))

    add_rule(world.multiworld.get_entrance("-> The Lava Cake", world.player),
             lambda state: state.has("Zipline Unlock - The Lava Cake Path", world.player))

    add_rule(world.multiworld.get_entrance("-> The Windmill", world.player),
             lambda state: state.has("Zipline Unlock - The Windmill Path", world.player))

    add_rule(world.multiworld.get_entrance("-> The Twilight Bell", world.player),
             lambda state: state.has("Zipline Unlock - The Twilight Bell Path", world.player))

    add_rule(world.multiworld.get_location("Act Completion (The Illness has Spread)", world.player),
             lambda state: state.has("Zipline Unlock - The Birdhouse Path", world.player)
             and state.has("Zipline Unlock - The Lava Cake Path", world.player)
             and state.has("Zipline Unlock - The Windmill Path", world.player))

    for (loc, zipline) in zipline_unlocks.items():
        add_rule(world.multiworld.get_location(loc, world.player), lambda state: state.has(zipline, world.player))


def reg_act_connection(world: World, region: typing.Union[str, Region], unlocked_entrance: typing.Union[str, Entrance]):
    reg: Region
    entrance: Entrance
    if isinstance(region, str):
        reg = world.multiworld.get_region(region, world.player)
    else:
        reg = region

    if isinstance(unlocked_entrance, str):
        entrance = world.multiworld.get_entrance(unlocked_entrance, world.player)
    else:
        entrance = unlocked_entrance

    world.multiworld.register_indirect_condition(reg, entrance)


# See randomize_act_entrances in Regions.py
# Called BEFORE set_rules!
def set_rift_rules(world: World, regions: typing.Dict[str, Region]):

    # This is accessing the regions in place of these time rifts, so we can set the rules on all the entrances.
    for entrance in regions["Time Rift - Gallery"].entrances:
        add_rule(entrance, lambda state: can_use_hat(state, world, HatType.BREWING)
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.BIRDS)))

    for entrance in regions["Time Rift - The Lab"].entrances:
        add_rule(entrance, lambda state: can_use_hat(state, world, HatType.DWELLER)
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.ALPINE)))

    for entrance in regions["Time Rift - Sewers"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Mafia Town - Act 4"))
        reg_act_connection(world, world.multiworld.get_entrance("Mafia Town - Act 4",
                                                                world.player).connected_region, entrance)

    for entrance in regions["Time Rift - Bazaar"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Mafia Town - Act 6"))
        reg_act_connection(world, world.multiworld.get_entrance("Mafia Town - Act 6",
                                                                world.player).connected_region, entrance)

    for entrance in regions["Time Rift - Mafia of Cooks"].entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Burger"))

    for entrance in regions["Time Rift - The Owl Express"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 2"))
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 3"))
        reg_act_connection(world, world.multiworld.get_entrance("Battle of the Birds - Act 2",
                                                                world.player).connected_region, entrance)
        reg_act_connection(world, world.multiworld.get_entrance("Battle of the Birds - Act 3",
                                                                world.player).connected_region, entrance)

    for entrance in regions["Time Rift - The Moon"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 4"))
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 5"))
        reg_act_connection(world, world.multiworld.get_entrance("Battle of the Birds - Act 4",
                                                                world.player).connected_region, entrance)
        reg_act_connection(world, world.multiworld.get_entrance("Battle of the Birds - Act 5",
                                                                world.player).connected_region, entrance)

    for entrance in regions["Time Rift - Dead Bird Studio"].entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Train"))

    for entrance in regions["Time Rift - Pipe"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Subcon Forest - Act 2"))
        reg_act_connection(world, world.multiworld.get_entrance("Subcon Forest - Act 2",
                                                                world.player).connected_region, entrance)

        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 2))

    for entrance in regions["Time Rift - Village"].entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Subcon Forest - Act 4"))
        reg_act_connection(world, world.multiworld.get_entrance("Subcon Forest - Act 4",
                                                                world.player).connected_region, entrance)

        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 2))

    for entrance in regions["Time Rift - Sleepy Subcon"].entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "UFO"))
        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 3))

    for entrance in regions["Time Rift - Curly Tail Trail"].entrances:
        add_rule(entrance, lambda state: state.has("Windmill Cleared", world.player))

    for entrance in regions["Time Rift - The Twilight Bell"].entrances:
        add_rule(entrance, lambda state: state.has("Twilight Bell Cleared", world.player))

    for entrance in regions["Time Rift - Alpine Skyline"].entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Crayon"))

    if world.multiworld.EnableDLC1[world.player].value > 0:
        for entrance in regions["Time Rift - Balcony"].entrances:
            add_rule(entrance, lambda state: can_clear_act(state, world, "The Arctic Cruise - Finale"))

        for entrance in regions["Time Rift - Deep Sea"].entrances:
            add_rule(entrance, lambda state: has_relic_combo(state, world, "Cake"))

    if world.multiworld.EnableDLC2[world.player].value > 0:
        for entrance in regions["Time Rift - Rumbi Factory"].entrances:
            add_rule(entrance, lambda state: has_relic_combo(state, world, "Necklace"))


# Basically the same as above, but without the need of the dict since we are just setting defaults
# Called if Act Rando is disabled
def set_default_rift_rules(world: World):

    for entrance in world.multiworld.get_region("Time Rift - Gallery", world.player).entrances:
        add_rule(entrance, lambda state: can_use_hat(state, world, HatType.BREWING)
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.BIRDS)))

    for entrance in world.multiworld.get_region("Time Rift - The Lab", world.player).entrances:
        add_rule(entrance, lambda state: can_use_hat(state, world, HatType.DWELLER)
                 and state.has("Time Piece", world.player, world.get_chapter_cost(ChapterIndex.ALPINE)))

    for entrance in world.multiworld.get_region("Time Rift - Sewers", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Mafia Town - Act 4"))
        reg_act_connection(world, "Down with the Mafia!", entrance.name)

    for entrance in world.multiworld.get_region("Time Rift - Bazaar", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Mafia Town - Act 6"))
        reg_act_connection(world, "Heating Up Mafia Town", entrance.name)

    for entrance in world.multiworld.get_region("Time Rift - Mafia of Cooks", world.player).entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Burger"))

    for entrance in world.multiworld.get_region("Time Rift - The Owl Express", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 2"))
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 3"))
        reg_act_connection(world, "Murder on the Owl Express", entrance.name)
        reg_act_connection(world, "Picture Perfect", entrance.name)

    for entrance in world.multiworld.get_region("Time Rift - The Moon", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 4"))
        add_rule(entrance, lambda state: can_clear_act(state, world, "Battle of the Birds - Act 5"))
        reg_act_connection(world, "Train Rush", entrance.name)
        reg_act_connection(world, "The Big Parade", entrance.name)

    for entrance in world.multiworld.get_region("Time Rift - Dead Bird Studio", world.player).entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Train"))

    for entrance in world.multiworld.get_region("Time Rift - Pipe", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Subcon Forest - Act 2"))
        reg_act_connection(world, "The Subcon Well", entrance.name)
        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 2))

    for entrance in world.multiworld.get_region("Time Rift - Village", world.player).entrances:
        add_rule(entrance, lambda state: can_clear_act(state, world, "Subcon Forest - Act 4"))
        reg_act_connection(world, "Queen Vanessa's Manor", entrance.name)
        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 2))

    for entrance in world.multiworld.get_region("Time Rift - Sleepy Subcon", world.player).entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "UFO"))
        if world.multiworld.ShuffleSubconPaintings[world.player].value > 0:
            add_rule(entrance, lambda state: state.has("Progressive Painting Unlock", world.player, 3))

    for entrance in world.multiworld.get_region("Time Rift - Curly Tail Trail", world.player).entrances:
        add_rule(entrance, lambda state: state.has("Windmill Cleared", world.player))

    for entrance in world.multiworld.get_region("Time Rift - The Twilight Bell", world.player).entrances:
        add_rule(entrance, lambda state: state.has("Twilight Bell Cleared", world.player))

    for entrance in world.multiworld.get_region("Time Rift - Alpine Skyline", world.player).entrances:
        add_rule(entrance, lambda state: has_relic_combo(state, world, "Crayon"))

    if world.multiworld.EnableDLC1[world.player].value > 0:
        for entrance in world.multiworld.get_region("Time Rift - Balcony", world.player).entrances:
            add_rule(entrance, lambda state: can_clear_act(state, world, "The Arctic Cruise - Finale"))

        for entrance in world.multiworld.get_region("Time Rift - Deep Sea", world.player).entrances:
            add_rule(entrance, lambda state: has_relic_combo(state, world, "Cake"))

    if world.multiworld.EnableDLC2[world.player].value > 0:
        for entrance in world.multiworld.get_region("Time Rift - Rumbi Factory", world.player).entrances:
            add_rule(entrance, lambda state: has_relic_combo(state, world, "Necklace"))


def connect_regions(start_region: Region, exit_region: Region, entrancename: str, player: int) -> Entrance:
    entrance = Entrance(player, entrancename, start_region)
    start_region.exits.append(entrance)
    entrance.connect(exit_region)
    return entrance
