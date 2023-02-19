from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Unknown_Struct:
    def __init__(self, binary_file: BinaryIO, num_fields: int):
        self.fields = []
        for _ in range(num_fields):
            self.fields.append(parse_uint(binary_file))


def parse_zt_unknown_struct(binary_file: BinaryIO, num_fields: int) -> ZT_Unknown_Struct:
    return ZT_Unknown_Struct(binary_file, num_fields)
