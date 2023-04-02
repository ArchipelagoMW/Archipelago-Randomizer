from typing import Dict
from Options import Toggle, Option, Range, Choice, DeathLink

# Should this be default on or off?
class AllowJustAsPlannedDLCSongs(Toggle):
    """Whether or not Just as Planned DLC songs, and all the DLCs along with it, will be included in the randomiser.
    Note: The newest DLC songs will most likely not be included in any randomisation."""
    display_name = "Allow Just As Planned DLC Songs"


class StreamerModeEnabled(Toggle):
    """Whether or not the randomisation will take into account Streamer Mode. If enabled, only songs available in Streamer Mode will be randomised."""
    display_name = "Streamer Mode Only Songs"


class StartingSongs(Range):
    """The number of songs that will be automatically unlocked at the start of a run."""
    display_name = "Starting Amout of Songs"
    range_start = 3
    range_end = 10
    default = 5
    display_name = "Starting Song Count"


class AdditionalSongs(Range):
    """The total number of songs that will be placed in the randomisation pool.
    - Does not count any starting songs or the final goal.
    - Final count may be lower due to other settings.
    """
    range_start = 15
    range_end = 500 #Note will probably not reach this high if any other settings are done.
    default = 50
    display_name = "Additional Song Count"


#Todo: Get feedback on these ranges.
class DifficultyMode(Choice):
    """Ensures that at any chosen song as at least 1 value falling within these values.
    - Easy: 1, 2 or 3
    - Medium: 4, 5
    - Hard: 6, 7
    - Expert: 8, 9
    - Master: 10+
    - Any: All songs are available"""
    display_name = "Song Difficulty"
    option_Any = 0
    option_Easy = 1
    option_Medium = 2
    option_Hard = 3
    option_Expert = 4
    option_Master = 5
    option_Manual = 6
    default = 0

class DifficultyModeOverrideMin(Range):
    """Ensures that 1 song has at least 1 song this value or higher."""
    range_start = 1
    range_end = 11
    default = 4

class DifficultyModeOverrideMax(Range):
    """Ensures that 1 song has at least 1 song this value or lower."""
    range_start = 1
    range_end = 11
    default = 8

class GradeNeeded(Choice):
    """Requires a grade of this or higher in order to get items.
    Grades are as follows:
    Silver S (SS): >= 95% accuracy
    Pink S (S): >= 90% accuracy
    A: >= 80% or a Full Combo
    B: >= 70%
    C: >= 60%
    """
    display_name = "Grade Needed"
    option_Any = 0
    option_C = 1
    option_B = 2
    option_A = 3
    option_PinkS = 4
    option_SilverS = 5
    default = 0


class MusicSheetCountPercentage(Range):
    """Music sheets are what you need to win Muse Dash. This controls how many sheets are in the item pool.
    This is based on the number of songs in the pool."""
    range_start = 5
    range_end = 25
    default = 15
    display_name = "Music Sheet Percentage"


class MusicSheetWinCountPercentage(Range):
    """The percentage of Music Sheets needed to unlock the winning song."""
    range_start = 50
    range_end = 100
    default = 80
    display_name = "Music Sheets Needed to Win"

class AdditionalItemPercentage(Range):
    """What percentage of songs will have 2 items instead of 1. Starting Songs will always have 2 locations."""
    display_name = "Additional Item %"
    range_start = 50
    default = 80
    range_end = 100


musedash_options: Dict[str, type(Option)] = {
    "allow_just_as_planned_dlc_songs": AllowJustAsPlannedDLCSongs,
    "streamer_mode_enabled": StreamerModeEnabled,
    "starting_song_count": StartingSongs,
    "additional_song_count": AdditionalSongs,
    "additional_item_percentage": AdditionalItemPercentage,
    "song_difficulty_mode": DifficultyMode,
    "song_difficulty_min": DifficultyModeOverrideMin,
    "song_difficulty_max": DifficultyModeOverrideMax,
    "grade_needed": GradeNeeded,
    "music_sheet_count_percentage": MusicSheetCountPercentage,
    "music_sheet_win_count_percentage": MusicSheetWinCountPercentage,
    "death_link": DeathLink
}
