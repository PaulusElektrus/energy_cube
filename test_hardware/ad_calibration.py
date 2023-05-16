from time import sleep
import spidev

voltage = [0,0,0,0,0,0,0,0]
steps = 1023
vref = 3.3
aoff = vref/2
conversion_factors = [1,1,1,1,4.668,9.336,1,1]
ampere_conversion_factors = [1,1,1,1,1,1,0.1,0.066]
label = ["3,3V","0V","Poti 1","Poti 2","15V","30V","20A","30A"]
n = 1

spi = spidev.SpiDev()
spi.open(1, 0)
spi.max_speed_hz = 976000

def readMCP3008(channel):
  adc=spi.xfer2([1,(8+channel)<<4,0])
  wert = ((adc[1]&3) << 8) + adc[2]
  return wert

while True:
    print(n, "te Abfrage: ")
    for x in range(0, 6):
        readings = 0.0
        repetitions = 200
        for y in range(repetitions):
            readings += readMCP3008(x)
        average = readings/repetitions
        volts = '{:6.3f}'.format(vref*average*conversion_factors[x]/steps)
        print(label[x], " - Kanal: ", x+1, ": ", volts, "V")
    for x in range(6, 8):
        readings = 0.0
        repetitions = 200
        for y in range(repetitions):
            readings += readMCP3008(x)
        average = readings/repetitions
        volts = vref*average*conversion_factors[x]/steps
        print_volts = '{:6.3f}'.format(volts)
        ampere = ((volts-aoff) / ampere_conversion_factors[x])
        print_ampere = '{:6.3f}'.format(ampere)
        print(label[x], " - Kanal: ", x+1, ": ", print_volts, "V, entspricht: ", ampere, "A")
    n+=1
    sleep(2)

    