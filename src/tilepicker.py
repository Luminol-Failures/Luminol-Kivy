from kivy.core import image
from kivy.uix.image import Image
from src.ruby_loader import DataLoader

class TilePicker(Image):
    def __init__(self, id = 1, **kwargs):
        super(TilePicker, self).__init__(**kwargs)
        self.map = DataLoader().map(id)
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        self.source = name

        self.size_hint_y = None
        self.size_hint_x = None
        self.allow_stretch = False
        self.width = self.texture.width
        self.height = self.texture.height
