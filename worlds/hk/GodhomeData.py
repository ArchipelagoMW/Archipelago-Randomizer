from functools import partial


godhome_event_names = ["Godhome_Flower_Quest", "Defeated_Pantheon_5", "GG_Atrium_Roof", "Defeated_Pantheon_1", "Defeated_Pantheon_2", "Defeated_Pantheon_3", "Opened_Pantheon_4", "Defeated_Pantheon_4", "GG_Atrium", "Hit_Pantheon_5_Unlock_Orb", "GG_Workshop", "Can_Damage_Crystal_Guardian", 'Defeated_Any_Soul_Warrior', "Defeated_Colosseum_3", "COMBAT[Radiance]", "COMBAT[Pantheon_1]", "COMBAT[Pantheon_2]", "COMBAT[Pantheon_3]", "COMBAT[Pantheon_4]", "COMBAT[Pantheon_5]", "COMBAT[Colosseum_3]", 'PROFICIENTCOMBAT', 'DIFFICULTSKIPS', "CURSED", 'Warp-Junk_Pit_to_Godhome', 'Bench-Godhome_Atrium', 'Bench-Hall_of_Gods', '*Boss_Geo-Massive_Moss_Charger/', 'Bench-Godhome_Atrium/', 'Bench-Hall_of_Gods/', 'Room_Colosseum_01[left1]/', "GODTUNERUNLOCK", 'WARPSTARTTOBENCH', "GG_Waterways", "Warp-Godhome_to_Junk_Pit", "NAILCOMBAT", "BOSS", "AERIALMINIBOSS", "ANYDASH", "FULLDASH", "SIDESLASH", "MILDCOMBATSKIPS", "SPICYCOMBATSKIPS", "FULLSHADOWDASH", "LEFTSHADOWDASH", "RIGHTSHADOWDASH", "ANYSHADOWDASH", "ANYCLAW"]


def set_godhome_rules(hk_world, hk_set_rule):
    player = hk_world.player
    fn = partial(hk_set_rule, hk_world)

    required_events = {
        # siple flowerquest logic for now as POC that includes normal flowerquest
        "Godhome_Flower_Quest": lambda state: (state.count('LEFTDASH', player) or state.count('LEFTSUPERDASH', player) and (state.count('RIGHTCLAW', player) or state.count('WINGS', player)) or state.count('WINGS', player) and state._hk_option(player, 'DifficultSkips')) and state.count('Room_Mansion[left1]', player) and state.count('Fungus3_49[right1]', player) and state.count('GG_Waterways[door1]', player),

        "Defeated_Pantheon_5": lambda state: state.count('GG_Atrium_Roof', player) and state.count('WINGS', player) and state.count('ANYCLAW', player) and ((state.count('Defeated_Pantheon_1', player) and state.count('Defeated_Pantheon_2', player) and state.count('Defeated_Pantheon_3', player) and state.count('Defeated_Pantheon_4', player) and state.count('COMBAT[Radiance]', player)) or (False) and state.count('COMBAT[Pantheon_5]', player)),
        "GG_Atrium_Roof": lambda state: state.count('GG_Atrium', player) and state.count('Hit_Pantheon_5_Unlock_Orb', player) and state.count('LEFTCLAW', player),

        "Defeated_Pantheon_1": lambda state: state.count('GG_Atrium', player) and ((state.count('Defeated_Gruz_Mother', player) and state.count('Defeated_False_Knight', player) and state.count('*Boss_Geo-Massive_Moss_Charger/', player) and state.count('Defeated_Hornet_1', player) and state.count('Defeated_Gorb', player) and state.count('Defeated_Dung_Defender', player) and state.count('Defeated_Any_Soul_Warrior', player) and state.count('Defeated_Brooding_Mawlek', player)) or False and state.count('COMBAT[Pantheon_1]', player)),
        "Defeated_Pantheon_2": lambda state: state.count('GG_Atrium', player) and ((state.count('Defeated_Xero', player) and state.count('Defeated_Crystal_Guardian', player) and state.count('Defeated_Soul_Master', player) and state.count('Defeated_Colosseum_2', player) and state.count('Defeated_Mantis_Lords', player) and state.count('Defeated_Marmu', player) and state.count('Defeated_Nosk', player) and state.count('Defeated_Flukemarm', player) and state.count('Defeated_Broken_Vessel', player)) or False and state.count('COMBAT[Pantheon_2]', player)),
        "Defeated_Pantheon_3": lambda state: state.count('GG_Atrium', player) and ((state.count('Defeated_Hive_Knight', player) and state.count('Defeated_Elder_Hu', player) and state.count('Defeated_Collector', player) and state.count('Defeated_Colosseum_2', player) and state.count('Defeated_Grimm', player) and state.count('Defeated_Galien', player) and state.count('Defeated_Uumuu', player) and state.count('Defeated_Hornet_2', player)) or False and state.count('COMBAT[Pantheon_3]', player)),
        "Opened_Pantheon_4": lambda state: state.count('GG_Atrium', player) and (state.count('Defeated_Pantheon_1', player) and state.count('Defeated_Pantheon_2', player) and state.count('Defeated_Pantheon_3', player) or False),
        "Defeated_Pantheon_4": lambda state: state.count('GG_Atrium', player) and state.count('Opened_Pantheon_4', player) and ((state.count('Defeated_Enraged_Guardian', player) and state.count('Defeated_Broken_Vessel', player) and state.count('Defeated_No_Eyes', player) and state.count('Defeated_Traitor_Lord', player) and state.count('Defeated_Dung_Defender', player) and state.count('Defeated_False_Knight', player) and state.count('Defeated_Markoth', player) and state.count('Defeated_Watcher_Knights', player) and state.count('Defeated_Soul_Master', player)) or False and state.count('COMBAT[Pantheon_4]', player)),
        "GG_Atrium": lambda state: state.count('Warp-Junk_Pit_to_Godhome', player) and (state.count('RIGHTCLAW', player) or state.count('WINGS', player) or state.count('LEFTCLAW', player) and state.count('RIGHTSUPERDASH', player)) or state.count('GG_Workshop', player) and (state.count('LEFTCLAW', player) or state.count('RIGHTCLAW', player) and state.count('WINGS', player) or False) or state.count('Bench-Godhome_Atrium', player),
        "Hit_Pantheon_5_Unlock_Orb": lambda state: state.count('GG_Atrium', player) and state.count('WINGS', player) and state.count('ANYCLAW', player) and (((state.count('Queen_Fragment', player) and state.count('King_Fragment', player) and state.count('Void_Heart', player)) and state.count('Defeated_Pantheon_1', player) and state.count('Defeated_Pantheon_2', player) and state.count('Defeated_Pantheon_3', player) and state.count('Defeated_Pantheon_4', player)) or False),
        "GG_Workshop": lambda state: state.count('GG_Atrium', player) and (state.count('SWIM', player) and True or True) or state.count('Bench-Hall_of_Gods', player),
        "Can_Damage_Crystal_Guardian": lambda state: state.count('UPSLASH', player) or state.count('LEFTSLASH', player) or state.count('RIGHTSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.count('CYCLONE', player) or state.count('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and (state.count('CYCLONE', player) or state.count('Great_Slash', player)) and (state.count('DREAMNAIL', player) and (state.count('SPELLS', player) or state.count('FOCUS', player) and state.count('Spore_Shroom', player) or state.count('Glowing_Womb', player)) or state.count('Weaversong', player)),
        'Defeated_Any_Soul_Warrior': lambda state: state.count('Defeated_Sanctum_Warrior', player) or state.count('Defeated_Elegant_Warrior', player) or state.count('Room_Colosseum_01[left1]/', player) and state.count('Defeated_Colosseum_3', player),
        "Defeated_Colosseum_3": lambda state: state.count('Room_Colosseum_01[left1]', player) and state.count('Can_Replenish_Geo', player) and (state.count('ANYCLAW', player) or ((state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and state.count('WINGS', player))) and state.count('COMBAT[Colosseum_3]', player) and (True) and (True),

        # MACROS
        "COMBAT[Radiance]": lambda state: state.count('FULLDASH', player) and (state.count('FULLSHADOWDASH', player) or state.count('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.count('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.count('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and state.count('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and (state.count('UPSLASH', player) or state.count('SIDESLASH', player) or state.count('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_1]": lambda state: state.count('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.count('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_2]": lambda state: state.count('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.count('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))) and state.count('Can_Damage_Crystal_Guardian', player),
        "COMBAT[Pantheon_3]": lambda state: state.count('AERIALMINIBOSS', player) and state.count('SPELLS', player) > 1 and (state.count('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_4]": lambda state: state.count('AERIALMINIBOSS', player) and (state.count('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))) and state.count('Can_Damage_Crystal_Guardian', player) and state.count('FULLDASH', player) and (state.count('FULLSHADOWDASH', player) or state.count('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.count('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.count('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and state.count('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and (state.count('UPSLASH', player) or state.count('SIDESLASH', player) or state.count('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Pantheon_5]": lambda state: state.count('AERIALMINIBOSS', player) and state.count('FOCUS', player) and state.count('Can_Damage_Crystal_Guardian', player) and state.count('FULLDASH', player) and (state.count('FULLSHADOWDASH', player) or state.count('QUAKE', player)) and (state.count('FIREBALL', player) > 1 and state.count('UPSLASH', player) or state.count('SCREAM', player) > 1 and state.count('UPSLASH', player) or state._hk_option(player, 'RemoveSpellUpgrades') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and state.count('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and (state.count('UPSLASH', player) or state.count('SIDESLASH', player) or state.count('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),
        "COMBAT[Colosseum_3]": lambda state: state.count('BOSS', player) and (state.count('FOCUS', player) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'))),



        # SETTINGS
        # 'PROFICIENTCOMBAT': lambda state: state._hk_option(player, 'ProficientCombat'),  # 'ProficientCombat',
        # 'DIFFICULTSKIPS': lambda state: state._hk_option(player, 'DifficultSkips'),  # 'DifficultSkips',
        # "CURSED": lambda state: state._hk_option(player, 'RemoveSpellUpgrades'),  # 'RemoveSpellUpgrades',
        # "MILDCOMBATSKIPS": lambda state: state._hk_option(player, 'ProficientCombat'),
        # "SPICYCOMBATSKIPS": lambda state: state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat'),

        # MISC
        'Warp-Junk_Pit_to_Godhome': lambda state: state.count('GG_Waterways', player) and state.count('GODTUNERUNLOCK', player) and state.count('DREAMNAIL', player),
        'Bench-Godhome_Atrium': lambda state: state.count('GG_Atrium', player) and (state.count('RIGHTCLAW', player) and (state.count('RIGHTDASH', player) or state.count('LEFTCLAW', player) and state.count('RIGHTSUPERDASH', player) or state.count('WINGS', player)) or state.count('LEFTCLAW', player) and state.count('WINGS', player) or False) and True or True and state.count('Bench-Godhome_Atrium/', player),
        'Bench-Hall_of_Gods': lambda state: state.count('GG_Workshop', player) and (state.count('ANYCLAW', player) or False) and True or True and state.count('Bench-Hall_of_Gods/', player),


        '*Boss_Geo-Massive_Moss_Charger/': lambda state: state.count('Fungus1_29[left1]', player) or state.count('Fungus1_29[right1]', player),
        'Bench-Godhome_Atrium/': lambda state: state.count('Bench-Godhome_Atrium', player),
        'Bench-Hall_of_Gods/': lambda state: state.count('Bench-Hall_of_Gods', player),
        'Room_Colosseum_01[left1]/': lambda state: state.count('Room_Colosseum_01[left1]', player),
        "GODTUNERUNLOCK": lambda state: state.count('SIMPLE', player) > 3,
        # 'WARPSTARTTOBENCH': lambda state: True,  # ap always allows warp to start
        "GG_Waterways": lambda state: state.count('GG_Waterways[door1]', player) or state.count('GG_Waterways[right1]', player) and (state.count('LEFTSUPERDASH', player) or state.count('SWIM', player)) or state.count('Warp-Godhome_to_Junk_Pit', player),
        "Warp-Godhome_to_Junk_Pit": lambda state: state.count('Warp-Junk_Pit_to_Godhome', player) or state.count('GG_Atrium', player),

        # COMBAT MACROS
        "NAILCOMBAT": lambda state: state.count('SIDESLASH', player) or state.count('UPSLASH', player) or state._hk_option(player, 'ProficientCombat') and (state.count('CYCLONE', player) or state.count('Great_Slash', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')),
        "BOSS": lambda state: state.count('SPELLS', player) > 1 and (state.count('ANYDASH', player) and (state.count('SIDESLASH', player) or state.count('UPSLASH', player)) or state._hk_option(player, 'ProficientCombat') and state.count('NAILCOMBAT', player)),
        "AERIALMINIBOSS": lambda state: (state.count('FIREBALL', player) or state.count('SCREAM', player)) and state.count('ANYDASH', player) and (state.count('SIDESLASH', player) or state.count('UPSLASH', player)) or state._hk_option(player, 'ProficientCombat') and (state.count('FIREBALL', player) or state.count('SCREAM', player)) and (state.count('SIDESLASH', player) or state.count('UPSLASH', player)) or (state._hk_option(player, 'DifficultSkips') and state._hk_option(player, 'ProficientCombat')) and (state.count('SIDESLASH', player) or state.count('UPSLASH', player) or state.count('CYCLONE', player) or state.count('Great_Slash', player)),

        # REPLACEMENT MACROS
        "ANYDASH": lambda state: state.count('LEFTDASH', player) or state.count('RIGHTDASH', player),
        "FULLDASH": lambda state: state.count('LEFTDASH', player) and state.count('RIGHTDASH', player),
        "SIDESLASH": lambda state: state.count('LEFTSLASH', player) or state.count('RIGHTSLASH', player),
        "FULLSHADOWDASH": lambda state: state.count('LEFTSHADOWDASH', player) and state.count('RIGHTSHADOWDASH', player),
        "LEFTSHADOWDASH": lambda state: state.count('ANYSHADOWDASH', player) and state.count('LEFTDASH', player),
        "RIGHTSHADOWDASH": lambda state: state.count('ANYSHADOWDASH', player) and state.count('RIGHTDASH', player),
        "ANYSHADOWDASH": lambda state: state.count('LEFTDASH', player) > 1 or state.count('RIGHTDASH', player) > 1,
        "ANYCLAW": lambda state: state.count('LEFTCLAW', player) or state.count('RIGHTCLAW', player),

        # RENAMES
        # 'Great_Slash': "Great_Slash",
        # 'Spore_Shroom': "Spore_Shroom",
        # 'Glowing_Womb': "Glowing_Womb",
        # 'Weaversong': "Weaversong",
        # 'VOIDHEART': "King_Fragment and Queen_Fragment and Void_Heart",
        # 'FIREBALL>1': "FIREBALL",
        # 'SCREAM>1': "SCREAM",
        # 'SPELLS>1': "SPELLS",
        # 'LEFTDASH>1': "LEFTDASH",
        # 'RIGHTDASH>1': "RIGHTDASH",
        # "SIMPLE>3": "SIMPLE",
        # '$SHRIEKPOGO[5]': "FALSE",
        # '$HOTSPRINGRESET': "TRUE",
        # '$SHRIEKPOGO[4,NOLEFTSTALL]': "FALSE",
        # '$BENCHRESET': "TRUE",
        # '$SHRIEKPOGO[6]': "FALSE",
    }

    for item, rule in required_events.items():
        fn(item, rule)
