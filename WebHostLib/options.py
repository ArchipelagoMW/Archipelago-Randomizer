import logging
import os
from Utils import __version__
from jinja2 import Template
import yaml
import json
import typing

from worlds.AutoWorld import AutoWorldRegister
import Options

target_folder = os.path.join("WebHostLib", "static", "generated")

handled_in_js = {"start_inventory", "local_items", "non_local_items", "start_hints", "start_location_hints",
                 "exclude_locations"}


def create():
    os.makedirs(os.path.join(target_folder, 'configs'), exist_ok=True)

    def dictify_range(option: typing.Union[Options.Range, Options.SpecialRange]):
        data = {}
        special = getattr(option, "special_range_cutoff", None)
        if special is not None:
            data[special] = 0
        data.update({
            option.range_start: 0,
            option.range_end: 0,
            "random": 0, "random-low": 0, "random-high": 0,
            option.default: 50
        })
        notes = {
            special: "minimum value without special meaning",
            option.range_start: "minimum value",
            option.range_end: "maximum value"
        }

        for name, number in getattr(option, "special_range_names", {}).items():
            if number in data:
                data[name] = data[number]
                del data[number]
            else:
                data[name] = 0

        return data, notes

    def default_converter(default_value):
        if isinstance(default_value, (set, frozenset)):
            return list(default_value)
        return default_value

    weighted_settings = {
        "baseOptions": {
            "description": "Generated by https://archipelago.gg/",
            "name": "Player",
            "game": {},
        },
        "games": {},
    }

    for game_name, world in AutoWorldRegister.world_types.items():

        all_options = {**Options.per_game_common_options, **world.options}
        res = Template(open(os.path.join("WebHostLib", "templates", "options.yaml")).read()).render(
            options=all_options,
            __version__=__version__, game=game_name, yaml_dump=yaml.dump,
            dictify_range=dictify_range, default_converter=default_converter,
        )

        with open(os.path.join(target_folder, 'configs', game_name + ".yaml"), "w") as f:
            f.write(res)

        # Generate JSON files for player-settings pages
        player_settings = {
            "baseOptions": {
                "description": "Generated by https://archipelago.gg/",
                "game": game_name,
                "name": "Player",
            },
        }

        game_options = {}
        for option_name, option in all_options.items():
            if option_name in handled_in_js:
                pass

            elif option.options:
                game_options[option_name] = this_option = {
                    "type": "select",
                    "displayName": option.display_name if hasattr(option, "display_name") else option_name,
                    "description": option.__doc__ if option.__doc__ else "Please document me!",
                    "defaultValue": None,
                    "options": []
                }

                for sub_option_id, sub_option_name in option.name_lookup.items():
                    this_option["options"].append({
                        "name": option.get_option_name(sub_option_id),
                        "value": sub_option_name,
                    })

                    if sub_option_id == option.default:
                        this_option["defaultValue"] = sub_option_name

                this_option["options"].append({
                    "name": "Random",
                    "value": "random",
                })

                if option.default == "random":
                    this_option["defaultValue"] = "random"

            elif issubclass(option, Options.Range):
                game_options[option_name] = {
                    "type": "range",
                    "displayName": option.display_name if hasattr(option, "display_name") else option_name,
                    "description": option.__doc__ if option.__doc__ else "Please document me!",
                    "defaultValue": option.default if hasattr(
                        option, "default") and option.default != "random" else option.range_start,
                    "min": option.range_start,
                    "max": option.range_end,
                }

                if issubclass(option, Options.SpecialRange):
                    game_options[option_name]["type"] = 'special_range'
                    game_options[option_name]["value_names"] = {}
                    for key, val in option.special_range_names.items():
                        game_options[option_name]["value_names"][key] = val

            elif getattr(option, "verify_item_name", False):
                game_options[option_name] = {
                    "type": "items-list",
                    "displayName": option.display_name if hasattr(option, "display_name") else option_name,
                    "description": option.__doc__ if option.__doc__ else "Please document me!",
                }

            elif getattr(option, "verify_location_name", False):
                game_options[option_name] = {
                    "type": "locations-list",
                    "displayName": option.display_name if hasattr(option, "display_name") else option_name,
                    "description": option.__doc__ if option.__doc__ else "Please document me!",
                }

            elif issubclass(option, Options.OptionList) or issubclass(option, Options.OptionSet):
                if option.valid_keys:
                    game_options[option_name] = {
                        "type": "custom-list",
                        "displayName": option.display_name if hasattr(option, "display_name") else option_name,
                        "description": option.__doc__ if option.__doc__ else "Please document me!",
                        "options": list(option.valid_keys),
                    }

            else:
                logging.debug(f"{option} not exported to Web Settings.")

        player_settings["gameOptions"] = game_options

        os.makedirs(os.path.join(target_folder, 'player-settings'), exist_ok=True)

        with open(os.path.join(target_folder, 'player-settings', game_name + ".json"), "w") as f:
            json.dump(player_settings, f, indent=2, separators=(',', ': '))

        if not world.hidden and world.web.settings_page is True:
            weighted_settings["baseOptions"]["game"][game_name] = 0
            weighted_settings["games"][game_name] = {}
            weighted_settings["games"][game_name]["gameSettings"] = game_options
            weighted_settings["games"][game_name]["gameItems"] = tuple(world.item_names)
            weighted_settings["games"][game_name]["gameLocations"] = tuple(world.location_names)

    with open(os.path.join(target_folder, 'weighted-settings.json'), "w") as f:
        json.dump(weighted_settings, f, indent=2, separators=(',', ': '))
