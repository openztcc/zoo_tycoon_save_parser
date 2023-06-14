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
        self.unknown_char_1 = parse_uchar(binary_file)
        self.unknown_int_6 = parse_uint(binary_file)
        self.unknown_int_7 = parse_uint(binary_file)
        self.unknown_int_8 = parse_uint(binary_file)
        self.unknown_int_9 = parse_uint(binary_file)
        self.unknown_int_10 = parse_uint(binary_file)
        self.unknown_int_11 = parse_uint(binary_file)
        self.unknown_string_3 = parse_string(binary_file)
        self.unknown_string_4 = parse_string(binary_file)
        self.unknown_int_12 = parse_uint(binary_file)
        self.unknown_int_13 = parse_uint(binary_file)
        discard_padding(binary_file, 4)                     # TODO: Repeated structure here
        self.unknown_string_5 = parse_string(binary_file)
        discard_padding(binary_file, 4)
        self.unknown_string_6 = parse_string(binary_file)
        discard_padding(binary_file, 8)
        self.unknown_int_5_2 = parse_uint(binary_file)
        self.unknown_char_1_2 = parse_uchar(binary_file)
        self.unknown_int_6_2 = parse_uint(binary_file)
        self.unknown_int_7_2 = parse_uint(binary_file)
        self.unknown_int_8_2 = parse_uint(binary_file)
        self.unknown_int_9_2 = parse_uint(binary_file)
        self.unknown_int_10_2 = parse_uint(binary_file)
        self.unknown_int_11_2 = parse_uint(binary_file)
        self.unknown_string_7 = parse_string(binary_file)
        self.unknown_string_8 = parse_string(binary_file)
        discard_bytes(binary_file, 22)  # TODO: Figure out these bytes, similar to other unknown sequences
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
             f"unknown_char_1: {self.unknown_char_1}\n" \
             f"unknown_int_6: {self.unknown_int_6}\n" \
             f"unknown_int_7: {self.unknown_int_7}\n" \
             f"unknown_int_8: {self.unknown_int_8}\n" \
             f"unknown_int_9: {self.unknown_int_9}\n" \
             f"unknown_int_10: {self.unknown_int_10}\n" \
             f"unknown_int_11: {self.unknown_int_11}\n" \
             f"unknown_string_3: {self.unknown_string_3}\n" \
             f"unknown_string_4: {self.unknown_string_4}\n" \
             f"unknown_int_12: {self.unknown_int_12}\n" \
             f"unknown_int_13: {self.unknown_int_13}\n" \
             f"unknown_string_5: {self.unknown_string_5}\n" \
             f"unknown_string_6: {self.unknown_string_6}\n" \
             f"unknown_int_5_2: {self.unknown_int_5_2}\n" \
             f"unknown_char_1_2: {self.unknown_char_1_2}\n" \
             f"unknown_int_6_2: {self.unknown_int_6_2}\n" \
             f"unknown_int_7_2: {self.unknown_int_7_2}\n" \
             f"unknown_int_8_2: {self.unknown_int_8_2}\n" \
             f"unknown_int_9_2: {self.unknown_int_9_2}\n" \
             f"unknown_int_10_2: {self.unknown_int_10_2}\n" \
             f"unknown_int_11_2: {self.unknown_int_11_2}\n" \
             f"unknown_string_7: {self.unknown_string_7}\n" \
             f"unknown_string_8: {self.unknown_string_8}\n"
        return s1


def parse_zt_unknown_tank_struct(binary_file: BinaryIO) -> ZTUnknownTankStruct:
    return ZTUnknownTankStruct(binary_file)
