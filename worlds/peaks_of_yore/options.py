from Options import Toggle, DefaultOnToggle, DeathLink, Choice, PerGameCommonOptions
from dataclasses import dataclass


class Goal(Choice):
    """
    Decide what needs to happen to be counted as a win

    **all peaks**: Finish all peaks in selected books to win/complete your run
    **all artefacts**: Collect all artefacts on selected peaks
    **all artefacts all peaks**: complete both of the above
    **all**: all items including bird seeds and ropes
    """
    display_name = "Goal"
    option_all_peaks = 0
    option_all_artefacts = 1
    option_all_artefacts_all_peaks = 2
    option_all = 3
    default = 0


class StartingBook(Choice):
    """Choose what book to start with. WARNING: Make sure your selected book is also enabled"""
    display_name = "Starting Book"
    option_fundamentals = 0
    option_intermediate = 1
    option_advanced = 2
    option_expert = 3
    default = 0


class StartWithBarometer(DefaultOnToggle):
    """Choose to start with the barometer, to locate items quicker"""
    display_name = "Start With Barometer"


class EnableFundamental(DefaultOnToggle):
    """Enables Fundamentals book, items and collectibles"""
    display_name = "Fundamental Peaks"


class EnableIntermediate(DefaultOnToggle):
    """Enables Intermediate book, items and collectibles"""
    display_name = "Intermediate Peaks"


class EnableAdvanced(DefaultOnToggle):
    """Enables Advanced book, items and collectibles"""
    display_name = "Advanced Peaks"


class EnableExpert(DefaultOnToggle):
    """Enables Expert book, items and collectibles"""
    display_name = "Expert Peaks"


class DisableSolemnTempest(DefaultOnToggle):
    """Removes Solemn Tempest from the locations pool, has no effect if \"Enable Expert Peaks\" is disabled"""
    display_name = "Disable Solemn Tempest"


@dataclass
class PeaksOfYoreOptions(PerGameCommonOptions):
    death_link: DeathLink
    goal: Goal
    starting_book: StartingBook
    start_with_barometer: StartWithBarometer
    enable_fundamental: EnableFundamental
    enable_intermediate: EnableIntermediate
    enable_advanced: EnableAdvanced
    enable_expert: EnableExpert
    disable_solemn_tempest: DisableSolemnTempest
