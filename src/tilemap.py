from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, texture
from kivy.uix.image import Image
from src.ruby_loader import DataLoader

class TileMap(Widget):
    def __init__(self, id = 274, **kwargs):
        super(TileMap, self).__init__(**kwargs)

        self.map = DataLoader().map(id)
        self.data = self.map.data
        self.coords = []
        self.load_coords(self.map.tileset_id)

        self.size_hint_x = None
        self.size_hint_y = None
        self.width = self.map.width * 32
        self.height = self.map.height * 32

        with self.canvas:
            #Rectangle(pos=self.pos, size=self.size)
            tileset = DataLoader().tileset(self.map.tileset_id)
            name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
            for z in range(self.map.data.zsize - 1):
                for y in range(self.map.height - 1):
                    for x in range(self.map.width - 1):
                        tile = self.data.xyz(x,y,z)
                        if tile > 384:
                            coords = self.coords[tile - 384]
                            Rectangle(source=name, pos = (x * 32, -((y - self.map.height - 1) * 32)), size = (32, 32), tex_coords = coords)

    def load_coords(self, tileset_id):
        tileset = DataLoader().tileset(tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image(source=name).texture
        for y in range(texture.height // 32):
            for x in range(8):
                u = 0
                v = 0
                if x > 0:
                    u = (x * 32) / texture.width
                if y > 0:
                    v = (y * 32 + 32) / texture.height
                w = 32 / texture.width 
                h = -32 / texture.height
                coords = u, v, u + w, v, u + w, v + h, u, v + h
                self.coords.append(coords)

        
            