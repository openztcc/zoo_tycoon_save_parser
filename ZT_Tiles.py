from typing import BinaryIO, Tuple

from ZT_Tile import parse_zt_tile
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float


class ZT_Tiles:
    def __init__(self, binary_file: BinaryIO, x_size: int, y_size: int):
        self.tiles = []
        for _ in range(y_size):
            inner_array = []
            for _ in range(x_size):
                inner_array.append(parse_zt_tile(binary_file))
            self.tiles.append(inner_array)


def parse_zt_tiles(binary_file: BinaryIO, x_size: int, y_size: int) -> ZT_Tiles:
    return ZT_Tiles(binary_file, x_size, y_size)
