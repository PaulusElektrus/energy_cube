from ._anvil_designer import homeTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.n = 1
    self.build_voltage_graph()
    
  def build_voltage_graph(self):
    voltage = self.n
    gauge = go.Indicator(
                          mode = "gauge+number",
                          value = voltage,
                          domain = {'x': [0, 1], 'y': [0, 1]},
                          title = {'text': "Gauge chart", 'font': {'size': 24}},
                          gauge = {
                              'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
                              'bar': {'color': "black", 'thickness': 0.4},
                              'bgcolor': "white",
                              'borderwidth': 2,
                              'bordercolor': "gray",
                              'steps': [
                                  {'range': [0, 2], 'color': 'darkgreen'},
                                  {'range': [2, 4], 'color': 'green'},
                                  {'range': [4, 6], 'color': 'orange'},
                                  {'range': [6, 8], 'color': 'yellow'},
                                  {'range': [8, 10], 'color': 'red'},
                              ],
                              'threshold': {
                                  'line': {'color': "royalblue", 'width': 4},
                                  'thickness': 0.75,
                                  'value': 7}}
                          )
    
    self.plot_1.data = gauge

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_4.visible = False
    anvil.server.call("einschalten")
    self.button_4.visible = True
    self.n = 5
    pass

  def button_1_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass

  def button_1_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.build_voltage_graph()





