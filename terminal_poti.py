print("*** Hello to Poti Controler ***")
print("Press Strg + C to abort execution.")

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

while True:

	pot = input("Enter poti state (0 - 511): ")
	pot = int(pot)
	write_pot(pot)
