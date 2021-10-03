from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
from kivy.uix.image import Image
from src.ruby_loader import DataLoader

class TileMap(Widget):
    def __init__(self, id = 128, **kwargs):
        super(TileMap, self).__init__(**kwargs)

        self.map = DataLoader().map(id)
        self.data = self.map.data

        self.size_hint_x = None
        self.size_hint_y = None
        self.width = self.map.width * 32
        self.height = self.map.height * 32

        self.tiles = []
        self.load_tiles()
        self.draw_map_tiles()


    def load_tiles(self):
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image(source=name).texture
        
        self.tiles = []
        for y in reversed(range(texture.height // 32)):
            for x in range(texture.width // 32):
                tile = texture.get_region(x * 32, y * 32, 32, 32)
                self.tiles.append(tile)
    
    def draw_map_tiles(self, *args):
        self.width = self.map.width * 32
        self.height = self.map.height * 32

        with self.canvas:
            tileset = DataLoader().tileset(self.map.tileset_id)
            if tileset.panorama_name.decode() != "":
                bg_name = f"Graphics/Panoramas/{tileset.panorama_name.decode()}.png"
                bg_texture = Image(source=bg_name).texture

                bg_texture.wrap = 'repeat'
                bg_texture.uvsize = (self.width, self.height)

                Rectangle(Texture=bg_texture)
            else:
                Rectangle()

            for z in range(self.map.data.zsize - 1):
                for y in range(self.map.height - 1):
                    for x in range(self.map.width - 1):
                        tile = self.data.xyz(x,y,z)
                        if tile > 384:
                            if tile > len(self.tiles):
                                Rectangle(texture= self.tiles[0], pos = (x * 32,-((y - self.map.height - 1) * 32 + 64)), size = (32, 32))
                            else:
                                Rectangle(texture= self.tiles[tile - 384], pos = (x * 32,-((y - self.map.height - 1) * 32 + 64)), size = (32, 32))