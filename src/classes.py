#-----------------------------------------------------
#   Define all RGSS classes in python because fuck you
#-----------------------------------------------------
from rubymarshal.classes import RubyObject, registry
from serialize import Table
from serialize import RGSSRegistry

class Tileset(RubyObject):
    ruby_class_name = "RPG::Tileset"

    @property
    def id(self):
        return self.attr('@id')
    
    @property
    def name(self):
        return self.attr('@name')
    
    @property
    def tileset_name(self):
        return self.attr('@tileset_name')

    @property
    def autotile_names(self):
        return self.attr('@autotile_names')
    
    @property
    def panorama_name(self):
        return self.attr('@panorama_name')
    
    @property
    def panorama_hue(self):
        return self.attr('@panorama_hue')
    
    @property
    def fog_name(self):
        return self.attr('@fog_hue')
    
    @property
    def fog_opacity(self):
        return self.attr('@fog_opacity')

    @property
    def fog_opacity(self):
        return self.attr('@fog_opacity')
    
    @property
    def fog_blend_type(self):
        return self.attr('@fog_blend_type')
    
    @property
    def fog_zoom(self):
        return self.attr('@fog_zoom')
    
    @property
    def fog_sx(self):
        return self.attr('@fog_sx')

    @property
    def fog_sy(self):
        return self.attr('@fog_sy')
    
    @property
    def battleback_name(self):
        return self.attr('@battleback_name')

    @property
    def passages(self):
        return Table()._load(self.attr('@passages')._private_data)
    
    @property
    def priorites(self):
        return Table()._load(self.attr('@priorities')._private_data)

    @property
    def terrain_tags(self):
        return Table()._load(self.attr('@terrain_tags')._private_data)

    def attr(self, attr):
        return self.attributes[attr]


class Map(RubyObject):
    ruby_class_name = "RPG::Map"
    @property
    def tileset_id(self):
        return self.attr('@tileset_id')
    
    @property
    def width(self):
        return self.attr('@width')
    
    @property
    def height(self):
        return self.attr('@height')
    
    @property
    def autoplay_bgm(self):
        return self.attr('@autoplay_bgm')
    
    @property
    def autoplay_bgm(self):
        return self.attr('@autoplay_bgm')
    
    @property
    def autoplay_bgs(self):
        return self.attr('@autoplay_bgs')
    
    @property
    def bgm(self):
        return self.attr('@bgm')

    @property
    def bgs(self):
        return self.attr('@bgs')
    
    @property
    def encounter_list(self):
        return self.attr('@encounter_list')
    
    @property
    def encounter_step(self):
        return self.attr('@encounter_step')
    
    @property
    def events(self):
        return self.attr('@events')
    
    @property
    def data(self):
        return Table()._load(self.attr('@data')._private_data)

    def attr(self, attr):
        return self.attributes[attr]

class AudioFile(RubyObject):
    ruby_class_name = "RPG::AudioFile"

    @property
    def volume(self):
        return self.attributes['@volume']

    @property
    def pitch(self):
        return self.attributes['@pitch']
    
    @property
    def name(self):
        return self.attributes['@name']

registry.register(Tileset)
registry.register(Map)
registry.register(AudioFile)