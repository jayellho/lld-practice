import time
import hashlib

class Ticket:
    def __init__(self, ticket_id: str, vehicle_id: str, exit_time: int):
        
        self.vehicle_id = vehicle_id
        self.entry_time = int(time.time())
        self.ticket_id = hashlib.sha256(f"{self.entry_time}{vehicle_id}".encode()).hexdigest()[:10]
        self.exit_time = exit_time
    
    def set_exit_time(self, exit_time: int):
        self.exit_time = exit_time

    def set_vehicle_id(self, vehicle_id: str):
        self.vehicle_id = vehicle_id
    