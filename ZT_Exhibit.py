from enum import Enum
from typing import BinaryIO, Tuple

from ZT_Common_Types import Rotation
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float, parse_int


class ZT_Exhibit:
    def __init__(self, binary_file: BinaryIO):
        self.exhibit_x_grid_coord = parse_uint(binary_file)
        self.exhibit_y_grid_coord = parse_uint(binary_file)
        self.exhibit_name = parse_string(binary_file)
        self.entrance_x_grid_coord = parse_uint(binary_file)
        self.entrance_y_grid_coord = parse_uint(binary_file)
        self.entrance_rotation = Rotation.from_int(parse_uint(binary_file))
        self.current_donations = parse_float(binary_file)
        self.last_donations = parse_float(binary_file)
        self.total_donations = parse_float(binary_file)
        self.current_upkeep = parse_float(binary_file)
        self.last_upkeep = parse_float(binary_file)
        self.total_upkeep = parse_float(binary_file)
        discard_padding(binary_file, 12)
        self.exhibit_creation_time = parse_timestamp(binary_file)
        discard_padding(binary_file, 12)
        self.is_tank = parse_uint(binary_file)
        self.is_show_tank = parse_uint(binary_file)
        if self.is_tank:
            self.tank_height = parse_uint(binary_file)
            self.unknown_int_8 = parse_uint(binary_file)
            self.tank_filled = parse_uchar(binary_file)
            self.unknown_int_8 = parse_uint(binary_file)
            self.unknown_int_9 = parse_int(binary_file)
            self.unknown_int_10 = parse_int(binary_file)
            if self.is_show_tank:
                pass

        print(self)

    def __str__(self):
        s1 = f"\nexhibit_x_grid_coord: {self.exhibit_x_grid_coord}\n" \
             f"exhibit_y_grid_coord: {self.exhibit_y_grid_coord}\n" \
             f"exhibit_name: {self.exhibit_name}\n" \
             f"entrance_x_grid_coord: {self.entrance_x_grid_coord}\n" \
             f"entrance_y_grid_coord: {self.entrance_y_grid_coord}\n" \
             f"entrance_rotation: {self.entrance_rotation}\n" \
             f"is_tank: {self.is_tank}\n" \
             f"is_show_tank: {self.is_show_tank}\n"
        if self.is_tank:
            s1 += f"tank_height: {self.tank_height}\n" \
                  f"unknown_int_8: {self.unknown_int_8}\n" \
                  f"tank_filled: {self.tank_filled}\n" \
                  f"unknown_int_8: {self.unknown_int_8}\n" \
                  f"unknown_int_9: {self.unknown_int_8}\n" \
                  f"unknown_int_10: {self.unknown_int_8}\n"
        return s1


def parse_zt_exhibit(binary_file: BinaryIO) -> ZT_Exhibit:
    return ZT_Exhibit(binary_file)
