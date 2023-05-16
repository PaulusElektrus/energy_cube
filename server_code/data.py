# Main Program for Data Acquisition and storing in mysql

import mysql.connector
import sdm_modbus
from time import sleep
from gpiozero import MCP3008

vref = 5

modbus_sql = ("INSERT INTO sdm120 "
                        "(ID,Datum,Voltage,Current,Power_Active,Power_Apparent,Power_Reactive,Power_Factor,Phase_Angle,Frequency,Imported_Energy_Active,Exported_Energy_Active,Imported_Energy_Reactive,Exported_Energy_Reactive,Total_Demand_Power_Active,Maximum_Total_Demand_Power_Active,Import_Demand_Power_Active,Maximum_Import_Demand_Power_Active,Export_Demand_Power_Active,Maximum_Export_Demand_Power_Active,Total_Demand_Current,Maximum_Total_Demand_Current,Total_Energy_Active,Total_Energy_Reactive) "
                        "VALUES (ID,UTC_TIMESTAMP(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

ad_sql = ()

db = mysql.connector.connect(
            host ="localhost",
            user ="root",
            password="Master2022",
            database = "energy_cube",
            )
cursor = db.cursor() 

meter = sdm_modbus.SDM120(
    device='/dev/ttyUSB0',
    stopbits=1,
    parity='N',
    baud=9600,
    timeout=2,
    unit=1
    )
            
def read_modbus():
    data = meter.read_all(sdm_modbus.registerType.INPUT)
    data_list = tuple(data.values())
    write(data_list, modbus_sql)
    sleep(0.5)

def read_voltage():
    with MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8) as device:
        voltage = device.voltage * vref
    write(voltage, ad_sql)
    sleep(0.5)

def write(data, sql):
    try:
        cursor.execute(sql, data)
        db.commit()
        return
    except:
        print("Ein Datenbankfehler ist aufgetreten, erneuter Versuch in 5 Sekunden.")
        return




