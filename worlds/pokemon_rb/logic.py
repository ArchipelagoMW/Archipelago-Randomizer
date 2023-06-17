import worlds.pokemon_rb.poke_data as poke_data


def can_surf(state, player):
    return (((state.has("HM03 Surf", player) and can_learn_hm(state, "10000", player))
             or state.has("Flippers", player)) and (state.has("Soul Badge", player) or
             state.has(state.multiworld.worlds[player].extra_badges.get("Surf"), player)
             or state.multiworld.badges_needed_for_hm_moves[player].value == 0))


def can_cut(state, player):
    return ((state.has("HM01 Cut", player) and can_learn_hm(state, "100", player) or state.has("Master Sword", player))
             and (state.has("Cascade Badge", player) or
             state.has(state.multiworld.worlds[player].extra_badges.get("Cut"), player) or
             state.multiworld.badges_needed_for_hm_moves[player].value == 0))


def can_fly(state, player):
    return (((state.has("HM02 Fly", player) and can_learn_hm(state, "1000", player)) or state.has("Flute", player)) and
           (state.has("Thunder Badge", player) or state.has(state.multiworld.worlds[player].extra_badges.get("Fly"), player)
            or state.multiworld.badges_needed_for_hm_moves[player].value == 0))


def can_strength(state, player):
    return ((state.has("HM04 Strength", player) and can_learn_hm(state, "100000", player)) or
            state.has("Titan's Mitt", player)) and (state.has("Rainbow Badge", player) or
            state.has(state.multiworld.worlds[player].extra_badges.get("Strength"), player)
            or state.multiworld.badges_needed_for_hm_moves[player].value == 0)


def can_flash(state, player):
    return (((state.has("HM05 Flash", player) and can_learn_hm(state, "1000000", player)) or state.has("Lamp", player))
             and (state.has("Boulder Badge", player) or state.has(state.multiworld.worlds[player].extra_badges.get("Flash"),
             player) or state.multiworld.badges_needed_for_hm_moves[player].value == 0))


def can_learn_hm(state, move, player):
    for pokemon, data in state.multiworld.worlds[player].local_poke_data.items():
        if state.has(pokemon, player) and data["tms"][6] & int(move, 2):
            return True
    return False


def can_get_hidden_items(state, player):
    return state.has("Item Finder", player) or not state.multiworld.require_item_finder[player].value


def cerulean_cave(state, player):
    badges = len([item for item in
                  ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge",
                   "Volcano Badge", "Earth Badge"] if state.has(item, player)])
    key_items = (len([item for item in ["Bicycle", "Silph Scope", "Item Finder", "Super Rod", "Good Rod",
                                        "Old Rod", "Lift Key", "Card Key", "Town Map", "Coin Case", "S.S. Ticket",
                                        "Secret Key", "Poke Flute", "Mansion Key", "Safari Pass", "Plant Key",
                                        "Hideout Key", "Card Key 2F", "Card Key 3F", "Card Key 4F", "Card Key 5F",
                                        "Card Key 6F", "Card Key 7F", "Card Key 8F", "Card Key 9F", "Card Key 10F",
                                        "Card Key 11F", "Exp. All", "Fire Stone", "Thunder Stone", "Water Stone",
                                        "Leaf Stone"] if state.has(item, player)])
                 + min(state.count("Progressive Card Key", player), 10))
    return (badges >= state.multiworld.cerulean_cave_badges_condition[player].value
            and key_items >= state.multiworld.cerulean_cave_key_items_condition[player].total)


def can_pass_guards(state, player):
    if state.multiworld.tea[player]:
        return state.has("Tea", player)
    else:
        return state.has("Vending Machine Drinks", player)


def has_badges(state, count, player):
    return len([item for item in ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Marsh Badge",
                                  "Soul Badge", "Volcano Badge", "Earth Badge"] if state.has(item, player)]) >= count


def oaks_aide(state, count, player):
    return ((not state.multiworld.require_pokedex[player] or state.has("Pokedex", player))
            and has_pokemon(state, count, player))


def has_pokemon(state, count, player):
    obtained_pokemon = set()
    for pokemon in poke_data.pokemon_data.keys():
        if state.has(pokemon, player) or state.has(f"Static {pokemon}", player):
            obtained_pokemon.add(pokemon)

    return len(obtained_pokemon) >= count


def fossil_checks(state, count, player):
    return (state.can_reach('Mt Moon B2F', 'Region', player) and
            state.can_reach('Cinnabar Lab Fossil Room', 'Region', player) and
            state.can_reach('Cinnabar Island', 'Region', player) and len(
        [item for item in ["Dome Fossil", "Helix Fossil", "Old Amber"] if state.has(item, player)]) >= count)


def cinnabar_gym(state, player):
    # ensures higher level Pokémon are obtainable before Cinnabar Gym is in logic
    return ((state.multiworld.old_man[player] != "vanilla") or (not state.multiworld.extra_key_items[player]) or
            state.has("Mansion Key", player) or state.has("Oak's Parcel", player) or can_surf(state, player))


def dojo(state, player):
    # ensures higher level Pokémon are obtainable before Fighting Dojo is in logic
    return (can_pass_guards(state, player) or state.has("Oak's Parcel", player) or
            can_surf(state, player))


def card_key(state, floor, player):
    return state.has(f"Card Key {floor}F", player) or state.has("Card Key", player) or \
           state.has("Progressive Card Key", player, floor - 1)


def rock_tunnel(state, player):
    return can_flash(state, player) or not state.multiworld.dark_rock_tunnel_logic[player]


def evolve_level(state, level, player):
    return len([item for item in (
        "Defeat Brock", "Defeat Misty", "Defeat Lt. Surge", "Defeat Erika", "Defeat Koga", "Defeat Blaine",
        "Defeat Sabrina", "Defeat Viridian Gym Giovanni") if state.has(item, player)]) > level / 7
