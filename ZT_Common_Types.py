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
