from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
from kivy.graphics.scissor_instructions import ScissorPush, ScissorPop
from kivy.uix.image import Image
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
        self.coords = []

        self.load_tiles()
        self.draw_map_tiles()
        self.draw_events()

    def set_map_id(self, id):
        self.map = DataLoader().map(id)
        self.data = self.map.data
        self.load_tiles()
        self.draw_map_tiles()
        self.draw_events()

    def set_scale(self, value):
        self.scale = value
        self.draw_map_tiles()
        self.draw_events()

    def load_tiles(self):
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image(source=name, mipmap = True).texture
        
        self.coords = []
        for y in range(texture.height // 32):
            for x in range(texture.width // 32):
                u = 0
                v = 32 / texture.height
                if x > 0:
                    u = (x * 32) / texture.width
                if y > 0:
                    v = (y * 32 + 32) / texture.height
                w = 32 / texture.width 
                h = -32 / texture.height
                coords = u, v, u + w, v, u + w, v + h, u, v + h
                self.coords.append(coords)
    
    def set_grid(self, value):
        if value == 'normal':
            self.grid = False
        else:
            self.grid = True
        self.draw_map_tiles()
    
    def draw_map_tiles(self, *args):
        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale
        tileset = DataLoader().tileset(self.map.tileset_id)
        grid_texture = Image(source='assets/tile_grid.png').texture
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        tileset_texture = Image(source = name).texture
        if tileset.panorama_name.decode() != "":
            bg_name = f"Graphics/Panoramas/{tileset.panorama_name.decode()}.png"
            bg_texture = Image(source=bg_name, mipmap = True).texture

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
                for y in range(self.map.height):
                    for x in range(self.map.width):
                        tile = self.data.xyz(x,y,z)
                        if tile > 384:
                            coords = self.coords[tile - 384]
                            Rectangle(
                                texture = tileset_texture, 
                                pos = (x * self.scale,-((y - self.map.height - 1) * self.scale + self.scale * 2)), 
                                size = (self.scale, self.scale),
                                tex_coords = coords
                            )

            if self.grid:
                for y in range(self.map.height):
                    for x in range(self.map.width):
                        Rectangle(
                            texture = grid_texture, 
                            pos = (x * self.scale, -((y - self.map.height - 1) * self.scale + self.scale * 2)), 
                            size = (self.scale, self.scale)
                        )

    def draw_events(self):
        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        tileset_texture = Image(source = name).texture

        events = self.map.events
        blank_event_texture = Image(source='assets/event.png').texture
        for id, event in events.items():
            graphic = event.pages[0].graphic
            try:
                name = graphic.character_name.decode()
            except AttributeError:
                name = graphic.character_name.text

            if name != "":
                event_graphic = Image(source=f"Graphics/Characters/{graphic.character_name.decode()}.png").texture
                with self.canvas:
                    cw = event_graphic.width // 4 
                    ch = event_graphic.height // 4

                    u = (cw * graphic.pattern) / event_graphic.width
                    v = (ch / event_graphic.height)
                    w = (cw / event_graphic.width)
                    h = -(ch / event_graphic.height)
                    coords = u, v, u + w, v, u + w, v + h, u, v + h

                    #x, y = self.to_window(*self.pos)
                    #ScissorPush(
                    #    x = event.x * self.scale + x,
                    #    y = event.y * self.scale + y,
                    #    width = 32,
                    #    height = 32
                    #)

                    Rectangle(
                        texture = event_graphic,
                        size = (cw * (self.scale / 32), ch * (self.scale / 32)),
                        pos = ((event.x * self.scale) + 16 - (cw / 2), -((event.y - self.map.height - 1) * self.scale + self.scale * 2)),
                        tex_coords = coords
                    )


            elif graphic.tile_id != 0:
                try:
                    coords = self.coords[graphic.tile_id - 384]
                except IndexError:
                    coords = self.coords[0]
                with self.canvas:
                    Rectangle(
                        texture = tileset_texture, 
                        pos = (event.x * self.scale,-((event.y - self.map.height - 1) * self.scale + self.scale * 2)), 
                        size = (self.scale, self.scale),
                        tex_coords = coords
                    )

        for id, event in events.items():
            with self.canvas:
                Rectangle(
                    texture=blank_event_texture, 
                    size = (self.scale, self.scale), 
                    pos = (event.x * self.scale, -((event.y - self.map.height - 1) * self.scale + self.scale * 2))
                )
    
