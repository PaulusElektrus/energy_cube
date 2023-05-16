from time import sleep
import spidev

voltage = [0,0,0,0,0,0,0,0]
vref = [3.3,3.3,3.3,3.3,15,30,3300,3300]
aref = [0,0,0,0,0,0,100,66]
aoff = 1090
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
    for x in range(0, 6):
        voltage[x] = readMCP3008(x)
        print(label[x], " - Kanal: ", x+1, ": ", voltage[x], "Einheiten = ", round(voltage[x]/1023.*vref[x],4), "V = ", round(voltage[x]/10.23,1), "%")
    for x in range(6, 8):
        voltage[x] = readMCP3008(x)
        a = (((voltage[x]/1023)*vref[x])-aoff)/aref[x]
        print(label[x], " - Kanal: ", x+1, ": ", voltage[x], "Einheiten = ", round(a,4), "A = ", round(voltage[x]/10.23,1), "%")
    print(n, "te Abfrage")
    n+=1
    sleep(1)