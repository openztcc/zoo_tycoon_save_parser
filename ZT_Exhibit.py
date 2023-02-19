from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Exhibit:
    def __init__(self, binary_file: BinaryIO):
        self.unknown_int_1 = parse_uint(binary_file)
        self.unknown_int_2 = parse_uint(binary_file)
        self.exhibit_name = parse_string(binary_file)
        self.unknown_int_3 = parse_uint(binary_file)
        self.unknown_int_4 = parse_uint(binary_file)
        self.unknown_int_5 = parse_uint(binary_file)
        self.last_donations = parse_float(binary_file)
        self.current_donations = parse_float(binary_file)
        self.total_donations = parse_float(binary_file)
        self.last_upkeep = parse_float(binary_file)
        self.current_upkeep = parse_float(binary_file)
        self.total_upkeep = parse_float(binary_file)
        discard_padding(binary_file, 12)
        self.exhibit_creation_time = parse_timestamp(binary_file)
        self.unknown_int_6 = parse_uint(binary_file)
        self.unknown_int_7 = parse_uint(binary_file)


def parse_zt_exhibit(binary_file: BinaryIO) -> ZT_Exhibit:
    return ZT_Exhibit(binary_file)
