from re import S
import kivy
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from src.tilemap import TileMap
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

class EditorLayout(AnchorLayout):

    def __init__(self, **kwargs):
        super(EditorLayout, self).__init__(**kwargs)

        self.anchor_x = 'left'
        self.anchor_y = 'top'

        left_layout = BoxLayout(orientation ='vertical')
        self.root = ScrollView(size_hint_y=None, height = Window.height - 40)
        self.root.bar_width = 5

        self.tilemap = TileMap()

        top_buttons = BoxLayout(orientation = 'horizontal')

        self.topbuttons = [
            ToggleButton(text='Scale: 1', font_size=14,  group = 'scale', state = 'down'),
            ToggleButton(text='Scale: 2', font_size=14,  group = 'scale'),
            ToggleButton(text='Scale: 3', font_size=14,  group = 'scale')
        ]

        self.topbuttons[0].bind(on_press=self.scale_map_1)
        self.topbuttons[1].bind(on_press=self.scale_map_2)
        self.topbuttons[2].bind(on_press=self.scale_map_3)

        for b in self.topbuttons: top_buttons.add_widget(b)
        self.root.add_widget(self.tilemap)

        left_layout.add_widget(top_buttons)
        left_layout.add_widget(self.root)
        
        self.add_widget(left_layout)
    
    def scale_map_1(self, *args):
        self.tilemap.set_scale(32)

    def scale_map_2(self, *args):
        self.tilemap.set_scale(16)

    def scale_map_3(self, *args):
        self.tilemap.set_scale(8)

    def resize(self, *args):
        self.root.height = Window.height - 40

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.layout = EditorLayout()
            Window.bind(on_resize=self.layout.resize)
            self.layout = self.layout

        def build(self):
            return self.layout

if __name__ == '__main__':
    LuminolApp().run()