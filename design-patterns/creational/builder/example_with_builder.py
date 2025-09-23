from dataclasses import dataclass

@dataclass
class Car:
    seats: int = 0
    engine: str = ""
    color: str = "white"
    gps: bool = False
    airbags: int = 0

class CarBuilder:
    """Fluent, stateful builder for Car."""
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()
        return self

    def seats(self, n: int):
        self._car.seats = n
        return self

    def engine(self, kind: str):
        self._car.engine = kind
        return self

    def color(self, name: str):
        self._car.color = name
        return self

    def gps(self, on: bool = True):
        self._car.gps = on
        return self

    def airbags(self, n: int):
        self._car.airbags = n
        return self

    def build(self) -> Car:
        # central place to validate construction rules
        if self._car.seats <= 0:
            raise ValueError("A car must have at least one seat.")
        if not self._car.engine:
            raise ValueError("An engine is required.")
        result = self._car
        self.reset()             # make builder reusable
        return result

class Director:
    """Encapsulates recipes; clients pick *what*, not *how*."""
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def make_sport_car(self) -> Car:
        return (self.builder
                .reset()
                .seats(2)
                .engine("V8")
                .color("red")
                .airbags(4)
                .gps(True)
                .build())

    def make_suv(self) -> Car:
        return (self.builder
                .reset()
                .seats(7)
                .engine("V6")
                .color("black")
                .airbags(6)
                .gps(True)
                .build())

if __name__ == "__main__":
    builder = CarBuilder()
    director = Director(builder)
    c1 = director.make_sport_car()
    c2 = director.make_suv()
    # you can also build ad-hoc without the director:
    c3 = builder.reset().seats(5).engine("Hybrid").color("blue").airbags(6).build()
    print(c1)
    print(c2)
    print(c3)
