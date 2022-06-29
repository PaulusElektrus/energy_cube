from gpiozero import MCP3008
from time import sleep
import spidev

voltage = [0,0,0,0,0,0,0,0]
vref = 3.3

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

# 104 Poti
#while True:
 #   for i in range(0xE1, 0x104, 1):
  #      write_pot(i)
   #     sleep(0.25)
    #print("On")
    #for i in range(0x104, 0xE1, -1):
     #   write_pot(i)
      #  sleep(0.25)
    #print("Off")

# 103 Poti
while True:
    with MCP3008(channel=0) as reading:
        for i in range(0x00, 0xFF, 1):
            write_pot(i)
            voltage[1] = reading.value * vref
            print(1,": ", voltage[1])
            sleep(0.01)
        print("On")
        sleep(1)
        for i in range(0xFF, 0x00, -1):
            write_pot(i)
            voltage[1] = reading.value * vref
            print(1,": ", voltage[1])
            sleep(0.01)
        print("Off")
        sleep(1)
    