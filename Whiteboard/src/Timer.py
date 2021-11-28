import time


class Timer:
    def __init__(self):
        self.start = time.perf_counter()
    
    def get_seconds(self):
        elapsed_time = time.perf_counter() - self.start
        return elapsed_time
    
    def str_seconds(self):
        return str(self.get_seconds()) + " s"

    def get_milliseconds(self):
        return 1000 * self.get_seconds()

    def str_milliseconds(self):
        return str(self.get_milliseconds()) + " ms"

    def get_microseconds(self):
        return 1000 * self.get_milliseconds()

    def str_microseconds(self):
        return str(round(self.get_microseconds(), 2)) + " us"

    def reset(self):
        self.start = time.perf_counter()