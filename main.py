import kivy

from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def build(self):
            return

if __name__ == '__main__':
    LuminolApp().run()