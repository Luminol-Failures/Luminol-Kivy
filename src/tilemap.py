from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
from kivy.uix.image import Image
from src.ruby_loader import DataLoader

class TileMap(Widget):
    def __init__(self, id = 12, **kwargs):
        super(TileMap, self).__init__(**kwargs)

        self.map = DataLoader().map(id)
        self.data = self.map.data

        self.size_hint_x = None
        self.size_hint_y = None
        self.scale = 32

        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale

        self.grid = True
        self.tiles = []
        self.load_tiles()
        self.draw_map_tiles()

    def set_scale(self, value):
        self.scale = value
        self.draw_map_tiles()

    def load_tiles(self):
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image(source=name, mipmap = True).texture
        
        self.tiles = []
        for y in reversed(range(texture.height // 32)):
            for x in range(texture.width // 32):
                tile = texture.get_region(x * 32, y * 32, 32, 32)
                self.tiles.append(tile)
    
    def set_grid(self, value):
        if value == 'normal':
            self.grid = False
        else:
            self.grid = True
        self.draw_map_tiles()
    
    def draw_map_tiles(self, *args):
        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale

        with self.canvas:
            self.canvas.clear()
            tileset = DataLoader().tileset(self.map.tileset_id)
            if tileset.panorama_name.decode() != "":
                bg_name = f"Graphics/Panoramas/{tileset.panorama_name.decode()}.png"
                bg_texture = Image(source=bg_name, mipmap = True).texture

                bg_texture.wrap = 'repeat'
                bg_texture.uvsize = (self.width / bg_texture.width, self.height / bg_texture.height)

                Rectangle(texture=bg_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
            else:
                Rectangle(size = (self.width, self.width), pos = self.pos)

            for z in range(self.map.data.zsize - 1):
                for y in range(self.map.height - 1):
                    for x in range(self.map.width - 1):
                        tile = self.data.xyz(x,y,z)
                        if tile > 384:
                            if tile > len(self.tiles):
                                Rectangle(
                                        texture= self.tiles[0], 
                                        pos = (x * self.scale,-((y - self.map.height - 1) * self.scale + self.scale * 2)), 
                                        size = (self.scale, self.scale)
                                    )
                            else:
                                Rectangle(
                                        texture= self.tiles[tile - 384], 
                                        pos = (x * self.scale,-((y - self.map.height - 1) * self.scale + self.scale * 2)), 
                                        size = (self.scale, self.scale)
                                    )
            if self.grid:
                grid_texture = Image(source='assets/tile_grid.png').texture
                for y in range(self.map.height - 1):
                    for x in range(self.map.width - 1):
                        Rectangle(
                            texture = grid_texture, 
                            pos = (x * self.scale,-((y - self.map.height - 1) * self.scale + self.scale * 2)), 
                            size = (self.scale, self.scale)
                        )
