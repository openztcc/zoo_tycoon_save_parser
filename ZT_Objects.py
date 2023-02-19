from typing import BinaryIO, Tuple

from ZT_Object import parse_zt_object
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Objects:
    def __init__(self, binary_file: BinaryIO):
        self.objects = []
        self.num_objects = parse_uint(binary_file)
        for _ in range(self.num_objects):
            self.objects.append(parse_zt_object(binary_file))


def parse_zt_objects(binary_file: BinaryIO) -> ZT_Objects:
    return ZT_Objects(binary_file)
