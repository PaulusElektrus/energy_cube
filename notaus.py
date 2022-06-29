try:
    from RPi import GPIO
except ImportError:
    import _fake_GPIO as GPIO
import time

relay_pins = {1: 14, 2: 15, 3: 18, 4: 23, 5: 24, 6: 25, 7: 8, 8: 7}

# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)

# GPIO 18 (Pin 12) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Callback-Funktion
def Interrupt():
    for relay_pin, board_pin in relay_pins.items():
        GPIO.output(board_pin, GPIO.HIGH)

# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(5, GPIO.RISING, callback = Interrupt, bouncetime = 1000)  