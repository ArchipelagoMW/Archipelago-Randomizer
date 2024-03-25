"""
Author: Louis M
Date: Fri, 15 Mar 2024 18:41:40 +0000
Description: Used to manage Regions in the Aquaria game multiworld randomizer
"""

from typing import Dict, Optional
from BaseClasses import MultiWorld, Region, Entrance, ItemClassification
from worlds.generic.Rules import set_rule
from .Items import AquariaItem
from .Locations import AquariaLocations, AquariaLocation


# Every condition to connect regions

def _has_hot_soup(state, player) -> bool:
    """`player` in `state` has the hotsoup item"""
    return state.has("Hot soup", player)


def _has_tongue_cleared(state, player) -> bool:
    """`player` in `state` has the Body tongue cleared item"""
    return state.has("Body tongue cleared", player)


def _has_body_doors_opened(state, player) -> bool:
    """`player` in `state` has the 4 body doors opened item"""
    return state.has("Body door 1 opened", player) and \
        state.has("Body door 2 opened", player) and \
        state.has("Body door 3 opened", player) and \
        state.has("Body door 4 opened", player)


def _has_li(state, player) -> bool:
    """`player` in `state` has Li in it's team"""
    return state.has("Li and Li song", player)


def _has_damaging_item(state, player) -> bool:
    """`player` in `state` has the shield song item"""
    return state.has_group("Damage", player)


def _has_shield_song(state, player) -> bool:
    """`player` in `state` has the shield song item"""
    return state.has("Shield song", player)


def _has_bind_song(state, player) -> bool:
    """`player` in `state` has the bind song item"""
    return state.has("Bind song", player)


def _has_energy_form(state, player) -> bool:
    """`player` in `state` has the energy form item"""
    return state.has("Energy form", player)


def _has_beast_form(state, player) -> bool:
    """`player` in `state` has the beast form item"""
    return state.has("Beast form", player)


def _has_nature_form(state, player) -> bool:
    """`player` in `state` has the nature form item"""
    return state.has("Nature form", player)


def _has_sun_form(state, player) -> bool:
    """`player` in `state` has the sun form item"""
    return state.has("Sun form", player)


def _has_dual_form(state, player) -> bool:
    """`player` in `state` has the dual form item"""
    return state.has("Dual form", player)


def _has_fish_form(state, player) -> bool:
    """`player` in `state` has the fish form item"""
    return state.has("Fish form", player)


def _has_spirit_form(state, player) -> bool:
    """`player` in `state` has the spirit form item"""
    return state.has("Spirit form", player)


class AquariaRegions:
    """
    Class used to create regions of the Aquaria game
    """

    verse_cave_r: Region
    verse_cave_l: Region
    home_water: Region
    home_water_nautilus: Region
    naija_home: Region
    song_cave: Region
    song_cave_anemone: Region
    energy_temple_1: Region
    energy_temple_2: Region
    energy_temple_3: Region
    energy_temple_boss: Region
    energy_temple_idol: Region
    energy_temple_blaster_room: Region
    energy_temple_altar: Region
    openwater_tl: Region
    openwater_tr: Region
    openwater_tr_urns: Region
    openwater_tr_turtle: Region
    openwater_bl: Region
    openwater_bl_fp: Region
    openwater_br: Region
    skeleton_path: Region
    skeleton_path_sc: Region
    arnassi: Region
    arnassi_path: Region
    arnassi_crab_boss: Region
    simon: Region
    mithalas_city: Region
    mithalas_city_urns: Region
    mithalas_city_top_path: Region
    mithalas_city_top_path_urn: Region
    mithalas_city_fishpass: Region
    cathedral_l: Region
    cathedral_l_urns: Region
    cathedral_l_tube: Region
    cathedral_l_sc: Region
    cathedral_r: Region
    cathedral_underground: Region
    cathedral_boss_l: Region
    cathedral_boss_r: Region
    forest_tl: Region
    forest_tl_fp: Region
    forest_tr: Region
    forest_tr_dark: Region
    forest_tr_fp: Region
    forest_bl: Region
    forest_bl_sc: Region
    forest_br: Region
    forest_br_ship: Region
    forest_boss: Region
    forest_boss_entrance: Region
    forest_sprite_cave: Region
    forest_sprite_cave_tube: Region
    mermog_cave: Region
    mermog_boss: Region
    forest_fish_cave: Region
    veil_tl: Region
    veil_tl_fp: Region
    veil_tl_rock: Region
    veil_tr_l: Region
    veil_tr_r: Region
    veil_tr_water_fall: Region
    veil_bl: Region
    veil_b_sc: Region
    veil_bl_fp: Region
    veil_br: Region
    octo_cave_t: Region
    octo_cave_b: Region
    turtle_cave: Region
    turtle_cave_rocks: Region
    turtle_cave_bubble: Region
    turtle_cave_top_bubble: Region
    sun_temple_l: Region
    sun_temple_r: Region
    sun_temple_boss_lt: Region
    sun_temple_boss_lb: Region
    sun_temple_boss_r: Region
    abyss_l: Region
    abyss_lb: Region
    abyss_l_fp: Region
    abyss_r: Region
    ice_cave: Region
    bubble_cave: Region
    king_jellyfish_cave: Region
    whale: Region
    sunken_city_l: Region
    sunken_city_r: Region
    sunken_city_boss: Region
    sunken_city_l_bedroom: Region
    body_c: Region
    body_l: Region
    body_rt: Region
    body_rb: Region
    body_b: Region
    final_boss: Region
    final_boss_tube: Region
    final_boss_3_form: Region
    final_boss_end: Region
    """
    Every Region of the game
    """

    world: MultiWorld
    """
    The Current Multiworld game.
    """

    player: int
    """
    The ID of the player
    """

    def __add_region(self, name: str, hint: str,
                     locations: Optional[Dict[str, Optional[int]]]) -> Region:
        """
        Create a new Region, add it to the `world` regions and return it.
        Be aware that this function have a side effect on ``world`.`regions`
        """
        region: Region = Region(name, self.player, self.world, hint)
        if locations is not None:
            region.add_locations(locations, AquariaLocation)
        return region

    def __create_home_water_area(self):
        """
        Create the `verse_cave`, `home_water` and `song_cave*` regions
        """
        self.verse_cave_r = (
            self.__add_region("Menu", "Verse Cave right area", AquariaLocations.locations_verse_cave_r))
        self.verse_cave_l = (
            self.__add_region("verse_cave_left_area", "Verse Cave left area", AquariaLocations.locations_verse_cave_l))
        self.home_water = self.__add_region("home_water", "Home Water", AquariaLocations.locations_home_water)
        self.home_water_nautilus = self.__add_region("home_water_nautilus", "Home Water",
                                                     AquariaLocations.locations_home_water_nautilus)
        self.naija_home = self.__add_region("naija_home", "Naija's home", AquariaLocations.locations_naija_home)
        self.song_cave = self.__add_region("song_cave", "Song cave", AquariaLocations.locations_song_cave)
        self.song_cave_anemone = self.__add_region("song_cave_anemone", "Song cave",
                                                   AquariaLocations.locations_song_cave_anemone)

    def __create_energy_temple(self):
        """
        Create the `energy_temple_*` regions
        """
        self.energy_temple_1 = self.__add_region("energy_temple_1", "Energy temple first area",
                                                 AquariaLocations.locations_energy_temple_1)
        self.energy_temple_2 = self.__add_region("energy_temple_2", "Energy temple second area",
                                                 AquariaLocations.locations_energy_temple_2)
        self.energy_temple_3 = self.__add_region("energy_temple_3", "Energy temple third area",
                                                 AquariaLocations.locations_energy_temple_3)
        self.energy_temple_altar = self.__add_region("energy_temple_altar", "Energy temple bottom entrance",
                                                     AquariaLocations.locations_energy_temple_altar)
        self.energy_temple_boss = self.__add_region("energy_temple_boss", "Energy temple fallen God room",
                                                    AquariaLocations.locations_energy_temple_boss)
        self.energy_temple_idol = self.__add_region("energy_temple_idol", "Energy temple Idol room",
                                                    AquariaLocations.locations_energy_temple_idol)
        self.energy_temple_blaster_room = self.__add_region("energy_temple_blaster_room", "Energy temple blaster room",
                                                            AquariaLocations.locations_energy_temple_blaster_room)

    def __create_openwater(self):
        """
        Create the `openwater_*`, `skeleton_path`, `arnassi*` and `simon`
        regions
        """
        self.openwater_tl = self.__add_region("openwater_tl", "Open water top left area",
                                              AquariaLocations.locations_openwater_tl)
        self.openwater_tr = self.__add_region("openwater_tr", "Open water top right area",
                                              AquariaLocations.locations_openwater_tr)
        self.openwater_tr_turtle = self.__add_region("openwater_tr_turtle", "Open water top right area, turtle room",
                                                     AquariaLocations.locations_openwater_tr_turtle)
        self.openwater_tr_urns = self.__add_region("openwater_tr_urns", "Open water top right area",
                                                   AquariaLocations.locations_openwater_tr_urns)
        self.openwater_bl = self.__add_region("openwater_bl", "Open water bottom left area",
                                              AquariaLocations.locations_openwater_bl)
        self.openwater_bl_fp = self.__add_region("openwater_bl_fp", "Open water bottom left area",
                                                 AquariaLocations.locations_openwater_bl_fp)
        self.openwater_br = self.__add_region("openwater_br", "Open water bottom right area", None)
        self.skeleton_path = self.__add_region("skeleton_path", "Open water skeleton path",
                                               AquariaLocations.locations_skeleton_path)
        self.skeleton_path_sc = self.__add_region("skeleton_path_sc", "Open water skeleton path",
                                                  AquariaLocations.locations_skeleton_path_sc)
        self.arnassi = self.__add_region("arnassi", "Arnassi Ruins", AquariaLocations.locations_arnassi)
        self.simon = self.__add_region("simon", "Arnassi Ruins, Simon's room", AquariaLocations.locations_simon)
        self.arnassi_path = self.__add_region("arnassi_path", "Arnassi Ruins, back entrance path",
                                              AquariaLocations.locations_arnassi_path)
        self.arnassi_crab_boss = self.__add_region("arnassi_crab_boss", "Arnassi Ruins, Crabbius Maximus lair",
                                                   AquariaLocations.locations_arnassi_crab_boss)

    def __create_mithalas(self):
        """
        Create the `mithalas_city*` and `cathedral_*` regions
        """
        self.mithalas_city = self.__add_region("mithalas_city", "Mithalas city",
                                               AquariaLocations.locations_mithalas_city)
        self.mithalas_city_urns = self.__add_region("mithalas_city_urns", "Mithalas city",
                                                    AquariaLocations.locations_mithalas_city_urns)
        self.mithalas_city_fishpass = self.__add_region("mithalas_city_fishpass", "Mithalas city",
                                                        AquariaLocations.locations_mithalas_city_fishpass)
        self.mithalas_city_top_path = self.__add_region("mithalas_city_top_path", "Mithalas city",
                                                        AquariaLocations.locations_mithalas_city_top_path)
        self.mithalas_city_top_path_urn = self.__add_region("mithalas_city_top_path_urn", "Mithalas city",
                                                            AquariaLocations.locations_mithalas_city_top_path_urn)
        self.cathedral_l = self.__add_region("cathedral_l", "Mithalas castle", AquariaLocations.locations_cathedral_l)
        self.cathedral_l_urns = self.__add_region("cathedral_l_urns", "Mithalas castle",
                                                  AquariaLocations.locations_cathedral_l_urns)
        self.cathedral_l_tube = self.__add_region("cathedral_l_tube", "Mithalas castle, plant tube entrance",
                                                  AquariaLocations.locations_cathedral_l_tube)
        self.cathedral_l_sc = self.__add_region("cathedral_l_sc", "Mithalas castle",
                                                AquariaLocations.locations_cathedral_l_sc)
        self.cathedral_r = self.__add_region("cathedral_r", "Mithalas Cathedral",
                                             AquariaLocations.locations_cathedral_r)
        self.cathedral_underground = self.__add_region("cathedral_underground", "Mithalas Cathedral underground area",
                                                       AquariaLocations.locations_cathedral_underground)
        self.cathedral_boss_r = self.__add_region("cathedral_boss_r", "Mithalas Cathedral, Mithalan God room",
                                                  AquariaLocations.locations_cathedral_boss)
        self.cathedral_boss_l = self.__add_region("cathedral_boss_l", "Mithalas Cathedral, Mithalan God room", None)

    def __create_forest(self):
        """
        Create the `forest_*` dans `mermog_cave` regions
        """
        self.forest_tl = self.__add_region("forest_tl", "Kelp forest top left area",
                                           AquariaLocations.locations_forest_tl)
        self.forest_tl_fp = self.__add_region("forest_tl_fp", "Kelp forest top left area",
                                              AquariaLocations.locations_forest_tl_fp)
        self.forest_tr = self.__add_region("forest_tr", "Kelp forest top right area",
                                           AquariaLocations.locations_forest_tr)
        self.forest_tr_fp = self.__add_region("forest_tr_fp", "Kelp forest top right area",
                                              AquariaLocations.locations_forest_tr_fp)
        self.forest_tr_dark = self.__add_region("forest_tr_dark",
                                                "Kelp forest top right area, the dark behind the seawolf",
                                                AquariaLocations.locations_forest_tr_dark)
        self.forest_bl = self.__add_region("forest_bl", "Kelp forest bottom left area",
                                           AquariaLocations.locations_forest_bl)
        self.forest_bl_sc = self.__add_region("forest_bl_sc", "Kelp forest bottom left area, spirit cristal",
                                              AquariaLocations.locations_forest_bl_sc)
        self.forest_br = self.__add_region("forest_br", "Kelp forest bottom right area", None)
        self.forest_br_ship = self.__add_region("forest_br_ship", "Kelp forest bottom right area, sunken ship",
                                                AquariaLocations.locations_forest_br_ship)
        self.forest_sprite_cave = self.__add_region("forest_sprite_cave", "Kelp forest spirit cave",
                                                    AquariaLocations.locations_forest_sprite_cave)
        self.forest_sprite_cave_tube = self.__add_region("forest_sprite_cave_tube",
                                                         "Kelp forest spirit cave after the plant tube",
                                                         AquariaLocations.locations_forest_sprite_cave_tube)
        self.forest_boss = self.__add_region("forest_boss", "Kelp forest Drunian God room",
                                             AquariaLocations.locations_forest_boss)
        self.forest_boss_entrance = self.__add_region("forest_boss_entrance", "Kelp forest Drunian God room",
                                                      AquariaLocations.locations_forest_boss_entrance)
        self.mermog_cave = self.__add_region("mermog_cave", "Kelp forest Mermog cave",
                                             AquariaLocations.locations_mermog_cave)
        self.mermog_boss = self.__add_region("mermog_boss", "Kelp forest Mermog cave",
                                             AquariaLocations.locations_mermog_boss)
        self.forest_fish_cave = self.__add_region("forest_fish_cave", "Kelp forest fish cave",
                                                  AquariaLocations.locations_forest_fish_cave)

    def __create_veil(self):
        """
        Create the `veil_*`, `octo_cave` and `turtle_cave` regions
        """
        self.veil_tl = self.__add_region("veil_tl", "The veil top left area", AquariaLocations.locations_veil_tl)
        self.veil_tl_fp = self.__add_region("veil_tl_fp", "The veil top left area",
                                            AquariaLocations.locations_veil_tl_fp)
        self.veil_tl_rock = self.__add_region("veil_tl_rock", "The veil top left area, after blocking rock",
                                              AquariaLocations.locations_veil_tl_rock)
        self.turtle_cave = self.__add_region("turtle_cave", "The veil top left area, turtle cave", None)
        self.turtle_cave_rocks = self.__add_region("turtle_cave_rocks", "The veil top left area, turtle cave",
                                                   AquariaLocations.locations_turtle_cave_rocks)
        self.turtle_cave_bubble = self.__add_region("turtle_cave_bubble",
                                                    "The veil top left area, turtle cave bubble cliff",
                                                    AquariaLocations.locations_turtle_cave_bubble)
        self.turtle_cave_top_bubble = self.__add_region("turtle_cave_top_bubble",
                                                        "The veil top left area, turtle cave bubble cliff",
                                                        AquariaLocations.locations_turtle_cave_top_bubble)
        self.veil_tr_l = self.__add_region("veil_tr_l", "The veil top right area, left of temple",
                                           AquariaLocations.locations_veil_tr_l)
        self.veil_tr_r = self.__add_region("veil_tr_r", "The veil top right area, right of temple",
                                           AquariaLocations.locations_veil_tr_r)
        self.veil_tr_water_fall = self.__add_region("veil_tr_water_fall",
                                                    "The veil top right area, top of the water fall",
                                                    AquariaLocations.locations_veil_tr_water_fall)
        self.octo_cave_t = self.__add_region("octo_cave_t", "Octopus cave top entrance",
                                             AquariaLocations.locations_octo_cave_t)
        self.octo_cave_b = self.__add_region("octo_cave_b", "Octopus cave bottom entrance",
                                             AquariaLocations.locations_octo_cave_b)
        self.veil_bl = self.__add_region("veil_bl", "The veil bottom left area",
                                         AquariaLocations.locations_veil_bl)
        self.veil_b_sc = self.__add_region("veil_b_sc", "The veil bottom spirit cristal area",
                                           AquariaLocations.locations_veil_b_sc)
        self.veil_bl_fp = self.__add_region("veil_bl_fp", "The veil bottom left area",
                                            AquariaLocations.locations_veil_bl_fp)
        self.veil_br = self.__add_region("veil_br", "The veil bottom right area",
                                         AquariaLocations.locations_veil_br)

    def __create_sun_temple(self):
        """
        Create the `sun_temple*` regions
        """
        self.sun_temple_l = self.__add_region("sun_temple_l", "Sun temple left area",
                                              AquariaLocations.locations_sun_temple_l)
        self.sun_temple_r = self.__add_region("sun_temple_r", "Sun temple right area",
                                              AquariaLocations.locations_sun_temple_r)
        self.sun_temple_boss_lt = self.__add_region("sun_temple_boss_lt",
                                                    "Sun temple before boss area, top of the cliffs",
                                                    AquariaLocations.locations_sun_temple_boss_lt)
        self.sun_temple_boss_lb = self.__add_region("sun_temple_boss_lb", "Sun temple before boss area",
                                                    AquariaLocations.locations_sun_temple_boss_lb)
        self.sun_temple_boss_r = self.__add_region("sun_temple_boss_r", "Sun temple boss area",
                                                   AquariaLocations.locations_sun_temple_boss_r)

    def __create_abyss(self):
        """
        Create the `abyss_*`, `ice_cave`, `king_jellyfish_cave` and `whale`
        regions
        """
        self.abyss_l = self.__add_region("abyss_l", "Abyss left area",
                                         AquariaLocations.locations_abyss_l)
        self.abyss_lb = self.__add_region("abyss_lb", "Abyss left bottom area", None)
        self.abyss_l_fp = self.__add_region("abyss_l_fp", "Abyss left buttom area",
                                            AquariaLocations.locations_abyss_l_fp)
        self.abyss_r = self.__add_region("abyss_r", "Abyss right area", AquariaLocations.locations_abyss_r)
        self.ice_cave = self.__add_region("ice_cave", "Ice cave", AquariaLocations.locations_ice_cave)
        self.bubble_cave = self.__add_region("bubble_cave", "Bubble cave", AquariaLocations.locations_bubble_cave)
        self.king_jellyfish_cave = self.__add_region("king_jellyfish_cave", "Abyss left area, King jellyfish cave",
                                                     AquariaLocations.locations_king_jellyfish_cave)
        self.whale = self.__add_region("whale", "Inside the whale", AquariaLocations.locations_whale)

    def __create_sunken_city(self):
        """
        Create the `sunken_city_*` regions
        """
        self.sunken_city_l = self.__add_region("sunken_city_l", "Sunken city left area",
                                               AquariaLocations.locations_sunken_city_l)
        self.sunken_city_l_bedroom = self.__add_region("sunken_city_l_bedroom", "Sunken city left area, bedroom",
                                                       AquariaLocations.locations_sunken_city_l_bedroom)
        self.sunken_city_r = self.__add_region("sunken_city_r", "Sunken city right area",
                                               AquariaLocations.locations_sunken_city_r)
        self.sunken_city_boss = (
            self.__add_region("sunken_city_boss", "Sunken city boss area",
                              AquariaLocations.locations_sunken_city_boss))

    def __create_body(self):
        """
        Create the `body_*` and `final_boss* regions
        """
        self.body_c = self.__add_region("body_c", "The body center area",
                                        AquariaLocations.locations_body_c)
        self.body_l = self.__add_region("body_l", "The body left area",
                                        AquariaLocations.locations_body_l)
        self.body_rt = self.__add_region("body_rt", "The body right area, top path",
                                         AquariaLocations.locations_body_rt)
        self.body_rb = self.__add_region("body_rb", "The body right area, bottom path",
                                         AquariaLocations.locations_body_rb)
        self.body_b = self.__add_region("body_b", "The body bottom area",
                                        AquariaLocations.locations_body_b)
        self.final_boss = self.__add_region("final_boss", "The body, final boss area", None)
        self.final_boss_tube = self.__add_region("final_boss_tube", "The body, final boss area turtle room",
                                                 AquariaLocations.locations_final_boss_tube)
        self.final_boss_3_form = self.__add_region("final_boss_3_form", "The body final boss third form area",
                                                   AquariaLocations.locations_final_boss_3_form)
        self.final_boss_end = self.__add_region("final_boss_end", "The body, final boss area", None)

    def __connect_one_way_regions(self, source_name: str, destination_name: str,
                                  source_region: Region,
                                  destination_region: Region, rule=None):
        """
        Connect from the `source_region` to the `destination_region`
        """
        entrance = Entrance(source_region.player, source_name + " to " + destination_name, source_region)
        source_region.exits.append(entrance)
        entrance.connect(destination_region)
        if rule is not None:
            set_rule(entrance, rule)

    def __connect_regions(self, source_name: str, destination_name: str,
                          source_region: Region,
                          destination_region: Region, rule=None):
        """
        Connect the `source_region` and the `destination_region` (two-way)
        """
        self.__connect_one_way_regions(source_name, destination_name, source_region, destination_region, rule)
        self.__connect_one_way_regions(destination_name, source_name, destination_region, source_region, rule)

    def __connect_home_water_regions(self):
        """
        Connect entrances of the different regions around `home_water`
        """
        self.__connect_regions("Verse cave left area", "Verse cave right area",
                               self.verse_cave_l, self.verse_cave_r)
        self.__connect_regions("Verse cave", "Home water", self.verse_cave_l, self.home_water)
        self.__connect_regions("Home Water", "Haija's home", self.home_water, self.naija_home)
        self.__connect_regions("Home Water", "Song cave", self.home_water, self.song_cave)
        self.__connect_regions("Home Water", "home_water_nautilus",
                               self.home_water, self.home_water_nautilus,
                               lambda state: _has_energy_form(state, self.player))  # Need energy form# ToDo: Remove
        self.__connect_regions("Song cave", "Song cave Anemone",
                               self.song_cave, self.song_cave_anemone,
                               lambda state: _has_nature_form(state, self.player))  # Need Nature Form  # ToDo: Remove
        self.__connect_regions("Home Water", "Energy temple first area",
                               self.home_water, self.energy_temple_1,
                               lambda state: _has_bind_song(state, self.player))  # Need bind song
        self.__connect_regions("Home Water", "Energy temple_altar",
                               self.home_water, self.energy_temple_altar,
                               lambda state: _has_energy_form(state, self.player))  # Need energy form
        self.__connect_regions("Energy temple first area", "Energy temple second area",
                               self.energy_temple_1, self.energy_temple_2,
                               lambda state: _has_energy_form(state, self.player))  # Need energy form
        self.__connect_regions("Energy temple first area", "Energy temple idol room",
                               self.energy_temple_1, self.energy_temple_idol,
                               lambda state: _has_fish_form(state, self.player))  # Need Fish form
        self.__connect_regions("Energy temple idol room", "Energy temple boss area",
                               self.energy_temple_idol, self.energy_temple_boss,
                               lambda state: _has_energy_form(state, self.player))  # Need Energy form
        self.__connect_one_way_regions("Energy temple first area", "Energy temple boss area",
                                       self.energy_temple_1, self.energy_temple_boss,
                                       lambda state: _has_beast_form(state, self.player) and
                                                     _has_energy_form(state,
                                                                      self.player))  # Need Beast forma and Energy form
        self.__connect_one_way_regions("Energy temple boss area", "Energy temple first area",
                                       self.energy_temple_boss, self.energy_temple_1,
                                       lambda state: _has_energy_form(state, self.player))  # Need Energy form
        self.__connect_regions("Energy temple second area", "Energy temple third area",
                               self.energy_temple_2, self.energy_temple_3,
                               lambda state: _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player))  # Need Bind form and Energy form
        self.__connect_regions("Energy temple boss area", "Energy temple blaster room",
                               self.energy_temple_boss, self.energy_temple_blaster_room,
                               lambda state: _has_nature_form(state, self.player) and
                                             _has_bind_song(state, self.player) and
                                             _has_energy_form(state,
                                                              self.player))  # Need Nature form, Bind form and energy form
        self.__connect_regions("Energy temple first area", "Energy temple_blaster_room",
                               self.energy_temple_1, self.energy_temple_blaster_room,
                               lambda state: _has_nature_form(state, self.player) and
                                             _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player) and
                                             _has_beast_form(state,
                                                             self.player))  # Need Nature form, Bind form, energy form and Beast form
        self.__connect_regions("Home Water", "Open water top left area",
                               self.home_water, self.openwater_tl,
                               lambda state: _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player))  # Need Bind song and energy form

    def __connect_open_water_regions(self):
        """
        Connect entrances of the different regions around open water
        """
        self.__connect_regions("Open water top left area", "Open water top right area",
                               self.openwater_tl, self.openwater_tr)
        self.__connect_regions("Open water top left area", "Open water bottom left area",
                               self.openwater_tl, self.openwater_bl)
        self.__connect_regions("Open water top left area", "forest bottom right area",
                               self.openwater_tl, self.forest_br)
        self.__connect_regions("Open water top right area", "Open water top right area, turtle room",
                               self.openwater_tr, self.openwater_tr_turtle,
                               lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Open water top right area", "Open water top right area_urns",
                                       self.openwater_tr, self.openwater_tr_urns,
                                       lambda state: _has_damaging_item(state, self.player))
        self.__connect_one_way_regions("Open water top right area_urns", "Open water top right area",
                                       self.openwater_tr_urns, self.openwater_tr)
        self.__connect_regions("Open water top right area", "Open water bottom right",
                               self.openwater_tr, self.openwater_br)
        self.__connect_regions("Open water top right area", "Mithalas city",
                               self.openwater_tr, self.mithalas_city)
        self.__connect_regions("Open water top right area", "Veil bottom left area",
                               self.openwater_tr, self.veil_bl)
        self.__connect_one_way_regions("Open water top right area", "Veil bottom right",
                                       self.openwater_tr, self.veil_br,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Veil bottom right", "Open water top right area",
                                       self.veil_br, self.openwater_tr,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_regions("Open water bottom left area", "Open water bottom right",
                               self.openwater_bl, self.openwater_br)
        self.__connect_regions("Open water bottom left area", "skeleton_path",
                               self.openwater_bl, self.skeleton_path)
        self.__connect_regions("Open water bottom left area", "Abyss left area",
                               self.openwater_bl, self.abyss_l)
        self.__connect_regions("Open water bottom left area", "Open water_bl_fp",
                               self.openwater_bl, self.openwater_bl_fp,
                               lambda state: _has_fish_form(state, self.player))  # Fish form
        self.__connect_regions("skeleton_path", "skeleton_path_sc",
                               self.skeleton_path, self.skeleton_path_sc,
                               lambda state: _has_spirit_form(state, self.player))  # Spirit form needed
        self.__connect_regions("Open water bottom right", "Abyss right area",
                               self.openwater_br, self.abyss_r)
        self.__connect_one_way_regions("Open water bottom right", "Arnassi",
                                       self.openwater_br, self.arnassi,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Arnassi", "Open water bottom right",
                                       self.arnassi, self.openwater_br)
        self.__connect_regions("Arnassi", "Arnassi path",
                               self.arnassi, self.arnassi_path)
        self.__connect_one_way_regions("Arnassi path", "Arnassi crab boss area",
                                       self.arnassi_path, self.arnassi_crab_boss,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Arnassi crab boss area", "Arnassi path",
                                       self.arnassi_crab_boss, self.arnassi_path)
        self.__connect_regions("Arnassi path", "simon", self.arnassi_path, self.simon,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed

    def __connect_mithalas_regions(self):
        """
        Connect entrances of the different regions around Mithalas
        """
        self.__connect_one_way_regions("Mithalas city", "Mithalas city_urns",
                                       self.mithalas_city, self.mithalas_city_urns,
                                       lambda state: _has_energy_form(state, self.player))  # Energy form needed
        self.__connect_one_way_regions("Mithalas city_urns", "Mithalas city",
                                       self.mithalas_city_urns, self.mithalas_city)
        self.__connect_one_way_regions("Mithalas city", "Mithalas city_top_path",
                                       self.mithalas_city, self.mithalas_city_top_path,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Mithalas city_top_path", "Mithalas city",
                                       self.mithalas_city_top_path, self.mithalas_city)
        self.__connect_regions("Mithalas city_top_path", "Mithalas city_top_path_urn",
                               self.mithalas_city_top_path, self.mithalas_city_top_path_urn,
                               lambda state: _has_energy_form(state, self.player))  # Energy form needed
        self.__connect_regions("Mithalas city", "Mithalas city home with fishpass",
                               self.mithalas_city, self.mithalas_city_fishpass,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed
        self.__connect_regions("Mithalas city", "Cathedral left area",
                               self.mithalas_city, self.cathedral_l,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed
        self.__connect_one_way_regions("Mithalas city top path", "Cathedral left area, flower tube",
                                       self.mithalas_city_top_path,
                                       self.cathedral_l_tube,
                                       lambda state: _has_nature_form(state, self.player))  # Nature form
        self.__connect_one_way_regions("Cathedral left area, flower tube area", "Mithalas city top path",
                                       self.cathedral_l_tube,
                                       self.mithalas_city_top_path,
                                       lambda state: _has_beast_form(state, self.player) and
                                                     _has_nature_form(state, self.player))  # Nature form
        self.__connect_regions("Cathedral left area flower tube area", "Cathedral left area, spirit crystals",
                               self.cathedral_l_tube, self.cathedral_l_sc,
                               lambda state: _has_spirit_form(state, self.player))  # spirit form needed
        self.__connect_regions("Cathedral left area_flower tube area", "Cathedral left area",
                               self.cathedral_l_tube, self.cathedral_l,
                               lambda state: _has_spirit_form(state, self.player))  # spirit form needed
        self.__connect_regions("Cathedral left area", "Cathedral left area, spirit crystals",
                               self.cathedral_l, self.cathedral_l_sc,
                               lambda state: _has_spirit_form(state, self.player))  # spirit form needed
        self.__connect_regions("Cathedral left area", "Cathedral left area urns",
                               self.cathedral_l, self.cathedral_l_urns,
                               lambda state: _has_energy_form(state, self.player))  # energy form needed
        self.__connect_regions("Cathedral left area", "Cathedral boss left area",
                               self.cathedral_l, self.cathedral_boss_l) # ToDo: beast form needed and Location mithalas boss needed
        self.__connect_regions("Cathedral left area", "Cathedral underground",
                               self.cathedral_l, self.cathedral_underground,
                               lambda state: _has_beast_form(state, self.player) and
                                             _has_bind_song(state, self.player))  # beast form and bind song needed
        self.__connect_regions("Cathedral left area", "Cathedral right area",
                               self.cathedral_l, self.cathedral_r,
                               lambda state: _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player))  # bind song and energy form needed
        self.__connect_regions("Cathedral right area", "Cathedral underground",
                               self.cathedral_r, self.cathedral_underground,
                               lambda state: _has_energy_form(state, self.player))  # energy form needed
        self.__connect_one_way_regions("Cathedral underground", "Cathedral boss left area",
                                       self.cathedral_underground, self.cathedral_boss_r,
                                       lambda state: _has_energy_form(state, self.player))  # bind song and energy form needed
        self.__connect_one_way_regions("Cathedral boss left area", "Cathedral underground",
                                       self.cathedral_boss_r, self.cathedral_underground,
                                       lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_one_way_regions("Cathedral boss right area", "Cathedral boss left area",
                                       self.cathedral_boss_r, self.cathedral_boss_l,
                                       lambda state: _has_bind_song(state, self.player) and
                                                     _has_energy_form(state, self.player))  # bind song and energy form
        self.__connect_one_way_regions("Cathedral boss left area", "Cathedral boss right area",
                                       self.cathedral_boss_l, self.cathedral_boss_r)

    def __connect_forest_regions(self):
        """
        Connect entrances of the different regions around the Kelp Forest
        """
        self.__connect_regions("forest bottom right", "forest_br_ship",
                               self.forest_br, self.forest_br_ship,
                               lambda state: _has_sun_form(state, self.player))  # Sun form needed
        self.__connect_regions("Forest bottom right", "Veil bottom left area",
                               self.forest_br, self.veil_bl)
        self.__connect_regions("Forest bottom right", "Forest bottom left area",
                               self.forest_br, self.forest_bl)
        self.__connect_regions("Forest bottom right", "Forest top right area",
                               self.forest_br, self.forest_tr)
        self.__connect_regions("Forest bottom left area", "Forest bottom left area, spirit crystals",
                               self.forest_bl, self.forest_bl_sc,
                               lambda state: _has_spirit_form(state, self.player))  # spirit form needed
        self.__connect_regions("Forest bottom left area", "Forest fish cave",
                               self.forest_bl, self.forest_fish_cave)
        self.__connect_regions("Forest bottom left area", "Forest top left area",
                               self.forest_bl, self.forest_tl)
        self.__connect_regions("Forest bottom left area", "Forest boss entrance",
                               self.forest_bl, self.forest_boss_entrance,
                               lambda state: _has_nature_form(state, self.player))  # Nature form needed
        self.__connect_regions("Forest top left area", "Forest top left area, fish pass",
                               self.forest_tl, self.forest_tl_fp,
                               lambda state: _has_nature_form(state, self.player) and
                                             _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player) and
                                             _has_fish_form(state, self.player))  # Nature form, Bind song, Energy form and Fish form needed
        self.__connect_regions("Forest top left area", "Forest top right area",
                               self.forest_tl, self.forest_tr)
        self.__connect_regions("Forest top left area", "Forest boss entrance",
                               self.forest_tl, self.forest_boss_entrance)
        self.__connect_regions("Forest boss area", "Forest boss entrance",
                               self.forest_boss, self.forest_boss_entrance,
                               lambda state: _has_energy_form(state, self.player))  # Energy form needed
        self.__connect_regions("Forest top right area", "Forest top right area dark place",
                               self.forest_tr, self.forest_tr_dark,
                               lambda state: _has_sun_form(state, self.player))  # Sun form needed
        self.__connect_regions("Forest top right area", "Forest top right area fish pass",
                               self.forest_tr, self.forest_tr_fp,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed
        self.__connect_regions("Forest top right area", "Forest sprite cave",
                               self.forest_tr, self.forest_sprite_cave)
        self.__connect_regions("Forest sprite cave", "Forest sprite cave flower tube",
                               self.forest_sprite_cave, self.forest_sprite_cave_tube,
                               lambda state: _has_nature_form(state, self.player))  # Nature form needed
        self.__connect_regions("Forest top right area", "Mermog cave",
                               self.forest_tr_fp, self.mermog_cave)
        self.__connect_regions("Fermog cave", "Fermog boss",
                               self.mermog_cave, self.mermog_boss,
                               lambda state: _has_beast_form(state, self.player) and
                                             _has_energy_form(state, self.player))  # Beast form and energy form needed

    def __connect_veil_regions(self):
        """
        Connect entrances of the different regions around The Veil
        """
        self.__connect_regions("Veil bottom left area", "Veil bottom left area, fish pass",
                               self.veil_bl, self.veil_bl_fp,
                               lambda state: _has_fish_form(state, self.player) and
                                             _has_bind_song(state, self.player) and
                                             _has_energy_form(state, self.player))  # Fish form, bind song and Energy form needed
        self.__connect_regions("Veil bottom left area", "Veil bottom area spirit crystals path",
                               self.veil_bl, self.veil_b_sc,
                               lambda state: _has_spirit_form(state, self.player))  # Spirit form needed
        self.__connect_regions("Veil bottom area spirit crystals path", "Veil bottom right",
                               self.veil_b_sc, self.veil_br,
                               lambda state: _has_spirit_form(state, self.player))  # Spirit form needed
        self.__connect_regions("Veil bottom right", "Veil top left area",
                               self.veil_br, self.veil_tl,
                               lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_regions("Veil top left area", "Veil_top left area, fish pass",
                               self.veil_tl, self.veil_tl_fp,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed
        self.__connect_regions("Veil top left area", "Veil_top left area, under the rock",
                               self.veil_tl, self.veil_tl_rock,
                               lambda state: _has_bind_song(state, self.player))  # Bind song needed
        self.__connect_regions("Veil top left area", "Veil right of sun temple",
                               self.veil_tl, self.veil_tr_r)
        self.__connect_regions("Veil top left area", "Turtle cave",
                               self.veil_tl, self.turtle_cave)
        self.__connect_regions("Turtle cave", "Turtle cave under the rocks",
                               self.turtle_cave, self.turtle_cave_rocks,
                               lambda state: _has_bind_song(state, self.player))  # Bind song needed
        self.__connect_regions("Turtle cave", "Turtle cave bubble cliff",
                               self.turtle_cave, self.turtle_cave_bubble,
                               lambda state: _has_beast_form(state, self.player))  # Beast form needed
        self.__connect_regions("Veil right of sun temple", "Sun temple right area",
                               self.veil_tr_r, self.sun_temple_r)
        self.__connect_regions("Sun temple right area", "Sun temple left area",
                               self.sun_temple_r, self.sun_temple_l,
                               lambda state: _has_bind_song(state, self.player))  # bind song needed
        self.__connect_regions("Sun temple left area", "Veil left of top sun temple",
                               self.sun_temple_l, self.veil_tr_l)
        self.__connect_regions("Sun temple left area", "Sun temple_boss left bottom area",
                               self.sun_temple_l, self.sun_temple_boss_lb)
        self.__connect_one_way_regions("Sun temple_boss left bottom area", "Sun temple_boss top of left area",
                                       self.sun_temple_boss_lb, self.sun_temple_boss_lt,
                                       lambda state: _has_hot_soup(state, self.player) and
                                                     _has_beast_form(state, self.player))# Beast form needed
        self.__connect_one_way_regions("Sun temple_boss top of left area", "Sun temple_boss left bottom area",
                                       self.sun_temple_boss_lt, self.sun_temple_boss_lb)
        self.__connect_regions("Sun temple_boss left bottom area", "Sun temple_boss right area",
                               self.sun_temple_boss_lb, self.sun_temple_boss_r,
                               lambda state: _has_energy_form(state, self.player))  # Energy form needed
        self.__connect_one_way_regions("Sun temple_boss right area", "Veil left of sun temple",
                                       self.sun_temple_boss_r, self.veil_tr_l)
        self.__connect_one_way_regions( "Turtle cave bubble cliff", "Turtle cave top bubble",
                                        self.turtle_cave_bubble, self.turtle_cave_top_bubble,
                                        lambda state: _has_hot_soup(state, self.player) and
                                                      _has_beast_form(state, self.player)) # Beast form needed
        self.__connect_one_way_regions(
            "Turtle cave top bubble", "Turtle cave bubble cliff",
            self.turtle_cave_top_bubble, self.turtle_cave_bubble)
        self.__connect_one_way_regions("Veil left of sun temple", "Veil left of sun temple, water fall",
                                       self.veil_tr_l, self.veil_tr_water_fall,
                                       lambda state: _has_hot_soup(state, self.player) and
                                                     _has_beast_form(state, self.player))# Beast form needed
        self.__connect_one_way_regions("Veil left of sun temple, water fall", "Veil left of sun temple",
                                       self.veil_tr_water_fall, self.veil_tr_l)
        self.__connect_regions("Veil left of sun temple", "Octo cave top path",
                               self.veil_tr_l, self.octo_cave_t,
                               lambda state: _has_fish_form(state, self.player) and
                                             _has_sun_form(state, self.player) and
                                             _has_beast_form(state, self.player))  # Fish, sun and beast form needed
        self.__connect_regions("Veil left of sun temple", "Octo cave bottom path",
                               self.veil_tr_l, self.octo_cave_b,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed

    def __connect_abyss_regions(self):
        """
        Connect entrances of the different regions around The Abyss
        """
        self.__connect_regions("Abyss left area", "Abyss bottom of left area",
                               self.abyss_l, self.abyss_lb,
                               lambda state: _has_nature_form(state, self.player))  # Nature form needed
        self.__connect_regions("Abyss bottom of left area", "Abyss left area, fish pass",
                               self.abyss_lb, self.abyss_l_fp,
                               lambda state: _has_fish_form(state, self.player))  # Fish form needed
        self.__connect_regions("Abyss left bottom area", "Sunken city right area",
                               self.abyss_lb, self.sunken_city_r,
                               lambda state: _has_li(state, self.player))  # Li needed
        self.__connect_regions( "Abyss left bottom area", "Body center area",
                                self.abyss_lb, self.body_c,
                                lambda state: _has_tongue_cleared(state, self.player))
        self.__connect_regions("Abyss left area", "king_jellyfish_cave",
                               self.abyss_l, self.king_jellyfish_cave,
                               lambda state: _has_energy_form(state, self.player))  # Energy form needed
        self.__connect_regions("Abyss left area", "Abyss right area",
                               self.abyss_l, self.abyss_r)
        self.__connect_regions("Abyss right area", "whale",
                               self.abyss_r, self.whale,
                               lambda state: _has_spirit_form(state, self.player) and
                                             _has_sun_form(state, self.player))  # Spirit form and sun form needed
        self.__connect_regions("Abyss right area", "ice_cave",
                               self.abyss_r, self.ice_cave,
                               lambda state: _has_spirit_form(state, self.player))  # Spirit form needed
        self.__connect_regions("Abyss right area", "bubble_cave",
                               self.abyss_r, self.bubble_cave,
                               lambda state: _has_beast_form(state, self.player))  # Beast form needed

    def __connect_sunken_city_regions(self):
        """
        Connect entrances of the different regions around The Sunken City
        """
        self.__connect_regions("Sunken city right area",
                               "Sunken city left area",
                               self.sunken_city_r, self.sunken_city_l)
        self.__connect_regions("Sunken city left area", "Sunken city bedroom",
                               self.sunken_city_l, self.sunken_city_l_bedroom,
                               lambda state: _has_spirit_form(state, self.player))  # Spirit form needed
        self.__connect_regions("Sunken city left area", "Sunken city boss area",
                               self.sunken_city_l, self.sunken_city_boss)

    def __connect_body_regions(self):
        """
        Connect entrances of the different regions around The body
        """
        self.__connect_regions("Body center area", "Body left area",
                               self.body_c, self.body_l)
        self.__connect_regions("Body center area", "Body right area top path",
                               self.body_c, self.body_rt)
        self.__connect_regions("Body center area", "Body right area bottom path",
                               self.body_c, self.body_rb)
        self.__connect_regions("Body center area", "Body bottom area",
                               self.body_c, self.body_b,
                               lambda state: _has_body_doors_opened(state, self.player))
        self.__connect_regions("Body bottom area", "Final boss area",
                               self.body_b, self.final_boss,
                               lambda state: _has_body_doors_opened(state, self.player))
        self.__connect_regions("Final boss area", "Final boss tube",
                               self.final_boss, self.final_boss_tube,
                               lambda state: _has_nature_form(state, self.player))  # Nature form needed
        self.__connect_one_way_regions("Final boss area", "Final boss third form area",
                                       self.final_boss, self.final_boss_3_form)  # ToDo: Need final boss conditions
        self.__connect_one_way_regions("final boss third form area", "final boss end",
                                       self.final_boss_3_form, self.final_boss_end)

    def connect_regions(self):
        """
        Connect every region (entrances and exits)
        """
        self.__connect_home_water_regions()
        self.__connect_open_water_regions()
        self.__connect_mithalas_regions()
        self.__connect_forest_regions()
        self.__connect_veil_regions()
        self.__connect_abyss_regions()
        self.__connect_sunken_city_regions()
        self.__connect_body_regions()

    def __add_event_location(self, region: Region, name: str, event_name: str):
        """
        Add an event to the `region` with the name `name` and the item
        `event_name`
        """
        location: AquariaLocation = AquariaLocation(
            self.player, name, None, region
        )
        region.locations.append(location)
        location.place_locked_item(AquariaItem(event_name,
                                               ItemClassification.progression,
                                               None,
                                               self.player))

    def add_event_locations(self):
        """
        Add every events (locations and items) to the `world`
        """
        self.__add_event_location(self.abyss_lb,
                                  "Sunken City cleared",
                                  "Body tongue cleared")
        self.__add_event_location(self.body_l,
                                  "Trotite spirit freed",
                                  "Body door 1 opened")
        self.__add_event_location(self.body_l, "Drask spirit freed",
                                  "Body door 2 opened")
        self.__add_event_location(self.body_rt, "Druniad spirit freed",
                                  "Body door 3 opened")
        self.__add_event_location(self.body_rb, "Erulian spirit freed",
                                  "Body door 4 opened")
        self.__add_event_location(self.final_boss_end, "Objective complete",
                                  "Victory")

    def __add_home_water_regions_to_world(self):
        """
        Add every region around home water to the `world`
        """
        self.world.regions.append(self.verse_cave_r)
        self.world.regions.append(self.verse_cave_l)
        self.world.regions.append(self.home_water)
        self.world.regions.append(self.home_water_nautilus)
        self.world.regions.append(self.naija_home)
        self.world.regions.append(self.song_cave)
        self.world.regions.append(self.song_cave_anemone)
        self.world.regions.append(self.energy_temple_1)
        self.world.regions.append(self.energy_temple_2)
        self.world.regions.append(self.energy_temple_3)
        self.world.regions.append(self.energy_temple_boss)
        self.world.regions.append(self.energy_temple_blaster_room)
        self.world.regions.append(self.energy_temple_altar)

    def __add_open_water_regions_to_world(self):
        """
        Add every region around open water to the `world`
        """
        self.world.regions.append(self.openwater_tl)
        self.world.regions.append(self.openwater_tr)
        self.world.regions.append(self.openwater_tr_turtle)
        self.world.regions.append(self.openwater_bl)
        self.world.regions.append(self.openwater_bl_fp)
        self.world.regions.append(self.openwater_br)
        self.world.regions.append(self.skeleton_path)
        self.world.regions.append(self.skeleton_path_sc)
        self.world.regions.append(self.arnassi)
        self.world.regions.append(self.arnassi_path)
        self.world.regions.append(self.arnassi_crab_boss)
        self.world.regions.append(self.simon)

    def __add_mithalas_regions_to_world(self):
        """
        Add every region around Mithalas to the `world`
        """
        self.world.regions.append(self.mithalas_city)
        self.world.regions.append(self.mithalas_city_urns)
        self.world.regions.append(self.mithalas_city_top_path)
        self.world.regions.append(self.mithalas_city_top_path_urn)
        self.world.regions.append(self.mithalas_city_fishpass)
        self.world.regions.append(self.cathedral_l)
        self.world.regions.append(self.cathedral_l_urns)
        self.world.regions.append(self.cathedral_l_tube)
        self.world.regions.append(self.cathedral_l_sc)
        self.world.regions.append(self.cathedral_r)
        self.world.regions.append(self.cathedral_underground)
        self.world.regions.append(self.cathedral_boss_l)
        self.world.regions.append(self.cathedral_boss_r)

    def __add_forest_regions_to_world(self):
        """
        Add every region around the kelp forest to the `world`
        """
        self.world.regions.append(self.forest_tl)
        self.world.regions.append(self.forest_tl_fp)
        self.world.regions.append(self.forest_tr)
        self.world.regions.append(self.forest_tr_dark)
        self.world.regions.append(self.forest_tr_fp)
        self.world.regions.append(self.forest_bl)
        self.world.regions.append(self.forest_bl_sc)
        self.world.regions.append(self.forest_br)
        self.world.regions.append(self.forest_br_ship)
        self.world.regions.append(self.forest_boss)
        self.world.regions.append(self.forest_boss_entrance)
        self.world.regions.append(self.forest_sprite_cave)
        self.world.regions.append(self.forest_sprite_cave_tube)
        self.world.regions.append(self.mermog_cave)
        self.world.regions.append(self.mermog_boss)
        self.world.regions.append(self.forest_fish_cave)

    def __add_veil_regions_to_world(self):
        """
        Add every region around the Veil to the `world`
        """
        self.world.regions.append(self.veil_tl)
        self.world.regions.append(self.veil_tl_fp)
        self.world.regions.append(self.veil_tl_rock)
        self.world.regions.append(self.veil_tr_l)
        self.world.regions.append(self.veil_tr_r)
        self.world.regions.append(self.veil_tr_water_fall)
        self.world.regions.append(self.veil_bl)
        self.world.regions.append(self.veil_b_sc)
        self.world.regions.append(self.veil_bl_fp)
        self.world.regions.append(self.veil_br)
        self.world.regions.append(self.octo_cave_t)
        self.world.regions.append(self.octo_cave_b)
        self.world.regions.append(self.turtle_cave)
        self.world.regions.append(self.turtle_cave_rocks)
        self.world.regions.append(self.turtle_cave_bubble)
        self.world.regions.append(self.turtle_cave_top_bubble)
        self.world.regions.append(self.sun_temple_l)
        self.world.regions.append(self.sun_temple_r)
        self.world.regions.append(self.sun_temple_boss_lt)
        self.world.regions.append(self.sun_temple_boss_lb)
        self.world.regions.append(self.sun_temple_boss_r)

    def __add_abyss_regions_to_world(self):
        """
        Add every region around the Abyss to the `world`
        """
        self.world.regions.append(self.abyss_l)
        self.world.regions.append(self.abyss_lb)
        self.world.regions.append(self.abyss_l_fp)
        self.world.regions.append(self.abyss_r)
        self.world.regions.append(self.ice_cave)
        self.world.regions.append(self.bubble_cave)
        self.world.regions.append(self.king_jellyfish_cave)
        self.world.regions.append(self.whale)
        self.world.regions.append(self.sunken_city_l)
        self.world.regions.append(self.sunken_city_r)
        self.world.regions.append(self.sunken_city_boss)
        self.world.regions.append(self.sunken_city_l_bedroom)

    def __add_body_regions_to_world(self):
        """
        Add every region around the Body to the `world`
        """
        self.world.regions.append(self.body_c)
        self.world.regions.append(self.body_l)
        self.world.regions.append(self.body_rt)
        self.world.regions.append(self.body_rb)
        self.world.regions.append(self.body_b)
        self.world.regions.append(self.final_boss)
        self.world.regions.append(self.final_boss_tube)
        self.world.regions.append(self.final_boss_3_form)
        self.world.regions.append(self.final_boss_end)

    def add_regions_to_world(self):
        """
        Add every region to the `world`
        """
        self.__add_home_water_regions_to_world()
        self.__add_open_water_regions_to_world()
        self.__add_mithalas_regions_to_world()
        self.__add_forest_regions_to_world()
        self.__add_veil_regions_to_world()
        self.__add_abyss_regions_to_world()
        self.__add_body_regions_to_world()

    def __init__(self, world: MultiWorld, player: int):
        """
        Initialisation of the regions
        """
        self.world = world
        self.player = player
        self.__create_home_water_area()
        self.__create_energy_temple()
        self.__create_openwater()
        self.__create_mithalas()
        self.__create_forest()
        self.__create_veil()
        self.__create_sun_temple()
        self.__create_abyss()
        self.__create_sunken_city()
        self.__create_body()
