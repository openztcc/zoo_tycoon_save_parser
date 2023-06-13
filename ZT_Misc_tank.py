from typing import BinaryIO, Tuple

from ZT_Common_Types import Rotation
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float, parse_int, discard_bytes


class ZTUnknownTankStruct:
    def __init__(self, binary_file: BinaryIO):
        self.unknown_int_1 = parse_uint(binary_file)
        self.unknown_int_2 = parse_uint(binary_file)
        discard_bytes(binary_file, 38)
        self.num_string = parse_uint(binary_file)
        self.unknown_int_3 = parse_uint(binary_file)
        self.unknown_int_4 = parse_uint(binary_file)
        discard_padding(binary_file, 4)
        self.unknown_string_1 = parse_string(binary_file)
        discard_padding(binary_file, 4)
        self.unknown_string_2 = parse_string(binary_file)
        discard_padding(binary_file, 8)
        self.unknown_int_5 = parse_uint(binary_file)
        self.unknown_int_6 = parse_uint(binary_file)
        print(self)

    def __str__(self):
        s1 = f"\nunknown_int_1: {self.unknown_int_1}\n" \
             f"unknown_int_2: {self.unknown_int_2}\n" \
             f"num_string: {self.num_string}\n" \
             f"unknown_int_3: {self.unknown_int_3}\n" \
             f"unknown_int_4: {self.unknown_int_4}\n" \
             f"unknown_string_1: {self.unknown_string_1}\n" \
             f"unknown_string_2: {self.unknown_string_2}\n" \
             f"unknown_int_5: {self.unknown_int_5}\n" \
             f"unknown_int_6: {self.unknown_int_6}\n"
        return s1


def parse_zt_unknown_tank_struct(binary_file: BinaryIO) -> ZTUnknownTankStruct:
    return ZTUnknownTankStruct(binary_file)
