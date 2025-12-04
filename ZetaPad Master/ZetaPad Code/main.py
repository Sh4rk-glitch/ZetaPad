"""
XIAO RP2040 Macropad (CircuitPython)

Features:
- Four mechanical push buttons mapped to W, A, S, D (press/hold supported)
- Rotary encoder controls system volume (increment/decrement)
- Encoder push-button toggles mute

Wiring: see README.md for pin suggestions and how to change pins.

Install requirements: `adafruit_hid`, `adafruit_debouncer` (see requirements.txt)
"""

import time
import board
import digitalio
import rotaryio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_debouncer import Debouncer

# ----------------------
# Pin configuration
# Change these to match your wiring. These use RP2040 GP pin names.
# Example pins for Seeed XIAO RP2040; adjust if you're using a different board.
BUTTON_PINS = [board.GP0, board.GP1, board.GP2, board.GP3]  # W, A, S, D
ENCODER_A = board.GP4
ENCODER_B = board.GP5
ENCODER_SW = board.GP6  # optional encoder push button

# ----------------------
# Key mapping (defaults to WASD). To use arrow keys instead, replace with
# Keycode.UP, Keycode.LEFT, Keycode.DOWN, Keycode.RIGHT
KEY_MAP = [Keycode.W, Keycode.A, Keycode.S, Keycode.D]

# Debounce + input setup
buttons = []
for p in BUTTON_PINS:
    d = digitalio.DigitalInOut(p)
    d.direction = digitalio.Direction.INPUT
    d.pull = digitalio.Pull.UP  # wiring uses ground when pressed
    buttons.append(Debouncer(d))

# Encoder setup
enc = rotaryio.IncrementalEncoder(ENCODER_A, ENCODER_B)
last_position = enc.position

# Encoder switch (optional)
enc_sw = digitalio.DigitalInOut(ENCODER_SW)
enc_sw.direction = digitalio.Direction.INPUT
enc_sw.pull = digitalio.Pull.UP
enc_btn = Debouncer(enc_sw)

# HID devices
keyboard = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)

print("XIAO macropad starting...")

try:
    while True:
        # update debouncers
        for b in buttons:
            b.update()
        enc_btn.update()

        # handle button press/hold behavior: press on fell, release on rose
        for i, b in enumerate(buttons):
            key = KEY_MAP[i]
            if b.fell:
                # pressed -> hold key
                keyboard.press(key)
            if b.rose:
                # released -> release key
                keyboard.release(key)

        # encoder rotation -> volume control
        position = enc.position
        delta = position - last_position
        if delta != 0:
            # positive delta usually means rotated one way; adjust magnitude
            if delta > 0:
                for _ in range(delta):
                    consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
            else:
                for _ in range(-delta):
                    consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
            last_position = position

        # encoder push -> toggle mute (on press)
        if enc_btn.fell:
            consumer.send(ConsumerControlCode.MUTE)

        time.sleep(0.01)

except Exception as e:
    # Keep a visible error if things go wrong
    print("Exception:", e)
    raise
