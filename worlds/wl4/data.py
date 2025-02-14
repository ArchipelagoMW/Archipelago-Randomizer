from __future__ import annotations

from enum import Enum, IntEnum, IntFlag
from io import StringIO
import pkgutil
from typing import Mapping


ap_id_offset = 0xEC0000


class Passage(IntEnum):
    ENTRY = 0
    EMERALD = 1
    RUBY = 2
    TOPAZ = 3
    SAPPHIRE = 4
    GOLDEN = 5

    def long_name(self):
        if self == Passage.GOLDEN:
            return 'Golden Pyramid'
        else:
            return self.short_name() + ' Passage'

    def short_name(self):
        return ('Entry', 'Emerald', 'Ruby', 'Topaz', 'Sapphire', 'Golden')[self]


class ItemFlag(IntFlag):
    JEWEL_NE = 1 << 0
    JEWEL_SE = 1 << 1
    JEWEL_SW = 1 << 2
    JEWEL_NW = 1 << 3
    CD = 1 << 4
    KEYZER = 1 << 5
    FULL_HEALTH = 1 << 6
    FULL_HEALTH_2 = 1 << 7

    BOSS_CLEAR = 1 << 5
    DIVA_CLEAR = 1 << 4


class Domain(Enum):
    SYSTEM_BUS = 0x0000000
    ROM = 0x8000000

    def convert_from(self, source: Domain, addr: int) -> int:
        difference = self.value - source.value
        # Doesn't bounds check against top, but that's okay for now
        assert addr > difference, f'{self.name} address {addr} is out of bounds for {source.name}'
        addr -= difference
        return addr


def data_path(file_name: str):
    return pkgutil.get_data(__name__, f'data/{file_name}')


def _get_symbols() -> Mapping[str, int]:
    symbols = {}
    symbol_data = data_path('basepatch.sym').decode('utf-8')
    with StringIO(symbol_data) as stream:
        for line in stream:
            try:
                addr, label, *_ = line.split()
            except ValueError:
                continue

            # These labels are either generated by assembler directives or are
            # file/function local. Either way, not useful here
            if label[0] in ('@', '.'):
                continue

            address = int(addr, base=16)
            symbols[label] = address
    return symbols


def _get_charset() -> Mapping[str, int]:
    charset = {}
    symbol_data = data_path('charset.tbl').decode('utf-8')
    with StringIO(symbol_data) as stream:
        for line in stream:
            try:
                encoded, character = line.strip().split('=')
            except ValueError:
                continue

            byte = int(encoded, base=16)
            charset[character] = byte
    return charset


symbols = _get_symbols()
charset = _get_charset()


def get_symbol(symbol: str, offset: int = 0) -> int:
    """Convert a label name and offset to an address on GBA system bus."""

    return symbols[symbol.lower()] + offset


def encode_str(msg: str) -> bytes:
    """Encode a string into Wario Land 4's text format. Unrecognized characters
    are converted to spaces."""

    encoded = []
    for c in msg:
        encoded.append(charset.get(c, 0xFF))
    return bytes(encoded)
