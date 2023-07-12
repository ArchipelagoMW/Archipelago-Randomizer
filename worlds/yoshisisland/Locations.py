from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .LogicExtensions import YoshiLogic
from .Options import get_option_value

EventId: Optional[int] = None


class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True


def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:

    logic = YoshiLogic(world, player)

    location_table: List[LocationData] = [

    LocationData('Make Eggs, Throw Eggs', 'Make Eggs, Throw Eggs: Red Coins', 0x305020, lambda state: logic._11Coins(state)),
    LocationData('Make Eggs, Throw Eggs', 'Make Eggs, Throw Eggs: Flowers', 0x305021, lambda state: logic._11Flowers(state)),
    LocationData('Make Eggs, Throw Eggs', 'Make Eggs, Throw Eggs: Stars', 0x305022, lambda state: logic._11Stars(state)),
    LocationData('Make Eggs, Throw Eggs', 'Make Eggs, Throw Eggs: Level Clear', 0x305023, lambda state: logic._11Clear(state)),

    LocationData('Watch Out Below!', 'Watch Out Below!: Red Coins', 0x305024, lambda state: logic._12Coins(state)),
    LocationData('Watch Out Below!', 'Watch Out Below!: Flowers', 0x305025, lambda state: logic._12Flowers(state)),
    LocationData('Watch Out Below!', 'Watch Out Below!: Stars', 0x305026, lambda state: logic._12Stars(state)),
    LocationData('Watch Out Below!', 'Watch Out Below!: Level Clear', 0x305027, lambda state: logic._12Clear(state)),

    LocationData('The Cave Of Chomp Rock', 'The Cave Of Chomp Rock: Red Coins', 0x305028, lambda state: logic._13Coins(state)),
    LocationData('The Cave Of Chomp Rock', 'The Cave Of Chomp Rock: Flowers', 0x305029, lambda state: logic._13Flowers(state)),
    LocationData('The Cave Of Chomp Rock', 'The Cave Of Chomp Rock: Stars', 0x30502A, lambda state: logic._13Stars(state)),
    LocationData('The Cave Of Chomp Rock', 'The Cave Of Chomp Rock: Level Clear', 0x30502B, lambda state: logic._13Clear(state)),

    LocationData("Burt The Bashful's Fort", "Burt The Bashful's Fort: Red Coins", 0x30502C, lambda state: logic._14Coins(state)),
    LocationData("Burt The Bashful's Fort", "Burt The Bashful's Fort: Flowers", 0x30502D, lambda state: logic._14Flowers(state)),
    LocationData("Burt The Bashful's Fort", "Burt The Bashful's Fort: Stars", 0x30502E, lambda state: logic._14Stars(state)),
    LocationData("Burt The Bashful's Fort", "Burt The Bashful's Fort: Level Clear", 0x30502F, lambda state: logic._14Boss(state)),
    LocationData("Burt The Bashful's Boss Room", 'Burt The Bashful Defeated', 0x305030, lambda state: logic._14Boss(state)),

    LocationData("Hop! Hop! Donut Lifts", "Hop! Hop! Donut Lifts: Red Coins", 0x305031, lambda state: logic._15Coins(state)),
    LocationData("Hop! Hop! Donut Lifts", "Hop! Hop! Donut Lifts: Flowers", 0x305032, lambda state: logic._15Flowers(state)),
    LocationData("Hop! Hop! Donut Lifts", "Hop! Hop! Donut Lifts: Stars", 0x305033, lambda state: logic._15Stars(state)),
    LocationData("Hop! Hop! Donut Lifts", "Hop! Hop! Donut Lifts: Level Clear", 0x305034, lambda state: logic._15Clear(state)),

    LocationData("Shy-Guys On Stilts", "Shy-Guys On Stilts: Red Coins", 0x305035, lambda state: logic._16Coins(state)),
    LocationData("Shy-Guys On Stilts", "Shy-Guys On Stilts: Flowers", 0x305036, lambda state: logic._16Flowers(state)),
    LocationData("Shy-Guys On Stilts", "Shy-Guys On Stilts: Stars", 0x305037, lambda state: logic._16Stars(state)),
    LocationData("Shy-Guys On Stilts", "Shy-Guys On Stilts: Level Clear", 0x305038, lambda state: logic._16Clear(state)),

    LocationData("Touch Fuzzy Get Dizzy", "Touch Fuzzy Get Dizzy: Red Coins", 0x305039, lambda state: logic._17Coins(state)),
    LocationData("Touch Fuzzy Get Dizzy", "Touch Fuzzy Get Dizzy: Flowers", 0x30503A, lambda state: logic._17Flowers(state)),
    LocationData("Touch Fuzzy Get Dizzy", "Touch Fuzzy Get Dizzy: Stars", 0x30503B, lambda state: logic._17Stars(state)),
    LocationData("Touch Fuzzy Get Dizzy", "Touch Fuzzy Get Dizzy: Level Clear", 0x30503C, lambda state: logic._17Clear(state)),
    LocationData("Touch Fuzzy Get Dizzy", 'Gather Coins', EventId, lambda state: logic._17Game(state)),

    LocationData("Salvo The Slime's Castle", "Salvo The Slime's Castle: Red Coins", 0x30503D, lambda state: logic._18Coins(state)),
    LocationData("Salvo The Slime's Castle", "Salvo The Slime's Castle: Flowers", 0x30503E, lambda state: logic._18Flowers(state)),
    LocationData("Salvo The Slime's Castle", "Salvo The Slime's Castle: Stars", 0x30503F, lambda state: logic._18Stars(state)),
    LocationData("Salvo The Slime's Castle", "Salvo The Slime's Castle: Level Clear", 0x305040, lambda state: logic._18Boss(state)),
    LocationData("Salvo The Slime's Boss Room", 'Salvo The Slime Defeated', 0x30510C, lambda state: logic._18Boss(state)),
    ############################################################################################
    LocationData("Visit Koopa And Para-Koopa", "Visit Koopa And Para-Koopa: Red Coins", 0x305041, lambda state: logic._21Coins(state)),
    LocationData("Visit Koopa And Para-Koopa", "Visit Koopa And Para-Koopa: Flowers", 0x305042, lambda state: logic._21Flowers(state)),
    LocationData("Visit Koopa And Para-Koopa", "Visit Koopa And Para-Koopa: Stars", 0x305043, lambda state: logic._21Stars(state)),
    LocationData("Visit Koopa And Para-Koopa", "Visit Koopa And Para-Koopa: Level Clear", 0x305044, lambda state: logic._21Clear(state)),

    LocationData("The Baseball Boys", "The Baseball Boys: Red Coins", 0x305045, lambda state: logic._22Coins(state)),
    LocationData("The Baseball Boys", "The Baseball Boys: Flowers", 0x305046, lambda state: logic._22Flowers(state)),
    LocationData("The Baseball Boys", "The Baseball Boys: Stars", 0x305047, lambda state: logic._22Stars(state)),
    LocationData("The Baseball Boys", "The Baseball Boys: Level Clear", 0x305048, lambda state: logic._22Clear(state)),

    LocationData("What's Gusty Taste Like?", "What's Gusty Taste Like?: Red Coins", 0x305049, lambda state: logic._23Coins(state)),
    LocationData("What's Gusty Taste Like?", "What's Gusty Taste Like?: Flowers", 0x30504A, lambda state: logic._23Flowers(state)),
    LocationData("What's Gusty Taste Like?", "What's Gusty Taste Like?: Stars", 0x30504B, lambda state: logic._23Stars(state)),
    LocationData("What's Gusty Taste Like?", "What's Gusty Taste Like?: Level Clear", 0x30504C, lambda state: logic._23Clear(state)),

    LocationData("Bigger Boo's Fort", "Bigger Boo's Fort: Red Coins", 0x30504D, lambda state: logic._24Coins(state)),
    LocationData("Bigger Boo's Fort", "Bigger Boo's Fort: Flowers", 0x30504E, lambda state: logic._24Flowers(state)),
    LocationData("Bigger Boo's Fort", "Bigger Boo's Fort: Stars", 0x30504F, lambda state: logic._24Stars(state)),
    LocationData("Bigger Boo's Fort", "Bigger Boo's Fort: Level Clear", 0x305050, lambda state: logic._24Boss(state)),
    LocationData("Bigger Boo's Boss Room", 'Bigger Boo Defeated', 0x30510D, lambda state: logic._24Boss(state)),

    LocationData("Watch Out For Lakitu", "Watch Out For Lakitu: Red Coins", 0x305051, lambda state: logic._25Coins(state)),
    LocationData("Watch Out For Lakitu", "Watch Out For Lakitu: Flowers", 0x305052, lambda state: logic._25Flowers(state)),
    LocationData("Watch Out For Lakitu", "Watch Out For Lakitu: Stars", 0x305053, lambda state: logic._25Stars(state)),
    LocationData("Watch Out For Lakitu", "Watch Out For Lakitu: Level Clear", 0x305054, lambda state: logic._25Clear(state)),

    LocationData("The Cave Of The Mystery Maze", "The Cave Of The Mystery Maze: Red Coins", 0x305055, lambda state: logic._26Coins(state)),
    LocationData("The Cave Of The Mystery Maze", "The Cave Of The Mystery Maze: Flowers", 0x305056, lambda state: logic._26Flowers(state)),
    LocationData("The Cave Of The Mystery Maze", "The Cave Of The Mystery Maze: Stars", 0x305057, lambda state: logic._26Stars(state)),
    LocationData("The Cave Of The Mystery Maze", "The Cave Of The Mystery Maze: Level Clear", 0x305058, lambda state: logic._26Clear(state)),
    LocationData("The Cave Of The Mystery Maze", 'Seed Spitting Contest', EventId, lambda state: logic._26Game(state)),

    LocationData("Lakitu's Wall", "Lakitu's Wall: Red Coins", 0x305059, lambda state: logic._27Coins(state)),
    LocationData("Lakitu's Wall", "Lakitu's Wall: Flowers", 0x30505A, lambda state: logic._27Flowers(state)),
    LocationData("Lakitu's Wall", "Lakitu's Wall: Stars", 0x30505B, lambda state: logic._27Stars(state)),
    LocationData("Lakitu's Wall", "Lakitu's Wall: Level Clear", 0x30505C, lambda state: logic._27Clear(state)),
    LocationData("Lakitu's Wall", 'Gather Coins', EventId, lambda state: logic._27Game(state)),

    LocationData("The Potted Ghost's Castle", "The Potted Ghost's Castle: Red Coins", 0x30505D, lambda state: logic._28Coins(state)),
    LocationData("The Potted Ghost's Castle", "The Potted Ghost's Castle: Flowers", 0x30505E, lambda state: logic._28Flowers(state)),
    LocationData("The Potted Ghost's Castle", "The Potted Ghost's Castle: Stars", 0x30505F, lambda state: logic._28Stars(state)),
    LocationData("The Potted Ghost's Castle", "The Potted Ghost's Castle: Level Clear", 0x305060, lambda state: logic._28Boss(state)),
    LocationData("Roger The Ghost's Boss Room", 'Roger The Ghost Defeated', 0x30510E, lambda state: logic._28Boss(state)),
    ###############################################################################################
    LocationData("Welcome To Monkey World!", "Welcome To Monkey World!: Red Coins", 0x305061, lambda state: logic._31Coins(state)),
    LocationData("Welcome To Monkey World!", "Welcome To Monkey World!: Flowers", 0x305062, lambda state: logic._31Flowers(state)),
    LocationData("Welcome To Monkey World!", "Welcome To Monkey World!: Stars", 0x305063, lambda state: logic._31Stars(state)),
    LocationData("Welcome To Monkey World!", "Welcome To Monkey World!: Level Clear", 0x305064, lambda state: logic._31Clear(state)),

    LocationData("Jungle Rhythm...", "Jungle Rhythm...: Red Coins", 0x305065, lambda state: logic._32Coins(state)),
    LocationData("Jungle Rhythm...", "Jungle Rhythm...: Flowers", 0x305066, lambda state: logic._32Flowers(state)),
    LocationData("Jungle Rhythm...", "Jungle Rhythm...: Stars", 0x305067, lambda state: logic._32Stars(state)),
    LocationData("Jungle Rhythm...", "Jungle Rhythm...: Level Clear", 0x305068, lambda state: logic._32Clear(state)),

    LocationData("Nep-Enuts' Domain", "Nep-Enuts' Domain: Red Coins", 0x305069, lambda state: logic._33Coins(state)),
    LocationData("Nep-Enuts' Domain", "Nep-Enuts' Domain: Flowers", 0x30506A, lambda state: logic._33Flowers(state)),
    LocationData("Nep-Enuts' Domain", "Nep-Enuts' Domain: Stars", 0x30506B, lambda state: logic._33Stars(state)),
    LocationData("Nep-Enuts' Domain", "Nep-Enuts' Domain: Level Clear", 0x30506C, lambda state: logic._33Clear(state)),

    LocationData("Prince Froggy's Fort", "Prince Froggy's Fort: Red Coins", 0x30506D, lambda state: logic._34Coins(state)),
    LocationData("Prince Froggy's Fort", "Prince Froggy's Fort: Flowers", 0x30506E, lambda state: logic._34Flowers(state)),
    LocationData("Prince Froggy's Fort", "Prince Froggy's Fort: Stars", 0x30506F, lambda state: logic._34Stars(state)),
    LocationData("Prince Froggy's Fort", "Prince Froggy's Fort: Level Clear", 0x305070, lambda state: logic._34Boss(state)),
    LocationData("Prince Froggy's Boss Room", 'Prince Froggy Defeated', 0x30510F, lambda state: logic._34Boss(state)),

    LocationData("Jammin' Through The Trees", "Jammin' Through The Trees: Red Coins", 0x305071, lambda state: logic._35Coins(state)),
    LocationData("Jammin' Through The Trees", "Jammin' Through The Trees: Flowers", 0x305072, lambda state: logic._35Flowers(state)),
    LocationData("Jammin' Through The Trees", "Jammin' Through The Trees: Stars", 0x305073, lambda state: logic._35Stars(state)),
    LocationData("Jammin' Through The Trees", "Jammin' Through The Trees: Level Clear", 0x305074, lambda state: logic._35Clear(state)),

    LocationData("The Cave Of Harry Hedgehog", "The Cave Of Harry Hedgehog: Red Coins", 0x305075, lambda state: logic._36Coins(state)),
    LocationData("The Cave Of Harry Hedgehog", "The Cave Of Harry Hedgehog: Flowers", 0x305076, lambda state: logic._36Flowers(state)),
    LocationData("The Cave Of Harry Hedgehog", "The Cave Of Harry Hedgehog: Stars", 0x305077, lambda state: logic._36Stars(state)),
    LocationData("The Cave Of Harry Hedgehog", "The Cave Of Harry Hedgehog: Level Clear", 0x305078, lambda state: logic._36Clear(state)),

    LocationData("Monkeys' Favorite Lake", "Monkeys' Favorite Lake: Red Coins", 0x305079, lambda state: logic._37Coins(state)),
    LocationData("Monkeys' Favorite Lake", "Monkeys' Favorite Lake: Flowers", 0x30507A, lambda state: logic._37Flowers(state)),
    LocationData("Monkeys' Favorite Lake", "Monkeys' Favorite Lake: Stars", 0x30507B, lambda state: logic._37Stars(state)),
    LocationData("Monkeys' Favorite Lake", "Monkeys' Favorite Lake: Level Clear", 0x30507C, lambda state: logic._37Clear(state)),

    LocationData("Naval Piranha's Castle", "Naval Piranha's Castle: Red Coins", 0x30507D, lambda state: logic._38Coins(state)),
    LocationData("Naval Piranha's Castle", "Naval Piranha's Castle: Flowers", 0x30507E, lambda state: logic._38Flowers(state)),
    LocationData("Naval Piranha's Castle", "Naval Piranha's Castle: Stars", 0x30507F, lambda state: logic._38Stars(state)),
    LocationData("Naval Piranha's Castle", "Naval Piranha's Castle: Level Clear", 0x305080, lambda state: logic._38Boss(state)),
    LocationData("Naval Piranha's Boss Room", 'Naval Piranha Defeated', 0x305110, lambda state: logic._38Boss(state)),
    ##############################################################################################
    LocationData("GO! GO! MARIO!!", "GO! GO! MARIO!!: Red Coins", 0x305081, lambda state: logic._41Coins(state)),
    LocationData("GO! GO! MARIO!!", "GO! GO! MARIO!!: Flowers", 0x305082, lambda state: logic._41Flowers(state)),
    LocationData("GO! GO! MARIO!!", "GO! GO! MARIO!!: Stars", 0x305083, lambda state: logic._41Stars(state)),
    LocationData("GO! GO! MARIO!!", "GO! GO! MARIO!!: Level Clear", 0x305084, lambda state: logic._41Clear(state)),

    LocationData("The Cave Of The Lakitus", "The Cave Of The Lakitus: Red Coins", 0x305085, lambda state: logic._42Coins(state)),
    LocationData("The Cave Of The Lakitus", "The Cave Of The Lakitus: Flowers", 0x305086, lambda state: logic._42Flowers(state)),
    LocationData("The Cave Of The Lakitus", "The Cave Of The Lakitus: Stars", 0x305087, lambda state: logic._42Stars(state)),
    LocationData("The Cave Of The Lakitus", "The Cave Of The Lakitus: Level Clear", 0x305088, lambda state: logic._42Clear(state)),

    LocationData("Don't Look Back!", "Don't Look Back!: Red Coins", 0x305089, lambda state: logic._43Coins(state)),
    LocationData("Don't Look Back!", "Don't Look Back!: Flowers", 0x30508A, lambda state: logic._43Flowers(state)),
    LocationData("Don't Look Back!", "Don't Look Back!: Stars", 0x30508B, lambda state: logic._43Stars(state)),
    LocationData("Don't Look Back!", "Don't Look Back!: Level Clear", 0x30508C, lambda state: logic._43Clear(state)),

    LocationData("Marching Milde's Fort", "Marching Milde's Fort: Red Coins", 0x30508D, lambda state: logic._44Coins(state)),
    LocationData("Marching Milde's Fort", "Marching Milde's Fort: Flowers", 0x30508E, lambda state: logic._44Flowers(state)),
    LocationData("Marching Milde's Fort", "Marching Milde's Fort: Stars", 0x30508F, lambda state: logic._44Stars(state)),
    LocationData("Marching Milde's Fort", "Marching Milde's Fort: Level Clear", 0x305090, lambda state: logic._44Boss(state)),
    LocationData("Marching Milde's Boss Room", 'Marching Milde Defeated', 0x305111, lambda state: logic._44Boss(state)),

    LocationData("Chomp Rock Zone", "Chomp Rock Zone: Red Coins", 0x305091, lambda state: logic._45Coins(state)),
    LocationData("Chomp Rock Zone", "Chomp Rock Zone: Flowers", 0x305092, lambda state: logic._45Flowers(state)),
    LocationData("Chomp Rock Zone", "Chomp Rock Zone: Stars", 0x305093, lambda state: logic._45Stars(state)),
    LocationData("Chomp Rock Zone", "Chomp Rock Zone: Level Clear", 0x305094, lambda state: logic._45Clear(state)),

    LocationData("Lake Shore Paradise", "Lake Shore Paradise: Red Coins", 0x305095, lambda state: logic._46Coins(state)),
    LocationData("Lake Shore Paradise", "Lake Shore Paradise: Flowers", 0x305096, lambda state: logic._46Flowers(state)),
    LocationData("Lake Shore Paradise", "Lake Shore Paradise: Stars", 0x305097, lambda state: logic._46Stars(state)),
    LocationData("Lake Shore Paradise", "Lake Shore Paradise: Level Clear", 0x305098, lambda state: logic._46Clear(state)),

    LocationData("Ride Like The Wind", "Ride Like The Wind: Red Coins", 0x305099, lambda state: logic._47Coins(state)),
    LocationData("Ride Like The Wind", "Ride Like The Wind: Flowers", 0x30509A, lambda state: logic._47Flowers(state)),
    LocationData("Ride Like The Wind", "Ride Like The Wind: Stars", 0x30509B, lambda state: logic._47Stars(state)),
    LocationData("Ride Like The Wind", "Ride Like The Wind: Level Clear", 0x30509C, lambda state: logic._47Clear(state)),
    LocationData("Ride Like The Wind", 'Gather Coins', EventId, lambda state: logic._47Game(state)),

    LocationData("Hookbill The Koopa's Castle", "Hookbill The Koopa's Castle: Red Coins", 0x30509D, lambda state: logic._48Coins(state)),
    LocationData("Hookbill The Koopa's Castle", "Hookbill The Koopa's Castle: Flowers", 0x30509E, lambda state: logic._48Flowers(state)),
    LocationData("Hookbill The Koopa's Castle", "Hookbill The Koopa's Castle: Stars", 0x30509F, lambda state: logic._48Stars(state)),
    LocationData("Hookbill The Koopa's Castle", "Hookbill The Koopa's Castle: Level Clear", 0x3050A0, lambda state: logic._48Boss(state)),
    LocationData("Hookbill The Koopa's Boss Room", 'Hookbill The Koopa Defeated', 0x305112, lambda state: logic._48Boss(state)),
    ######################################################################################################
    LocationData("BLIZZARD!!!", "BLIZZARD!!!: Red Coins", 0x3050A1, lambda state: logic._51Coins(state)),
    LocationData("BLIZZARD!!!", "BLIZZARD!!!: Flowers", 0x3050A2, lambda state: logic._51Flowers(state)),
    LocationData("BLIZZARD!!!", "BLIZZARD!!!: Stars", 0x3050A3, lambda state: logic._51Stars(state)),
    LocationData("BLIZZARD!!!", "BLIZZARD!!!: Level Clear", 0x3050A4, lambda state: logic._51Clear(state)),

    LocationData("Ride The Ski Lifts", "Ride The Ski Lifts: Red Coins", 0x3050A5, lambda state: logic._52Coins(state)),
    LocationData("Ride The Ski Lifts", "Ride The Ski Lifts: Flowers", 0x3050A6, lambda state: logic._52Flowers(state)),
    LocationData("Ride The Ski Lifts", "Ride The Ski Lifts: Stars", 0x3050A7, lambda state: logic._52Stars(state)),
    LocationData("Ride The Ski Lifts", "Ride The Ski Lifts: Level Clear", 0x3050A8, lambda state: logic._52Clear(state)),

    LocationData("Danger - Icy Conditions Ahead", "Danger - Icy Conditions Ahead: Red Coins", 0x3050A9, lambda state: logic._53Coins(state)),
    LocationData("Danger - Icy Conditions Ahead", "Danger - Icy Conditions Ahead: Flowers", 0x3050AA, lambda state: logic._53Flowers(state)),
    LocationData("Danger - Icy Conditions Ahead", "Danger - Icy Conditions Ahead: Stars", 0x3050AB, lambda state: logic._53Stars(state)),
    LocationData("Danger - Icy Conditions Ahead", "Danger - Icy Conditions Ahead: Level Clear", 0x3050AC, lambda state: logic._53Clear(state)),

    LocationData("Sluggy The Unshaven's Fort", "Sluggy The Unshaven's Fort: Red Coins", 0x3050AD, lambda state: logic._54Coins(state)),
    LocationData("Sluggy The Unshaven's Fort", "Sluggy The Unshaven's Fort: Flowers", 0x3050AE, lambda state: logic._54Flowers(state)),
    LocationData("Sluggy The Unshaven's Fort", "Sluggy The Unshaven's Fort: Stars", 0x3050AF, lambda state: logic._54Stars(state)),
    LocationData("Sluggy The Unshaven's Fort", "Sluggy The Unshaven's Fort: Level Clear", 0x3050B0, lambda state: logic._54Boss(state)),
    LocationData("Sluggy The Unshaven's Boss Room", 'Sluggy The Unshaven Defeated', 0x305113, lambda state: logic._54Boss(state)),

    LocationData("Goonie Rides!", "Goonie Rides!: Red Coins", 0x3050B1, lambda state: logic._55Coins(state)),
    LocationData("Goonie Rides!", "Goonie Rides!: Flowers", 0x3050B2, lambda state: logic._55Flowers(state)),
    LocationData("Goonie Rides!", "Goonie Rides!: Stars", 0x3050B3, lambda state: logic._55Stars(state)),
    LocationData("Goonie Rides!", "Goonie Rides!: Level Clear", 0x3050B4, lambda state: logic._55Clear(state)),

    LocationData("Welcome To Cloud World", "Welcome To Cloud World: Red Coins", 0x3050B5, lambda state: logic._56Coins(state)),
    LocationData("Welcome To Cloud World", "Welcome To Cloud World: Flowers", 0x3050B6, lambda state: logic._56Flowers(state)),
    LocationData("Welcome To Cloud World", "Welcome To Cloud World: Stars", 0x3050B7, lambda state: logic._56Stars(state)),
    LocationData("Welcome To Cloud World", "Welcome To Cloud World: Level Clear", 0x3050B8, lambda state: logic._56Clear(state)),

    LocationData("Shifting Platforms Ahead", "Shifting Platforms Ahead: Red Coins", 0x3050B9, lambda state: logic._57Coins(state)),
    LocationData("Shifting Platforms Ahead", "Shifting Platforms Ahead: Flowers", 0x3050BA, lambda state: logic._57Flowers(state)),
    LocationData("Shifting Platforms Ahead", "Shifting Platforms Ahead: Stars", 0x3050BB, lambda state: logic._57Stars(state)),
    LocationData("Shifting Platforms Ahead", "Shifting Platforms Ahead: Level Clear", 0x3050BC, lambda state: logic._57Clear(state)),

    LocationData("Raphael The Raven's Castle", "Raphael The Raven's Castle: Red Coins", 0x3050BD, lambda state: logic._58Coins(state)),
    LocationData("Raphael The Raven's Castle", "Raphael The Raven's Castle: Flowers", 0x3050BE, lambda state: logic._58Flowers(state)),
    LocationData("Raphael The Raven's Castle", "Raphael The Raven's Castle: Stars", 0x3050BF, lambda state: logic._58Stars(state)),
    LocationData("Raphael The Raven's Castle", "Raphael The Raven's Castle: Level Clear", 0x3050C0, lambda state: logic._58Boss(state)),
    LocationData("Raphael The Raven's Boss Room", 'Raphael The Raven Defeated', 0x305114, lambda state: logic._58Boss(state)),
    ######################################################################################################

    LocationData("Scary Skeleton Goonies!", "Scary Skeleton Goonies!: Red Coins", 0x3050C1, lambda state: logic._61Coins(state)),
    LocationData("Scary Skeleton Goonies!", "Scary Skeleton Goonies!: Flowers", 0x3050C2, lambda state: logic._61Flowers(state)),
    LocationData("Scary Skeleton Goonies!", "Scary Skeleton Goonies!: Stars", 0x3050C3, lambda state: logic._61Stars(state)),
    LocationData("Scary Skeleton Goonies!", "Scary Skeleton Goonies!: Level Clear", 0x3050C4, lambda state: logic._61Clear(state)),

    LocationData("The Cave Of The Bandits", "The Cave Of The Bandits: Red Coins", 0x3050C5, lambda state: logic._62Coins(state)),
    LocationData("The Cave Of The Bandits", "The Cave Of The Bandits: Flowers", 0x3050C6, lambda state: logic._62Flowers(state)),
    LocationData("The Cave Of The Bandits", "The Cave Of The Bandits: Stars", 0x3050C7, lambda state: logic._62Stars(state)),
    LocationData("The Cave Of The Bandits", "The Cave Of The Bandits: Level Clear", 0x3050C8, lambda state: logic._62Clear(state)),

    LocationData("Beware The Spinning Logs", "Beware The Spinning Logs: Red Coins", 0x3050C9, lambda state: logic._63Coins(state)),
    LocationData("Beware The Spinning Logs", "Beware The Spinning Logs: Flowers", 0x3050CA, lambda state: logic._63Flowers(state)),
    LocationData("Beware The Spinning Logs", "Beware The Spinning Logs: Stars", 0x3050CB, lambda state: logic._63Stars(state)),
    LocationData("Beware The Spinning Logs", "Beware The Spinning Logs: Level Clear", 0x3050CC, lambda state: logic._63Clear(state)),

    LocationData("Tap-Tap The Red Nose's Fort", "Tap-Tap The Red Nose's Fort: Red Coins", 0x3050CD, lambda state: logic._64Coins(state)),
    LocationData("Tap-Tap The Red Nose's Fort", "Tap-Tap The Red Nose's Fort: Flowers", 0x3050CE, lambda state: logic._64Flowers(state)),
    LocationData("Tap-Tap The Red Nose's Fort", "Tap-Tap The Red Nose's Fort: Stars", 0x3050CF, lambda state: logic._64Stars(state)),
    LocationData("Tap-Tap The Red Nose's Fort", "Tap-Tap The Red Nose's Fort: Level Clear", 0x3050D0, lambda state: logic._64Boss(state)),
    LocationData("Tap-Tap The Red Nose's Boss Room", 'Tap-Tap The Red Nose Defeated', 0x305115, lambda state: logic._64Boss(state)),

    LocationData("The Very Loooooong Cave", "The Very Loooooong Cave: Red Coins", 0x3050D1, lambda state: logic._65Coins(state)),
    LocationData("The Very Loooooong Cave", "The Very Loooooong Cave: Flowers", 0x3050D2, lambda state: logic._65Flowers(state)),
    LocationData("The Very Loooooong Cave", "The Very Loooooong Cave: Stars", 0x3050D3, lambda state: logic._65Stars(state)),
    LocationData("The Very Loooooong Cave", "The Very Loooooong Cave: Level Clear", 0x3050D4, lambda state: logic._65Clear(state)),

    LocationData("The Deep, Underground Maze", "The Deep, Underground Maze: Red Coins", 0x3050D5, lambda state: logic._66Coins(state)),
    LocationData("The Deep, Underground Maze", "The Deep, Underground Maze: Flowers", 0x3050D6, lambda state: logic._66Flowers(state)),
    LocationData("The Deep, Underground Maze", "The Deep, Underground Maze: Stars", 0x3050D7, lambda state: logic._66Stars(state)),
    LocationData("The Deep, Underground Maze", "The Deep, Underground Maze: Level Clear", 0x3050D8, lambda state: logic._66Clear(state)),

    LocationData("KEEP MOVING!!!!", "KEEP MOVING!!!!: Red Coins", 0x3050D9, lambda state: logic._67Coins(state)),
    LocationData("KEEP MOVING!!!!", "KEEP MOVING!!!!: Flowers", 0x3050DA, lambda state: logic._67Flowers(state)),
    LocationData("KEEP MOVING!!!!", "KEEP MOVING!!!!: Stars", 0x3050DB, lambda state: logic._67Stars(state)),
    LocationData("KEEP MOVING!!!!", "KEEP MOVING!!!!: Level Clear", 0x3050DC, lambda state: logic._67Clear(state)),

    LocationData("King Bowser's Castle", "King Bowser's Castle: Red Coins", 0x3050DD, lambda state: logic._68Coins(state)),
    LocationData("King Bowser's Castle", "King Bowser's Castle: Flowers", 0x3050DE, lambda state: logic._68Flowers(state)),
    LocationData("King Bowser's Castle", "King Bowser's Castle: Stars", 0x3050DF, lambda state: logic._68Stars(state)),
    LocationData("Bowser's Room", 'Saved Baby Luigi', EventId, lambda state: logic._68Clear(state))
    ]
    if not world or get_option_value(world, player, "extras_enabled") == 1:
        location_table += ( 
            LocationData("Poochy Ain't Stupid", "Poochy Ain't Stupid: Red Coins", 0x3050E0, lambda state: logic._1ECoins(state)),
            LocationData("Poochy Ain't Stupid", "Poochy Ain't Stupid: Flowers", 0x3050E1, lambda state: logic._1EFlowers(state)),
            LocationData("Poochy Ain't Stupid", "Poochy Ain't Stupid: Stars", 0x3050E2, lambda state: logic._1EStars(state)),
            LocationData("Poochy Ain't Stupid", "Poochy Ain't Stupid: Level Clear", 0x3050E3, lambda state: logic._1EClear(state)),

            LocationData("Hit That Switch!!", "Hit That Switch!!: Red Coins", 0x3050E4, lambda state: logic._2ECoins(state)),
            LocationData("Hit That Switch!!", "Hit That Switch!!: Flowers", 0x3050E5, lambda state: logic._2EFlowers(state)),
            LocationData("Hit That Switch!!", "Hit That Switch!!: Stars", 0x3050E6, lambda state: logic._2EStars(state)),
            LocationData("Hit That Switch!!", "Hit That Switch!!: Level Clear", 0x3050E7, lambda state: logic._2EClear(state)),

            LocationData("More Monkey Madness", "More Monkey Madness: Red Coins", 0x3050E8, lambda state: logic._3ECoins(state)),
            LocationData("More Monkey Madness", "More Monkey Madness: Flowers", 0x3050E9, lambda state: logic._3EFlowers(state)),
            LocationData("More Monkey Madness", "More Monkey Madness: Stars", 0x3050EA, lambda state: logic._3EStars(state)),
            LocationData("More Monkey Madness", "More Monkey Madness: Level Clear", 0x3050EB, lambda state: logic._3EClear(state)),

            LocationData("The Impossible? Maze", "The Impossible? Maze: Red Coins", 0x3050EC, lambda state: logic._4ECoins(state)),
            LocationData("The Impossible? Maze", "The Impossible? Maze: Flowers", 0x3050ED, lambda state: logic._4EFlowers(state)),
            LocationData("The Impossible? Maze", "The Impossible? Maze: Stars", 0x3050EE, lambda state: logic._4EStars(state)),
            LocationData("The Impossible? Maze", "The Impossible? Maze: Level Clear", 0x3050EF, lambda state: logic._4EClear(state)),

            LocationData("Kamek's Revenge", "Kamek's Revenge: Red Coins", 0x3050F0, lambda state: logic._5ECoins(state)),
            LocationData("Kamek's Revenge", "Kamek's Revenge: Flowers", 0x3050F1, lambda state: logic._5EFlowers(state)),
            LocationData("Kamek's Revenge", "Kamek's Revenge: Stars", 0x3050F2, lambda state: logic._5EStars(state)),
            LocationData("Kamek's Revenge", "Kamek's Revenge: Level Clear", 0x3050F3, lambda state: logic._5EClear(state)),

            LocationData("Castles - Masterpiece Set", "Castles - Masterpiece Set: Red Coins", 0x3050F4, lambda state: logic._6ECoins(state)),
            LocationData("Castles - Masterpiece Set", "Castles - Masterpiece Set: Flowers", 0x3050F5, lambda state: logic._6EFlowers(state)),
            LocationData("Castles - Masterpiece Set", "Castles - Masterpiece Set: Stars", 0x3050F6, lambda state: logic._6EStars(state)),
            LocationData("Castles - Masterpiece Set", "Castles - Masterpiece Set: Level Clear", 0x3050F7, lambda state: logic._6EClear(state)),
        )

    if not world or get_option_value(world, player, "minigame_checks") == 1 or get_option_value(world, player, "minigame_checks") == 3:
        location_table += ( 
            LocationData("The Cave Of Chomp Rock", "The Cave Of Chomp Rock: Bandit Game", 0x3050F8, lambda state: logic._13Game(state)),
            LocationData("Touch Fuzzy Get Dizzy", "Touch Fuzzy Get Dizzy: Bandit Game", 0x3050F9, lambda state: logic._17Game(state)),
            LocationData("Visit Koopa And Para-Koopa", "Visit Koopa And Para-Koopa: Bandit Game", 0x3050FA, lambda state: logic._21Game(state)),
            LocationData("What's Gusty Taste Like?", "What's Gusty Taste Like?: Bandit Game", 0x3050FB, lambda state: logic._23Game(state)),
            LocationData("The Cave Of The Mystery Maze", "The Cave Of The Mystery Maze: Bandit Game", 0x3050FC, lambda state: logic._26Game(state)),
            LocationData("Lakitu's Wall", "Lakitu's Wall: Bandit Game", 0x3050FD, lambda state: logic._27Game(state)),
            LocationData("Jungle Rhythm...", "Jungle Rhythm...: Bandit Game", 0x3050FE, lambda state: logic._32Game(state)),
            LocationData("Monkeys' Favorite Lake", "Monkeys' Favorite Lake: Bandit Game", 0x3050FF, lambda state: logic._37Game(state)),
            LocationData("The Cave Of The Lakitus", "The Cave Of The Lakitus: Bandit Game", 0x305100, lambda state: logic._42Game(state)),
            LocationData("Lake Shore Paradise", "Lake Shore Paradise: Bandit Game", 0x305101, lambda state: logic._46Game(state)),
            LocationData("Ride Like The Wind", "Ride Like The Wind: Bandit Game", 0x305102, lambda state: logic._47Game(state)),
            LocationData("BLIZZARD!!!", "BLIZZARD!!!: Bandit Game", 0x305103, lambda state: logic._51Game(state)),
            LocationData("Scary Skeleton Goonies!", "Scary Skeleton Goonies!: Bandit Game", 0x305104, lambda state: logic._61Game(state)),
            LocationData("KEEP MOVING!!!!", "KEEP MOVING!!!!: Bandit Game", 0x305105, lambda state: logic._67Game(state)),
        )

    if not world or get_option_value(world, player, "minigame_checks") == 2 or get_option_value(world, player, "minigame_checks") == 3:
        location_table += ( 
            LocationData("Flip Cards", "Flip Cards: Victory", 0x305106),
            LocationData("Scratch And Match", "Scratch And Match: Victory", 0x305107),
            LocationData("Drawing Lots", "Drawing Lots: Victory", 0x305108),
            LocationData("Match Cards", "Match Cards: Victory", 0x305109),
            LocationData("Roulette", "Roulette: Victory", 0x30510A),
            LocationData("Slot Machine", "Slot Machine: Victory", 0x30510B),
        )

    if not world or get_option_value(world, player, "item_logic") == 1:
        location_table += ( 
            LocationData("Flip Cards", 'Flip Cards', EventId),
            LocationData("Drawing Lots", 'Drawing Lots', EventId),
            LocationData("Match Cards", 'Match Cards', EventId),
        )
    return tuple(location_table)