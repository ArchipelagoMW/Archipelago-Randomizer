from BaseClasses import Item
import typing
import codecs

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]


class Overcooked2Item(Item):
    game: str = "Overcooked! 2"

oc2_base_id: int = int.from_bytes(codecs.encode(b"oc2", "hex"), byteorder="big")

item_table: dict[str, ItemData] = {
    "Wood"                          : ItemData(oc2_base_id + 1 ) ,
    "Coal Bucket"                   : ItemData(oc2_base_id + 2 ) ,
    "Spare Plate"                   : ItemData(oc2_base_id + 3 ) ,
    "Fire Extinguisher"             : ItemData(oc2_base_id + 4 ) ,
    "Bellows"                       : ItemData(oc2_base_id + 5 ) ,
    "Clean Dishes"                  : ItemData(oc2_base_id + 6 ) ,
    "Larger Tip Jar"                : ItemData(oc2_base_id + 7 ) ,
    "Larger Tip Jar"                : ItemData(oc2_base_id + 8 ) ,
    "Dash"                          : ItemData(oc2_base_id + 9 ) ,
    "Throw"                         : ItemData(oc2_base_id + 10) ,
    "Catch"                         : ItemData(oc2_base_id + 11) ,
    "Remote Control Batteries"      : ItemData(oc2_base_id + 12) ,
    "Wok Wheels"                    : ItemData(oc2_base_id + 13) ,
    "Dish Scrubber"                 : ItemData(oc2_base_id + 14) ,
    "Burn Leniency"                 : ItemData(oc2_base_id + 15) ,
    "Sharp Knife"                   : ItemData(oc2_base_id + 16) ,
    "Order Lookahead"               : ItemData(oc2_base_id + 17) ,
    "Order Lookahead"               : ItemData(oc2_base_id + 18) ,
    "Lightweight Backpack"          : ItemData(oc2_base_id + 19) ,
    "Faster Respawn Time"           : ItemData(oc2_base_id + 20) ,
    "Faster Condiment/Drink Switch" : ItemData(oc2_base_id + 21) ,
    "Guest Patience"                : ItemData(oc2_base_id + 22) ,
    "Kevin-1"                       : ItemData(oc2_base_id + 23) ,
    "Kevin-2"                       : ItemData(oc2_base_id + 24) ,
    "Kevin-3"                       : ItemData(oc2_base_id + 25) ,
    "Kevin-4"                       : ItemData(oc2_base_id + 26) ,
    "Kevin-5"                       : ItemData(oc2_base_id + 27) ,
    "Kevin-6"                       : ItemData(oc2_base_id + 28) ,
    "Kevin-7"                       : ItemData(oc2_base_id + 29) ,
    "Kevin-8"                       : ItemData(oc2_base_id + 30) ,
    "Cooking Emote"                 : ItemData(oc2_base_id + 31) ,
    "Curse Emote"                   : ItemData(oc2_base_id + 32) ,
    "Serving Emote"                 : ItemData(oc2_base_id + 33) ,
    "Preparing Emote"               : ItemData(oc2_base_id + 34) ,
    "Washing Up Emote"              : ItemData(oc2_base_id + 35) ,
    "Ok Emote"                      : ItemData(oc2_base_id + 36) ,
}

item_name_to_config_name = {
    "Wood"                         : "DisableWood"                   ,
    "Coal Bucket"                  : "DisableCoal"                   ,
    "Spare Plate"                  : "DisableOnePlate"               ,
    "Fire Extinguisher"            : "DisableFireExtinguisher"       ,
    "Bellows"                      : "DisableBellows"                ,
    "Clean Dishes"                 : "PlatesStartDirty"              ,
    "Dash"                         : "DisableDash"                   ,
    "Throw"                        : "DisableThrow"                  ,
    "Catch"                        : "DisableCatch"                  ,
    "Remote Control Batteries"     : "DisableControlStick"           ,
    "Wok Wheels"                   : "DisableWokDrag"                ,
    "Dish Scrubber"                : "WashTimeMultiplier"            ,
    "Burn Leniency"                : "BurnSpeedMultiplier"           ,
    "Sharp Knife"                  : "ChoppingTimeScale"             ,
    "Lightweight Backpack"         : "BackpackMovementScale"         ,
    "Faster Respawn Time"          : "RespawnTime"                   ,
    "Faster Condiment/Drink Switch": "CarnivalDispenserRefactoryTime",
    "Guest Patience"               : "CustomOrderLifetime"           ,
}

vanilla_values = {
    "DisableWood": False,
    "DisableCoal": False,
    "DisableOnePlate": False,
    "DisableFireExtinguisher": False,
    "DisableBellows": False,
    "PlatesStartDirty": False,
    "DisableDash": False,
    "DisableThrow": False,
    "DisableCatch": False,
    "DisableControlStick": False,
    "DisableWokDrag": False,
    "WashTimeMultiplier": 1.0,
    "BurnSpeedMultiplier": 1.0,
    "ChoppingTimeScale": 1.0,
    "BackpackMovementScale": 1.0,
    "RespawnTime": 5.0,
    "CarnivalDispenserRefactoryTime": 0.0,
    "CustomOrderLifetime": 100.0,
}

item_id_to_name: typing.Dict[int, str] = {
    data.code: item_name for item_name, data in item_table.items() if data.code
}

item_name_to_id: typing.Dict[str, int] = {
    item_name: data.code for item_name, data in item_table.items() if data.code
}


def is_progression(item_name: str) -> bool:
    return not item_name.endswith("Emote")


def item_to_unlock_event(item_name: str) -> dict[str, str]:
    message = f"{item_name} Acquired!"
    action = ""
    payload = ""
    if item_name.startswith("Kevin"):
        kevin_num = int(item_name.split("-")[-1])
        action = "UNLOCK_LEVEL"
        payload = str(kevin_num + 36)
    elif "Emote" in item_name:
        action = "UNLOCK_EMOTE"
        payload = str(item_table[item_name].code - 30)
    elif item_name == "Larger Tip Jar":
        action = "INC_TIP_COMBO"
    elif item_name == "Order Lookahead":
        action = "INC_ORDERS_ON_SCREEN"
    else:
        config_name = item_name_to_config_name[item_name]
        vanilla_value = vanilla_values[config_name]

        action = "SET_VALUE"
        payload = f"{config_name}={vanilla_value}"

    return {
        "message": message,
        "action": action,
        "payload": payload,
    }
