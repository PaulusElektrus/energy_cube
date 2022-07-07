try:
    from RPi import GPIO
except ImportError:
    import _fake_GPIO as GPIO
from time import sleep

relay_pins = {1: 14, 2: 15, 3: 18, 4: 23, 5: 24, 6: 25, 7: 8, 8: 7}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for relay_pin, board_pin in relay_pins.items():
    GPIO.setup(board_pin, GPIO.OUT)
    GPIO.output(board_pin, GPIO.HIGH)


def switch_single(relay_pins, status, relais):
    board_pin = relay_pins[relais]
    if status == True:
        GPIO.output(board_pin, GPIO.LOW)
        return
    if status == False:
        GPIO.output(board_pin, GPIO.HIGH)
        return


def switch(relay_pins, status, *relais):
    for x in relais:
        board_pin = relay_pins[x]
        if status == True:
            GPIO.output(board_pin, GPIO.LOW)
        if status == False:
            GPIO.output(board_pin, GPIO.HIGH)

def off():
    for relay_pin, board_pin in relay_pins.items():
        GPIO.output(board_pin, GPIO.HIGH)

def laden():
    switch(relay_pins, False, 1, 2)
    sleep(1)
    switch(relay_pins, True, 3, 4, 5)
    sleep(1)
    switch(relay_pins, True, 6)
    return

def einspeisen():
    switch(relay_pins, False, 3, 4, 5)
    sleep(1)
    switch(relay_pins, True, 7)
    sleep(1)
    switch(relay_pins, True, 1, 2)
    return
    
