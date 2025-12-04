"""Minimal stub for adafruit_debouncer.Debouncer used in the project."""

class Debouncer:
    def __init__(self, pin_or_obj):
        # pin_or_obj is typically a DigitalInOut instance
        self._pin = pin_or_obj
        self._last = False
        # properties expected by code
        self.fell = False
        self.rose = False

    def update(self):
        # simple no-op for static analysis; don't attempt to read hardware
        self.fell = False
        self.rose = False
