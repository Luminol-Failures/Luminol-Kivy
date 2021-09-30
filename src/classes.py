#-----------------------------------------------------
#   Define all RGSS classes in python because fuck you
#-----------------------------------------------------
from serialize import Table
from serialize import RGSSRegistry

class Tileset:
    def __init__(self, rubyobj):
        self.rubyobj = rubyobj
    
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
        return self.rubyobj.attributes[attr]