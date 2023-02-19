from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Header:
    def __init__(self, binary_file: BinaryIO):
        self.file_type = parse_uint(binary_file)
        assert self.file_type == 1111906900
        self.version = parse_uint(binary_file)
        self.x_tile_size = parse_uint(binary_file)
        self.y_tile_size = parse_uint(binary_file)
        self.unknown_uint_1 = parse_uint(binary_file)
        self.unknown_uint_2 = parse_uint(binary_file)


def parse_zt_header(binary_file: BinaryIO) -> ZT_Header:
    return ZT_Header(binary_file)
