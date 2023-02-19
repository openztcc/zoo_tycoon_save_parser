from typing import BinaryIO, Tuple, List

from ZT_Exhibit import ZT_Exhibit, parse_zt_exhibit
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Exhibits:
    def __init__(self, binary_file: BinaryIO):
        self.num_exhibits = parse_uint(binary_file)
        self.exhibits: List[ZT_Exhibit] = []
        for _ in range(self.num_exhibits):
            self.exhibits.append(parse_zt_exhibit(binary_file))


def parse_zt_exhibits(binary_file: BinaryIO) -> ZT_Exhibits:
    return ZT_Exhibits(binary_file)
