from gpiozero import MCP3008

vref = 5

def read_voltage():
    with MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8) as device:
        voltage = device.voltage * vref
    return voltage
