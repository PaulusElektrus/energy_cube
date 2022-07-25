# from gpiozero import MCP3008
from time import sleep
import spidev

voltage = [0,0,0,0,0,0,0,0]
vref = 3.3

spi = spidev.SpiDev()
spi.open(1, 1)
spi.max_speed_hz = 976000

spi2 = spidev.SpiDev()      
spi2.open(1,0)              
spi2.max_speed_hz=1000000   

def readMCP3008(channel):
  adc=spi2.xfer2([1,(8+channel)<<4,0])
  wert = ((adc[1]&3) << 8) + adc[2]
  return wert

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
    for i in range(0x00, 0xFF, 1):
        write_pot(i)
        v=readMCP3008(2)
        print("Channel", 2, ": ", v, "Einh. = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
        sleep(0.01)
    print("On")
    sleep(1)
    for i in range(0xFF, 0x00, -1):
        write_pot(i)
        v=readMCP3008(2)
        print("Channel", 2, ": ", v, "Einh. = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
        sleep(0.01)
    print("Off")
    sleep(1)
    