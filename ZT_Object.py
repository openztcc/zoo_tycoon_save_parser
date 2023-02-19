from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float

from enum import Enum


class Rotation(Enum):
    NORTH = 2
    EAST = 4
    SOUTH = 6
    WEST = 0

    @classmethod
    def from_int(cls, value):
        for direction in cls:
            if direction.value == value:
                return direction
        raise ValueError("Invalid value for CardinalDirection")


class ZT_Object:
    def __init__(self, binary_file: BinaryIO):
        self.object_class: str = parse_string(binary_file)
        self.object_type: str = parse_string(binary_file)
        self.object_subtype: str = parse_string(binary_file)
        discard_padding(binary_file, 4)                     ## Could indicate 0 length string?
        x_coord = parse_grid_coord(binary_file)
        y_coord = parse_grid_coord(binary_file)
        z_coord = parse_grid_coord(binary_file)
        self.coords: Tuple[int, int, int] = (x_coord, y_coord, z_coord)
        # discard_padding(binary_file, 4)                     ## Height? 16 per height level
        self.rotation = Rotation.from_int(parse_uint(binary_file))
        self.object_id = parse_uint(binary_file)
        self.object_name = parse_string(binary_file)
        discard_padding(binary_file, 4)
        self.unknown_char_1 = parse_uchar(binary_file)
        if self.object_class != "building":
            self.unknown_int_1 = parse_uint(binary_file)
            return
        self.last_customers = parse_uint(binary_file)
        self.current_customers = parse_uint(binary_file)
        self.total_customers = parse_uint(binary_file)
        self.total_income = parse_float(binary_file)
        self.current_price = parse_float(binary_file)
        self.number_of_current_customers = parse_uint(binary_file)
        self.current_customers_array = []
        for _ in range(self.number_of_current_customers):
            self.current_customers_array.append(
                (
                    parse_uint(binary_file),
                    parse_uint(binary_file)
                )
            )
        self.object_status = parse_uint(binary_file)        # E.g how full a bin is
        self.last_income = parse_float(binary_file)
        self.current_income = parse_float(binary_file)
        self.unknown_int_4 = parse_uint(binary_file)
        self.unknown_int_5 = parse_uint(binary_file)
        self.object_creation_time = parse_timestamp(binary_file)
        self.unknown_int_6 = parse_uint(binary_file)

    def __str__(self):
        s1 = f"object_class: {self.object_class}\n" \
        f"object_subclass: {self.object_type}\n" \
        f"object_type: {self.object_subtype}\n" \
        f"coords: {self.coords}\n" \
        f"rotation: {self.rotation}\n" \
        f"object_id: {self.object_id}\n" \
        f"object_name: {self.object_name}\n" \
        f"unknown_char_1: {self.unknown_char_1}\n" \
        f"last_customers: {self.last_customers}\n" \
        f"current_customers: {self.current_customers}\n" \
        f"total_customers: {self.total_customers}\n" \
        f"total_income: {self.total_income}\n" \
        f"current_price: {self.current_price}\n" \
        f"last_income: {self.last_income}\n" \
        f"current_income: {self.current_income}\n" \
        f"object_status: {self.object_status}\n" \
        f"unknown_int_4: {self.unknown_int_4}\n" \
        f"unknown_int_5: {self.unknown_int_5}\n" \
        f"object_creation_time: {self.object_creation_time}\n" \
        f"unknown_int_6: {self.unknown_int_6}\n"
        if self.number_of_current_customers:
            s1 += "Customers\n"
        for customer in self.current_customers_array:
            s1 += f"\tCustomer id {customer[0]} loc_{customer[1]}\n"
        return s1


def parse_zt_object(binary_file: BinaryIO) -> ZT_Object:
    return ZT_Object(binary_file)