from Options import Choice, Option, Range, Toggle, OptionSet
import typing


class SoraEXP(Range):
    """Sora Level Exp Multiplier"""
    display = "Sora Level EXP"
    range_start = 1
    range_end = 10
    default = 5


class FinalEXP(Range):
    """Final Form Exp Multiplier"""
    display_name = "Final Form EXP"
    range_start = 1
    range_end = 10
    default = 3


class MasterEXP(Range):
    """Master Form Exp Multiplier"""
    display_name = "Master Form EXP"
    range_start = 1
    range_end = 10
    default = 3


class LimitEXP(Range):
    """Limit Form Exp Multiplier"""
    display_name = "Limit Form EXP"
    range_start = 1
    range_end = 10
    default = 3


class WisdomEXP(Range):
    """WIsdom Form exp Multiplier"""
    display_name = "Wisdom Form EXP"
    range_start = 1
    range_end = 10
    default = 3


class ValorEXP(Range):
    """Valor Form Exp Multiplier"""
    display_name = "Valor Form EXP"
    range_start = 1
    range_end = 10
    default = 3


class SummonEXP(Range):
    """Summon's Exp Multiplier"""
    display_name = "Summon level EXP"
    range_start = 1
    range_end = 10
    default = 5


class Schmovement(Choice):
    """Level of Growth You Start With"""
    display_name = "Schmovement"
    option_level_0 = 0
    option_level_1 = 1
    option_level_2 = 2
    option_level_3 = 3
    option_level_4 = 4
    default = 1


class RandomGrowth(Range):
    """Amount of Random Growth Abilites You Start With"""
    display_name = "Random Starting Growth"
    range_start = 0
    range_end = 20
    default = 0


class KeybladeMin(Range):
    """Minimum Stats for the Keyblade"""
    display_name = "Keyblade Minimum Stats"
    range_start = 0
    range_end = 20
    default = 3


class KeybladeMax(Range):
    """Maximum Stats for the Keyblade"""
    display_name = "Keyblade Max Stats"
    range_start = 0
    range_end = 20
    default = 7


class Visitlocking(Choice):
    # What is locked being on
    # if 0 then no visit locking  if 1 then second visits if 2 then first and second visits with one item
    display_name = "Visit locking"
    option_no_visit_locking = 0
    option_second_visit_locking = 1
    option_first_visit_locking = 2
    default = 0


class SuperBosses(Toggle):
    """Terra, Sephiroth and Data Fights Toggle"""
    display_name = "Super Bosses"
    default = False


class LevelDepth(Choice):
    # What is locked being on
    # if 0 then no visit locking  if 1 then second visits if 2 then first and second visits with one item
    display_name = "Level Depth"
    option_level_50 = 0
    option_level_99 = 1
    option_level_99_sanity = 2
    option_level_50_sanity = 3
    option_level_1 = 4
    default = 0


class MaxLogic(Toggle):
    """Forms on forms and torn pages in cor/ag"""
    display_name = "Max Logic"
    default = True


class PromiseCharm(Toggle):
    """Add Promise Charm to the Pool"""
    display_name = "Promise Charm"
    default = False


class KeybladeAbilities(Choice):
    """Action:Has Action Abilites on Keyblades Support:Has Support Abilites on Keyblades"""
    display_name = "Keyblade Abilities"
    option_support = 0
    option_action = 1
    option_both = 2
    default = 2


class BlacklistKeyblade(OptionSet):
    """Black List these Abilities on Keyblades"""
    display_name = "Blacklist Keyblade Abilities"
    verify_item_name = True


class Goal(Choice):
    """Win Condition"""
    display_name = "Goal"
    #three proof kill final xemnas
    option_three_proofs = 0
    #have all important checks
    option_all_blue_numbers = 1
    #luckey emblem hunt
    option_lucky_emblem_hunt = 2
    default = 0

class FinalXemnas(Toggle):
    """Kill Final Xemnas to Beat the Game"""
    display_name = "Final Xemnas"
    default=True
class LuckyEmblemsRequired(Range):
    """Number of Lucky Emblems to collect to Open The Final Door bosses."""
    display_name = "Lucky Emblems Required"
    range_start = 0
    range_end = 60
    default = 25

class LuckyEmblemsAmount(Range):
    """Number of Lucky Emblems that are in the pool"""
    display_name = "Lucky Emblems Available"
    range_start = 0
    range_end = 60
    default = 40


KH2_Options: typing.Dict[str, type(Option)] = {
    "Sora_Level_EXP":       SoraEXP,
    "Final_Form_EXP":       FinalEXP,
    "Master_Form_EXP":      MasterEXP,
    "Limit_Form_EXP":       LimitEXP,
    "Wisdom_Form_EXP":      WisdomEXP,
    "Valor_Form_EXP":       ValorEXP,
    "Summon_EXP":           SummonEXP,
    "Schmovement":          Schmovement,
    "Keyblade_Minimum":     KeybladeMin,
    "Keyblade_Maximum":     KeybladeMax,
    "Visit_locking":        Visitlocking,
    "Super_Bosses":         SuperBosses,
    "Level_Depth":          LevelDepth,
    "Max_Logic":            MaxLogic,
    "Promise_Charm":        PromiseCharm,
    "KeybladeAbilities":    KeybladeAbilities,
    "BlacklistKeyblade":    BlacklistKeyblade,
    "RandomGrowth":         RandomGrowth,
    "Goal":                 Goal,
    "FinalXemnas":FinalXemnas,
    "LuckyEmblemsAmount":   LuckyEmblemsAmount,
    "LuckyEmblemsRequired": LuckyEmblemsRequired
}
