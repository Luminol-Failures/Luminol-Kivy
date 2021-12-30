from kivy import graphics
from kivy.core.image import Texture
from kivy.uix.widget import Widget
from kivy.graphics import (
    RenderContext, BindTexture, Rectangle, Color
)
from kivy.graphics.scissor_instructions import ScissorPush, ScissorPop
from kivy.uix.image import Image as kiImage
from kivy.core.image import Image as CoreImage
from PIL import Image, ImageDraw, ImageFont, ImageColor

from src.ruby_loader import DataLoader
import src.config

import numpy as np
import colorsys

autotile_config = [
    [26, 27, 32, 33],
    [4, 27, 32, 33],
    [26, 5, 32, 33],
    [4, 5, 32, 33],
    [26, 27, 32, 11],
    [4, 27, 32, 11],
    [26, 5, 32, 11],
    [4, 5, 32, 11],
    [26, 27, 10, 33],
    [4, 27, 10, 33],
    [26, 5, 10, 33],
    [4, 5, 10, 33],
    [26, 27, 10, 11],
    [4, 27, 10, 11],
    [26, 5, 10, 11],
    [4, 5, 10, 11],
    [24, 25, 30, 31],
    [24, 5, 30, 31],
    [24, 25, 30, 11],
    [24, 5, 30, 11],
    [14, 15, 20, 21],
    [14, 15, 20, 11],
    [14, 15, 10, 21],
    [14, 15, 10, 11],
    [28, 29, 34, 35],
    [28, 29, 10, 35],
    [4, 29, 34, 35],
    [4, 29, 10, 35],
    [38, 39, 44, 45],
    [4, 39, 44, 45],
    [38, 5, 44, 45],
    [4, 5, 44, 45],
    [24, 29, 30, 35],
    [14, 15, 44, 45],
    [12, 13, 18, 19],
    [12, 13, 18, 11],
    [16, 17, 22, 23],
    [16, 17, 10, 23],
    [40, 41, 46, 47],
    [4, 41, 46, 47],
    [36, 37, 42, 43],
    [36, 5, 42, 43],
    [12, 17, 18, 23],
    [12, 13, 42, 43],
    [36, 41, 42, 47],
    [16, 17, 46, 47],
    [12, 17, 42, 47],
    [0, 1, 6, 7]
]

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = h + hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def wrapRange(value, min, max):
	if (value >= min and value <= max):
		return value

	while (value < min):
		value += (max - min)

	return value % (max - min)

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
        self.event_graphic = True
        self.boxes = True
        self.tileset = DataLoader().tileset(self.map.tileset_id)

        self.cursor_x = 0
        self.cursor_y = 0

        cursor = kiImage(source=src.config.luminol_dir +'/assets/cursor.png')
        texture = cursor.texture
        with self.canvas.after:
            self.cursor = Rectangle(
                texture=texture,
                size=(self.scale, self.scale),
                pos=(self.cursor_x * self.scale, (self.map.height - self.cursor_y) * self.scale),
            )

        self.set_cursor(20, 0)

        self.layers = {}
        self.autotiles = {}
        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def on_touch_down(self, touch):
       if self.collide_point(*touch.pos):
            x = touch.pos[0] // self.scale
            y = self.map.height - (touch.pos[1] // self.scale) + 1
            if self.cursor_x == x and self.cursor_y == y:
                print('cursor')
            else:
                self.set_cursor(x, y)
    
    def set_cursor(self, x, y):
        self.cursor_x = x
        self.cursor_y = y

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
        self.tileset = DataLoader().tileset(self.map.tileset_id)

        self.layers = {}
        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def set_scale(self, value):
        self.scale = value
        self.set_cursor(self.cursor_x, self.cursor_y)
        self.draw_layers()
    
    def set_grid(self, value):
        if value == 'normal':
            self.grid = False
        else:
            self.grid = True

        self.draw_layers()
    
    def set_event_graphic(self, value):
        if value == 'normal':
            self.event_graphic = False
        else:
            self.event_graphic = True
            self.create_event_layer()
        self.draw_layers()
    
    def set_boxes(self, value):
        if value == 'normal':
            self.boxes = False
        else:
            self.boxes = True
        self.draw_layers()

    
    def load_autotiles(self):
        autotile_names = self.tileset.autotile_names
        autotiles = []
        self.autotiles = {}
        for graphic in autotile_names:
            if graphic.decode() != "":
                autotiles.append(Image.open(f"Graphics/Autotiles/{graphic.decode()}.png"))
            else:
                autotiles.append(None)
        
        a = 1
        blank_tile = Image.new('RGBA', (32, 32))
        for i in range(48):
            self.autotiles[i] = blank_tile
        for autotile in autotiles:
            autotile_list = []
            if autotile == None:
                tile = Image.new('RGBA', (32, 32))
                for i in range(48):
                    autotile_list.append(tile)
            else:
                corners = []
                t = 0
                for y in range(128 // 16):
                    for x in range(96 // 16):
                        corners.append(autotile.crop((
                            x * 16, y * 16,
                            x * 16 + 16, y * 16 + 16
                        )))
                        t += 1
                for i in range(48):
                    tile = self.create_autotile(
                        corners, *autotile_config[i]
                    )
                    autotile_list.append(tile)
            t = 0
            for tile in autotile_list:
                self.autotiles[t + (a * 48)] = tile
                t += 1
            a += 1
    
    def create_autotile(self, tiles, c1, c2, c3, c4):
        tile = Image.new('RGBA', (32, 32))
        tile.paste(tiles[c1], (0, 0))
        tile.paste(tiles[c2], (16, 0))
        tile.paste(tiles[c3], (0, 16))
        tile.paste(tiles[c4], (16, 16))
        return tile

    
    def create_map_layer(self, *args):
        self.load_autotiles()
        grid_texture = Image.open(src.config.luminol_dir + '/assets/tile_grid.png')

        name = f"Graphics/Tilesets/{self.tileset.tileset_name.decode()}.png"
        try:
            texture = Image.open(name)
        except FileNotFoundError:
            texture = Image.open(src.config.luminol_dir + '/assets/placeholder.png')

        self.layers = {}
        loaded_tiles = {}
        for z in range(self.map.data.zsize):
            layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
            for y in range(self.map.height):
                for x in range(self.map.width):
                    tile_id = self.data.xyz(x,y,z)
                    if tile_id >= 384:
                        tile_num = tile_id - 384
                        ty = tile_num // 8 * 32
                        tx = tile_num % 8 * 32
                        if tile_id in list(loaded_tiles.keys()):
                            tile = loaded_tiles[tile_id]
                        else:
                            tile = texture.crop((tx, ty, tx + 32, ty + 32))
                            loaded_tiles[tile_id] = tile
                        layer.paste(tile, (x * 32, y * 32))
                    else:
                        tile = self.autotiles[tile_id]
                        layer.paste(tile, (x * 32, y * 32))

            layer.save(f'temp/{z}_temp.png')
            self.layers[z] = None
        
        gridlayer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        for y in range(self.map.height):
            for x in range(self.map.width):
                gridlayer.paste(grid_texture, (x * 32, y * 32))

        gridlayer.save(f'temp/grid_temp.png')
        self.layers['grid'] = None


    def create_event_layer(self):
        events = dict(sorted(self.map.events.items(), key=lambda  item: item[1].y))
        blank_event_texture = Image.open(src.config.luminol_dir + '/assets/event.png')

        name = f"Graphics/Tilesets/{self.tileset.tileset_name.decode()}.png"
        try:
            texture = Image.open(name)
        except FileNotFoundError:
            texture = Image.open(src.config.luminol_dir + '/assets/placeholder.png')

        event_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        box_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))

        if self.set_event_graphic:
            graphics = {}
            for id, event in events.items():
                graphic = event.pages[0].graphic
                name = graphic.character_name.decode()
                if name in list(graphics.keys()):
                    continue
                try:
                    graphics[name] = Image.open(f"Graphics/Characters/{graphic.character_name.decode()}.png")
                except FileNotFoundError:
                   graphics[name] = Image.open(src.config.luminol_dir + '/assets/placeholder.png')

            for id, event in events.items():
                graphic = event.pages[0].graphic
                name = graphic.character_name.decode()

                if name != "":
                    event_sheet = graphics[graphic.character_name.decode()]

                    cw = event_sheet.width // 4
                    ch = event_sheet.height // 4
                    sx = cw * graphic.pattern
                    sy = (graphic.direction - 2) / 2 * ch

                    sprite = event_sheet.crop((
                        sx, sy,
                        sx + cw, sy + ch
                    ))

                    sprite = sprite.convert('RGBA')
                    if graphic.character_hue != 0:
                        hue = wrapRange(graphic.character_hue, 0, 359)
                        arr = np.array(np.asarray(sprite).astype('float'))
                        sprite = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')

                    event_layer.paste(sprite, (event.x * 32 + 16 - cw // 2, event.y * 32 + 32 - ch), sprite)

                elif graphic.tile_id != 0:

                    tile_num = graphic.tile_id - 384
                    ty = tile_num // 8 * 32
                    tx = tile_num % 8 * 32
                    tile = texture.crop((tx, ty, tx + 32, ty + 32))
                    tile = tile.convert('RGBA')

                    if graphic.character_hue != 0:
                        hue = wrapRange(graphic.character_hue, 0, 359)
                        arr = np.array(np.asarray(tile).astype('float'))
                        tile = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')
                    event_layer.paste(tile, (event.x * 32, event.y * 32), tile)

        for id, event in events.items():
            box_layer.paste(blank_event_texture, (event.x * 32, event.y * 32))

        box_layer.save('temp/box_temp.png')
        event_layer.save('temp/events_temp.png')
        self.layers['events'] = None
        self.layers['box'] = None
    
    def draw_layers(self):
        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale

        self.canvas.clear()

        with self.canvas:
            if self.tileset.panorama_name.decode() != "":
                bg_name = f"Graphics/Panoramas/{self.tileset.panorama_name.decode()}.png"
                try:
                    bg_image = Image.open(bg_name)
                except FileNotFoundError:
                    bg_image = Image.open(src.config.luminol_dir + '/assets/placeholder.png')
                bg_image = bg_image.convert('RGBA')

                if self.tileset.panorama_hue != 0:
                    hue = wrapRange(self.tileset.panorama_hue, 0, 359)
                    arr = np.array(np.asarray(bg_image).astype('float'))
                    bg_image = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')
                
                bg_image.save('temp/bg_temp.png')
                bg_image = kiImage(source='temp/bg_temp.png')
                bg_image.reload()
                bg_texture = bg_image.texture

                bg_texture.wrap = 'repeat'
                bg_texture.uvsize = (self.width / bg_texture.width, self.height / bg_texture.height)
                bg_texture.flip_vertical()
            if self.tileset.panorama_name.decode() != "":
                Rectangle(texture=bg_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
            else:
                Color(0.10, 0.10, 0.10, 1)
                Rectangle(size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
                Color(1,1,1,1)
        
        for key, layer in self.layers.items():
            if not(self.grid) and key == 'grid':
                continue
            if not(self.event_graphic) and key == 'events':
                continue
            if not(self.boxes) and key == "box":
                continue

            image = kiImage(source=f'temp/{key}_temp.png')
            image.reload()
            texture = image.texture

            with self.canvas:
                Rectangle(
                    texture=texture,
                    size=(self.map.width * self.scale, self.map.height * self.scale),
                    pos=self.pos
                )

        if self.tileset.fog_name.decode() != "":
            fog_name = f"Graphics/Fogs/{self.tileset.fog_name.decode()}.png"
            try:
                fog_image = Image.open(fog_name)
            except FileNotFoundError:
                fog_image = Image.open(src.config.luminol_dir + '/assets/placeholder.png')
            fog_image = fog_image.convert('RGBA')

            if self.tileset.fog_hue != 0:
                hue = wrapRange(self.tileset.fog_hue, 0, 359)
                arr = np.array(np.asarray(fog_image).astype('float'))
                fog_image = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')

            fog_image.save('temp/fog_temp.png')
            fog_image = kiImage(source='temp/fog_temp.png')
            fog_image.reload()
            fog_texture = fog_image.texture

            fog_texture.wrap = 'repeat'
            fog_texture.uvsize = (self.width / fog_texture.width, self.height / fog_texture.height)
            fog_texture.flip_vertical()
            with self.canvas:
                Color(1, 1, 1, self.tileset.fog_opacity / 255)
                Rectangle(texture=fog_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
                Color(1, 1, 1, 1)
        