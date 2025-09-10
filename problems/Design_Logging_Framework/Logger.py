from LogLevel import LogLevel
from Destination import Destination
from ConsoleDestination import ConsoleDestination
from LogMessage import LogMessage
import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This should be a singleton!")
        Logger._instance = self
        self.level = "INFO" # defaults
        self.destination = ConsoleDestination()
    

    @staticmethod
    def get():
        if not Logger._instance:
            Logger()
        return Logger._instance
    
    def setLevel(self, name: str):
        if name not in LogLevel._dictOfLevels:
            raise Exception(f"Log level {name} is not in available log levels!")
        self.level = name

    def setDestination(self, destination: Destination):
        self.destination = destination

    def getLevels(self) -> None:
        print(f"Current log levels available: {LogLevel._dictOfLevels}")

    def log(self, msg: LogMessage):
        if LogLevel._dictOfLevels[msg.level] < LogLevel._dictOfLevels[self.level]:
            return
        
        with Logger._lock:
            self.destination.append(str(msg))
    
