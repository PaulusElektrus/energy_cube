from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil.js.window import jQuery
from anvil.js import get_dom_node

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    iframe = jQuery("<iframe width='100%' height='800px'>").attr("src","http://localhost:3000/d/jlnf9AgRz/1?orgId=1&from=1658310136824&to=1658331736824")
    iframe.appendTo(get_dom_node(self.content_panel))
    
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_4.visible = False
    anvil.server.call("einschalten")
    anvil.server.call("ausschalten")
    self.button_4.visible = True
    return

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    x = anvil.server.call("read_data")
    alert(x)
    return

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("write_pot", 0x00)
    return

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("write_pot", 0xFF)
    return

  def button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def button_1_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    #self.build_voltage_graph()
    pass


