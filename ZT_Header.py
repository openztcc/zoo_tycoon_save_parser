from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float

from enum import Enum


class Campaign(Enum):
    FREEFORM = 0
    ZT = 1
    DD = 2
    MM = 3

    @classmethod
    def from_int(cls, value):
        for campaign in cls:
            if campaign.value == value:
                return campaign
        raise ValueError("Invalid value for Campaign")

class ZT_Header:
    def __init__(self, binary_file: BinaryIO):
        self.file_type = parse_uint(binary_file)
        assert self.file_type == 1111906900
        self.version = parse_uint(binary_file)
        self.language = parse_uint(binary_file)
        assert self.language == 1033
        self.campaign = Campaign.from_int(parse_uint(binary_file))
        self.x_tile_size = parse_uint(binary_file)
        self.y_tile_size = parse_uint(binary_file)
        self.unknown_uint_1 = parse_uint(binary_file)
        self.unknown_uint_2 = parse_uint(binary_file)


def parse_zt_header(binary_file: BinaryIO) -> ZT_Header:
    return ZT_Header(binary_file)
