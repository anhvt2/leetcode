class Logger:

    def __init__(self):
        # dict: message -> last-printed timestamp
        self.last_printed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        prev = self.last_printed.get(message, '#')
        if prev == '#' or timestamp - prev >= 10:
            self.last_printed[message] = timestamp # update
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
