from __future__ import annotations
from typing import Optional, Dict, Set
from vehicle import Vehicle
from vehicle_type import SpotSize  # CHANGED: use SpotSize instead of VehicleType

FIT_MATRIX: Dict[SpotSize, Set[str]] = {
    SpotSize.MOTO:    {"motorcycle"},
    SpotSize.COMPACT: {"motorcycle", "car"},
    SpotSize.LARGE:   {"motorcycle", "car", "truck"},
}


class ParkingSpot:
    def __init__(self, spot_num: int, size: SpotSize):
        self.spot_num = spot_num
        self.size = size
        self.parked_vehicle: Optional[Vehicle] = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None
    
    def can_fit(self, vehicle: Vehicle) -> bool:
        return vehicle.kind in FIT_MATRIX[self.size]
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        if not self.is_available() or not self.can_fit(vehicle):
            raise Exception(
                f"Failed to park at spot {self.spot_num} ({self.size.name}) "
                f"with vehicle {vehicle.license_plate} ({vehicle.kind}). "
                f"Not compatible or occupied!"
            )
        self.parked_vehicle = vehicle
    
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
    
    # getters.
    def get_spot_num(self) -> int:
        return self.spot_num

    def get_parked_vehicle(self) -> Optional[Vehicle]:
        return self.parked_vehicle
    

