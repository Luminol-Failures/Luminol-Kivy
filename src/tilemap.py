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
from io import BytesIO

from numpy.lib.shape_base import tile
from src.ruby_loader import DataLoader

import numpy as np
import colorsys

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

        self.layers = {}

        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def set_map_id(self, id):
        self.map = DataLoader().map(id)
        self.data = self.map.data

        self.layers = {}
        self.create_map_layer()
        self.create_event_layer()
        self.draw_layers()

    def set_scale(self, value):
        self.scale = value
        self.draw_layers()
    
    def set_grid(self, value):
        if value == 'normal':
            self.grid = False
        else:
            self.grid = True

        self.draw_layers()
    
    def create_map_layer(self, *args):
        self.width = self.map.width * self.scale
        self.height = self.map.height * self.scale
        grid_texture = Image.open('assets/tile_grid.png')

        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image.open(name)

        self.layers = {}
        for z in range(self.map.data.zsize):
            layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
            for y in range(self.map.height):
                for x in range(self.map.width):
                    tile_id = self.data.xyz(x,y,z)
                    if tile_id >= 384:
                        tile_num = tile_id - 384
                        ty = tile_num // 8 * 32
                        tx = tile_num % 8 * 32
                        tile = texture.crop((tx, ty, tx + 32, ty + 32))
                        layer.paste(tile, (x * 32, y * 32))
            self.layers[z] = layer
        
        gridlayer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        for y in range(self.map.height):
            for x in range(self.map.width):
                gridlayer.paste(grid_texture, (x * 32, y * 32))
        self.layers['grid'] = gridlayer


    def create_event_layer(self):
        events = dict(sorted(self.map.events.items(), key=lambda  item: item[1].y))
        blank_event_texture = Image.open('assets/event.png')

        tileset = DataLoader().tileset(self.map.tileset_id)
        name = f"Graphics/Tilesets/{tileset.tileset_name.decode()}.png"
        texture = Image.open(name)

        event_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        box_layer = Image.new('RGBA', (self.map.width * 32, self.map.height * 32))
        for id, event in events.items():
            graphic = event.pages[0].graphic
            name = graphic.character_name.decode()

            if name != "":
                try:
                    event_sheet = Image.open(f"Graphics/Characters/{graphic.character_name.decode()}.png")
                except FileNotFoundError:
                    event_sheet = Image.open('assets/placeholder.png')

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

        self.layers['events'] = event_layer
        self.layers['box'] = box_layer
    
    def draw_layers(self):
        self.canvas.clear()

        tileset = DataLoader().tileset(self.map.tileset_id)
        with self.canvas:
            if tileset.panorama_name.decode() != "":
                bg_name = f"Graphics/Panoramas/{tileset.panorama_name.decode()}.png"
                bg_image = Image.open(bg_name)

                if tileset.panorama_hue != 0:
                    hue = wrapRange(tileset.panorama_hue, 0, 359)
                    arr = np.array(np.asarray(bg_image).astype('float'))
                    bg_image = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')
                
                data = BytesIO()
                bg_image.save(data, format='png')
                data.seek(0)
                bg_texture = CoreImage(BytesIO(data.read()), ext='png').texture

                bg_texture.wrap = 'repeat'
                bg_texture.uvsize = (self.width / bg_texture.width, self.height / bg_texture.height)
                bg_texture.flip_vertical()
            if tileset.panorama_name.decode() != "":
                Rectangle(texture=bg_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
            else:
                Color(0.10, 0.10, 0.10, 1)
                Rectangle(size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
                Color(1,1,1,1)
        
        for key, layer in self.layers.items():
            if key == 'grid':
                if tileset.fog_name.decode() != "":
                    fog_name = f"Graphics/Fogs/{tileset.fog_name.decode()}.png"
                    fog_image = Image.open(fog_name)

                    if tileset.fog_hue != 0:
                        hue = wrapRange(tileset.fog_hue, 0, 359)
                        arr = np.array(np.asarray(fog_image).astype('float'))
                        fog_image = Image.fromarray(shift_hue(arr, hue / 360).astype('uint8'), 'RGBA')

                    data = BytesIO()
                    fog_image.save(data, format='png')
                    data.seek(0)
                    fog_texture = CoreImage(BytesIO(data.read()), ext='png').texture

                    fog_texture.wrap = 'repeat'
                    fog_texture.uvsize = (self.width / fog_texture.width, self.height / fog_texture.height)
                    fog_texture.flip_vertical()
                    with self.canvas:
                        Color(1, 1, 1, tileset.fog_opacity / 255)
                        Rectangle(texture=fog_texture, size = (self.map.width * self.scale, self.map.height * self.scale), pos = self.pos)
                        Color(1, 1, 1, 1)

            if not(self.grid) and key == 'grid':
                continue

            data = BytesIO()
            layer.save(data, format='png')
            data.seek(0)
            texture = CoreImage(BytesIO(data.read()), ext='png').texture
            with self.canvas:
                Rectangle(
                    texture=texture,
                    size=(self.map.width * self.scale, self.map.height * self.scale),
                    pos=self.pos
                )
        