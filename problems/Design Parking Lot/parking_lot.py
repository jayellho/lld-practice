from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List, Tuple, Dict, Optional
from level import Level
from vehicle import Vehicle
from vehicle_type import SpotSize

@dataclass(frozen=True)
class Ticket:  # NEW
    ticket_id: str
    plate: str
    level_idx: int
    spot_num: int
    start: datetime

class ParkingLot:
    _instance = None
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        ParkingLot._instance = self
        self.levels: List[Level] = []
        self._plate_index: Dict[str, Tuple[int, int]] = {}  # NEW: plate -> (level_idx, spot_num)
        self._seq = 0

    @staticmethod
    def get_instance():
        if not ParkingLot._instance:
            ParkingLot()
        return ParkingLot._instance


    def add_level(self, level):
        self.levels.append(level)

    # displays availability by calling the function at the 'level' level.
    def display_availability(self):
        for level in self.levels:
            level.display_availability()
    
    # park vehicles.
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for i, level in enumerate(self.levels):
            spot_num = level.park_vehicle(vehicle)  # CHANGED: get assigned spot
            if spot_num is not None:
                self._seq += 1
                ticket = Ticket(
                    ticket_id=f"T{self._seq:06d}",
                    plate=vehicle.license_plate,
                    level_idx=i,
                    spot_num=spot_num,
                    start=datetime.now(),
                )
                # Index by plate for fast unparking
                self._plate_index[vehicle.license_plate] = (i, spot_num)  # NEW
                # You may store the Ticket if you need billing later.
                return True
        return False
    

    # unpark vehicles.
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        loc = self._plate_index.pop(vehicle.license_plate, None)  # NEW
        if not loc:
            return False
        level_idx, spot_num = loc
        return self.levels[level_idx].unpark_vehicle(spot_num)
    
    def display_availability(self):
        for idx, level in enumerate(self.levels, start=1):
            snap = level.availability_snapshot()
            print(f"[Level {idx}] free -> "
                  f"MOTO={snap[SpotSize.MOTO]}  "
                  f"COMPACT={snap[SpotSize.COMPACT]}  "
                  f"LARGE={snap[SpotSize.LARGE]}")

    # Optional: structured API (useful for UIs instead of print)
    def get_availability(self) -> List[Dict[SpotSize, int]]:  # NEW
        return [lvl.availability_snapshot() for lvl in self.levels]