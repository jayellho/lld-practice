import threading

class LogLevel:
    _dictOfLevels = {"INFO": 0} # default log level.
    _lock = threading.Lock()

    @classmethod
    def addLevel(cls, name, value):
        # protect shared registry:
        with cls._lock:
            if name in cls._dictOfLevels:
                raise Exception(f"Log level {name} already exists!")
            cls._dictOfLevels[name] = value



        