from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image

import firebase_admin

APIkey = open("apiKey")

class ChoreManagerApp(App):
    def build(self):
        return ChoreManagerInterface()
    
class ChoreManagerInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#=======================================================================================================

if __name__ == '__main__':
    ChoreManagerApp().run()