from kivy.core import image
from kivy.uix.image import Image
from src.ruby_loader import DataLoader
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
class TilePicker(Image):
    def __init__(self, id = 1, **kwargs):
        super(TilePicker, self).__init__(**kwargs)
        self.size_hint_y = None
        self.size_hint_x = None
        self.allow_stretch = False
        self.map = DataLoader().map(id)
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        self.source = name

        self.width = self.texture.width
        self.height = self.texture.height

        with self.canvas.before:
            Color(0.10, 0.10, 0.10)
            Rectangle(size = self.size, pos = self.pos)

    def set_map_id(self, id):
        self.map = DataLoader().map(id)
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        self.source = name

        self.width = self.texture.width
        self.height = self.texture.height
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.10, 0.10, 0.10)
            Rectangle(size = self.size, pos = self.pos)
