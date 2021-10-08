from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner

class RightBar(BoxLayout):
    def __init__(self, **kwargs):
        super(RightBar, self).__init__(**kwargs)

        self.orientation = 'vertical'