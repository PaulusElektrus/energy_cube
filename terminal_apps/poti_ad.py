print("*** Hello to Poti Controler & Measurement***")
print("Press Strg + C to abort execution.")

import spidev
from gpiozero import MCP3008
from time import sleep

vref = 9

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

while True:    
    pot = input("Enter poti state (0 - 511): ")
    pot = int(pot)
    write_pot(pot)    
    voltage = MCP3008(channel=0).value * vref
    print("Resulting Voltage: ", voltage)
