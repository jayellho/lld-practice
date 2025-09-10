# driver.py
from parking_lot import ParkingLot
from level import Level
from vehicle import VehicleFactory
from vehicle_type import SpotSize  # NEW

def main():
    # Create Parking Lot and create Levels within.
    parking_lot = ParkingLot.get_instance()

    # CHANGED: define each level with a mix of spot sizes
    parking_lot.add_level(Level(1, {
        SpotSize.MOTO: 10,
        SpotSize.COMPACT: 50,
        SpotSize.LARGE: 20,
    }))
    parking_lot.add_level(Level(2, {
        SpotSize.MOTO: 8,
        SpotSize.COMPACT: 40,
        SpotSize.LARGE: 12,
    }))

    # Vehicles via factory
    factory = VehicleFactory()
    car = factory.create("car", "car-456")
    truck = factory.create("truck", "trk-789")
    motorcycle = factory.create("motorcycle", "mc-123")

    # Park vehicles
    parking_lot.park_vehicle(car)
    parking_lot.park_vehicle(truck)
    parking_lot.park_vehicle(motorcycle)

    # Unpark vehicles
    parking_lot.unpark_vehicle(car)

    # Availability
    parking_lot.display_availability()

if __name__=='__main__':
    main()
