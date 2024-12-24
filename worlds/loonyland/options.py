from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions


class WinCondition(Choice):
    """Evilizer: Beat the final boss
    NOT IMPLEMENTED: 40 badges: get all 40 badge locs
    NOT IMPLEMENTED: normal_remix: Beat the final boss in normal and remix"""

    display_name = "Win Condition"
    option_evilizer = 0
    option_40badges = 1
    option_normal_remix = 2
    default = 0


class Difficulty(Choice):
    """Difficulty Setting"""

    display_name = "Difficulty"
    option_beginner = 0
    option_normal = 1
    option_hard = 2
    option_challenge = 3
    option_mad = 4
    option_loony = 5
    default = 1


class LongChecks(Choice):
    """Excluded: Remove 100%, 39 badges, swampdog to 50, witch to lvl 9 spells, 5000 gems, and the monster point badges
    Does nothing if badges are already set to none
    """

    display_name = "Long Checks"
    option_excluded = 0
    option_included = 1
    default = 0


class Remix(Choice):
    """Excluded: Remix mode not included"""

    display_name = "Remix"
    option_excluded = 0
    option_included = 1
    default = 0


class Badges(Choice):
    """Full: All badges and their cheats are in logic
    Reasonable: Remove hard to get badges and overpowered cheats
    Vanilla: Badges aren't randomized, but are in logic
    None: Badges aren't in logic"""

    display_name = "Badges"
    option_full = 0
    option_vanilla = 1
    option_none = 2
    default = 2


class MonsterDolls(Choice):
    """Full: Monsters can drop randomized items, monster dolls can be found at locations
    Vanilla: Monsters drop their normal monster doll
    None: Dolls aren't in logic"""

    display_name = "Monster Dolls"
    option_full = 0
    option_vanilla = 1
    option_none = 2
    default = 0


@dataclass
class LoonylandOptions(PerGameCommonOptions):
    # win_condition: WinCondition
    difficulty: Difficulty
    long_checks: LongChecks
    remix: Remix
    badges: Badges
    dolls: MonsterDolls
    death_link: DeathLink
