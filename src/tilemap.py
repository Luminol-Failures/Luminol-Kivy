from kivy import graphics
from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
from kivy.graphics.scissor_instructions import ScissorPush, ScissorPop
from kivy.uix.image import Image as kiImage
from kivy.core.image import Image as CoreImage
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from src.ruby_loader import DataLoader

class TileMap(Widget):
    def __init__(self, id = 1, **kwargs):
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

        self.layers = []
        self.load_tiles()

        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def set_map_id(self, id):
        self.map = DataLoader().map(id)
        self.data = self.map.data
        self.load_tiles()

        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def set_scale(self, value):
        self.scale = value

        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def load_tiles(self):
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image.open(name)
        
        self.tiles = []
        for y in range(texture.height // 32):
            for x in range(texture.width // 32):
                self.tiles.append(
                    texture.crop((
                        x * 32, y * 32,
                        x * 32 + 32, y * 32 + 32
                    ))
                )
    
    def set_grid(self, value):
        if value == 'normal':
            self.grid = False
        else:
            self.grid = True

        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()
    
    def create_map_layer(self, *args):
        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale
        tileset = DataLoader().tileset(self.map.tileset_id)
        grid_texture = Image.open('assets/tile_grid.png')

        self.layers = []
        if tileset.panorama_name.decode() != "":
            bg_name = f"Graphics/Panoramas/{tileset.panorama_name.decode()}.png"
            bg_texture = kiImage(source=bg_name, mipmap = True).texture

            bg_texture.wrap = 'repeat'
            bg_texture.uvsize = (self.width / bg_texture.width, self.height / bg_texture.height)

        self.canvas.clear()
        with self.canvas:
            if tileset.panorama_name.decode() != "":

                Rectangle(texture=bg_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
            else:
                Color(0.10, 0.10, 0.10)
                Rectangle(size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
                Color(1,1,1,1)

            for z in range(self.map.data.zsize):
                layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
                for y in range(self.map.height):
                    for x in range(self.map.width):
                        tile_id = self.data.xyz(x,y,z)
                        if tile_id > 384:
                            tile = self.tiles[tile_id - 384]
                            layer.paste(tile, (x * 32, y * 32))
                self.layers.append(layer)
            

            if self.grid:
                gridlayer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
                for y in range(self.map.height):
                    for x in range(self.map.width):
                        gridlayer.paste(grid_texture, (x * 32, y * 32))
                self.layers.append(gridlayer)


    def create_event_layer(self):
        events = self.map.events
        blank_event_texture = Image.open('assets/event.png')

        event_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        box_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        for id, event in events.items():
            graphic = event.pages[0].graphic
            try:
                name = graphic.character_name.decode()
            except AttributeError:
                name = graphic.character_name.text

            if name != "":
                event_sheet = Image.open(f"Graphics/Characters/{graphic.character_name.decode()}.png")

                cw = event_sheet.width // 4
                ch = event_sheet.height // 4
                sx = cw * graphic.pattern
                sy = (graphic.direction - 2) / 2 * ch

                sprite = event_sheet.crop((
                    sx, sy,
                    sx + cw, sy + ch
                ))

                event_layer.paste(sprite, (event.x * 32 + 16 - cw // 2, event.y * 32 + 32 - ch), sprite.convert('RGBA'))

            elif graphic.tile_id != 0:
                try:
                    tile = self.tiles[graphic.tile_id - 384]
                except IndexError:
                    tile = self.tiles[0]
                event_layer.paste(tile, (event.x * 32, event.y * 32), tile.convert('RGBA'))

        for id, event in events.items():
            box_layer.paste(blank_event_texture, (event.x * 32, event.y * 32))

        self.layers.append(event_layer)
        self.layers.append(box_layer)
    
    def draw_layers(self):
        for layer in self.layers:
            data = BytesIO()
            layer.save(data, format='png')
            data.seek(0)
            texture = CoreImage(BytesIO(data.read()), ext='png').texture
            with self.canvas:
                Rectangle(
                    texture=texture,
                    size=(self.width, self.height),
                    pos=self.pos
                )