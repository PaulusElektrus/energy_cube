from time import sleep
import spidev

spi = spidev.SpiDev()
spi.open(1, 1)
spi.max_speed_hz = 976000

spi2 = spidev.SpiDev()      
spi2.open(1, 0)              
spi2.max_speed_hz=1000000   

spi3 = spidev.SpiDev()
spi3.open(1, 2)
spi3.max_speed_hz = 976000

def readMCP3008(channel):
  adc=spi2.xfer2([1,(8+channel)<<4,0])
  wert = ((adc[1]&3) << 8) + adc[2]
  return wert

def write_pot_1(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi.xfer([msb, lsb])

def write_pot_2(input):
    msb = input >> 8
    lsb = input & 0xFF
    spi3.xfer([msb, lsb])

while True:
    print("Poti 100 kOhm: 0x00 - On --> Off - 0xFF")
    sleep(5)
    for i in range(0x00, 0xFF, 1):
        write_pot_1(i)
        v=readMCP3008(2)
        print(round(v/1023.*3.3,2), "V")
        sleep(0.05)
    v=readMCP3008(1)
    print("Referenz 0 Volt: ", v, "Einheiten = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
    print("Ende")
    sleep(5)
    print("Poti 100 kOhm: 0xFF - Off --> On - 0xFF")
    sleep(5)
    for i in range(0xFF, 0x00, -1):
        write_pot_1(i)
        v=readMCP3008(2)
        print(round(v/1023.*3.3,2), "V")
        sleep(0.05)
    v=readMCP3008(0)
    print("Referenz 3,3 Volt: ", v, "Einheiten = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
    print("Ende")
    sleep(5)
    print("Poti 10 kOhm: 0x00 - On --> Off - 0xFF")
    sleep(5)
    for i in range(0x00, 0xFF, 1):
        write_pot_2(i)
        v=readMCP3008(3)
        print(round(v/1023.*3.3,2), "V")
        sleep(0.05)
    v=readMCP3008(1)
    print("Referenz 0 Volt: ", v, "Einheiten = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
    print("Ende")
    sleep(5)
    print("Poti 10 kOhm: 0xFF - Off --> On - 0xFF")
    sleep(5)
    for i in range(0xFF, 0x00, -1):
        write_pot_2(i)
        v=readMCP3008(3)
        print(round(v/1023.*3.3,2), "V")
        sleep(0.05)
    v=readMCP3008(0)
    print("Referenz 3,3 Volt: ", v, "Einheiten = ", round(v/1023.*3.3,4), "V = ", round(v/10.23,1), "%")
    print("Ende")
    sleep(5)