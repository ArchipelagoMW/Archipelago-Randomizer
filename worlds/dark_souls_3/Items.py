from BaseClasses import Item
from worlds.dark_souls_3.data.items_data import item_tables


class DarkSouls3Item(Item):
    game: str = "Dark Souls III"

    @staticmethod
    def get_name_to_id() -> dict:
        base_id = 100000
        table_offset = 100

        output = {}
        i = 0
        for table in item_tables:
            output |= {name: id for id, name in enumerate(table, base_id + (table_offset * i))}
            i += 1

        return output
