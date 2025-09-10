from enum import Enum, auto

class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    MOTORCYCLE = 3

class SpotSize(Enum):
    MOTO = auto()
    COMPACT = auto()
    LARGE = auto()