# XIAO RP2040 Macropad (WASD + Volume Encoder)

Small CircuitPython firmware for a 4-key macropad (W, A, S, D) and a rotary encoder for system volume control. Designed for Seeed XIAO RP2040 but pins can be changed.

Files
- `main.py` — firmware to copy onto the `CIRCUITPY` drive.
- `requirements.txt` — libraries needed from the CircuitPython Bundle.

Wiring (suggested pins)
- Buttons (4): `GP0`, `GP1`, `GP2`, `GP3` — connect one side of each button to the pin, the other side to GND.
- Rotary encoder A: `GP4`  
- Rotary encoder B: `GP5`  
- Encoder push switch: `GP6` — optional; press toggles mute.

Notes about wiring
- Buttons use internal pull-ups; wire them to GND when pressed (active low).
- If your encoder has integrated pull-ups or requires different wiring, adapt pins and code accordingly.

Installing CircuitPython and libraries
1. Install CircuitPython for the XIAO RP2040: download the correct UF2 from circuitpython.org and flash it to the board. The board will mount as `CIRCUITPY`.
2. Copy `main.py` to the root of `CIRCUITPY`.
3. Create a `lib` folder on `CIRCUITPY` and add the required library modules. See `requirements.txt` for the libraries to include from the CircuitPython bundle.

Required libraries
See `requirements.txt`. At minimum, include:
- `adafruit_hid`  
- `adafruit_debouncer`  

Changing key behavior
- The default keys are `W, A, S, D` (good for gaming). To use arrow keys instead, edit `KEY_MAP` in `main.py` and replace the entries with `Keycode.UP`, `Keycode.LEFT`, `Keycode.DOWN`, `Keycode.RIGHT`.

Customization
- Change `BUTTON_PINS`, `ENCODER_A`, `ENCODER_B`, and `ENCODER_SW` at the top of `main.py` to match your physical wiring.

Usage
- Plug the XIAO into your PC. `main.py` will run and present as a USB keyboard + consumer control device. Press buttons to send/hold WASD; rotate encoder to change system volume; press encoder button to mute.

Troubleshooting
- If you don't see HID behavior, ensure CircuitPython is installed and you copied required libraries into `lib`.
- Use the serial REPL (Mu or screen/serial tool) to see printouts for debugging.

License
- Use/modify freely for personal projects.

#Images

Overall Hackpad:
<img width="1024" height="898" alt="image" src="https://github.com/user-attachments/assets/d126d55e-35dd-490f-8c0d-659dfe155de0" />
