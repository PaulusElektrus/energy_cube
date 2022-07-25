import spidev
import time

spi = spidev.SpiDev()
spi.open(1, 1)
spi.max_speed_hz = 976000

def write_pot(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

# 104 Poti
#while True:
 #   for i in range(0xE1, 0x104, 1):
  #      write_pot(i)
   #     time.sleep(0.25)
    #print("On")
    #for i in range(0x104, 0xE1, -1):
     #   write_pot(i)
      #  time.sleep(0.25)
    #print("Off")

# 103 Poti
while True:
    for i in range(0x00, 0xFF, 1):
        write_pot(i)
        time.sleep(0.1)
    print("On")
    time.sleep(2)
    for i in range(0xFF, 0x00, -1):
        write_pot(i)
        time.sleep(0.1)
    print("Off")
    time.sleep(2)