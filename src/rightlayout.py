from kivy.uix.splitter import Splitter
from kivy.uix.boxlayout import BoxLayout

from src.rightbar import RightBar

class RightLayout(Splitter):
     def __init__(self, root, **kwargs):
        super(RightLayout, self).__init__(**kwargs)

        self.root = root

        self.sizable_from = 'left'
        self.min_size = 15
        self.max_size = 270

        self.layout = BoxLayout(orientation ='horizontal')
        self.add_widget(self.layout)
        self.rightbar = RightBar()
        self.layout.add_widget(self.rightbar)