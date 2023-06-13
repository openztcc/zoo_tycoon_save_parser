from typing import BinaryIO, Tuple

from ZT_Features import parse_zt_features
from ZT_Misc_tank import parse_zt_unknown_tank_struct
from ZT_Tiles import parse_zt_tiles
from ZT_Unknown_Struct import parse_zt_unknown_struct
from parsing_functions import parse_string, discard_padding, parse_subgrid_coord, parse_grid_coord, parse_uint, \
    parse_uchar, parse_timestamp, parse_float

from ZT_Header import parse_zt_header

from ZT_Exhibits import parse_zt_exhibits

from ZT_Objects import parse_zt_objects

class ZT_Savefile:
    def __init__(self, binary_file: BinaryIO):
        self.header = parse_zt_header(binary_file)
        self.exhibits = parse_zt_exhibits(binary_file)
        self.unknown_tank_struct = parse_zt_unknown_tank_struct(binary_file)
        self.tile_list = parse_zt_tiles(binary_file, self.header.x_tile_size, self.header.y_tile_size)
        self.unknown_uint_1 = parse_uint(binary_file)
        self.object_list = parse_zt_objects(binary_file)
        self.unknown_struct_1 = parse_zt_unknown_struct(binary_file, 6)
        self.features = parse_zt_features(binary_file)
        print("Test")


def parse_zt_savefile(binary_file: BinaryIO) -> ZT_Savefile:
    return ZT_Savefile(binary_file)
