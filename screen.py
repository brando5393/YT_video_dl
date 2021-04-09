from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Screen(GridLayout):
  def __init__(self, **kwargs):
    super(Screen,self).__init__(**kwargs)
    # set columns
    self.cols = 1
    # add widgets
    self.add_widget(Label(text="YouTube Video Downloader"))
    self.add_widget(Label(text="Paste your video link below"))
    self.add_widget(TextInput(multiline=False))