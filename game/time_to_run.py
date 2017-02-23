import time
from copy import copy

class TimeLimitReached(Exception):
    def __init__(self, time_limit):
        self.time_limit = time_limit

class TimeLimitsCalculator(object):
    def __init__(self):
        self.prepare_time_limit = None
        self.play_time_limit = None

    def run(self):
        self.prepare_time_limit = self.time_to_complete(35)
        self.play_time_limit = self.time_to_complete(30)

    def fib(self, n):
        if n == 0: return 0
        elif n == 1: return 1
        else: return self.fib(n-1) + self.fib(n-2)

    def time_to_complete(self, base_number):
        start_time = time.time()
        self.fib(base_number)
        end_time = time.time()
        return end_time - start_time

    def get_prepare_limit(self):
        return copy(self.prepare_time_limit)

    def get_play_limit(self):
        return copy(self.play_time_limit)

if __name__ == "__main__":
    calculator = TimeLimitsCalculator()
    calculator.run()
    print "Based on your hardware:"
    print "The time limit for each preparing your strategy is: {} seconds".format(calculator.get_prepare_limit())
    print "The time limit for each play is: {} seconds".format(calculator.get_play_limit())
