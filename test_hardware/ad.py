from gpiozero import MCP3008
from time import sleep

voltage = [0,0,0,0,0,0,0,0]
vref = 3.3

while True:
    for x in range(0, 8):
        with MCP3008(channel=x, clock_pin=21, mosi_pin=20, miso_pin=19, select_pin=18) as reading:
            voltage[x] = reading.value * vref
            print(x,": ", voltage[x])
            sleep(0.5)