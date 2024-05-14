from worlds.generic.Rules import add_rule, set_rule

from . import MMX3World, item_groups
from .Names import LocationName, ItemName, RegionName, EventName
from .Weaknesses import boss_weaknesses

mavericks = [
    "Blizzard Buffalo",
    "Toxic Seahorse",
    "Tunnel Rhino",
    "Volt Catfish",
    "Crush Crawfish",
    "Neon Tiger",
    "Gravity Beetle",
    "Blast Hornet",
]

bosses = {
    "Blizzard Buffalo": [
        f"{RegionName.blizzard_buffalo_after_bit_byte} -> {RegionName.blizzard_buffalo_boss}",
        LocationName.doppler_lab_3_blizzard_buffalo,
        EventName.blizzard_buffalo_rematch
    ],
    "Toxic Seahorse": [
        f"{RegionName.toxic_seahorse_dam} -> {RegionName.toxic_seahorse_boss}",
        LocationName.doppler_lab_3_toxic_seahorse,
        EventName.toxic_seahorse_rematch
    ],
    "Tunnel Rhino": [
        f"{RegionName.tunnel_rhino_climbing} -> {RegionName.tunnel_rhino_boss}",
        LocationName.doppler_lab_3_tunnel_rhino,
        EventName.tunnel_rhino_rematch
    ],
    "Volt Catfish": [
        f"{RegionName.volt_catfish_inside} -> {RegionName.volt_catfish_boss}",
        LocationName.doppler_lab_3_volt_catfish,
        EventName.volt_catfish_rematch
    ],
    "Crush Crawfish": [
        f"{RegionName.crush_crawfish_inside} -> {RegionName.crush_crawfish_boss}",
        LocationName.doppler_lab_3_crush_crawfish,
        EventName.crush_crawfish_rematch
    ],
    "Neon Tiger": [
        f"{RegionName.neon_tiger_hill} -> {RegionName.neon_tiger_boss}",
        LocationName.doppler_lab_3_neon_tiger,
        EventName.neon_tiger_rematch
    ],
    "Gravity Beetle": [
        f"{RegionName.gravity_beetle_inside} -> {RegionName.gravity_beetle_boss}",
        LocationName.doppler_lab_3_gravity_beetle,
        EventName.gravity_beetle_rematch,
    ],
    "Blast Hornet": [
        f"{RegionName.blast_hornet_bit_byte} -> {RegionName.blast_hornet_boss}",
        LocationName.doppler_lab_3_blast_hornet,
        EventName.blast_hornet_rematch
    ],
    "Bit": [
        LocationName.bit_defeat
    ],
    "Byte": [
        LocationName.byte_defeat
    ],
    "Hotareeca": [
        f"{RegionName.toxic_seahorse_underwater} -> {RegionName.toxic_seahorse_hootareca}"
    ],
    "Hell Crusher": [
        f"{RegionName.tunnel_rhino_wall_jump} -> {RegionName.tunnel_rhino_hell_crusher}",
    ],
    "Worm Seeker-R": [
        f"{RegionName.neon_tiger_start} -> {RegionName.neon_tiger_worm}",
    ],
    "Shurikein": [
        f"{RegionName.blast_hornet_conveyors} -> {RegionName.blast_hornet_shurikein}",
    ],
    "Vile": [
        f"{RegionName.vile_before} -> {RegionName.vile_boss}",
    ],
    "Press Disposer": [
        LocationName.doppler_lab_1_boss,
        EventName.dr_doppler_lab_1_clear
    ],
    "Godkarmachine": [
        LocationName.doppler_lab_1_boss,
        EventName.dr_doppler_lab_1_clear
    ],
    "Dr. Doppler's Lab 2 Boss": [
        LocationName.doppler_lab_2_boss,
        EventName.dr_doppler_lab_2_clear
    ],
    "Doppler": [
        LocationName.doppler_lab_3_boss,
        EventName.dr_doppler_lab_3_clear
    ],
    "Sigma": [
        f"{RegionName.dr_doppler_lab_3_boss} -> {RegionName.dr_doppler_lab_4}"
    ],
    "Kaiser Sigma": [
        f"{RegionName.dr_doppler_lab_3_boss} -> {RegionName.dr_doppler_lab_4}"
    ]
}
        

def set_rules(world: MMX3World):
    player = world.player
    multiworld = world.multiworld
    jammed_buster = world.options.jammed_buster.value

    multiworld.completion_condition[player] = lambda state: state.has(ItemName.victory, player)

    # Hunter base entrance rules
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.blizzard_buffalo}", player),
             lambda state: state.has(ItemName.stage_blizzard_buffalo, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.toxic_seahorse}", player),
             lambda state: state.has(ItemName.stage_toxic_seahorse, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.tunnel_rhino}", player),
             lambda state: state.has(ItemName.stage_tunnel_rhino, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.volt_catfish}", player),
             lambda state: state.has(ItemName.stage_volt_catfish, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.crush_crawfish}", player),
             lambda state: state.has(ItemName.stage_crush_crawfish, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.neon_tiger}", player),
             lambda state: state.has(ItemName.stage_neon_tiger, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.gravity_beetle}", player),
             lambda state: state.has(ItemName.stage_gravity_beetle, player))
    set_rule(multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.blast_hornet}", player),
             lambda state: state.has(ItemName.stage_blast_hornet, player))

    # Doppler Lab entrance rules
    doppler_open = world.options.doppler_open
    entrance = multiworld.get_entrance(f"{RegionName.intro_stage} -> {RegionName.dr_doppler_lab}", player)

    if doppler_open == "multiworld":
        set_rule(entrance, lambda state: state.has(ItemName.stage_doppler_lab, player))
    if doppler_open in ("medals", "all") and world.options.doppler_medal_count.value > 0:
        add_rule(entrance, lambda state: state.has(ItemName.maverick_medal, player, world.options.doppler_medal_count.value))
    if doppler_open in ("weapons", "all") and world.options.doppler_weapon_count.value > 0:
        add_rule(entrance, lambda state: state.has_group("Weapons", player, world.options.doppler_weapon_count.value))
    if doppler_open in ("armor_upgrades", "all") and world.options.doppler_upgrade_count.value > 0:
        add_rule(entrance, lambda state: state.has_group("Armor Upgrades", player, world.options.doppler_upgrade_count.value))
    if doppler_open in ("heart_tanks", "all") and world.options.doppler_heart_tank_count.value > 0:
        add_rule(entrance, lambda state: state.has(ItemName.heart_tank, player, world.options.doppler_heart_tank_count.value))
    if doppler_open in ("sub_tanks", "all") and world.options.doppler_sub_tank_count.value > 0:
        add_rule(entrance, lambda state: state.has(ItemName.sub_tank, player, world.options.doppler_sub_tank_count.value))

    if world.options.logic_vile_required.value:
        add_rule(entrance, lambda state: state.has(EventName.vile_defeated, player))

    # Doppler Lab level rules
    set_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_1} -> {RegionName.dr_doppler_lab_2}", player),
             lambda state: state.has(EventName.dr_doppler_lab_1_clear, player))
    set_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_2} -> {RegionName.dr_doppler_lab_3}", player),
             lambda state: state.has(EventName.dr_doppler_lab_2_clear, player))
    set_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_3_boss} -> {RegionName.dr_doppler_lab_4}", player),
             lambda state: state.has(EventName.dr_doppler_lab_3_clear, player))

    # Set Boss rematch rules
    set_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_3_rematches} -> {RegionName.dr_doppler_lab_3_boss}", player),
             lambda state: state.has(EventName.boss_rematch_clear, player, world.options.doppler_lab_3_boss_rematch_count.value))
    
    # Vile entrance rules
    vile_open = world.options.vile_open
    entrance_blizzard = multiworld.get_entrance(f"{RegionName.blizzard_buffalo_start} -> {RegionName.vile}", player)
    entrance_volt = multiworld.get_entrance(f"{RegionName.volt_catfish_start} -> {RegionName.vile}", player)
    entrance_crush = multiworld.get_entrance(f"{RegionName.crush_crawfish_start} -> {RegionName.vile}", player)
    if vile_open == "multiworld":
        set_rule(entrance_blizzard, lambda state: state.has(ItemName.stage_vile, player))
        set_rule(entrance_volt, lambda state: state.has(ItemName.stage_vile, player))
        set_rule(entrance_crush, lambda state: state.has(ItemName.stage_vile, player))
    if vile_open in ("medals", "all") and world.options.vile_medal_count.value > 0:
        add_rule(entrance_blizzard, lambda state: state.has(ItemName.maverick_medal, player, world.options.vile_medal_count.value))
        add_rule(entrance_volt, lambda state: state.has(ItemName.maverick_medal, player, world.options.vile_medal_count.value))
        add_rule(entrance_crush, lambda state: state.has(ItemName.maverick_medal, player, world.options.vile_medal_count.value))
    if vile_open in ("weapons", "all") and world.options.vile_weapon_count.value > 0:
        add_rule(entrance_blizzard, lambda state: state.has_group("Weapons", player, world.options.vile_weapon_count.value))
        add_rule(entrance_volt, lambda state: state.has_group("Weapons", player, world.options.vile_weapon_count.value))
        add_rule(entrance_crush, lambda state: state.has_group("Weapons", player, world.options.vile_weapon_count.value))
    if vile_open in ("armor_upgrades", "all") and world.options.vile_upgrade_count.value > 0:
        add_rule(entrance_blizzard, lambda state: state.has_group("Armor Upgrades", player, world.options.vile_upgrade_count.value))
        add_rule(entrance_volt, lambda state: state.has_group("Armor Upgrades", player, world.options.vile_upgrade_count.value))
        add_rule(entrance_crush, lambda state: state.has_group("Armor Upgrades", player, world.options.vile_upgrade_count.value))
    if vile_open in ("heart_tanks", "all") and world.options.vile_heart_tank_count.value > 0:
        add_rule(entrance_blizzard, lambda state: state.has(ItemName.heart_tank, player, world.options.vile_heart_tank_count.value))
        add_rule(entrance_volt, lambda state: state.has(ItemName.heart_tank, player, world.options.vile_heart_tank_count.value))
        add_rule(entrance_crush, lambda state: state.has(ItemName.heart_tank, player, world.options.vile_heart_tank_count.value))
    if vile_open in ("sub_tanks", "all") and world.options.vile_sub_tank_count.value > 0:
        add_rule(entrance_blizzard, lambda state: state.has(ItemName.sub_tank, player, world.options.vile_sub_tank_count.value))
        add_rule(entrance_volt, lambda state: state.has(ItemName.sub_tank, player, world.options.vile_sub_tank_count.value))
        add_rule(entrance_crush, lambda state: state.has(ItemName.sub_tank, player, world.options.vile_sub_tank_count.value))

    # Bit & Byte arena entrance rules
    set_rule(multiworld.get_entrance(f"{RegionName.blast_hornet_bit_byte} -> {RegionName.bit_byte}", player), 
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.blizzard_buffalo_bit_byte} -> {RegionName.bit_byte}", player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.toxic_seahorse_bit_byte} -> {RegionName.bit_byte}", player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.tunnel_rhino_bit_byte} -> {RegionName.bit_byte}", player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.volt_catfish_bit_byte} -> {RegionName.bit_byte}", player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.crush_crawfish_bit_byte} -> {RegionName.bit_byte}", player), 
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.neon_tiger_bit_byte} -> {RegionName.bit_byte}", player), 
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_entrance(f"{RegionName.gravity_beetle_bit_byte} -> {RegionName.bit_byte}", player), 
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    
    # Set Bit rules
    set_rule(multiworld.get_location(LocationName.bit_defeat, player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    set_rule(multiworld.get_location(EventName.bit_defeated, player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.bit_medal_count.value))
    
    # Set Byte rules
    set_rule(multiworld.get_location(LocationName.byte_defeat, player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.byte_medal_count.value))
    set_rule(multiworld.get_location(EventName.byte_defeated, player),
             lambda state: state.has(ItemName.maverick_medal, player, world.options.byte_medal_count.value))

    # Set Blizzard Buffalo collectible rules
    set_rule(multiworld.get_location(LocationName.blizzard_buffalo_heart_tank, player),
             lambda state: (
                state.has(ItemName.tornado_fang, player) or
                state.has(ItemName.ride_chimera, player) or
                state.has(ItemName.ride_kangaroo, player)
             ))
    set_rule(multiworld.get_location(LocationName.blizzard_buffalo_sub_tank, player),
             lambda state: state.has(ItemName.third_armor_legs, player, 1))
    
    # Set Toxic Seahorse collectible rules
    set_rule(multiworld.get_location(LocationName.toxic_seahorse_kangaroo_ride, player),
             lambda state: (
                state.has(ItemName.third_armor_legs, player, 1) and
                (
                    state.has(ItemName.ride_frog, player) or 
                    (   
                        state.has(ItemName.frost_shield, player) and
                        state.has(ItemName.third_armor_arms, player, jammed_buster + 1)
                    )
                )
             ))
    
    set_rule(multiworld.get_location(LocationName.toxic_seahorse_leg, player),
             lambda state: (
                state.has(ItemName.ride_frog, player) or 
                (   
                    state.has(ItemName.frost_shield, player) and
                    state.has(ItemName.third_armor_arms, player, jammed_buster + 1)
                )
             ))
    
    # Set Tunnel Rhino collectible rules
    set_rule(multiworld.get_location(LocationName.tunnel_rhino_heart_tank, player),
             lambda state: (
                state.has(ItemName.third_armor_arms, player, jammed_buster + 1) and
                state.has(ItemName.triad_thunder, player)
             ))
    set_rule(multiworld.get_location(LocationName.tunnel_rhino_helmet, player),
             lambda state: (
                state.has(ItemName.third_armor_arms, player, jammed_buster + 1) and
                state.has(ItemName.triad_thunder, player)
             ))
    
    # Set Volt Catfish collectible rules
    set_rule(multiworld.get_location(LocationName.volt_catfish_sub_tank, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.volt_catfish_body, player),
             lambda state: (
                state.has(ItemName.third_armor_arms, player, jammed_buster + 1) and
                state.has(ItemName.gravity_well, player)
             ))
    
    # Set Crush Crawfish collectible rules
    set_rule(multiworld.get_location(LocationName.crush_crawfish_heart_tank, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.crush_crawfish_body, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.crush_crawfish_hawk_ride, player),
             lambda state: (
                state.has(ItemName.third_armor_arms, player, jammed_buster + 1) and
                state.has(ItemName.triad_thunder, player)
             ))
    
    # Set Neon Tiger collectible rules
    set_rule(multiworld.get_location(LocationName.neon_tiger_arms, player),
             lambda state: (
                state.has(ItemName.third_armor_legs, player, 1) and
                state.has(ItemName.tornado_fang, player)
             ))
    
    # Set Gravity Beetle collectible rules
    set_rule(multiworld.get_location(LocationName.gravity_beetle_heart_tank, player),
             lambda state: state.has(EventName.blast_hornet_defeated, player))
    set_rule(multiworld.get_location(LocationName.gravity_beetle_frog_ride, player),
             lambda state: state.has(ItemName.third_armor_legs, player, 1))
    set_rule(multiworld.get_location(LocationName.gravity_beetle_arms, player),
             lambda state: (
                state.has(ItemName.ride_chimera, player) or
                state.has(ItemName.ride_kangaroo, player) or
                state.has(ItemName.ride_hawk, player)
             ))
    
    # Set Blast Hornet collectible rules
    set_rule(multiworld.get_location(LocationName.blast_hornet_heart_tank, player),
             lambda state: state.has(ItemName.third_armor_legs, player, 1))
    set_rule(multiworld.get_location(LocationName.blast_hornet_chimera_ride, player),
             lambda state: state.has(ItemName.tornado_fang, player))
    set_rule(multiworld.get_location(LocationName.blast_hornet_helmet, player),
             lambda state: (
                state.has(ItemName.third_armor_legs, player, 2) or
                (
                    state.has(ItemName.third_armor_legs, player, 1) and
                    state.has(ItemName.ride_hawk, player)
                )
             ))
    
    # Handle bosses weakness
    if world.options.logic_boss_weakness.value or world.options.boss_weakness_strictness.value >= 2:
        add_boss_weakness_logic(world)

    # Z-Saber logic
    if world.options.logic_z_saber != "not_required":
        add_z_saber_logic(world)
        
    # Handle pickupsanity logic
    if world.options.pickupsanity.value:
        add_pickupsanity_logic(world)


def add_boss_weakness_logic(world):
    player = world.player
    multiworld = world.multiworld
    jammed_buster = world.options.jammed_buster.value

    if world.options.doppler_lab_3_boss_rematch_count.value == 0:
        for boss in mavericks:
            bosses[boss].pop()
            bosses[boss].pop()

    for boss, regions in bosses.items():
        weaknesses = boss_weaknesses[boss]
        for weakness in weaknesses:
            weakness = weakness[0]
            if weakness is not None:
                for region in regions:
                    is_entrance = "->" in region
                    if "Check Charge" in weakness[0]:
                        charge_level = int(weakness[0][-1:]) - 1
                        if len(weakness) == 1:
                            if is_entrance:
                                add_rule(multiworld.get_entrance(region, player),
                                        lambda state: state.has(ItemName.third_armor_arms, player, jammed_buster + charge_level))
                            else:
                                add_rule(multiworld.get_location(region, player),
                                        lambda state: state.has(ItemName.third_armor_arms, player, jammed_buster + charge_level))
                        else:
                            if is_entrance:
                                add_rule(multiworld.get_entrance(region, player),
                                        lambda state, weapons=tuple([weakness[1]]): (
                                            state.has(ItemName.third_armor_arms, player, jammed_buster + charge_level) and
                                            state.has_all(weapons, player)
                                        ))
                            else:
                                add_rule(multiworld.get_location(region, player),
                                        lambda state, weapons=tuple([weakness[1]]): (
                                            state.has(ItemName.third_armor_arms, player, jammed_buster + charge_level) and
                                            state.has_all(weapons, player)
                                        ))
                    else:
                        if is_entrance:
                            add_rule(multiworld.get_entrance(region, player),
                                    lambda state, weapons=tuple(weakness): state.has_all(weapons, player))
                        else:
                            add_rule(multiworld.get_location(region, player),
                                    lambda state, weapons=tuple(weakness): state.has_all(weapons, player))

    if world.options.boss_weakness_rando == "vanilla":
        if world.options.doppler_lab_2_boss == "volt_kurageil":
            # Set Volt Kurageil rules
            set_rule(multiworld.get_location(EventName.dr_doppler_lab_2_clear, player),
                    lambda state: (
                        state.has(ItemName.frost_shield, player) or
                        state.has(ItemName.triad_thunder, player)
                    ))
            set_rule(multiworld.get_location(LocationName.doppler_lab_2_boss, player),
                    lambda state: (
                        state.has(ItemName.frost_shield, player) or
                        state.has(ItemName.triad_thunder, player)
                    ))
        elif world.options.doppler_lab_2_boss == "vile":
            # Set Vile rematch rules
            set_rule(multiworld.get_location(EventName.dr_doppler_lab_2_clear, player),
                    lambda state: (
                        (
                            state.has(ItemName.parasitic_bomb, player) or 
                            state.has(ItemName.tornado_fang, player)
                        ) and (
                            state.has(ItemName.spinning_blade, player) or
                            state.has(ItemName.ray_splasher, player)
                        )
                    ))
            set_rule(multiworld.get_location(LocationName.doppler_lab_2_boss, player),
                    lambda state: (
                        (
                            state.has(ItemName.parasitic_bomb, player) or 
                            state.has(ItemName.tornado_fang, player)
                        ) and (
                            state.has(ItemName.spinning_blade, player) or
                            state.has(ItemName.ray_splasher, player)
                        )
                    ))

def add_z_saber_logic(world):
    player = world.player
    multiworld = world.multiworld

    logic_z_saber = world.options.logic_z_saber
    if logic_z_saber == 0:
        add_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab} -> {RegionName.dr_doppler_lab_1}", player),
                 lambda state: state.has(ItemName.z_saber, player))
    elif logic_z_saber == 1:
        add_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_1} -> {RegionName.dr_doppler_lab_2}", player), 
                 lambda state: state.has(ItemName.z_saber, player))
    elif logic_z_saber == 2:
        add_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_2} -> {RegionName.dr_doppler_lab_3}", player), 
                 lambda state: state.has(ItemName.z_saber, player))
    elif logic_z_saber == 3:
        add_rule(multiworld.get_location(LocationName.doppler_lab_3_boss, player), 
                 lambda state: state.has(ItemName.z_saber, player))
    elif logic_z_saber == 4:
        add_rule(multiworld.get_entrance(f"{RegionName.dr_doppler_lab_3_boss} -> {RegionName.dr_doppler_lab_4}", player), 
                 lambda state: state.has(ItemName.z_saber, player))


def add_pickupsanity_logic(world):
    player = world.player
    multiworld = world.multiworld

    # Volt Catfish
    set_rule(multiworld.get_location(LocationName.volt_catfish_energy_2, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.volt_catfish_energy_3, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.volt_catfish_hp_3, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.volt_catfish_hp_4, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    set_rule(multiworld.get_location(LocationName.volt_catfish_hp_5, player),
             lambda state: state.has_group("Ride Armors", player, 1))
    
    # Crush Crawfish
    set_rule(multiworld.get_location(LocationName.crush_crawfish_1up_1, player),
             lambda state: state.has(ItemName.tornado_fang, player))
    set_rule(multiworld.get_location(LocationName.crush_crawfish_1up_2, player),
             lambda state: state.has(ItemName.tornado_fang, player))
    
