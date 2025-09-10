# Read more about the pattern here: https://refactoring.guru/design-patterns/factory-method
# AKA "Virtual Constructor"
# Replace direct object construction calls with calls to a special factory method.

# ================= Example without factory pattern: ========================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing import Dict, Any, List


# ---------- Product interface (optional but useful) ----------
class Shape(ABC):
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def draw(self) -> str: ...


# ---------- Concrete products ----------
class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r
    def name(self) -> str: return "Circle"
    def area(self) -> float: return pi * self.r * self.r
    def draw(self) -> str: return f"Drawing a circle (r={self.r})"

class Square(Shape):
    def __init__(self, s: float) -> None:
        self.s = s
    def name(self) -> str: return "Square"
    def area(self) -> float: return self.s * self.s
    def draw(self) -> str: return f"Drawing a square (s={self.s})"

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
    def name(self) -> str: return "Triangle"
    def area(self) -> float: return 0.5 * self.base * self.height
    def draw(self) -> str: return f"Drawing a triangle (b={self.base}, h={self.height})"

# class Hexagon(Shape):
#     def __init__(self, side: float) -> None:
#         self.side = side
#     def name(self) -> str: return "Hexagon"
#     def area(self) -> float:
#         from math import sqrt
#         return (3 * sqrt(3) / 2) * self.side * self.side
#     def draw(self) -> str: return f"Drawing a hexagon (side={self.side})"

# ---------- Client-side constructors (NO factory; branching here) ----------
def make_shape(shape_type: str, **kwargs) -> Shape:
    st = shape_type.lower()
    if st == "circle":
        return Circle(kwargs["r"])
    elif st == "square":
        return Square(kwargs["s"])
    elif st == "triangle":
        return Triangle(kwargs["base"], kwargs["height"])
    # elif st == "hexagon":
    #     return Hexagon(kwargs["side"]) 
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")


# ---------- Multiple call sites that each construct shapes ----------
def render_and_report(shape_type: str, **kwargs) -> str:
    # Creation logic lives here (duplication risk)
    shape = make_shape(shape_type, **kwargs)
    return f"{shape.draw()}\n→ {shape.name()} area: {shape.area():.2f}"

def export_shape_json(shape_type: str, **kwargs) -> Dict[str, Any]:
    # Another place that ends up constructing shapes
    shape = make_shape(shape_type, **kwargs)
    return {"type": shape.name(), "area": shape.area(), "preview": shape.draw()}


# ---------- Example usage ----------
if __name__ == "__main__":
    inputs: List[Dict[str, Any]] = [
        {"shape": "circle", "r": 3.0},
        {"shape": "square", "s": 4.0},
        {"shape": "triangle", "base": 6.0, "height": 2.5},
        # {"shape": "hexagon", "side": 2.0},
    ]

    for spec in inputs:
        st = spec.pop("shape")
        print(render_and_report(st, **spec))
        print(export_shape_json(st, **spec))
        print("---")



# ================= Example with factory pattern: ========================================================================================
from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing import List


# =========================
# Product Interface
# =========================
class Shape(ABC):
    @abstractmethod
    def name(self) -> str: ...
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def draw(self) -> str: ...


# =========================
# Concrete Products
# =========================
class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r
    def name(self) -> str: return "Circle"
    def area(self) -> float: return pi * self.r * self.r
    def draw(self) -> str: return f"Drawing a circle (r={self.r})"

class Square(Shape):
    def __init__(self, s: float) -> None:
        self.s = s
    def name(self) -> str: return "Square"
    def area(self) -> float: return self.s * self.s
    def draw(self) -> str: return f"Drawing a square (s={self.s})"

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
    def name(self) -> str: return "Triangle"
    def area(self) -> float: return 0.5 * self.base * self.height
    def draw(self) -> str: return f"Drawing a triangle (b={self.base}, h={self.height})"

# # (Optional) Another product to show extensibility
# class Hexagon(Shape):
#     def __init__(self, side: float) -> None:
#         self.side = side
#     def name(self) -> str: return "Hexagon"
#     def area(self) -> float:
#         # Regular hexagon area = (3*sqrt(3)/2) * side^2
#         from math import sqrt
#         return (3 * sqrt(3) / 2) * self.side * self.side
#     def draw(self) -> str: return f"Drawing a hexagon (side={self.side})"


# =========================
# Creator (declares factory method + workflow)
# =========================
class ShapeCreator(ABC):
    @abstractmethod
    def create_shape(self) -> Shape:
        """Factory Method: subclasses return a concrete Shape."""
        ...

    # Core business logic that uses the created product
    def render_and_report(self) -> str:
        shape = self.create_shape()
        drawing = shape.draw()
        return f"{drawing}\n→ {shape.name()} area: {shape.area():.2f}"


# =========================
# Concrete Creators
# =========================
class CircleCreator(ShapeCreator):
    def __init__(self, r: float) -> None:
        self.r = r
    def create_shape(self) -> Shape:
        return Circle(self.r)

class SquareCreator(ShapeCreator):
    def __init__(self, s: float) -> None:
        self.s = s
    def create_shape(self) -> Shape:
        return Square(self.s)

class TriangleCreator(ShapeCreator):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
    def create_shape(self) -> Shape:
        return Triangle(self.base, self.height)

# # (Optional) New creator mapping to the new product
# class HexagonCreator(ShapeCreator):
#     def __init__(self, side: float) -> None:
#         self.side = side
#     def create_shape(self) -> Shape:
#         return Hexagon(self.side)


# =========================
# Client code
# =========================
if __name__ == "__main__":
    creators: List[ShapeCreator] = [
        CircleCreator(3.0),
        SquareCreator(4.0),
        TriangleCreator(6.0, 2.5),
        # HexagonCreator(2.0),  # optional extension
    ]
    for c in creators:
        print(c.render_and_report())
        print("---")
