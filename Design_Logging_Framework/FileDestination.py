from Destination import Destination

class FileDestination(Destination):
    def __init__(self, filepath):
        self.filepath = filepath

    def append(self, msg):
        # with open(self.filepath, "w") as f:
        #     f.write(msg)
        pass
