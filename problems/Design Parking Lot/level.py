from __future__ import annotations
from typing import Optional, Dict, List
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import SpotSize

class Level:
    def __init__(self, floor: int, spots_config: Dict[SpotSize, int]):  # CHANGED signature
        """
        spots_config example:
            {
                SpotSize.MOTO: 10,
                SpotSize.COMPACT: 50,
                SpotSize.LARGE: 20
            }
        """
        self.floor = floor
        self.parking_spots: List[ParkingSpot] = []
        seq = 1
        for size, count in spots_config.items():  # CHANGED
            for _ in range(count):
                self.parking_spots.append(ParkingSpot(seq, size))
                seq += 1

    def park_vehicle(self, vehicle: Vehicle) -> Optional[int]:  # CHANGED: returns spot_num or None
        # Allocation policy: try smallest spot that fits (MOTO → COMPACT → LARGE)
        for size in (SpotSize.MOTO, SpotSize.COMPACT, SpotSize.LARGE):
            for spot in self.parking_spots:
                if spot.size == size and spot.is_available() and spot.can_fit(vehicle):
                    spot.park_vehicle(vehicle)
                    return spot.get_spot_num()
        return None
    
    def unpark_vehicle(self, spot_num: int) -> bool:  # CHANGED: unpark by spot id
        for spot in self.parking_spots:
            if spot.get_spot_num() == spot_num and not spot.is_available():
                spot.unpark_vehicle()
                return True
        return False
    
    def availability_snapshot(self) -> Dict[SpotSize, int]:  # NEW: structured availability
        free = {SpotSize.MOTO: 0, SpotSize.COMPACT: 0, SpotSize.LARGE: 0}
        for s in self.parking_spots:
            if s.is_available():
                free[s.size] += 1
        return free
    
    # Optional: keep your old method but delegate to snapshot
    def display_availability(self) -> None:  # CHANGED: summarize by size
        snap = self.availability_snapshot()
        print(f"[Level {self.floor}] free -> "
              f"MOTO={snap[SpotSize.MOTO]}  "
              f"COMPACT={snap[SpotSize.COMPACT]}  "
              f"LARGE={snap[SpotSize.LARGE]}")


    



