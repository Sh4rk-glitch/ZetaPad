# Minimal stub for `rotaryio.IncrementalEncoder`

class IncrementalEncoder:
    def __init__(self, a_pin, b_pin):
        self._pos = 0

    @property
    def position(self):
        return self._pos

    # allow setting in tests
    @position.setter
    def position(self, v):
        self._pos = v
