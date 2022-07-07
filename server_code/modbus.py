import sdm_modbus

# Settings of Sensor Device
meter = sdm_modbus.SDM120(
    device='/dev/ttyUSB0',
    stopbits=1,
    parity='N',
    baud=9600,
    timeout=2,
    unit=1
    )
            
def read_data():
    data = meter.read_all(sdm_modbus.registerType.INPUT)
    print(data)
    return data