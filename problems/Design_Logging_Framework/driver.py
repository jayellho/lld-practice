# driver.py

from Logger             import Logger
from ConsoleDestination import ConsoleDestination
from FileDestination    import FileDestination
from LogLevel           import LogLevel
from LogMessage         import LogMessage

def main():
    # 1) Get the singleton logger
    logger = Logger.get()

    # 1b) Add log levels.
    LogLevel.addLevel("DEBUG", 1)
    LogLevel.addLevel("WARNING", 2)
    LogLevel.addLevel("ERROR", 4)

    # 2) Configure threshold and destination
    logger.setLevel("DEBUG")                        # allow DEBUG and above
    logger.setDestination(ConsoleDestination())     # print to console

    # 3) Emit some messages
    logger.log(LogMessage("Application starting", "INFO"))
    logger.log(LogMessage("Loading modules", "DEBUG"))
    logger.log(LogMessage("Cache miss for key 'X'", "WARNING"))
    logger.log(LogMessage("Unable to connect to DB", "ERROR"))

    # 4) Dynamically register a new level
    LogLevel.addLevel("TRACE", 5)
    logger.log(LogMessage("Fine-grained trace data", "TRACE"))

    # 5) Switch to file output
    file_dest = FileDestination("app.log")
    logger.setDestination(file_dest)

    logger.log(LogMessage("Now logging to file", "INFO"))
    logger.log(LogMessage("Trace entry in file", "TRACE"))

if __name__ == "__main__":
    main()
