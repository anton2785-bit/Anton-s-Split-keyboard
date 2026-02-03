# ============================================================
# KMK Split Keyboard - Single File Firmware
# MCU: Seeed XIAO nRF52840 (SMD)
# Layout: 5x4 per half (20 keys each)
# Features:
#   - BLE split keyboard
#   - Rotary encoder controls volume
#   - 3 LEDs on LEFT half controlled by keys
# CircuitPython: 8.x
# ============================================================

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.split import Split, SplitType
from kmk.extensions.encoder import EncoderHandler
from kmk.extensions.led import LED
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence

# ------------------------------------------------------------
# Keyboard object
# ------------------------------------------------------------
keyboard = KMKKeyboard()

# ------------------------------------------------------------
# MATRIX CONFIGURATION
# (Change pin names here if needed later)
# ------------------------------------------------------------
keyboard.col_pins = ('D4', 'D5', 'D6', 'D7', 'D8')
keyboard.row_pins = ('D0', 'D1', 'D2', 'D3')
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# ------------------------------------------------------------
# SPLIT CONFIGURATION (BLE)
# ------------------------------------------------------------
keyboard.extensions.append(
    Split(
        split_type=SplitType.BLE,
        split_side=None  # auto-detect left/right
    )
)

# ------------------------------------------------------------
# ROTARY ENCODER (LEFT HALF ONLY)
# ------------------------------------------------------------
encoder = EncoderHandler()
encoder.pins = (
    ('D9', 'D10', None),  # (A, B, Button)
)
encoder.map = [
    ((KC.VOLD, KC.VOLU),),
]
keyboard.extensions.append(encoder)

# ------------------------------------------------------------
# LEDs (LEFT HALF ONLY)
# ------------------------------------------------------------
led = LED(
    pins=('D20', 'D21', 'D22'),
    brightness=100
)
keyboard.extensions.append(led)

# ------------------------------------------------------------
# LED KEY HANDLERS
# ------------------------------------------------------------
def led_1(keyboard):
    keyboard.extensions['LED'].on(0)

def led_2(keyboard):
    keyboard.extensions['LED'].on(1)

def led_3(keyboard):
    keyboard.extensions['LED'].on(2)

def leds_off(keyboard):
    keyboard.extensions['LED'].off()

LED1 = simple_key_sequence(press=led_1)
LED2 = simple_key_sequence(press=led_2)
LED3 = simple_key_sequence(press=led_3)
LEDOFF = simple_key_sequence(press=leds_off)

# ------------------------------------------------------------
# KEYMAP (40 KEYS TOTAL)
# Order:
#   LEFT  (20 keys) then RIGHT (20 keys)
# ------------------------------------------------------------
keyboard.keymap = [
    [
        # LEFT HALF (5x4)
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.Z, KC.X, KC.C, KC.V, KC.B,
        LED1, LED2, LED3, LEDOFF, KC.SPC,

        # RIGHT HALF (5x4)
        KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.H, KC.J, KC.K, KC.L, KC.ENT,
        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH,
        KC.BSPC, KC.TAB, KC.LSFT, KC.LCTL, KC.LALT,
    ]
]

# ------------------------------------------------------------
# START KEYBOARD
# ------------------------------------------------------------
keyboard.go()
