class LogLevel:
    _dictOfLevels = {"INFO": 0} # default log level.

    @classmethod
    def addLevel(cls, name, value):
        if name in cls._dictOfLevels:
            raise Exception(f"Log level {name} already exists!")
        cls._dictOfLevels[name] = value



        