from typing import BinaryIO, Tuple

from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Features:
    def __init__(self, binary_file: BinaryIO):
        self.num_features = parse_uint(binary_file)
        self.features = []
        for _ in range(self.num_features):
            self.features.append({"feature_name": parse_string(binary_file), "number": parse_uint(binary_file)})


def parse_zt_features(binary_file: BinaryIO) -> ZT_Features:
    return ZT_Features(binary_file)
