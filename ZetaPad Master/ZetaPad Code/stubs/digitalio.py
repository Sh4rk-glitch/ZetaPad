# Minimal stub for `digitalio` module used in CircuitPython

class Direction:
    INPUT = 0
    OUTPUT = 1

class Pull:
    UP = 1
    DOWN = 2

class DigitalInOut:
    def __init__(self, pin):
        self.pin = pin
        self.direction = Direction.INPUT
        self.pull = None

    def switch_to_input(self, pull=None):
        self.direction = Direction.INPUT
        self.pull = pull

    def switch_to_output(self, value=False):
        self.direction = Direction.OUTPUT

    # convenience for code that accesses .value
    @property
    def value(self):
        return False

    @value.setter
    def value(self, v):
        pass
