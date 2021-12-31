import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config as kvConfig
kvConfig.set('graphics', 'width', '1600')
kvConfig.set('graphics', 'height', '900')

from kivy.core.window import Window
import os, sys
from kivy.resources import resource_add_path, resource_find

from src.leftlayout import LeftLayout
from src.centerlayout import CenterLayout
from src.rightlayout import RightLayout
import src.config

class EditorLayout(GridLayout):

    def __init__(self, **kwargs):
        super(EditorLayout, self).__init__(**kwargs)

        self.cols = 3

        self.map_id = 1
        
        self.center_layout = CenterLayout(self)
        self.left_layout = LeftLayout(self)

        self.add_widget(self.left_layout)
        self.add_widget(self.center_layout)
        
        self.on_map_select()
    
    def scale_map_1(self, *args):
        self.center_layout.tilemap.set_scale(32)

    def scale_map_2(self, *args):
        self.center_layout.tilemap.set_scale(16)

    def scale_map_3(self, *args):
        self.center_layout.tilemap.set_scale(8)
    
    def grid(self, instance, *args):
        self.center_layout.tilemap.set_grid(instance.state)
    
    def event_graphics(self, instance, *args):
        self.center_layout.tilemap.set_event_graphic(instance.state)
    
    def event_boxes(self, instance, *args):
        self.center_layout.tilemap.set_boxes(instance.state)

    def resize(self, *args):
        self.center_layout.map_scroller.height = Window.height - 40
    
    def set_map_id(self, id):
        self.map_id = id
        self.left_layout.tilepicker.set_map_id(id)
        self.center_layout.tilemap.set_map_id(id)
    
    def on_map_select(self, *args):
        map_id = self.left_layout.maplist.get_selected_map()
        if self.map_id != map_id:
            self.set_map_id(map_id)

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'temp')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)
            self.layout = EditorLayout()
            Window.bind(on_resize=self.layout.resize)
            Window.set_icon("assets/icon.png")
            self.layout = self.layout

        def build(self):
            #self.layout.set_map_id(347)
            return self.layout

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))

    # External working directory handling
    if(len(sys.argv) >= 2):
        working_dir = os.getcwd()
        try:
            working_dir = sys.argv[1]
            if not os.path.exists(working_dir):
                raise AssertionError('Path does not exist')
            src.config.luminol_dir = os.getcwd()
        except:
            raise AssertionError('Invalid working directory')
        os.chdir(working_dir)

    LuminolApp().run()