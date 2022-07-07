import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import relais
import notaus
import ad
import poti
import modbus

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

@anvil.server.callable
def einschalten():
    relais.einspeisen()
    return

def get_voltage():
    return ad.read_voltage()

def write_pot(value):
    poti.write_pot(value)
    return

def read_data():
    return modbus.read_data()