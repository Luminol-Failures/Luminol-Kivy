from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from src.tilemap import TileMap
class CenterLayout(BoxLayout):
    def __init__(self, root, **kwargs):
        super(CenterLayout, self).__init__(**kwargs)

        self.root = root
        self.orientation ='vertical'
        
        self.topbuttons = [
            ToggleButton(text='Scale: 1', font_size=14,  group = 'scale', state = 'down'),
            ToggleButton(text='Scale: 2', font_size=14,  group = 'scale'),
            ToggleButton(text='Scale: 3', font_size=14,  group = 'scale'),
            ToggleButton(text='Show grid', font_size=14, state = 'down'),
            ToggleButton(text='Show event graphics', font_size=14, state = 'down'),
            ToggleButton(text='Show event boxes', font_size=14, state = 'down')
        ]

        self.topbuttons[0].bind(on_press=self.root.scale_map_1)
        self.topbuttons[1].bind(on_press=self.root.scale_map_2)
        self.topbuttons[2].bind(on_press=self.root.scale_map_3)
        self.topbuttons[3].bind(state=self.root.grid)
        self.topbuttons[4].bind(state=self.root.event_graphics)
        self.topbuttons[5].bind(state=self.root.event_boxes)

        top_buttons = BoxLayout(orientation = 'horizontal')

        for b in self.topbuttons: top_buttons.add_widget(b)

        self.add_widget(top_buttons)

        self.map_scroller = ScrollView(size_hint_y=None, height = Window.height - 40, scroll_type = ['bars', 'content'], bar_width = 5)
        
        self.tilemap = TileMap(self.root.map_id)

        self.map_scroller.add_widget(self.tilemap)

        self.add_widget(self.map_scroller)
