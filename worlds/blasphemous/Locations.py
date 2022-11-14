from typing import List, TypedDict


class LocationDict(TypedDict):
    name: str
    region: str
    game_id: str


location_table: List[LocationDict] = [
    # Albero (35)
    {'name': "Albero: Sick house",
        'region': "albero",
        'game_id': "RB01"},
    {'name': "Albero: Outside ossuary",
        'region': "albero",
        'game_id': "CO43"},
    {'name': "Albero: Graveyard",
        'region': "albero",
        'game_id': "CO16"},
    {'name': "Albero: Warp room",
        'region': "albero",
        'game_id': "QI65"},
    {'name': "Albero: Elevator cherub",
        'region': "albero",
        'game_id': "RESCUED_CHERUB_08"},
    {'name': "Albero: Bless cloth",
        'region': "albero",
        'game_id': "RE04"},
    {'name': "Albero: Bless egg",
        'region': "albero",
        'game_id': "RE10"},
    {'name': "Albero: Bless hand",
        'region': "albero",
        'game_id': "RE02"},
    {'name': "Albero: Cleofas gift initial",
        'region': "albero",
        'game_id': "QI01"},
    {'name': "Albero: Cleofas gift final",
        'region': "albero",
        'game_id': "PR11"},
    {'name': "Albero: Tirso reward 1",
        'region': "albero",
        'game_id': "QI66"},
    {'name': "Albero: Tirso reward 2",
        'region': "albero",
        'game_id': "Tirso[500]"},
    {'name': "Albero: Tirso reward 3",
        'region': "albero",
        'game_id': "Tirso[1000]"},
    {'name': "Albero: Tirso reward 4",
        'region': "albero",
        'game_id': "Tirso[2000]"},
    {'name': "Albero: Tirso reward 5",
        'region': "albero",
        'game_id': "Tirso[5000]"},
    {'name': "Albero: Tirso reward 6",
        'region': "albero",
        'game_id': "Tirso[10000]"},
    {'name': "Albero: Tirso reward final",
        'region': "albero",
        'game_id': "QI56"},
    {'name': "Albero: Tentudia reward 1",
        'region': "albero",
        'game_id': "Lvdovico[500]"},
    {'name': "Albero: Tentudia reward 2",
        'region': "albero",
        'game_id': "Lvdovico[1000]"},
    {'name': "Albero: Tentudia reward 3",
        'region': "albero",
        'game_id': "PR03"},
    {'name': "Ossuary: Isidora reward main",
        'region': "albero",
        'game_id': "QI201"},
    {'name': "Albero: Sword room",
        'region': "albero",
        'game_id': "Sword[D01Z02S06]"},
    {'name': "Albero: Church donation 1",
        'region': "albero",
        'game_id': "RB104"},
    {'name': "Albero: Church donation 2",
        'region': "albero",
        'game_id': "RB105"},
    {'name': "Ossuary: Reward 1",
        'region': "albero",
        'game_id': "Undertaker[250]"},
    {'name': "Ossuary: Reward 2",
        'region': "albero",
        'game_id': "Undertaker[500]"},
    {'name': "Ossuary: Reward 3",
        'region': "albero",
        'game_id': "Undertaker[750]"},
    {'name': "Ossuary: Reward 4",
        'region': "albero",
        'game_id': "Undertaker[1000]"},
    {'name': "Ossuary: Reward 5",
        'region': "albero",
        'game_id': "Undertaker[1250]"},
    {'name': "Ossuary: Reward 6",
        'region': "albero",
        'game_id': "Undertaker[1500]"},
    {'name': "Ossuary: Reward 7",
        'region': "albero",
        'game_id': "Undertaker[1750]"},
    {'name': "Ossuary: Reward 8",
        'region': "albero",
        'game_id': "Undertaker[2000]"},
    {'name': "Ossuary: Reward 9",
        'region': "albero",
        'game_id': "Undertaker[2500]"},
    {'name': "Ossuary: Reward 10",
        'region': "albero",
        'game_id': "Undertaker[3000]"},
    {'name': "Ossuary: Reward 11",
        'region': "albero",
        'game_id': "Undertaker[5000]"},
    
    # All the Tears of the Sea (1)
    {'name': "AtTotS: Miriam gift",
        'region': "attots",
        'game_id': "PR201"},

    # Archcathedral Rooftops (11)
    {'name': "AR: Bridge fight 1",
        'region': "ar",
        'game_id': "QI02"},
    {'name': "AR: Bridge fight 2",
        'region': "ar",
        'game_id': "QI03"},
    {'name': "AR: Bridge fight 3",
        'region': "ar",
        'game_id': "QI04"},
    {'name': "AR: Western shaft ledge",
        'region': "ar",
        'game_id': "CO06"},
    {'name': "AR: Western shaft cherub",
        'region': "ar",
        'game_id': "RESCUED_CHERUB_36"},
    {'name': "AR: Western shaft chest",
        'region': "ar",
        'game_id': "PR12"},
    {'name': "AR: MoM east entrance",
        'region': "ar",
        'game_id': "HE04"},
    {'name': "AR: Lady room",
        'region': "ar",
        'game_id': "Lady[D06Z01S24]"},
    {'name': "AR: Second checkpoint ledge",
        'region': "ar",
        'game_id': "CO40"},
    {'name': "AR: Sword room",
        'region': "ar",
        'game_id': "Sword[D06Z01S11]"},
    {'name': "AR: Crisanta",
        'region': "ar",
        'game_id': "BS16"},

    # Bridge of the Three Cavalries (3)
    {'name': "BotTC: Esdras",
        'region': "bottc",
        'game_id': "BS12"},
    {'name': "BotTC: Esdras gift initial",
        'region': "bottc",
        'game_id': "PR09"},
    {'name': "BotTC: Amanecida core",
        'region': "bottc",
        'game_id': "HE101"},

    # Brotherhood of the Silent Sorrow (11)
    {'name': "BotSS: Beginning gift",
        'region': "botss",
        'game_id': "QI106"},
    {'name': "BotSS: Initial room cherub",
        'region': "botss",
        'game_id': "RESCUED_CHERUB_06"},
    {'name': "BotSS: Initial room ledge",
        'region': "botss",
        'game_id': "RB204"},
    {'name': "BotSS: Elder Brother's room",
        'region': "botss",
        'game_id': "RE01"},
    {'name': "BotSS: Sword room",
        'region': "botss",
        'game_id': "Sword[D17Z01S08]"},
    {'name': "BotSS: Spike gauntlet exit",
        'region': "botss",
        'game_id': "CO25"},
    {'name': "BotSS: Blue candle",
        'region': "botss",
        'game_id': "RB25"},
    {'name': "BotSS: Church entrance",
        'region': "botss",
        'game_id': "PR203"},
    {'name': "BotSS: Esdras gift final",
        'region': "botss",
        'game_id': "QI204"},
    {'name': "BotSS: Crisanta gift",
        'region': "botss",
        'game_id': "QI301"},
    {'name': "BotSS: Warden of the Silent Sorrow",
        'region': "botss",
        'game_id': "BS13"},
    
    # Convent of Our Lady of the Charred Visage (13)
    {'name': "CoOLotCV: Blood platform ledge",
        'region': "coolotcv",
        'game_id': "CO05"},
    {'name': "CoOLotCV: Ghost death room",
        'region': "coolotcv",
        'game_id': "CO15"},
    {'name': "CoOLotCV: Central lung room",
        'region': "coolotcv",
        'game_id': "RB08"},
    {'name': "CoOLotCV: Southwest lung room",
        'region': "coolotcv",
        'game_id': "HE03"},
    {'name': "CoOLotCV: Lady room",
        'region': "coolotcv",
        'game_id': "Lady[D02Z03S15]"},
    {'name': "CoOLotCV: Sword room",
        'region': "coolotcv",
        'game_id': "Sword[D02Z03S13]"},
    {'name': "CoOLotCV: Red candle",
        'region': "coolotcv",
        'game_id': "RB18"},
    {'name': "CoOLotCV: Blue candle",
        'region': "coolotcv",
        'game_id': "RB24"},
    {'name': "CoOLotCV: Outside area",
        'region': "coolotcv",
        'game_id': "RB107"},
    {'name': "CoOLotCV: Burning oil fountain",
        'region': "coolotcv",
        'game_id': "QI57"},
    {'name': "CoOLotCV: Our Lady of the Charred Visage",
        'region': "coolotcv",
        'game_id': "BS03"},
    {'name': "CoOLotCV: Holy Visage gift",
        'region': "coolotcv",
        'game_id': "QI40"},
    {'name': "CoOLotCV: Mask room",
        'region': "coolotcv",
        'game_id': "QI61"},

    # Deambulatory of His Holiness (3)
    {'name': "DoHH: Complete Penitence 1",
        'region': "dohh",
        'game_id': "RB101"},
    {'name': "DoHH: Complete Penitence 2",
        'region': "dohh",
        'game_id': "RB102"},
    {'name': "DoHH: Complete Penitence 3",
        'region': "dohh",
        'game_id': "RB103"},

    # Desecrated Cistern (20)
    {'name': "DC: MeD lady room",
        'region': "dc",
        'game_id': "Lady[D01Z05S22]"},
    {'name': "DC: MeD entrance",
        'region': "dc",
        'game_id': "CO41"},
    {'name': "DC: Water room cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_11"},
    {'name': "DC: Eastern lower tunnel chest",
        'region': "dc",
        'game_id': "QI45"},
    {'name': "DC: Eastern upper tunnel chest",
        'region': "dc",
        'game_id': "PR16"},
    {'name': "DC: Eastern upper tunnel cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_13"},
    {'name': "DC: Hidden hand room",
        'region': "dc",
        'game_id': "QI67"},
    {'name': "DC: WaBC entrance",
        'region': "dc",
        'game_id': "CO09"},
    {'name': "DC: Oil room",
        'region': "dc",
        'game_id': "Oil[D01Z05S07]"},
    {'name': "DC: Veil room cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_14"},
    {'name': "DC: Veil room ledge",
        'region': "dc",
        'game_id': "QI12"},
    {'name': "DC: Lung tunnel cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_12"},
    {'name': "DC: Lung tunnel ledge",
        'region': "dc",
        'game_id': "CO32"},
    {'name': "DC: Shroud puzzle",
        'region': "dc",
        'game_id': "RB03"},
    {'name': "DC: Chalice room",
        'region': "dc",
        'game_id': "QI75"},
    {'name': "DC: Sword room",
        'region': "dc",
        'game_id': "Sword[D01Z05S24]"},
    {'name': "DC: GrA lady room",
        'region': "dc",
        'game_id': "Lady[D01Z05S26]"},
    {'name': "DC: Elevator exit cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_15"},
    {'name': "DC: Elevator shaft cherub",
        'region': "dc",
        'game_id': "RESCUED_CHERUB_22"},
    {'name': "DC: Elevator shaft ledge",
        'region': "dc",
        'game_id': "CO44"},

    # Echoes of Salt (2)
    {'name': "EoS: MoED entrance",
        'region': "eos",
        'game_id': "RB108"},
    {'name': "EoS: Near elevator shaft",
        'region': "eos",
        'game_id': "RB202"},
    
    # Graveyard of the Peaks (21)
    {'name': "GotP: Shop cave cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_31"},
    {'name': "GotP: Shop cave hole",
        'region': "gotp",
        'game_id': "CO42"},
    {'name': "GotP: Shop left",
        'region': "gotp",
        'game_id': "QI11"},
    {'name': "GotP: Shop middle",
        'region': "gotp",
        'game_id': "RB37"},
    {'name': "GotP: Shop right",
        'region': "gotp",
        'game_id': "RB02"},
    {'name': "GotP: Guilt room",
        'region': "gotp",
        'game_id': "RB38"},
    {'name': "GotP: Elevator shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_26"},
    {'name': "GotP: Elevator shaft ledge",
        'region': "gotp",
        'game_id': "QI53"},
    {'name': "GotP: Lady room",
        'region': "gotp",
        'game_id': "Lady[D02Z02S12]"},
    {'name': "GotP: Bleed room",
        'region': "gotp",
        'game_id': "HE11"},
    {'name': "GotP: Eastern shaft lower",
        'region': "gotp",
        'game_id': "QI46"},
    {'name': "GotP: Eastern shaft middle",
        'region': "gotp",
        'game_id': "CO29"},
    {'name': "GotP: Eastern shaft upper",
        'region': "gotp",
        'game_id': "QI08"},
    {'name': "GotP: Amanecida ledge",
        'region': "gotp",
        'game_id': "RB106"},
    {'name': "GotP: Western shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_25"},
    {'name': "GotP: Western shaft lower",
        'region': "gotp",
        'game_id': "RB32"},
    {'name': "GotP: Western shaft upper",
        'region': "gotp",
        'game_id': "CO01"},
    {'name': "GotP: Center shaft cherub",
        'region': "gotp",
        'game_id': "RESCUED_CHERUB_24"},
    {'name': "GotP: Center shaft ledge",
        'region': "gotp",
        'game_id': "RB15"},
    {'name': "GotP: Oil room",
        'region': "gotp",
        'game_id': "Oil[D02Z02S10]"},
    {'name': "GotP: Bow Amanecida",
        'region': "gotp",
        'game_id': "D02Z02S14[18000]"},
    
    # Grievance Ascends (12)
    {'name': "GA: Western lung ledge",
        'region': "ga",
        'game_id': "QI44"},
    {'name': "GA: Lung room upper",
        'region': "ga",
        'game_id': "RE07"},
    {'name': "GA: Lung room cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_19"},
    {'name': "GA: Lung room lower",
        'region': "ga",
        'game_id': "CO12"},
    {'name': "GA: Oil room",
        'region': "ga",
        'game_id': "Oil[D03Z03S13]"},
    {'name': "GA: Blood tunnel ledge",
        'region': "ga",
        'game_id': "QI10"},
    {'name': "GA: Blood tunnel cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_21"},
    {'name': "GA: Altasgracias cherub",
        'region': "ga",
        'game_id': "RESCUED_CHERUB_20"},
    {'name': "GA: Altasgracias gift",
        'region': "ga",
        'game_id': "QI13"},
    {'name': "GA: Altasgracias cacoon",
        'region': "ga",
        'game_id': "RB06"},
    {'name': "GA: Tres Angustias",
        'region': "ga",
        'game_id': "BS04"},
    {'name': "GA: Holy Visage gift",
        'region': "ga",
        'game_id': "QI39"},
    
    # Hall of the Dawning (2)
    {'name': "HotD: Mirror room",
        'region': "hotd",
        'game_id': "QI105"},
    {'name': "HotD: Laudes",
        'region': "hotd",
        'game_id': "LaudesBossTrigger[30000]"},
    
    # Jondo (13)
    {'name': "Jondo: Eastern entrance ledge",
        'region': "jondo",
        'game_id': "CO08"},
    {'name': "Jondo: Eastern entrance chest",
        'region': "jondo",
        'game_id': "PR10"},
    {'name': "Jondo: Eastern shaft bell chargers",
        'region': "jondo",
        'game_id': "CO33"},
    {'name': "Jondo: Eastern shaft bell trap",
        'region': "jondo",
        'game_id': "QI19"},
    {'name': "Jondo: Eastern shaft cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_18"},
    {'name': "Jondo: Spike tunnel cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_37"},
    {'name': "Jondo: Spike tunnel ledge",
        'region': "jondo",
        'game_id': "HE06"},
    {'name': "Jondo: EcS entrance",
        'region': "jondo",
        'game_id': "QI103"},
    {'name': "Jondo: Western shaft lower slide",
        'region': "jondo",
        'game_id': "CO47"},
    {'name': "Jondo: Western shaft bell trap",
        'region': "jondo",
        'game_id': "QI41"},
    {'name': "Jondo: Western shaft bell puzzle",
        'region': "jondo",
        'game_id': "QI52"},
    {'name': "Jondo: Western shaft root puzzle",
        'region': "jondo",
        'game_id': "RB28"},
    {'name': "Jondo: Western shaft cherub",
        'region': "jondo",
        'game_id': "RESCUED_CHERUB_17"},
    
    # Knot of the Three Words (1)
    {'name': "KotTW: Fourth Visage gift",
        'region': "kottw",
        'game_id': "HE201"},
    
    # Library of the Negated Words (18)
    {'name': "LotNW: Platform room cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_01"},
    {'name': "LotNW: Platform room ledge",
        'region': "lotnw",
        'game_id': "CO18"},
    {'name': "LotNW: Upper cathedral ledge",
        'region': "lotnw",
        'game_id': "CO22"},
    {'name': "LotNW: Hidden floor",
        'region': "lotnw",
        'game_id': "QI50"},
    {'name': "LotNW: Lung ambush chest",
        'region': "lotnw",
        'game_id': "RB31"},
    {'name': "LotNW: Lady room",
        'region': "lotnw",
        'game_id': "Lady[D05Z01S14]"},
    {'name': "LotNW: Bone puzzle",
        'region': "lotnw",
        'game_id': "PR15"},
    {'name': "LotNW: Diosdado ledge",
        'region': "lotnw",
        'game_id': "CO28"},
    {'name': "LotNW: Platform puzzle chest",
        'region': "lotnw",
        'game_id': "PR07"},
    {'name': "LotNW: Final shaft ledge",
        'region': "lotnw",
        'game_id': "RB30"},
    {'name': "LotNW: Final shaft cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_02"},
    {'name': "LotNW: Oil room",
        'region': "lotnw",
        'game_id': "Oil[D05Z01S19]"},
    {'name': "LotNW: Elevator cherub",
        'region': "lotnw",
        'game_id': "RESCUED_CHERUB_32"},
    {'name': "LotNW: Mask room",
        'region': "lotnw",
        'game_id': "QI62"},
    {'name': "LotNW: Sword room",
        'region': "lotnw",
        'game_id': "Sword[D05Z01S13]"},
    {'name': "LotNW: Red candle",
        'region': "lotnw",
        'game_id': "RB19"},
    {'name': "LotNW: Diosdado gift",
        'region': "lotnw",
        'game_id': "RB203"},
    {'name': "LotNW: Fourth Visage hidden wall",
        'region': "lotnw",
        'game_id': "RB301"},

    # Mercy Dreams (15)
    {'name': "MD: First section hidden wall",
        'region': "md",
        'game_id': "CO30"},
    {'name': "MD: Second section ghost ambush",
        'region': "md",
        'game_id': "PR01"},
    {'name': "MD: Second section ledge",
        'region': "md",
        'game_id': "CO03"},
    {'name': "MD: Second section cherub",
        'region': "md",
        'game_id': "RESCUED_CHERUB_09"},
    {'name': "MD: Red candle",
        'region': "md",
        'game_id': "RB17"},
    {'name': "MD: Shop left",
        'region': "md",
        'game_id': "QI58"},
    {'name': "MD: Shop middle",
        'region': "md",
        'game_id': "RB05"},
    {'name': "MD: Shop right",
        'region': "md",
        'game_id': "RB09"},
    {'name': "MD: Third section hidden wall",
        'region': "md",
        'game_id': "QI48"},
    {'name': "MD: Third section lower corridor",
        'region': "md",
        'game_id': "CO38"},
    {'name': "MD: Ten Piedad",
        'region': "md",
        'game_id': "BS01"},
    {'name': "MD: Holy Visage gift",
        'region': "md",
        'game_id': "QI38"},
    {'name': "MD: Blue candle",
        'region': "md",
        'game_id': "RB26"},
    {'name': "MD: SlC entrance cherub",
        'region': "md",
        'game_id': "RESCUED_CHERUB_33"},
    {'name': "MD: SlC entrance ledge",
        'region': "md",
        'game_id': "CO03"},

    # Mother of Mothers (14)
    {'name': "MoM: Oil room",
        'region': "mom",
        'game_id': "Oil[D04Z02S14]"},
    {'name': "MoM: Eastern room upper",
        'region': "mom",
        'game_id': "RB33"},
    {'name': "MoM: Eastern room lower",
        'region': "mom",
        'game_id': "CO35"},
    {'name': "MoM: Western room cherub",
        'region': "mom",
        'game_id': "RESCUED_CHERUB_30"},
    {'name': "MoM: Western room ledge",
        'region': "mom",
        'game_id': "CO17"},
    {'name': "MoM: Redento prayer room",
        'region': "mom",
        'game_id': "RE03"},
    {'name': "MoM: Redento corpse",
        'region': "mom",
        'game_id': "QI54"},
    {'name': "MoM: Blood incense shaft",
        'region': "mom",
        'game_id': "HE01"},
    {'name': "MoM: Outside Cleofas room",
        'region': "mom",
        'game_id': "CO34"},
    {'name': "MoM: Center room ledge",
        'region': "mom",
        'game_id': "CO20"},
    {'name': "MoM: Center room cherub",
        'region': "mom",
        'game_id': "RESCUED_CHERUB_29"},
    {'name': "MoM: Sword room",
        'region': "mom",
        'game_id': "Sword[D04Z02S12]"},
    {'name': "MoM: Melquiades",
        'region': "mom",
        'game_id': "BS05"},
    {'name': "MoM: Mask room",
        'region': "mom",
        'game_id': "QI60"},

    # Mountains of the Endless Dusk (8)
    {'name': "MotED: DeC entrance",
        'region': "moted",
        'game_id': "CO13"},
    {'name': "MotED: Petpetua gift",
        'region': "moted",
        'game_id': "RB13"},
    {'name': "MotED: Bell gap cherub",
        'region': "moted",
        'game_id': "RESCUED_CHERUB_16"},
    {'name': "MotED: Bell gap ledge",
        'region': "moted",
        'game_id': "QI47"},
    {'name': "MotED: Redento meeting 1",
        'region': "moted",
        'game_id': "RB22"},
    {'name': "MotED: Blood platform",
        'region': "moted",
        'game_id': "QI63"},
    {'name': "MotED: Egg hatching",
        'region': "moted",
        'game_id': "QI14"},
    {'name': "MotED: Axe Amanecida",
        'region': "moted",
        'game_id': "D03Z01S03[18000]"},

    # Mourning and Havoc (4)
    {'name': "MaH: Western chest",
        'region': "mah",
        'game_id': "PR202"},
    {'name': "MaH: Eastern chest",
        'region': "mah",
        'game_id': "RB201"},
    {'name': "MaH: Sierpes reward",
        'region': "mah",
        'game_id': "QI202"},
    {'name': "MaH: Sierpes",
        'region': "mah",
        'game_id': "BossTrigger[5000]"},
    
    # Patio of the Silent Steps (9)
    {'name': "PotSS: Garden 1 cherub",
        'region': "potss",
        'game_id': "RESCUED_CHERUB_35"},
    {'name': "PotSS: Garden 1 ledge",
        'region': "potss",
        'game_id': "CO23"},
    {'name': "PotSS: Garden 2 ledge",
        'region': "potss",
        'game_id': "RB14"},
    {'name': "PotSS: Garden 3 cherub",
        'region': "potss",
        'game_id': "RESCUED_CHERUB_28"},
    {'name': "PotSS: Garden 3 lower ledge",
        'region': "potss",
        'game_id': "QI37"},
    {'name': "PotSS: Garden 3 upper ledge",
        'region': "potss",
        'game_id': "CO39"},
    {'name': "PotSS: Northern shaft",
        'region': "potss",
        'game_id': "QI102"},
    {'name': "PotSS: Redento meeting 4",
        'region': "potss",
        'game_id': "RB21"},
    {'name': "PotSS: Falcata Amanecida",
        'region': "potss",
        'game_id': "D04Z01S04[18000]"},

    # Petrous (1)
    {'name': "Petrous: Entrance room",
        'region': "petrous",
        'game_id': "QI101"},

    # The Resting Place of the Sister (1)
    {'name': "TRPotS: Perpetua shrine",
        'region': "trpots",
        'game_id': "QI203"},
    
    # The Sleeping Canvases (10)
    {'name': "TSC: Herb shaft",
        'region': "tsc",
        'game_id': "QI64"},
    {'name': "TSC: Wax bleed puzzle",
        'region': "tsc",
        'game_id': "HE07"},
    {'name': "TSC: Shop left",
        'region': "tsc",
        'game_id': "RB12"},
    {'name': "TSC: Shop middle",
        'region': "tsc",
        'game_id': "QI49"},
    {'name': "TSC: Shop right",
        'region': "tsc",
        'game_id': "QI71"},
    {'name': "TSC: Low tunnel blade trap",
        'region': "tsc",
        'game_id': "QI104"},
    {'name': "TSC: Expositio",
        'region': "tsc",
        'game_id': "BS06"},
    {'name': "TSC: Linen drop room",
        'region': "tsc",
        'game_id': "CO31"},
    {'name': "TSC: Jocinero gift initial",
        'region': "tsc",
        'game_id': "RE05"},
    {'name': "TSC: Jocinero gift final",
        'region': "tsc",
        'game_id': "PR05"},

    # The Holy Line (6)
    {'name': "THL: Deosgracias gift",
        'region': "thl",
        'game_id': "QI31"},
    {'name': "THL: Mud ledge lower",
        'region': "thl",
        'game_id': "PR14"},
    {'name': "THL: Mud ledge upper",
        'region': "thl",
        'game_id': "RB07"},
    {'name': "THL: Mud cherub",
        'region': "thl",
        'game_id': "RESCUED_CHERUB_07"},
    {'name': "THL: Cave ledge",
        'region': "thl",
        'game_id': "CO04"},
    {'name': "THL: Cave chest",
        'region': "thl",
        'game_id': "QI55"},

    # Wall of the Holy Prohibitions (19)
    {'name': "WotHP: Q1 lift puzzle",
        'region': "wothp",
        'game_id': "RB11"},
    {'name': "WotHP: Q1 drop room upper",
        'region': "wothp",
        'game_id': "CO10"},
    {'name': "WotHP: Q1 drop room lower",
        'region': "wothp",
        'game_id': "QI69"},
    {'name': "WotHP: Q1 upper bronze door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_03"},
    {'name': "WotHP: Q1 upper silver door",
        'region': "wothp",
        'game_id': "CO24"},
    {'name': "WotHP: Q1 middle gold door",
        'region': "wothp",
        'game_id': "QI51"},
    {'name': "WotHP: Q2 middle gold door",
        'region': "wothp",
        'game_id': "CO26"},
    {'name': "WotHP: Q3 lower gold door",
        'region': "wothp",
        'game_id': "CO02"},
    {'name': "WotHP: Q3 upper silver door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_34"},
    {'name': "WotHP: Q3 upper ledge",
        'region': "wothp",
        'game_id': "RB16"},
    {'name': "WotHP: Q4 hidden ledge",
        'region': "wothp",
        'game_id': "CO27"},
    {'name': "WotHP: Q4 lower silver door",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_04"},
    {'name': "WotHP: Q4 upper bronze door",
        'region': "wothp",
        'game_id': "QI70"},
    {'name': "WotHP: Q4 upper silver door",
        'region': "wothp",
        'game_id': "CO37"},
    {'name': "WotHP: CoLCV entrance",
        'region': "wothp",
        'game_id': "RESCUED_CHERUB_05"},
    {'name': "WotHP: Oil room",
        'region': "wothp",
        'game_id': "Oil[D09Z01S12]"},
    {'name': "WotHP: Quirce",
        'region': "wothp",
        'game_id': "BS14"},
    {'name': "WotHP: Quirce room",
        'region': "wothp",
        'game_id': "QI72"},
    {'name': "WotHP: Lance Amanecida",
        'region': "wothp",
        'game_id': "D09Z01S01[18000]"},

    # Wasteland of the Buried Churches (8)
    {'name': "WotBC: Lower tree path",
        'region': "wotbc",
        'game_id': "RB04"},
    {'name': "WotBC: Building slide",
        'region': "wotbc",
        'game_id': "CO14"},
    {'name': "WotBC: Exterior ledge",
        'region': "wotbc",
        'game_id': "CO36"},
    {'name': "WotBC: Exterior cherub",
        'region': "wotbc",
        'game_id': "RESCUED_CHERUB_10"},
    {'name': "WotBC: Underneath MeD bridge",
        'region': "wotbc",
        'game_id': "QI06"},
    {'name': "WotBC: Cliffside ledge",
        'region': "wotbc",
        'game_id': "HE02"},
    {'name': "WotBC: Cliffside cherub",
        'region': "wotbc",
        'game_id': "RESCUED_CHERUB_38"},
    {'name': "WotBC: Redento meeting 3",
        'region': "wotbc",
        'game_id': "RB20"},
    
    # Where Olive Trees Wither (11)
    {'name': "WOTW: WaBC entrance",
        'region': "wotw",
        'game_id': "CO11"},
    {'name': "WOTW: Healing cave",
        'region': "wotw",
        'game_id': "QI20"},
    {'name': "WOTW: White lady flower",
        'region': "wotw",
        'game_id': "QI68"},
    {'name': "WOTW: White lady tomb",
        'region': "wotw",
        'game_id': "PR04"},
    {'name': "WOTW: White lady cave cherub",
        'region': "wotw",
        'game_id': "RESCUED_CHERUB_17"},
    {'name': "WOTW: White lady cave ledge",
        'region': "wotw",
        'game_id': "CO19"},
    {'name': "WOTW: Eastern root cherub",
        'region': "wotw",
        'game_id': "RESCUED_CHERUB_23"},
    {'name': "WOTW: Eastern root ledge",
        'region': "wotw",
        'game_id': "HE05"},
    {'name': "WOTW: Death run",
        'region': "wotw",
        'game_id': "QI07"},
    {'name': "WOTW: Gemino gift initial",
        'region': "wotw",
        'game_id': "QI59"},
    {'name': "WOTW: Gemino gift final",
        'region': "wotw",
        'game_id': "RB10"},

    # Various (20)
    {'name': "Guilt arena 1 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[1000]"},
    {'name': "Guilt arena 1 main",
        'region': "dungeon",
        'game_id': "QI32"},
    {'name': "Guilt arena 2 extra",
        'region': "dungeon",
        'game_id': "HE10"},
    {'name': "Guilt arena 2 main",
        'region': "dungeon",
        'game_id': "QI33"},
    {'name': "Guilt arena 3 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[3000]"},
    {'name': "Guilt arena 3 main",
        'region': "dungeon",
        'game_id': "QI34"},
    {'name': "Guilt arena 4 extra",
        'region': "dungeon",
        'game_id': "RB34"},
    {'name': "Guilt arena 4 main",
        'region': "dungeon",
        'game_id': "QI35"},
    {'name': "Guilt arena 5 extra",
        'region': "dungeon",
        'game_id': "Arena_NailManager[5000]"},
    {'name': "Guilt arena 5 main",
        'region': "dungeon",
        'game_id': "QI79"},
    {'name': "Guilt arena 6 extra",
        'region': "dungeon",
        'game_id': "RB35"},
    {'name': "Guilt arena 6 main",
        'region': "dungeon",
        'game_id': "QI80"},
    {'name': "Guilt arena 7 extra",
        'region': "dungeon",
        'game_id': "RB36"},
    {'name': "Guilt arena 7 main",
        'region': "dungeon",
        'game_id': "QI81"},
    {'name': "Viridiana gift",
        'region': "ar",
        'game_id': "PR08"},
    {'name': "Amanecida 1",
        'region': "dungeon",
        'game_id': "QI107"},
    {'name': "Amanecida 2",
        'region': "dungeon",
        'game_id': "QI108"},
    {'name': "Amanecida 3",
        'region': "dungeon",
        'game_id': "QI109"},
    {'name': "Amanecida 4",
        'region': "dungeon",
        'game_id': "QI110"},
    {'name': "All amanecidas reward",
        'region': "dungeon",
        'game_id': "PR101"}
]