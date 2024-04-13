from dataclasses import dataclass

from Options import Choice, Range, DeathLink, PerGameCommonOptions


class DeathLinkAmnesty(Range):
    """How many deaths it takes to send a DeathLink"""
    display_name = "Death Link Amnesty"
    range_start = 1
    range_end = 30
    default = 10

class TotalStrawberries(Range):
    """How many Strawberries exist"""
    display_name = "Total Strawberries"
    range_start = 0
    range_end = 20
    default = 15

class StrawberriesRequiredPercentage(Range):
    """Percentage of existing Strawberries you must receive to finish"""
    display_name = "Strawberries Required Percentage"
    range_start = 0
    range_end = 100
    default = 80

class BadelineChaserSource(Choice):
    """
    What type of action causes more Badeline Chasers to start spawning
    Locations: The amount of locations you've checked contributes to Badeline Chasers
    Strawberries: The amount of Strawberry items you've received contibutes to Badeline Chasers
    """
    display_name = "Badeline Chaser Source"
    option_locations = 0
    option_strawberries = 1
    default = 0

class BadelineChaserFrequency(Range):
    """
    How many of the `Badeline Chaser Source` actions must occur to make each Badeline Chaser start spawning
    NOTE: Choosing `0` disables Badeline Chasers entirely
    """
    display_name = "Badeline Chaser Frequency"
    range_start = 0
    range_end = 10
    default = 5

class BadelineChaserSpeed(Range):
    """How many seconds behind you each Badeline Chaser will be"""
    display_name = "Badeline Chaser Speed"
    range_start = 2
    range_end = 10
    default = 3


@dataclass
class Celeste64Options(PerGameCommonOptions):
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty

    total_strawberries: TotalStrawberries
    strawberries_required_percentage: StrawberriesRequiredPercentage

    badeline_chaser_source: BadelineChaserSource
    badeline_chaser_frequency: BadelineChaserFrequency
    badeline_chaser_speed: BadelineChaserSpeed
