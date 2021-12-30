from src.ruby_loader import DataLoader
import src.config

from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class TileMap(Widget):
    def __init__(self, id = 1, **kwargs):
        super(TileMap, self).__init__(**kwargs)
        
        self.cursor = Rectangle(texture=Image(source=src.config.luminol_dir +'/assets/cursor.png').texture)
        self.size_hint_x = None
        self.size_hint_y = None

        self.set_map_id(id)

    def on_touch_down(self, touch):
       if self.collide_point(*touch.pos):
            x = touch.pos[0] // self.scale
            y = self.map.height - (touch.pos[1] // self.scale) + 1
            if self.cursor_x == x and self.cursor_y == y:
                print('cursor')
            else:
                self.set_cursor(x, y)
    
    def set_cursor(self, x, y):
        self.cursor_x = max(0, min(x, self.map.width - 1))
        self.cursor_y = max(0, min(y, self.map.height - 1))
        
        with self.canvas.after:
            self.canvas.after.clear()
            self.cursor = Rectangle(
                texture=self.cursor.texture,
                size=(self.scale, self.scale),
                pos=(self.cursor_x * self.scale, (self.map.height - self.cursor_y + 1) * self.scale),
            )
    
    def set_map_id(self, id):
        self.map = DataLoader().map(id)
        self.data = self.map.data
        self.cursor_x = 0
        self.cursor_y = 0

        self.set_scale(32)
    
    def set_scale(self, scale):
        self.scale = scale
        self.width = (self.map.width * self.scale)
        self.height = (self.map.height * self.scale)
        self.set_cursor(self.cursor_x, self.cursor_y)