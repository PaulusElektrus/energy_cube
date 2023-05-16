import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])
