from dataclasses import dataclass

@dataclass
class Car:
    seats: int
    engine: str
    color: str = "white"
    gps: bool = False
    airbags: int = 0

# client code mixes construction details everywhere:
def build_sport_car_without_builder():
    # hard to see the “recipe”, easy to miss a field or set them out of order
    car = Car(seats=2, engine="V8", color="red")
    # later… someone remembers safety:
    car.airbags = 4
    # later… optional gadget:
    car.gps = True
    return car

def build_suv_without_builder():
    return Car(seats=7, engine="V6", color="black", gps=True, airbags=6)

if __name__ == "__main__":
    s1 = build_sport_car_without_builder()
    s2 = build_suv_without_builder()
    print(s1)
    print(s2)
