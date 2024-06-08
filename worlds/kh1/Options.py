from dataclasses import dataclass

from Options import NamedRange, Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions

class StrengthIncrease(Range):
    """
    Number of Strength Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "STR Increases"
    range_start = 0
    range_end = 100
    default = 24

class DefenseIncrease(Range):
    """
    Number of Defense Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "DEF Increases"
    range_start = 0
    range_end = 100
    default = 24

class HPIncrease(Range):
    """
    Number of HP Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "HP Increases"
    range_start = 0
    range_end = 100
    default = 23

class APIncrease(Range):
    """
    Number of AP Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "AP Increases"
    range_start = 0
    range_end = 100
    default = 18

class MPIncrease(Range):
    """
    Number of MP Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "MP Increases"
    range_start = 0
    range_end = 20
    default = 7

class AccessorySlotIncrease(Range):
    """
    Number of Accessory Slot Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "Accessory Slot Increases"
    range_start = 0
    range_end = 6
    default = 1

class ItemSlotIncrease(Range):
    """
    Number of Item Slot Increases to Add to the Level Up Rewards
    
    The randomizer will add all stat up defined here into a pool and choose up to 100 to add to the multiworld.
    Accessory Slot Increases and Item Slot Increases are prioritized first, then the remaining items (up to 100 total) are chosen at random.
    """
    display_name = "Item Slot Increases"
    range_start = 0
    range_end = 5
    default = 3

class Atlantica(Toggle):
    """
    Toggle whether Atlantica locations/items should be included.
    """
    display_name = "Atlantica"

class HundredAcreWood(Toggle):
    """
    Toggle whether to include checks in the 100 Acre Wood
    """
    display_name = "100 Acre Wood"

class SuperBosses(Toggle):
    """
    Toggle whether to include checks behind Super Bosses.
    """
    display_name = "Super Bosses"

class Cups(Toggle):
    """
    Toggle whether to include checks behind completing Phil, Pegasus, Hercules, or Hades cups.  Please note that the items will still appear in the multiworld, as they are required to challenge Sephiroth.
    """
    display_name = "Cups"

class Goal(Choice):
    """
    Determines when victory is achieved in your playthrough.
    
    Sephiroth: Defeat Sephiroth.
    Unknown: Defeat Unknown.
    Postcards: Turn in all 10 postcards in Traverse Town
    Final Ansem: Enter End of the World and defeat Ansem as normal
    Puppies: Rescue and return all 99 puppies in Traverse Town.
    """
    display_name = "Goal"
    option_sephiroth = 0
    option_unknown = 1
    option_postcards = 2
    option_final_ansem = 3
    option_puppies = 4
    default = 3

class EndoftheWorldUnlock(Choice):
    """Determines how End of the World is Unlocked"""
    display_name = "End of the World Unlock"
    option_item = 0
    option_reports = 1
    default = 1

class FinalRestDoor(Choice):
    """Determines what conditions need to be met to manifest the door in Final Rest, allowing the player to challenge Ansem
    
    Reports: A certain number of Ansem's Reports are required.  That number is defined in another setting.
    Puppies: Having all 99 puppies is required.
    Postcards: Turning in all 10 postcards is required.
    Superbosses: Defeating Sephiroth, Unknown, Kurt Zisa, and Phantom are required.
    """
    display_name = "Final Rest Door"
    option_reports = 0
    option_puppies = 1
    option_postcards = 2
    option_superbosses = 3

class Puppies(Choice):
    """
    Determines how dalmation puppies are shuffled into the pool.
    Full: All puppies are in one location
    Triplets: Puppies are found in triplets just as they are in the base game
    Individual: One puppy can be found per location
    """
    display_name = "Puppies"
    option_full = 0
    option_triplets = 1
    option_individual = 2
    default = 1

class EXPMultiplier(NamedRange):
    """
    Determines the multiplier to apply to EXP gained
    """
    display_name = "EXP Multiplier"
    default = 16
    range_start = default / 4
    range_end = 128
    special_range_names = {
        "0.25x": default / 4,
        "0.5x": default / 2,
        "1x": default,
        "2x": default * 2,
        "3x": default * 3,
        "4x": default * 4,
        "8x": default * 8,
    }

class RequiredReportsEotW(Range):
    """
    If End of the World Unlock is set to "Reports", determines the number of Ansem's Reports required to open End of the World.
    """
    display_name = "Reports to Open End of the World"
    default = 4
    range_start = 0
    range_end = 13
    
class RequiredReportsDoor(Range):
    """
    If Final Rest Door is set to "Reports", determines the number of Ansem's Reports required to manifest the door in Final Rest to challenge Ansem.
    """
    display_name = "Reports to Open Final Rest Door"
    default = 4
    range_start = 0
    range_end = 13

class ReportsInPool(Range):
    """
    Determines the number of Ansem's Reports in the item pool.
    """
    display_name = "Reports in Pool"
    default = 4
    range_start = 0
    range_end = 13

class RandomizeKeybladeStats(DefaultOnToggle):
    """
    Determines whether Keyblade stats should be randomized
    """
    display_name = "Randomize Keyblade Stats"

class KeybladeMinStrength(Range):
    """
    Determines the lowest STR bonus a keyblade can have
    """
    display_name = "Keyblade Minimum STR Bonus"
    default = 3
    range_start = 0
    range_end = 20

class KeybladeMaxStrength(Range):
    """
    Determines the maximum STR bonus a keyblade can have
    """
    display_name = "Keyblade Maximum STR Bonus"
    default = 14
    range_start = 0
    range_end = 20

class KeybladeMinMP(Range):
    """
    Determines the minimum MP bonus a keyblade can have
    """
    display_name = "Keyblade Minimum MP Bonus"
    default = -2
    range_start = -2
    range_end = 5

class KeybladeMaxMP(Range):
    """
    Determines the maximum MP bonus a keyblade can have
    """
    display_name = "Keyblade Maximum MP Bonus"
    default = 3
    range_start = -2
    range_end = 5

class LevelChecks(Range):
    """
    Determines the maximum level for which checks can be obtained.
    """
    display_name = "Level Checks"
    default = 100
    range_start = 0
    range_end = 100

class ForceStatsOnLevels(NamedRange):
    """
    If this value is less than the value for Level Checks, this determines the minimum level from which only stat ups are obtained at level up locations
    For example, if you want to be able to find any multiworld item from levels 1-50, then just stat ups for levels 51-100, set this value to 51.
    """
    display_name = "Force Stats on Level Starting From"
    default = 1
    range_start = 1
    range_end = 101
    special_range_names = {
        "none": 101,
        "multiworld-to-level-50": 51,
        "all": 1
    }

class BadStartingWeapons(Toggle):
    """
    Forces Kingdom Key, Dream Sword, Dream Shield, and Dream Staff to have bad stats
    """
    display_name = "Bad Starting Weapons"

class DonaldDeathLink(Toggle):
    """
    If Donald is KO'ed, so is Sora.  If Death Link is toggled on in your client, this will send a death to everyone.
    """
    display_name = "Donald Death Link"

class GoofyDeathLink(Toggle):
    """
    If Goofy is KO'ed, so is Sora.  If Death Link is toggled on in your client, this will send a death to everyone.
    """
    display_name = "Goofy Death Link"

class KeybladesUnlockChests(Toggle):
    """
    If toggled on, the player is required to have a certain keyblade to open chests in certain worlds.
    TT   - Lionheart
    WL   - Lady Luck
    OC   - Olympia
    DJ   - Jungle King
    AG   - Three Wishes
    MS   - Wishing Star
    HT   - Pumpkinhead
    NL   - Fairy Harp
    HB   - Divine Rose
    EotW - Oblivion
    
    Note: Does not apply to Atlantica, 100 Acre Wood, The emblem and carousel chests in Hollow Bastion, or the Aero chest in Neverland currently.
    """
    display_name = "Keyblades Unlock Chests"

class InteractInBattle(Toggle):
    """
    Allow Sora to talk, examine, and open chests in battle
    """
    display_name = "Interact in Battle"

class AdvancedLogic(Toggle):
    """
    If on, logic may expect you to do advanced skips like combo master, dumbo, and other unusual methods for reaching locations.
    """
    display_name = "Advanced Logic"

class ExtraSharedAbilities(Toggle):
    """
    If on, adds extra shared abilities to the pool.  These can stack, so multiple high jumps make you jump higher and multiple glides make you superglide faster.
    """
    display_name = "Extra Shared Abilities"

class EXPZeroInPool(Toggle):
    """
    If on, adds EXP Zero ability to the item pool.  This is redundant if you are planning on playing on Proud.
    """
    display_name = "EXP Zero in Pool"

class VanillaEmblemPieces(DefaultOnToggle):
    """
    If on, the Hollow Bastion emblem pieces are in their vanilla locations.
    """
    display_name = "Vanilla Emblem Pieces"

class JunkInMissableLocations(DefaultOnToggle):
    """
    If on, will place Elixirs in missable locations.  If turned off, there is a chance you will need to play the game multiple times to get the missed items.
    Locations include:
        Leon Gift
        Aerith Gift
        Clock Tower Doors
        World Terminus Hollow Bastion Chest
    """
    display_name = "Junk in Missable Locations"

@dataclass
class KH1Options(PerGameCommonOptions):
    goal: Goal
    end_of_the_world_unlock: EndoftheWorldUnlock
    final_rest_door: FinalRestDoor
    required_reports_eotw: RequiredReportsEotW
    required_reports_door: RequiredReportsDoor
    reports_in_pool: ReportsInPool
    super_bosses: SuperBosses
    atlantica: Atlantica
    hundred_acre_wood: HundredAcreWood
    cups: Cups
    puppies: Puppies
    keyblades_unlock_chests: KeybladesUnlockChests
    interact_in_battle: InteractInBattle
    exp_multiplier: EXPMultiplier
    advanced_logic: AdvancedLogic
    extra_shared_abilities: ExtraSharedAbilities
    exp_zero_in_pool: EXPZeroInPool
    vanilla_emblem_pieces: VanillaEmblemPieces
    junk_in_missable_locations: JunkInMissableLocations
    donald_death_link: DonaldDeathLink
    goofy_death_link: GoofyDeathLink
    randomize_keyblade_stats: RandomizeKeybladeStats
    bad_starting_weapons: BadStartingWeapons
    keyblade_max_str: KeybladeMaxStrength
    keyblade_min_str: KeybladeMinStrength
    keyblade_max_mp: KeybladeMaxMP
    keyblade_min_mp: KeybladeMinMP
    level_checks: LevelChecks
    force_stats_on_levels: ForceStatsOnLevels
    strength_increase: StrengthIncrease
    defense_increase: DefenseIncrease
    hp_increase: HPIncrease
    ap_increase: APIncrease
    mp_increase: MPIncrease
    accessory_slot_increase: AccessorySlotIncrease
    item_slot_increase: ItemSlotIncrease
    
    
