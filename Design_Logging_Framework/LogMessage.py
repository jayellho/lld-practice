import time

class LogMessage:
    def __init__(self, msg, level):
        self.timestamp = int(time.time() * 1000)
        self.msg = msg
        self.level = level

    def __str__(self):
        return f"[{self.level}] {self.timestamp} - {self.msg}"
