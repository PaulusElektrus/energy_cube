import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

import time

import relais
import data
import poti

try:
    from RPi import GPIO
except ImportError:
    import _fake_GPIO as GPIO

# Callback-Funktion: Notaus
def Interrupt():
    for relay_pin, board_pin in relay_pins.items():
        GPIO.output(board_pin, GPIO.HIGH)

# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(5, GPIO.RISING, callback = Interrupt, bouncetime = 1000)  

@anvil.server.callable
def einschalten():
    relais.einspeisen()
    return

@anvil.server.callable
def ausschalten():
    relais.off()
    return

@anvil.server.callable
def get_voltage():
    data.read_voltage()
    return 42

@anvil.server.callable
def write_pot(value):
    poti.write_pot(value)
    return

@anvil.server.callable
def read_data():
    data.read_modbus()
    return 43