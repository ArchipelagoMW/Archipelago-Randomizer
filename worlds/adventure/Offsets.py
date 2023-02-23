# probably I should generate this from the list file

static_item_data_location = 0xe9d
static_item_element_size = 9
static_first_dragon_index = 6
item_position_table = 0x402
items_ram_start = 0xa1
connector_port_offset = 0xff9
# dragon speeds are hardcoded directly in their respective movement subroutines, not in their item table or state data
# so this is the second byte of an LDA immediate instruction
yorgle_speed_data_location = 0x724
grundle_speed_data_location = 0x73f
rhindle_speed_data_location = 0x709


# in case I need to place a rom address in the rom
rom_address_space_start = 0xf000

