from Destination import Destination

class ConsoleDestination(Destination):
    def append(self, msg):
        print(msg)
