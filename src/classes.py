#-----------------------------------------------------
#   Define all RGSS classes in python because it makes my life easier
#-----------------------------------------------------
import re
import sys, inspect
from rubymarshal.classes import RubyObject, registry
from serialize import Table
from serialize import Color
from serialize import Tone

# There's probably a better and faster way to do this but whatever
class Tileset(RubyObject):
    ruby_class_name = "RPG::Tileset"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.passages = Table()._load(self.attributes['@passages']._private_data)
        self.terrain_tags = Table()._load(self.attributes['@terrain_tags']._private_data)
        self.priorites = Table()._load(self.attributes['@priorities']._private_data)

    @property
    def id(self):
        return self.attributes['@id']

    @id.setter
    def id(self, value):
        self.attributes['@id'] = value
    
    @property
    def name(self):
        return self.attributes['@name']
    
    @name.setter
    def name(self, value):
        self.attributes['@name'] = value
    
    @property
    def tileset_name(self):
        return self.attributes['@tileset_name']

    @tileset_name.setter
    def tileset_name(self, value):
        self.attributes['@tileset_name'] = value
 
    @property
    def autotile_names(self):
        return self.attributes['@autotile_names']
    
    @autotile_names.setter
    def autotile_names(self, value):
        self.attributes['@autotile_names'] = value
    
    @property
    def panorama_name(self):
        return self.attributes['@panorama_name']
    
    @panorama_name.setter
    def panorama_name(self, value):
        self.attributes['@panorama_name'] = value
    
    @property
    def panorama_hue(self):
        return self.attributes['@panorama_hue']
    
    @panorama_hue.setter
    def panorama_hue(self, value):
        self.attributes['@panorama_hue'] = value
    
    @property
    def fog_name(self):
        return self.attributes['@fog_hue']
    
    @fog_name.setter
    def fog_name(self, value):
        self.attributes['@fog_name'] = value
    
    @property
    def fog_opacity(self):
        return self.attributes['@fog_opacity']
    
    @fog_opacity.setter
    def fog_opacity(self, value):
        self.attributes['@fog_opacity'] = value

    @property
    def fog_opacity(self):
        return self.attributes['@fog_opacity']
    
    @property
    def fog_blend_type(self):
        return self.attributes['@fog_blend_type']
    
    @property
    def fog_zoom(self):
        return self.attributes['@fog_zoom']
    
    @fog_zoom.setter
    def fog_zoom(self, value):
        self.attributes['@fog_zoom'] = value
    
    @property
    def fog_sx(self):
        return self.attributes['@fog_sx']
    
    @fog_sx.setter
    def fog_sx(self, value):
        self.attributes['@fog_sx'] = value

    @property
    def fog_sy(self):
        return self.attributes['@fog_sy']
    
    @fog_sy.setter
    def fog_sy(self, value):
        self.attributes['@fog_sy'] = value
    
    @property
    def battleback_name(self):
        return self.attributes['@battleback_name']
    
    @battleback_name.setter
    def batteleback_name(self, value):
        self.attributes['@battleback_name'] = value

    @property
    def passages(self):
        return self.attributes['@passages']

    @passages.setter
    def passages(self, value: Table):
        self.attributes['@passages'] = value
    
    @property
    def priorities(self):
        return self.attributes['@priorities']
    
    @priorities.setter
    def priorities(self, value: Table):
        self.attributes['@priorities'] = value

    @property
    def terrain_tags(self):
        return self.attributes['@terrain_tags']
    
    @terrain_tags.setter
    def terrain_tags(self, value: Table):
        self.attributes['@terrain_tags'] = value


class Map(RubyObject):
    ruby_class_name = "RPG::Map"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.data = Table()._load(self.attributes['@data']._private_data)

    @property
    def tileset_id(self):
        return self.attributes['@tileset_id']
    
    @tileset_id.setter
    def tileset_id(self, value):
        self.attributes['@tilest_id'] = value
    
    @property
    def width(self):
        return self.attributes['@width']
    
    @width.setter
    def width(self, value):
        self.attributes['@width'] = value
    
    @property
    def height(self):
        return self.attributes['@height']
    
    @height.setter
    def height(self, value):
        self.attributes['@height'] = value
    
    @property
    def autoplay_bgm(self):
        return self.attributes['@autoplay_bgm']
    
    @autoplay_bgm.setter
    def autoplay_bgm(self, value):
        self.attributes['@autoplay_bgm'] = value
    
    @property
    def autoplay_bgs(self):
        return self.attributes['@autoplay_bgs']
    
    @autoplay_bgs.setter
    def autoplay_bgs(self, value):
        self.attributes['@autoplay_bgs'] = value
    
    @property
    def bgm(self):
        return self.attributes['@bgm']

    @bgm.setter
    def bgm(self, value):
        self.attributes['@bgm'] = value
    
    @property
    def bgs(self):
        return self.attributes['@bgs']
    
    @bgs.setter
    def bgs(self, value):
        self.attributes['@bgs'] = value
    
    @property
    def encounter_list(self):
        return self.attributes['@encounter_list']
    
    @encounter_list.setter
    def encounter_list(self, value):
        self.attributes['@encounter_list'] = value
    
    @property
    def encounter_step(self):
        return self.attributes['@encounter_step']
    
    @encounter_step.setter
    def encounter_step(self, value):
        self.attributes['@encounter_step'] = value
    
    @property
    def events(self):
        return self.attributes['@events']
    
    @events.setter
    def events(self, value):
        self.attributes['@events'] = value
    
    @property
    def data(self):
        return self.attributes['@data']
    
    @data.setter
    def data(self, value: Table):
        self.attributes['@data'] = value


class Event(RubyObject):
    ruby_class_name = "RPG::Event"

    @property
    def id(self):
        return self.attributes['@id']
    
    
    @id.setter
    def id(self, value):
        self.attributes['@id'] = value

    @property
    def name(self):
        return self.attributes['@name']
    
    @name.setter
    def name(self, value):
        self.attributes['@name'] = value

    @property
    def x(self):
        return self.attributes['@x']
    
    @x.setter
    def x(self, value):
        self.attributes['@x'] = value

    @property
    def y(self):
        return self.attributes['@y']
    
    @y.setter
    def y(self, value):
        self.attributes['@y'] = value
    
    @property
    def pages(self):
        return self.attributes['@pages']
    
    @pages.setter
    def pages(self, value):
        self.attributes['@pages'] = value

class EventPage(RubyObject):
    ruby_class_name = "RPG::Event::Page"

    @property
    def condition(self):
        return self.attributes['@condition']
    
    @condition.setter
    def condition(self, value):
        self.attributes['@condition'] = value

    @property
    def graphic(self):
        return self.attributes['@graphic']
    
    @graphic.setter
    def graphic(self, value):
        self.attributes['@graphic'] = value
    
    @property
    def  move_type(self):
        return self.attributes['@move_type']

    @move_type.setter
    def move_type(self, value):
        self.attributes['@move_type'] = value

    @property
    def  move_speed(self):
        return self.attributes['@move_speed']
    
    @move_speed.setter
    def move_speed(self, value):
        self.attributes['@move_speed'] = value

    @property
    def move_frequency(self):
        return self.attributes['@move_frequency']
    
    @move_frequency.setter
    def move_frequency(self, value):
        self.attributes['@move_frequency'] = value

    @property
    def move_route(self):
        return self.attributes['@move_route']
    
    @move_route.setter
    def move_route(self, value):
        self.attributes['@move_route'] = value
    
    @property
    def walk_anime(self):
        return self.attributes['@walk_anime']
    
    @walk_anime.setter
    def walk_anime(self, value):
        self.attributes['@walk_anime'] = value

class EventCondition(RubyObject):
    ruby_class_name = "RPG::Event::Page::Condition"

class EventGraphic(RubyObject):
    ruby_class_name = "RPG::Event::Page::Graphic"

class EventCommand(RubyObject):
    ruby_class_name = "RPG::EventCommand"

class MoveRoute(RubyObject):
    ruby_class_name = "RPG:::MoveRoute"

class MoveCommand(RubyObject):
    ruby_class_name = "RPG::MoveCommand"

class MapInfo(RubyObject):
    ruby_class_name = "RPG::MapInfo"

class AudioFile(RubyObject):
    ruby_class_name = "RPG::AudioFile"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)

    @property
    def volume(self):
        return self.attributes['@volume']
    
    @volume.setter
    def volume(self, value):
        self.attributes['@volume'] = value

    @property
    def pitch(self):
        return self.attributes['@pitch']
    
    @pitch.setter
    def pitch(self, value):
        self.attributes['@pitch'] = value
    
    @property
    def name(self):
        return self.attributes['@name']
    
    @name.setter
    def name(self, value):
        self.attributes['@name'] = value

# Load all classes into registry
# Python moment
for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        registry.register(obj)