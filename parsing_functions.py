import struct
from datetime import datetime, timedelta
from typing import BinaryIO


def discard_padding(binary_file: BinaryIO, num_bytes):
    for _ in range(num_bytes):
        _char = parse_uchar(binary_file)
        assert _char == 0


def parse_uint(binary_file: BinaryIO):
    int_format = "<I"
    int_bytes = binary_file.read(struct.calcsize(int_format))
    int_decoded = struct.unpack(int_format, int_bytes)[0]
    return int_decoded


def parse_int(binary_file: BinaryIO):
    int_format = "<i"
    int_bytes = binary_file.read(struct.calcsize(int_format))
    int_decoded = struct.unpack(int_format, int_bytes)[0]
    return int_decoded


def parse_uchar(binary_file: BinaryIO):
    char_format = "<B"
    char_bytes = binary_file.read(struct.calcsize(char_format))
    char_decoded = struct.unpack(char_format, char_bytes)[0]
    return char_decoded


def parse_float(binary_file: BinaryIO):
    float_format = "<f"
    float_bytes = binary_file.read(struct.calcsize(float_format))
    float_decoded = struct.unpack(float_format, float_bytes)[0]
    return float_decoded

def parse_timestamp(binary_file: BinaryIO):
    timestamp_format = "<Q"
    timestamp_bytes = binary_file.read(struct.calcsize(timestamp_format))
    timestamp_decoded = struct.unpack(timestamp_format, timestamp_bytes)[0]
    return datetime(1601, 1, 1) + timedelta(microseconds=timestamp_decoded//10)

def parse_string(_bytes: BinaryIO) -> str:
    string_size_format = "<I"
    string_size_bytes = _bytes.read(struct.calcsize(string_size_format))
    string_size_decoded = struct.unpack(string_size_format, string_size_bytes)[0]
    string_format = str(string_size_decoded) + "s"
    string_decoded = struct.unpack(string_format, _bytes.read(string_size_decoded))[0].decode()
    return string_decoded


def parse_grid_coord(binary_file):
    coord = parse_int(binary_file)
    return coord >> 6


def parse_subgrid_coord(binary_file):
    coord = parse_uint(binary_file)
    return coord >> 5
