from typing import BinaryIO, Tuple

from ZT_Common_Types import Rotation
from parsing_functions import parse_string, discard_padding, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float, discard_bytes


class ZT_Object:
    def __init__(self, binary_file: BinaryIO):
        self.object_class: str = parse_string(binary_file)
        self.object_type: str = parse_string(binary_file)
        self.object_subtype: str = parse_string(binary_file)
        self.remaining_length = parse_uint(binary_file)
        if self.remaining_length == 0:
            print(self)
            return
        self.unknown_int_1 = parse_uint(binary_file)
        x_coord = parse_grid_coord(binary_file)
        y_coord = parse_grid_coord(binary_file)
        z_coord = parse_grid_coord(binary_file)
        self.coords: Tuple[int, int, int] = (x_coord, y_coord, z_coord)
        self.rotation = Rotation.from_int(parse_uint(binary_file))
        if self.object_class == "ambient":
            self.unknown_ambient_int_1 = parse_uint(binary_file)
        self.object_id = parse_uint(binary_file)
        self.object_name = parse_string(binary_file)
        if self.object_class != "building":
            bytes_to_discard = self.remaining_length - 28 - len(self.object_name)
            if self.object_class == "ambient":
                bytes_to_discard -= 4
            print(f"Discarding bytes {bytes_to_discard}")
            discard_bytes(binary_file, bytes_to_discard)
            print(self)
            return
        discard_bytes(binary_file, 83)
        # self.unknown_char_1 = parse_uchar(binary_file)
        # self.last_customers = parse_uint(binary_file)
        # self.current_customers = parse_uint(binary_file)
        # self.total_customers = parse_uint(binary_file)
        # self.total_income = parse_float(binary_file)
        # self.current_price = parse_float(binary_file)
        # self.number_of_current_customers = parse_uint(binary_file)
        # self.current_customers_array = []
        # for _ in range(self.number_of_current_customers):
        #     self.current_customers_array.append(
        #         (
        #             parse_uint(binary_file),
        #             parse_uint(binary_file)
        #         )
        #     )
        # self.object_status = parse_uint(binary_file)        # E.g how full a bin is
        # self.last_income = parse_float(binary_file)
        # self.current_income = parse_float(binary_file)
        # self.unknown_int_4 = parse_uint(binary_file)
        # self.unknown_int_5 = parse_uint(binary_file)
        self.object_creation_time = parse_timestamp(binary_file)
        # self.unknown_int_6 = parse_uint(binary_file)
        discard_bytes(binary_file, 12)
        print(self)

    def __str__(self):
        s1 = f"\nobject_class: {self.object_class}\n" \
        f"object_type: {self.object_type}\n" \
        f"object_subtype: {self.object_subtype}\n" \
        f"remaining_length: {self.remaining_length}\n"
        if self.remaining_length == 0:
            return s1
        s1 += f"unknown_int_1: {self.unknown_int_1}\n" \
        f"coords: {self.coords}\n" \
        f"rotation: {self.rotation}\n" \
        f"object_id: {self.object_id}\n" \
        f"object_name: {self.object_name}\n"
        if self.object_class == "ambient":
            s1 += f"unknown_ambient_int_1: {self.unknown_ambient_int_1}\n"
        if self.object_class != "building":
            return s1
        #     s1 += f"unknown_int_1: {self.unknown_int_1}\n"
        # s1 += f"unknown_char_1: {self.unknown_char_1}\n" \
        # s1 += f"last_customers: {self.last_customers}\n" \
        # f"current_customers: {self.current_customers}\n" \
        # f"total_customers: {self.total_customers}\n" \
        # f"total_income: {self.total_income}\n" \
        # f"current_price: {self.current_price}\n" \
        # f"last_income: {self.last_income}\n" \
        # f"current_income: {self.current_income}\n" \
        # f"object_status: {self.object_status}\n" \
        # f"unknown_int_4: {self.unknown_int_4}\n" \
        # f"unknown_int_5: {self.unknown_int_5}\n" \
        s1 += f"object_creation_time: {self.object_creation_time}\n" \
        # f"unknown_int_6: {self.unknown_int_6}\n"
        # if self.number_of_current_customers:
        #     s1 += "Customers\n"
        # for customer in self.current_customers_array:
        #     s1 += f"\tCustomer id {customer[0]} loc_{customer[1]}\n"
        return s1


def parse_zt_object(binary_file: BinaryIO) -> ZT_Object:
    return ZT_Object(binary_file)