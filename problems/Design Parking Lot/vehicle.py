from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type, Dict

class Vehicle(ABC):
    def __init__(self, license_plate: str) -> None:
        self.license_plate = license_plate

    # Convenience for spot fit checks (used by ParkingSpot.can_fit)
    @property
    def kind(self) -> str:
        return self.__class__.__name__.lower()

    @abstractmethod
    def base_rate(self) -> float: ...

class Car(Vehicle):
    def base_rate(self) -> float: return 2.0

class Motorcycle(Vehicle):
    def base_rate(self) -> float: return 1.0

class Truck(Vehicle):
    def base_rate(self) -> float: return 3.5

class VehicleFactory:
    _creators: Dict[str, Type[Vehicle]] = {
        "car": Car,
        "motorcycle": Motorcycle,
        "truck": Truck,
    }

    @classmethod
    def create(cls, kind: str, plate: str) -> Vehicle:
        try:
            plate = plate.strip().upper()
            return cls._creators[kind.lower()](plate)
        except KeyError:
            raise ValueError(f"Unknown vehicle type: {kind}")
