import logging
import os

logger = logging.getLogger("Ocarina of Time")

from .Location import OOTLocation, LocationFactory
from .Entrance import OOTEntrance
from .Items import item_table, ItemFactory, MakeEventItem
from .ItemPool import generate_itempool
from .Regions import OOTRegion, TimeOfDay
from .Rules import set_rules, set_shop_rules, set_age_rules
from .RuleParser import Rule_AST_Transformer
from .Options import oot_options
from .Utils import data_path, read_json
from .LocationList import business_scrubs, set_drop_location_names
from .DungeonList import dungeon_table, create_dungeons

import Utils
from BaseClasses import Region, Entrance, Location, MultiWorld, Item
from Options import Range
from Fill import fill_restrictive
from ..AutoWorld import World


class OOTWorld(World):
    game: str = "Ocarina of Time"
    options = oot_options

    def __init__(self, world, player):
        super(OOTWorld, self).__init__(world, player)
        self.parser = Rule_AST_Transformer(self, self.player)
        for (option_name, option) in oot_options.items(): 
            result = getattr(self.world, option_name)[self.player]
            setattr(self, option_name, int(result) if isinstance(result, Range) else result.get_option_name())
        self.dungeon_mq = {item['name']: False for item in dungeon_table}  # sets all dungeons to non-MQ for now; need this to not break things
        self.shop_prices = {}
        self.regions = []  # internal cache of regions for this world, used later

        self.keysanity = self.shuffle_smallkeys in ['keysanity', 'remove', 'any_dungeon', 'overworld']
        self.ensure_tod_access = False
        # self.ensure_tod_access = self.shuffle_interior_entrances or self.shuffle_overworld_entrances or self.randomize_overworld_spawns

        # Determine skipped trials in GT
        # This needs to be done before the logic rules in GT are parsed
        self.skipped_trials = {}
        trial_list = ['Forest', 'Fire', 'Water', 'Spirit', 'Shadow', 'Light']
        chosen_trials = self.world.random.sample(trial_list, self.trials)  # chooses a list of trials to NOT skip
        for t in trial_list:
            self.skipped_trials[t] = False if t in chosen_trials else True


    def load_regions_from_json(self, file_path):
        region_json = read_json(file_path)
            
        for region in region_json:
            new_region = OOTRegion(region['region_name'], None, None, self.player)
            new_region.world = self.world
            if 'scene' in region:
                new_region.scene = region['scene']
            if 'hint' in region:
                new_region.hint_text = region['hint']  # changed from new_region.hint
            if 'dungeon' in region:
                new_region.dungeon = region['dungeon']
            if 'time_passes' in region:
                new_region.time_passes = region['time_passes']
                new_region.provides_time = TimeOfDay.ALL
            if new_region.name == 'Ganons Castle Grounds':
                new_region.provides_time = TimeOfDay.DAMPE
            if 'locations' in region:
                for location, rule in region['locations'].items():
                    new_location = LocationFactory(location, self.player)
                    if new_location.type in ['HintStone', 'Hint']:
                        continue
                    new_location.parent_region = new_region
                    new_location.rule_string = rule
                    if self.world.logic_rules != 'none':
                        self.parser.parse_spot_rule(new_location)
                    if new_location.never:
                        # We still need to fill the location even if ALR is off.
                        logging.getLogger('').debug('Unreachable location: %s', new_location.name)
                    # new_location.world = world
                    new_location.player = self.player
                    new_region.locations.append(new_location)
            if 'events' in region:
                for event, rule in region['events'].items():
                    # Allow duplicate placement of events
                    lname = '%s from %s' % (event, new_region.name)
                    new_location = OOTLocation(self.player, lname, type='Event', parent=new_region)
                    new_location.rule_string = rule
                    if self.world.logic_rules != 'none':
                        self.parser.parse_spot_rule(new_location)
                    if new_location.never:
                        logging.getLogger('').debug('Dropping unreachable event: %s', new_location.name)
                    else:
                        # new_location.world = world
                        new_location.player = self.player
                        new_region.locations.append(new_location)
                        MakeEventItem(self.world, self.player, event, new_location)
            if 'exits' in region:
                for exit, rule in region['exits'].items():
                    new_exit = OOTEntrance(self.player, '%s => %s' % (new_region.name, exit), new_region)
                    new_exit.connected_region = exit
                    new_exit.rule_string = rule
                    if self.world.logic_rules != 'none':
                        self.parser.parse_spot_rule(new_exit)
                    if new_exit.never:
                        logging.getLogger('').debug('Dropping unreachable exit: %s', new_exit.name)
                    else:
                        new_region.exits.append(new_exit)
            # Making child and adult access events. Rules for these are set after entrances are bound. 
            # child_access_location = OOTLocation(self.player, name=f'Child Access: {new_region.name}', type='Event', parent=new_region)
            # adult_access_location = OOTLocation(self.player, name=f'Adult Access: {new_region.name}', type='Event', parent=new_region)
            # new_region.locations.extend([child_access_location, adult_access_location])
            # MakeEventItem(self.world, self.player, f'Child Access: {new_region.name}', child_access_location)
            # MakeEventItem(self.world, self.player, f'Adult Access: {new_region.name}', adult_access_location)

            self.world.regions.append(new_region)
            self.regions.append(new_region)
        self.world._recache()

    def set_scrub_prices(self):
        # Get Deku Scrub Locations
        scrub_locations = [location for location in self.world.get_locations() if 'Deku Scrub' in location.name]
        scrub_dictionary = {}
        self.scrub_prices = {}
        for location in scrub_locations:
            if location.default not in scrub_dictionary:
                scrub_dictionary[location.default] = []
            scrub_dictionary[location.default].append(location)

        # Loop through each type of scrub.
        for (scrub_item, default_price, text_id, text_replacement) in business_scrubs:
            price = default_price
            if self.shuffle_scrubs == 'low':
                price = 10
            elif self.shuffle_scrubs == 'random':
                # this is a random value between 0-99
                # average value is ~33 rupees
                price = int(self.world.random.betavariate(1, 2) * 99)

            # Set price in the dictionary as well as the location.
            self.scrub_prices[scrub_item] = price
            if scrub_item in scrub_dictionary:
                for location in scrub_dictionary[scrub_item]:
                    location.price = price
                    if location.item is not None:
                        location.item.price = price


    def fill_bosses(self, bossCount=9):    
        rewardlist = (
            'Kokiri Emerald',
            'Goron Ruby',
            'Zora Sapphire',
            'Forest Medallion',
            'Fire Medallion',
            'Water Medallion',
            'Spirit Medallion',
            'Shadow Medallion',
            'Light Medallion'
        )
        boss_location_names = (
            'Queen Gohma',
            'King Dodongo',
            'Barinade',
            'Phantom Ganon',
            'Volvagia',
            'Morpha',
            'Bongo Bongo',
            'Twinrova',
            'Links Pocket'
        )
        boss_rewards = ItemFactory(rewardlist, self.player)
        boss_locations = [self.world.get_location(loc, self.player) for loc in boss_location_names]

        placed_prizes = [loc.item.name for loc in boss_locations if loc.item is not None]
        unplaced_prizes = [item for item in boss_rewards if item.name not in placed_prizes]
        empty_boss_locations = [loc for loc in boss_locations if loc.item is None]
        prizepool = list(unplaced_prizes)
        prize_locs = list(empty_boss_locations)

        while bossCount:
            bossCount -= 1
            self.world.random.shuffle(prizepool)
            self.world.random.shuffle(prize_locs)
            item = prizepool.pop()
            loc = prize_locs.pop()
            self.world.push_item(loc, item, collect=False)
            loc.locked = True
            loc.event = True


    def create_regions(self):  # build_world_graphs
        logger.info('Generating World.')
        overworld_data_path = data_path('World', 'Overworld.json')
        menu = OOTRegion('Menu', None, None, self.player)
        start = OOTEntrance(self.player, 'New Game', menu)
        menu.exits.append(start)
        self.world.regions.append(menu)
        self.load_regions_from_json(overworld_data_path)
        start.connect(self.world.get_region('Root', self.player))
        create_dungeons(self)
        self.parser.create_delayed_rules() # replaces self.create_internal_locations(); I don't know exactly what it does though

        # if settings.shopsanity != 'off':
        #     world.random_shop_prices()
        self.set_scrub_prices()


    def set_rules(self): 
        logger.info('Calculating Access Rules.')
        set_rules(self)


    def generate_basic(self):  # link entrances, generate item pools, place fixed items
        # hopefully switching the order of these blocks doesn't matter
        logger.info('Setting Entrances.')
        # set_entrances(self)
        # Enforce vanilla for now
        for region in self.regions:
            for exit in region.exits:
                exit.connect(self.world.get_region(exit.connected_region, self.player))

        logger.info('Generating Item Pool.')
        generate_itempool(self)
        self.world.itempool += self.itempool
        set_shop_rules(self)
        set_drop_location_names(self.world)
        self.fill_bosses()

        logger.info('Placing Dungeon Items.')
        for dungeon in self.dungeons: 
            dungeon_itempool = []
            # Assemble items to go into this dungeon. 
            # Build in reverse order since we need to fill boss key first and pop() returns the last element
            # remove and vanilla are handled differently
            # TODO: make this less bad
            if self.shuffle_mapcompass == 'dungeon': 
                dungeon_itempool.extend(dungeon.dungeon_items)
            elif self.shuffle_mapcompass == 'keysanity': 
                self.world.itempool.extend(dungeon.dungeon_items)

            if self.shuffle_smallkeys == 'dungeon': 
                dungeon_itempool.extend(dungeon.small_keys)
            elif self.shuffle_smallkeys == 'keysanity': 
                self.world.itempool.extend(dungeon.small_keys)

            shufflebk = self.shuffle_bosskeys if dungeon.name != 'Ganons Castle' else self.shuffle_ganon_bosskey
            if shufflebk == 'dungeon': 
                dungeon_itempool.extend(dungeon.boss_key)
            elif shufflebk == 'keysanity': 
                self.world.itempool.extend(dungeon.boss_key)

            if dungeon_itempool: # only do this if there's anything to shuffle
                dungeon_locations = [loc for region in dungeon.regions for loc in region.locations if loc.item is None]
                self.world.random.shuffle(dungeon_locations)
                base_state = self.world.get_all_state()
                base_state.stale[self.player] = True
                fill_restrictive(self.world, base_state, dungeon_locations, dungeon_itempool, True, True)


        if self.shuffle_song_items != 'any': 
            logger.info('Placing Songs.')
            song_location_names = [
                'Song from Composers Grave', 'Song from Impa', 'Song from Malon', 'Song from Saria',
                'Song from Ocarina of Time', 'Song from Windmill', 'Sheik in Forest', 'Sheik at Temple',
                'Sheik in Crater', 'Sheik in Ice Cavern', 'Sheik in Kakariko', 'Sheik at Colossus']
            song_locations = list(filter(lambda location: location.type == 'Song', self.world.get_unfilled_locations(player=self.player)))
            songs = list(filter(lambda item: item.player == self.player and item.type == 'Song', self.world.itempool))
            self.world.random.shuffle(songs)
            self.world.random.shuffle(song_locations) # probably don't need to shuffle both but it can't hurt
            for song in songs: 
                self.world.itempool.remove(song)
            base_state = self.world.get_all_state()
            base_state.stale[self.player] = True  # force recalculation of the reachable regions
            fill_restrictive(self.world, base_state, song_locations, songs, True, True)
            

    def generate_output(self):  # ROM patching, cosmetics, etc. 
        logger.info('Patching ROM.') 




