from abc import ABC, abstractmethod
from __future__ import annotations
from vehicle import Vehicle, VehicleFactory
from ticket import Ticket



class PaymentStrategyContext():
    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy
    
    @property
    def strategy(self) -> PaymentStrategy:
        return self._strategy
    
class PaymentStrategy(ABC):
    @abstractmethod
    def calculate_payment(self, vehicle: Vehicle, ticket: Ticket) -> float:
        pass

class VehicleBasedPaymentStrategy(PaymentStrategy):
    def calculate_payment(self, vehicle: Vehicle, ticket: Ticket) -> float:
        duration = ticket.exit_time - ticket.entry_time
        hours = duration / 3600
        return vehicle.base_rate() * hours

class FlatRatePaymentStrategy(PaymentStrategy):
    def calculate_payment(self, vehicle, ticket):
        return 5.0

# driver code.
if __name__ == "__main__":
    context = PaymentStrategyContext(VehicleBasedPaymentStrategy())
    vehicle = VehicleFactory.create("car", "ABC123")
    ticket = Ticket()
    payment = context.strategy.calculate_payment(vehicle, ticket)
