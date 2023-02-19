from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Tile:
    def __init__(self, binary_file: BinaryIO):
        self.char_1 = parse_uchar(binary_file)
        self.char_2 = parse_uchar(binary_file)
        self.char_3 = parse_uchar(binary_file)
        self.char_4 = parse_uchar(binary_file)
        self.char_5 = parse_uchar(binary_file)
        self.char_6 = parse_uchar(binary_file)
        self.char_7 = parse_uchar(binary_file)
        self.char_8 = parse_uchar(binary_file)
        self.char_9 = parse_uchar(binary_file)
        self.char_10 = parse_uchar(binary_file)


def parse_zt_tile(binary_file: BinaryIO) -> ZT_Tile:
    return ZT_Tile(binary_file)
