import kivy
from kivy_deps import sdl2, glew
from kivy.app import App
from kivy.core import window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from src.tilemap import TileMap
from src.mapinfo import MapList
from src.tilepicker import TilePicker
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.splitter import Splitter
import os, sys
from kivy.resources import resource_add_path, resource_find

class EditorLayout(GridLayout):

    def __init__(self, **kwargs):
        super(EditorLayout, self).__init__(**kwargs)

        self.cols = 2

        self.map_id = 1

        left_layout = BoxLayout(orientation ='vertical')
        right_layout = Splitter(sizable_from = 'right', min_size = 15, max_size = 270)
        right_box = BoxLayout(orientation ='vertical')
        right_layout.add_widget(right_box)

        self.root = ScrollView(size_hint_y=None, height = Window.height - 40, scroll_type = ['bars', 'content'], bar_width = 5)

        self.tilemap = TileMap(self.map_id)

        top_buttons = BoxLayout(orientation = 'horizontal')

        self.topbuttons = [
            ToggleButton(text='Scale: 1', font_size=14,  group = 'scale', state = 'down'),
            ToggleButton(text='Scale: 2', font_size=14,  group = 'scale'),
            ToggleButton(text='Scale: 3', font_size=14,  group = 'scale'),
            ToggleButton(text='Show grid', font_size=14, state = 'down')
        ]

        self.topbuttons[0].bind(on_press=self.scale_map_1)
        self.topbuttons[1].bind(on_press=self.scale_map_2)
        self.topbuttons[2].bind(on_press=self.scale_map_3)
        self.topbuttons[3].bind(state=self.grid)

        for b in self.topbuttons: top_buttons.add_widget(b)
        self.root.add_widget(self.tilemap)

        left_layout.add_widget(top_buttons)
        left_layout.add_widget(self.root)
        
        self.maplist = MapList()
        self.maplist.bind(on_touch_down=self.on_map_select)
        maplist_scroller = ScrollView(scroll_type = ['bars', 'content'], bar_width = 10)
        maplist_scroller.add_widget(self.maplist)
        maplist_splitter = Splitter(sizable_from = 'top')
        maplist_splitter.add_widget(maplist_scroller)
        mappicker_scroller = ScrollView(scroll_type = ['bars', 'content'], bar_width = 10, effect_cls = ScrollEffect)
        self.tilepicker = TilePicker(self.map_id)
        mappicker_scroller.add_widget(self.tilepicker)
        right_box.add_widget(mappicker_scroller)
        right_box.add_widget(maplist_splitter)
        
        self.add_widget(right_layout)
        self.add_widget(left_layout)
        
        self.on_map_select()
    
    def scale_map_1(self, *args):
        self.tilemap.set_scale(32)

    def scale_map_2(self, *args):
        self.tilemap.set_scale(16)

    def scale_map_3(self, *args):
        self.tilemap.set_scale(8)
    
    def grid(self, instance, *args):
        self.tilemap.set_grid(instance.state)

    def resize(self, *args):
        self.root.height = Window.height - 40
    
    def set_map_id(self, id):
        self.map_id = id
        self.tilepicker.set_map_id(id)
        self.tilemap.set_map_id(id)
    
    def on_map_select(self, *args):
        map_id = self.maplist.get_selected_map()
        if self.map_id != map_id:
            self.set_map_id(map_id)

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.layout = EditorLayout()
            Window.bind(on_resize=self.layout.resize)
            self.layout = self.layout

        def build(self):
            #self.layout.set_map_id(347)
            return self.layout

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    LuminolApp().run()