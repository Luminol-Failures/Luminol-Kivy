#-----------------------------------------------------
#   Define all RGSS classes in python because it makes my life easier
#-----------------------------------------------------
import sys
import inspect
from src.rubymarshal.classes import RubyObject, registry
from src.serialize import Table
from src.serialize import Color
from src.serialize import Tone
from src.config import Config

#from config import Config

# There's probably a better and faster way to do this but whatever
class Tileset(RubyObject):
    ruby_class_name = "RPG::Tileset"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@id': 0,
                '@name': "",
                '@tileset_name': '',
                '@autotile_names': [""] * 7,
                '@panorama_name': "",
                '@fog_name': "",
                '@fog_hue': 0,
                '@fog_opacity': 64,
                '@fog_blend_type': 0,
                '@fog_zoom': 200,
                '@fog_sx': 0,
                '@fog_sy': 0,
                '@battleback_name': "",
                '@passages': Table('Table', None, 384),
                '@priorities': Table('Table', None, 384),
                '@terrain_tags': Table('Table', None, 384),
            }
            self.priorities.set_x(0, 5)
        else:
            self.passages = Table()._load(self.attributes['@passages']._private_data)
            self.terrain_tags = Table()._load(self.attributes['@terrain_tags']._private_data)
            self.priorities = Table()._load(self.attributes['@priorities']._private_data)

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
        return self.attributes['@fog_name']
    
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
    def __init__(self, ruby_class_name=None, attributes=None, width = 20, height = 20):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.set_attributes({
                '@tileset_id': 1,
                '@width': width,
                '@height': height,
                '@autoplay_bgm': False,
                '@bgm': AudioFile(None, None, "", 80),
                '@autoplay_bgs': False,
                '@bgs': AudioFile(None, None, "", 80),
                '@encounter_list': [],
                '@data': Table('Table', None, width, height, 3),
                '@events': {}
            })
        else:
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
    def __init__(self, ruby_class_name=None, attributes=None, x = None, y = None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                "@id": 0,
                "@name": "",
                "@x": x,
                "@y": y,
                "@pages": EventPage()
            }

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
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@condition': EventCondition(),
                '@graphic': EventGraphic(),
                '@move_type': 0,
                '@move_speed': 3,
                '@move_frequency': 3,
                '@move_route': MoveRoute(),
                '@walk_anime': True,
                '@step_anime': True,
                '@direction_fix': False,
                '@through': False,
                '@always_on_top': False,
                '@trigger': 0,
                '@list': [EventCommand()]
            }

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
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@switch1_valid': False,
                '@switch2_valid': False,
                '@variable_valid': False,
                '@self_switch_valid': False,
                '@switch1_id': 1,
                '@switch2_id': 1,
                '@variable_id': 1,
                '@variable_value': 0,
                '@self_switch_ch': "A"
            }
    
    @property
    def switch1_valid(self):
        return self.attributes['@switch1_valid']
    
    @switch1_valid.setter
    def switch1_valid(self, value):
        self.attributes['@switch1_valid'] = value

    @property
    def switch2_valid(self):
        return self.attributes['@switch2_valid']
    
    @switch2_valid.setter
    def switch2_valid(self, value):
        self.attributes['@switch2_valid'] = value
    
    @property
    def variable_valid(self):
        return self.attributes['@variable_valid']
    
    @variable_valid.setter
    def variable_valid(self, value):
        self.attributes['@variable_valid'] = value

    @property
    def switch1_id(self):
        return self.attributes['@switch1_id']
    
    @switch1_id.setter
    def switch1_id(self, value):
        self.attributes['@switch1_id'] = value

    @property
    def switch2_id(self):
        return self.attributes['@switch2_id']
    
    @switch2_id.setter
    def switch2_id(self, value):
        self.attributes['@switch2_id'] = value
    
    @property
    def variable_id(self):
        return self.attributes['@variable_id']
    
    @variable_id.setter
    def variable_id(self, value):
        self.attributes['@variable_id'] = value
    
    @property
    def self_switch_ch(self):
        return self.attributes['@self_switch_ch']
    
    @self_switch_ch.setter
    def self_switch_ch(self, value):
        self.attributes['@self_switch_ch'] = value

class EventGraphic(RubyObject):
    ruby_class_name = "RPG::Event::Page::Graphic"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@tile_id': 0,
                '@character_name': "",
                '@character_hue': 0,
                '@direction': 2,
                '@pattern': 0,
                '@opacity': 255,
                '@blend_type': 0
            }
    
    @property
    def tile_id(self):
        return self.attributes['@tile_id']
    
    @tile_id.setter
    def tile_id(self, value):
        self.attributes['@tile_id'] = value
    
    @property
    def character_name(self):
        return self.attributes['@character_name']
    
    @character_name.setter
    def character_name(self, value):
        self.attributes['@character_name'] = value
    
    @property
    def direction(self):
        return self.attributes['@direction']
    
    @direction.setter
    def direction(self, value):
        self.attributes['@direction'] = value
    
    @property
    def pattern(self):
        return self.attributes['@pattern']
    
    @pattern.setter
    def pattern(self, value):
        self.attributes['@pattern'] = value

    @property
    def opacity(self):
        return self.attributes['@opacity']
    
    @opacity.setter
    def opacity(self, value):
        self.attributes['@opacity'] = value
    
    @property
    def blend_type(self):
        return self.attributes['@blend_type']
    
    @blend_type.setter
    def blend_type(self, value):
        self.attributes['@blend_type'] = value

    @property
    def character_hue(self):
        return self.attributes['@character_hue'] 

    @character_hue.setter
    def character_hue(self, value):
        self.attributes['@character_hue'] = value

class EventCommand(RubyObject):
    ruby_class_name = "RPG::EventCommand"
    def __init__(self, ruby_class_name=None, attributes=None, code = 0, indent = 0, parameters = []):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@code': code,
                '@indent': indent,
                '@parameters': parameters
            }
        code_special = Config().code_config(self.code)
        if (code_special[0]):
            # Hacky switch statement beecause python doesn't have one for some reason
            if code_special[1] == "color":
                c = Color()
                c._load(self.parameters[code_special[2]]._private_data)
                self.parameters[code_special[2]] = c
            elif code_special[1] == "tone":
                t = Tone()
                t._load(self.parameters[code_special[2]]._private_data)
                self.parameters[code_special[2]] = t

    @property
    def code(self):
        return self.attributes['@code']
    
    @code.setter
    def code(self, value):
        self.attributes['@code'] = value

    @property
    def indent(self):
        return self.attributes['@indent']
    
    @indent.setter
    def indent(self, value):
        self.attributes['@indent'] = value
    
    @property
    def parameters(self):
        return self.attributes['@parameters']

    @parameters.setter
    def parameters(self, value):
        self.attributes['@parameters'] = value

class MoveRoute(RubyObject):
    ruby_class_name = "RPG::MoveRoute"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@repeat': True,
                '@skippable': False,
                '@list': [MoveCommand()]
            }
    
    @property
    def repeat(self):
        return self.attributes['@repeat']
    
    @repeat.setter
    def repeat(self, value):
        self.attributes['@repeat'] = value

    @property
    def skippable(self):
        return self.attributes['@skippable']
    
    @skippable.setter
    def skippable(self, value):
        self.attributes['@skippable'] = True
    
    @property
    def list(self):
        return self.attributes['@list']
    
    @list.setter
    def list(self, value):
        self.attributes['@list'] = value

class MoveCommand(RubyObject):
    ruby_class_name = "RPG::MoveCommand"
    def __init__(self, ruby_class_name=None, attributes=None, code = 0, parameters = []):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@code': code,
                '@parameters': parameters
            }
    
    @property
    def code(self):
        return self.attributes['@code']
    
    @code.setter
    def code(self, value):
        self.attributes['@code'] = value
    
    @property
    def parameters(self):
        return self.attributes['@parameters']
    
    @parameters.setter
    def parameters(self, value):
        self.attributes['@parameters'] = value

class MapInfo(RubyObject):
    ruby_class_name = "RPG::MapInfo"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@name': "",
                '@parent_id': 0,
                '@order': 0,
                '@expanded': False,
                '@scroll_x': 0,
                '@scrolly_y': 0
            }
    
    @property
    def name(self):
        return self.attributes['@name']
    
    @name.setter
    def name(self, value):
        self.attributes['@name'] = value
    
    @property
    def parent_id(self):
        return self.attributes['@parent_id']
    
    @parent_id.setter
    def parent_id(self, value):
        self.attributes['@parent_id'] = value
    
    @property
    def order(self):
        return self.attributes['@order']
    
    @order.setter
    def order(self, value):
        self.attributes['@order'] = value
    
    @property
    def expanded(self):
        return self.attributes['@expanded']
    
    @expanded.setter
    def expanded(self, value):
        self.attributes['@expanded'] = value

class AudioFile(RubyObject):
    ruby_class_name = "RPG::AudioFile"
    def __init__(self, ruby_class_name=None, attributes=None, name = "", volume = 100, pitch = 100):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        # Default values
        if (self.attributes == {}):
            self.attributes = {
                '@name': name,
                '@volume': volume,
                '@pitch': pitch
            }

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

# TODO Finish these classes to be equivalent with the others
# Not done these yet since I've been working on other stuff and this is super repetitive.
class Actor(RubyObject):
    ruby_class_name = "RPG::Actor"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['parameters'] = Table()._load(self.attributes['@parameters']._private_data)
    
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
    def class_id(self):
        return self.attributes['@class_id']

    @class_id.setter
    def class_id(self, value):
        self.attributes['class_id'] = value

    @property
    def initial_level(self):
        return self.attributes['initial_level']

    @initial_level.setter
    def initial_level(self, value):
        self.attributes['initial_level'] = value

    @property
    def final_level(self):
        return self.attributes['final_level']

    @final_level.setter
    def final_level(self, value):
        self.attributes['final_level'] = value

    @property
    def exp_basis(self):
        return self.attributes['exp_basis']

    @exp_basis.setter
    def exp_basis(self, value):
        self.attributes['exp_basis'] = value

    @property
    def exp_inflation(self):
        return self.attributes['exp_inflation']

    @exp_inflation.setter
    def exp_inflation(self, value):
        self.attributes['exp_inflation'] = value
    
    @property
    def character_name(self):
        return self.attributes['character_name']

    @character_name.setter
    def character_name(self, value):
        self.attributes['character_name'] = value

    @property
    def character_hue(self):
        return self.attributes['character_hue'] 

    @character_hue.setter
    def character_hue(self, value):
        self.attributes['character_hue'] = value

    @property
    def battler_name(self):
        return self.attributes['battler_name']

    @battler_name.setter
    def battler_name(self, value):
        self.attributes['battler_name'] = value
    
    @property
    def battler_hue(self):
        return self.attributes['battler_hue']

    @battler_hue.setter
    def battler_hue(self, value):
        self.attributes['battler_hue'] = value

    @property
    def parameters(self):
        return self.attributes['parameters']

    @parameters.setter
    def parameters(self, value):
        self.attributes['parameters'] = value
    
    @property
    def weapon_id(self):
        return self.attributes['weapon_id']

    @weapon_id.setter
    def weapon_id(self, value):
        self.attributes['weapon_id'] = value
    
    @property
    def armor1_id(self):
        return self.attributes['armor1_id']

    @armor1_id.setter
    def armor1_id(self, value):
        self.attributes['armor2_id'] = value
    
    @property
    def armor2_id(self):
        return self.attributes['armor2_id']

    @armor2_id.setter
    def armor2_id(self, value):
        self.attributes['armor2_id'] = value
    
    @property
    def armor3_id(self):
        return self.attributes['armor3_id']

    @armor3_id.setter
    def armor3_id(self, value):
        self.attributes['armor3_id'] = value
    
    @property
    def armor4_id(self):
        return self.attributes['armor4_id']

    @armor4_id.setter
    def armor4_id(self, value):
        self.attributes['armor4_id'] = value

    @property
    def weapon_fix(self):
        return self.attributes['weapon_fix']

    @weapon_fix.setter
    def weapon_fix(self, value):
        self.attributes['weapon_fix'] = value

    @property
    def armor1_fix(self):
        return self.attributes['armor1_fix']
    
    @armor1_fix.setter
    def armor1_fix(self, value):
        self.attributes['armor2_fix'] = value
    
    @property
    def armor2_fix(self):
        return self.attributes['armor2_fix']

    @armor2_fix.setter
    def armor2_fix(self, value):
        self.attributes['armor2_fix'] = value
    
    @property
    def armor3_fix(self):
        return self.attributes['armor3_fix']

    @armor3_fix.setter
    def armor3_fix(self, value):
        self.attributes['armor3_fix'] = value
    
    @property
    def armor4_fix(self):
        return self.attributes['armor4_fix']

    @armor4_fix.setter
    def armor4_fix(self, value):
        self.attributes['armor4_fix'] = value

class RPGClass(RubyObject):
    ruby_class_name = "RPG::Class"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value
    
    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def position(self):
        return self.attributes['position']

    @position.setter
    def position(self, value):
        self.attributes['position'] = value
    
    @property
    def weapon_set(self):
        return self.attributes['weapon_set']

    @weapon_set.setter
    def weapon_set(self, value):
        self.attributes['weapon_set'] = value
    
    @property
    def armor_set(self):
        return self.attributes['armor_set']

    @armor_set.setter
    def armor_set(self, value):
        self.attributes['armor_set'] = value
    
    @property
    def element_ranks(self):
        return self.attributes['element_ranks']

    @element_ranks.setter
    def element_ranks(self, value):
        self.attributes['element_ranks'] = value
    
    @property
    def state_ranks(self):
        return self.attributes['state_ranks']

    @state_ranks.setter
    def state_ranks(self, value):
        self.attributes['state_ranks'] = value

    @property
    def learnings(self):
        return self.attributes['learnings']
    
    @learnings.setter
    def learnings(self, value):
        self.attributes['learnings'] = value

# this class is nested inside RPGClass according to RPG_Base.rb
class Learning(RubyObject):
    ruby_class_name = "RPG::Class::Learning"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@element_ranks'] = Table()._load(self.attributes['@element_ranks']._private_data)
        self.attributes['@state_ranks'] = Table()._load(self.attributes['@state_ranks']._private_data)
    
    @property
    def level(self):
        return self.attributes['level']
    
    @level.setter
    def level(self, value):
        self.attributes['level'] = value
    
    @property
    def skill_id(self):
        return self.attributes['skill_id']

    @skill_id.setter
    def skill_id(self, value):
        self.attributes['skill_id'] = value

class Skill(RubyObject):
    ruby_class_name = "RPG::Skill"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value
    
    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value
    
    @property
    def icon_name(self):
        return self.attributes['icon_name']

    @icon_name.setter
    def icon_name(self, value):
        self.attributes['icon_name'] = value

    @property
    def description(self):
        return self.attributes['description']

    @description.setter
    def description(self, value):
        self.attributes['description'] = value
    
    @property
    def scope(self):
        return self.attributes['scope']

    @scope.setter
    def scope(self, value):
        self.attributes['scope'] = value

    @property
    def occasion(self):
        return self.attributes['occasion']

    @occasion.setter
    def occasion(self, value):
        self.attributes['occasion'] = value

    # if there's any weird bugs beyond this point that's because i wrote a python script to automate it lol

    @property
    def animation1_id(self):
        return self.attributes['animation1_id']

    @animation1_id.setter
    def animation1_id(self, value):
        self.attributes['animation1_id'] = value

    @property
    def animation2_id(self):
        return self.attributes['animation2_id']

    @animation2_id.setter
    def animation2_id(self, value):
        self.attributes['animation2_id'] = value

    @property
    def menu_se(self):
        return self.attributes['menu_se']

    @menu_se.setter
    def menu_se(self, value):
        self.attributes['menu_se'] = value

    @property
    def common_event_id(self):
        return self.attributes['common_event_id']

    @common_event_id.setter
    def common_event_id(self, value):
        self.attributes['common_event_id'] = value

    @property
    def sp_cost(self):
        return self.attributes['sp_cost']

    @sp_cost.setter
    def sp_cost(self, value):
        self.attributes['sp_cost'] = value

    @property
    def power(self):
        return self.attributes['power']

    @power.setter
    def power(self, value):
        self.attributes['power'] = value

    @property
    def atk_f(self):
        return self.attributes['atk_f']

    @atk_f.setter
    def atk_f(self, value):
        self.attributes['atk_f'] = value

    @property
    def eva_f(self):
        return self.attributes['eva_f']

    @eva_f.setter
    def eva_f(self, value):
        self.attributes['eva_f'] = value

    @property
    def str_f(self):
        return self.attributes['str_f']

    @str_f.setter
    def str_f(self, value):
        self.attributes['str_f'] = value

    @property
    def dex_f(self):
        return self.attributes['dex_f']

    @dex_f.setter
    def dex_f(self, value):
        self.attributes['dex_f'] = value

    @property
    def agi_f(self):
        return self.attributes['agi_f']

    @agi_f.setter
    def agi_f(self, value):
        self.attributes['agi_f'] = value

    @property
    def int_f(self):
        return self.attributes['int_f']

    @int_f.setter
    def int_f(self, value):
        self.attributes['int_f'] = value

    @property
    def hit(self):
        return self.attributes['hit']

    @hit.setter
    def hit(self, value):
        self.attributes['hit'] = value

    @property
    def pdef_f(self):
        return self.attributes['pdef_f']

    @pdef_f.setter
    def pdef_f(self, value):
        self.attributes['pdef_f'] = value

    @property
    def mdef_f(self):
        return self.attributes['mdef_f']

    @mdef_f.setter
    def mdef_f(self, value):
        self.attributes['mdef_f'] = value

    @property
    def variance(self):
        return self.attributes['variance']

    @variance.setter
    def variance(self, value):
        self.attributes['variance'] = value

    @property
    def element_set(self):
        return self.attributes['element_set']

    @element_set.setter
    def element_set(self, value):
        self.attributes['element_set'] = value

    @property
    def plus_state_set(self):
        return self.attributes['plus_state_set']

    @plus_state_set.setter
    def plus_state_set(self, value):
        self.attributes['plus_state_set'] = value

    @property
    def minus_state_set(self):
        return self.attributes['minus_state_set']

    @minus_state_set.setter
    def minus_state_set(self, value):
        self.attributes['minus_state_set'] = value

class Item(RubyObject):
    ruby_class_name = "RPG::Item"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def icon_name(self):
        return self.attributes['icon_name']

    @icon_name.setter
    def icon_name(self, value):
        self.attributes['icon_name'] = value

    @property
    def description(self):
        return self.attributes['description']

    @description.setter
    def description(self, value):
        self.attributes['description'] = value

    @property
    def scope(self):
        return self.attributes['scope']

    @scope.setter
    def scope(self, value):
        self.attributes['scope'] = value

    @property
    def occasion(self):
        return self.attributes['occasion']

    @occasion.setter
    def occasion(self, value):
        self.attributes['occasion'] = value

    @property
    def animation1_id(self):
        return self.attributes['animation1_id']

    @animation1_id.setter
    def animation1_id(self, value):
        self.attributes['animation1_id'] = value

    @property
    def animation2_id(self):
        return self.attributes['animation2_id']

    @animation2_id.setter
    def animation2_id(self, value):
        self.attributes['animation2_id'] = value

    @property
    def menu_se(self):
        return self.attributes['menu_se']

    @menu_se.setter
    def menu_se(self, value):
        self.attributes['menu_se'] = value

    @property
    def common_event_id(self):
        return self.attributes['common_event_id']

    @common_event_id.setter
    def common_event_id(self, value):
        self.attributes['common_event_id'] = value

    @property
    def price(self):
        return self.attributes['price']

    @price.setter
    def price(self, value):
        self.attributes['price'] = value

    @property
    def consumable(self):
        return self.attributes['consumable']

    @consumable.setter
    def consumable(self, value):
        self.attributes['consumable'] = value

    @property
    def parameter_type(self):
        return self.attributes['parameter_type']

    @parameter_type.setter
    def parameter_type(self, value):
        self.attributes['parameter_type'] = value

    @property
    def parameter_points(self):
        return self.attributes['parameter_points']

    @parameter_points.setter
    def parameter_points(self, value):
        self.attributes['parameter_points'] = value

    @property
    def recover_hp_rate(self):
        return self.attributes['recover_hp_rate']

    @recover_hp_rate.setter
    def recover_hp_rate(self, value):
        self.attributes['recover_hp_rate'] = value

    @property
    def recover_hp(self):
        return self.attributes['recover_hp']

    @recover_hp.setter
    def recover_hp(self, value):
        self.attributes['recover_hp'] = value

    @property
    def recover_sp_rate(self):
        return self.attributes['recover_sp_rate']

    @recover_sp_rate.setter
    def recover_sp_rate(self, value):
        self.attributes['recover_sp_rate'] = value

    @property
    def recover_sp(self):
        return self.attributes['recover_sp']

    @recover_sp.setter
    def recover_sp(self, value):
        self.attributes['recover_sp'] = value

    @property
    def hit(self):
        return self.attributes['hit']

    @hit.setter
    def hit(self, value):
        self.attributes['hit'] = value

    @property
    def pdef_f(self):
        return self.attributes['pdef_f']

    @pdef_f.setter
    def pdef_f(self, value):
        self.attributes['pdef_f'] = value

    @property
    def mdef_f(self):
        return self.attributes['mdef_f']

    @mdef_f.setter
    def mdef_f(self, value):
        self.attributes['mdef_f'] = value

    @property
    def variance(self):
        return self.attributes['variance']

    @variance.setter
    def variance(self, value):
        self.attributes['variance'] = value

    @property
    def element_set(self):
        return self.attributes['element_set']

    @element_set.setter
    def element_set(self, value):
        self.attributes['element_set'] = value

    @property
    def plus_state_set(self):
        return self.attributes['plus_state_set']

    @plus_state_set.setter
    def plus_state_set(self, value):
        self.attributes['plus_state_set'] = value

    @property
    def minus_state_set(self):
        return self.attributes['minus_state_set']

    @minus_state_set.setter
    def minus_state_set(self, value):
        self.attributes['minus_state_set'] = value

class Weapon(RubyObject):
    ruby_class_name = "RPG::Weapon"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def icon_name(self):
        return self.attributes['icon_name']

    @icon_name.setter
    def icon_name(self, value):
        self.attributes['icon_name'] = value

    @property
    def description(self):
        return self.attributes['description']

    @description.setter
    def description(self, value):
        self.attributes['description'] = value

    @property
    def animation1_id(self):
        return self.attributes['animation1_id']

    @animation1_id.setter
    def animation1_id(self, value):
        self.attributes['animation1_id'] = value

    @property
    def animation2_id(self):
        return self.attributes['animation2_id']

    @animation2_id.setter
    def animation2_id(self, value):
        self.attributes['animation2_id'] = value

    @property
    def price(self):
        return self.attributes['price']

    @price.setter
    def price(self, value):
        self.attributes['price'] = value

    @property
    def atk(self):
        return self.attributes['atk']

    @atk.setter
    def atk(self, value):
        self.attributes['atk'] = value

    @property
    def pdef(self):
        return self.attributes['pdef']

    @pdef.setter
    def pdef(self, value):
        self.attributes['pdef'] = value

    @property
    def mdef(self):
        return self.attributes['mdef']

    @mdef.setter
    def mdef(self, value):
        self.attributes['mdef'] = value

    @property
    def str_plus(self):
        return self.attributes['str_plus']

    @str_plus.setter
    def str_plus(self, value):
        self.attributes['str_plus'] = value

    @property
    def dex_plus(self):
        return self.attributes['dex_plus']

    @dex_plus.setter
    def dex_plus(self, value):
        self.attributes['dex_plus'] = value

    @property
    def agi_plus(self):
        return self.attributes['agi_plus']

    @agi_plus.setter
    def agi_plus(self, value):
        self.attributes['agi_plus'] = value

    @property
    def int_plus(self):
        return self.attributes['int_plus']

    @int_plus.setter
    def int_plus(self, value):
        self.attributes['int_plus'] = value

    @property
    def element_set(self):
        return self.attributes['element_set']

    @element_set.setter
    def element_set(self, value):
        self.attributes['element_set'] = value

    @property
    def plus_state_set(self):
        return self.attributes['plus_state_set']

    @plus_state_set.setter
    def plus_state_set(self, value):
        self.attributes['plus_state_set'] = value

    @property
    def minus_state_set(self):
        return self.attributes['minus_state_set']

    @minus_state_set.setter
    def minus_state_set(self, value):
        self.attributes['minus_state_set'] = value

class Armor(RubyObject):
    ruby_class_name = "RPG::Armor"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def icon_name(self):
        return self.attributes['icon_name']

    @icon_name.setter
    def icon_name(self, value):
        self.attributes['icon_name'] = value

    @property
    def description(self):
        return self.attributes['description']

    @description.setter
    def description(self, value):
        self.attributes['description'] = value

    @property
    def kind(self):
        return self.attributes['kind']

    @kind.setter
    def kind(self, value):
        self.attributes['kind'] = value

    @property
    def auto_state_id(self):
        return self.attributes['auto_state_id']

    @auto_state_id.setter
    def auto_state_id(self, value):
        self.attributes['auto_state_id'] = value

    @property
    def price(self):
        return self.attributes['price']

    @price.setter
    def price(self, value):
        self.attributes['price'] = value

    @property
    def pdef(self):
        return self.attributes['pdef']

    @pdef.setter
    def pdef(self, value):
        self.attributes['pdef'] = value

    @property
    def mdef(self):
        return self.attributes['mdef']

    @mdef.setter
    def mdef(self, value):
        self.attributes['mdef'] = value

    @property
    def eva(self):
        return self.attributes['eva']

    @eva.setter
    def eva(self, value):
        self.attributes['eva'] = value

    @property
    def str_plus(self):
        return self.attributes['str_plus']

    @str_plus.setter
    def str_plus(self, value):
        self.attributes['str_plus'] = value

    @property
    def dex_plus(self):
        return self.attributes['dex_plus']

    @dex_plus.setter
    def dex_plus(self, value):
        self.attributes['dex_plus'] = value

    @property
    def agi_plus(self):
        return self.attributes['agi_plus']

    @agi_plus.setter
    def agi_plus(self, value):
        self.attributes['agi_plus'] = value

    @property
    def int_plus(self):
        return self.attributes['int_plus']

    @int_plus.setter
    def int_plus(self, value):
        self.attributes['int_plus'] = value

    @property
    def guard_element_set(self):
        return self.attributes['guard_element_set']

    @guard_element_set.setter
    def guard_element_set(self, value):
        self.attributes['guard_element_set'] = value

    @property
    def guard_state_set(self):
        return self.attributes['guard_state_set']

    @guard_state_set.setter
    def guard_state_set(self, value):
        self.attributes['guard_state_set'] = value

class Enemy(RubyObject):
    ruby_class_name = "RPG::Enemy"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def battler_name(self):
        return self.attributes['battler_name']

    @battler_name.setter
    def battler_name(self, value):
        self.attributes['battler_name'] = value

    @property
    def battler_hue(self):
        return self.attributes['battler_hue']

    @battler_hue.setter
    def battler_hue(self, value):
        self.attributes['battler_hue'] = value

    @property
    def maxhp(self):
        return self.attributes['maxhp']

    @maxhp.setter
    def maxhp(self, value):
        self.attributes['maxhp'] = value

    @property
    def maxsp(self):
        return self.attributes['maxsp']

    @maxsp.setter
    def maxsp(self, value):
        self.attributes['maxsp'] = value

    @property
    def str(self):
        return self.attributes['str']

    @str.setter
    def str(self, value):
        self.attributes['str'] = value

    @property
    def dex(self):
        return self.attributes['dex']

    @dex.setter
    def dex(self, value):
        self.attributes['dex'] = value

    @property
    def agi(self):
        return self.attributes['agi']

    @agi.setter
    def agi(self, value):
        self.attributes['agi'] = value

    @property
    def int(self):
        return self.attributes['int']

    @int.setter
    def int(self, value):
        self.attributes['int'] = value

    @property
    def atk(self):
        return self.attributes['atk']

    @atk.setter
    def atk(self, value):
        self.attributes['atk'] = value

    @property
    def pdef(self):
        return self.attributes['pdef']

    @pdef.setter
    def pdef(self, value):
        self.attributes['pdef'] = value

    @property
    def mdef(self):
        return self.attributes['mdef']

    @mdef.setter
    def mdef(self, value):
        self.attributes['mdef'] = value

    @property
    def eva(self):
        return self.attributes['eva']

    @eva.setter
    def eva(self, value):
        self.attributes['eva'] = value

    @property
    def animation1_id(self):
        return self.attributes['animation1_id']

    @animation1_id.setter
    def animation1_id(self, value):
        self.attributes['animation1_id'] = value

    @property
    def animation2_id(self):
        return self.attributes['animation2_id']

    @animation2_id.setter
    def animation2_id(self, value):
        self.attributes['animation2_id'] = value

    @property
    def element_ranks(self):
        return self.attributes['element_ranks']

    @element_ranks.setter
    def element_ranks(self, value):
        self.attributes['element_ranks'] = value

    @property
    def state_ranks(self):
        return self.attributes['state_ranks']

    @state_ranks.setter
    def state_ranks(self, value):
        self.attributes['state_ranks'] = value

    @property
    def actions(self):
        return self.attributes['actions']

    @actions.setter
    def actions(self, value):
        self.attributes['actions'] = value

    @property
    def exp(self):
        return self.attributes['exp']

    @exp.setter
    def exp(self, value):
        self.attributes['exp'] = value

    @property
    def gold(self):
        return self.attributes['gold']

    @gold.setter
    def gold(self, value):
        self.attributes['gold'] = value

    @property
    def item_id(self):
        return self.attributes['item_id']

    @item_id.setter
    def item_id(self, value):
        self.attributes['item_id'] = value

    @property
    def weapon_id(self):
        return self.attributes['weapon_id']

    @weapon_id.setter
    def weapon_id(self, value):
        self.attributes['weapon_id'] = value

    @property
    def armor_id(self):
        return self.attributes['armor_id']

    @armor_id.setter
    def armor_id(self, value):
        self.attributes['armor_id'] = value

    @property
    def treasure_prob(self):
        return self.attributes['treasure_prob']

    @treasure_prob.setter
    def treasure_prob(self, value):
        self.attributes['treasure_prob'] = value

class EnemyAction(RubyObject):
    ruby_class_name = "RPG::Enemy::Action"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@element_ranks'] = Table()._load(self.attributes['@element_ranks']._private_data)
        self.attributes['@state_ranks'] = Table()._load(self.attributes['@state_ranks']._private_data)
    
    @property
    def kind(self):
        return self.attributes['kind']

    @kind.setter
    def kind(self, value):
        self.attributes['kind'] = value

    @property
    def basic(self):
        return self.attributes['basic']

    @basic.setter
    def basic(self, value):
        self.attributes['basic'] = value

    @property
    def skill_id(self):
        return self.attributes['skill_id']

    @skill_id.setter
    def skill_id(self, value):
        self.attributes['skill_id'] = value

    @property
    def condition_turn_a(self):
        return self.attributes['condition_turn_a']

    @condition_turn_a.setter
    def condition_turn_a(self, value):
        self.attributes['condition_turn_a'] = value

    @property
    def condition_turn_b(self):
        return self.attributes['condition_turn_b']

    @condition_turn_b.setter
    def condition_turn_b(self, value):
        self.attributes['condition_turn_b'] = value

    @property
    def condition_hp(self):
        return self.attributes['condition_hp']

    @condition_hp.setter
    def condition_hp(self, value):
        self.attributes['condition_hp'] = value

    @property
    def condition_level(self):
        return self.attributes['condition_level']

    @condition_level.setter
    def condition_level(self, value):
        self.attributes['condition_level'] = value

    @property
    def condition_switch_id(self):
        return self.attributes['condition_switch_id']

    @condition_switch_id.setter
    def condition_switch_id(self, value):
        self.attributes['condition_switch_id'] = value

    @property
    def rating(self):
        return self.attributes['rating']

    @rating.setter
    def rating(self, value):
        self.attributes['rating'] = value

class Troop(RubyObject):
    ruby_class_name = "RPG::Troop"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def members(self):
        return self.attributes['members']

    @members.setter
    def members(self, value):
        self.attributes['members'] = value

    @property
    def pages(self):
        return self.attributes['pages']

    @pages.setter
    def pages(self, value):
        self.attributes['pages'] = value

class TroopMember(RubyObject):
    ruby_class_name = "RPG::Troop::Member"

    @property
    def member(self):
        return self.attributes['member']

    @member.setter
    def member(self, value):
        self.attributes['member'] = value

    @property
    def x(self):
        return self.attributes['x']

    @x.setter
    def x(self, value):
        self.attributes['x'] = value

    @property
    def y(self):
        return self.attributes['y']

    @y.setter
    def y(self, value):
        self.attributes['y'] = value

    @property
    def hidden(self):
        return self.attributes['hidden']

    @hidden.setter
    def hidden(self, value):
        self.attributes['hidden'] = value

    @property
    def immortal(self):
        return self.attributes['immortal']

    @immortal.setter
    def immortal(self, value):
        self.attributes['immortal'] = value

class TroopPage(RubyObject):
    ruby_class_name = "RPG::Troop::Page"

    @property
    def condition(self):
        return self.attributes['condition']

    @condition.setter
    def condition(self, value):
        self.attributes['condition'] = value

    @property
    def page(self):
        return self.attributes['page']

    @page.setter
    def page(self, value):
        self.attributes['page'] = value

    @property
    def list(self):
        return self.attributes['list']

    @list.setter
    def list(self, value):
        self.attributes['list'] = value

class TroopPageCondition(RubyObject):
    ruby_class_name = "RPG::Troop::Page::Condition"

    @property
    def turn_valid(self):
        return self.attributes['turn_valid']

    @turn_valid.setter
    def turn_valid(self, value):
        self.attributes['turn_valid'] = value

    @property
    def enemy_valid(self):
        return self.attributes['enemy_valid']

    @enemy_valid.setter
    def enemy_valid(self, value):
        self.attributes['enemy_valid'] = value

    @property
    def actor_valid(self):
        return self.attributes['actor_valid']

    @actor_valid.setter
    def actor_valid(self, value):
        self.attributes['actor_valid'] = value

    @property
    def switch_valid(self):
        return self.attributes['switch_valid']

    @switch_valid.setter
    def switch_valid(self, value):
        self.attributes['switch_valid'] = value

    @property
    def turn_a(self):
        return self.attributes['turn_a']

    @turn_a.setter
    def turn_a(self, value):
        self.attributes['turn_a'] = value

    @property
    def turn_b(self):
        return self.attributes['turn_b']

    @turn_b.setter
    def turn_b(self, value):
        self.attributes['turn_b'] = value

    @property
    def enemy_index(self):
        return self.attributes['enemy_index']

    @enemy_index.setter
    def enemy_index(self, value):
        self.attributes['enemy_index'] = value

    @property
    def enemy_hp(self):
        return self.attributes['enemy_hp']

    @enemy_hp.setter
    def enemy_hp(self, value):
        self.attributes['enemy_hp'] = value

    @property
    def actor_id(self):
        return self.attributes['actor_id']

    @actor_id.setter
    def actor_id(self, value):
        self.attributes['actor_id'] = value

    @property
    def actor_hp(self):
        return self.attributes['actor_hp']

    @actor_hp.setter
    def actor_hp(self, value):
        self.attributes['actor_hp'] = value

    @property
    def switch_id(self):
        return self.attributes['switch_id']

    @switch_id.setter
    def switch_id(self, value):
        self.attributes['switch_id'] = value

class State(RubyObject):
    ruby_class_name = "RPG::State"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def animation_id(self):
        return self.attributes['animation_id']

    @animation_id.setter
    def animation_id(self, value):
        self.attributes['animation_id'] = value

    @property
    def restriction(self):
        return self.attributes['restriction']

    @restriction.setter
    def restriction(self, value):
        self.attributes['restriction'] = value

    @property
    def nonresistance(self):
        return self.attributes['nonresistance']

    @nonresistance.setter
    def nonresistance(self, value):
        self.attributes['nonresistance'] = value

    @property
    def zero_hp(self):
        return self.attributes['zero_hp']

    @zero_hp.setter
    def zero_hp(self, value):
        self.attributes['zero_hp'] = value

    @property
    def cant_get_exp(self):
        return self.attributes['cant_get_exp']

    @cant_get_exp.setter
    def cant_get_exp(self, value):
        self.attributes['cant_get_exp'] = value

    @property
    def cant_evade(self):
        return self.attributes['cant_evade']

    @cant_evade.setter
    def cant_evade(self, value):
        self.attributes['cant_evade'] = value

    @property
    def slip_damage(self):
        return self.attributes['slip_damage']

    @slip_damage.setter
    def slip_damage(self, value):
        self.attributes['slip_damage'] = value

    @property
    def rating(self):
        return self.attributes['rating']

    @rating.setter
    def rating(self, value):
        self.attributes['rating'] = value

    @property
    def hit_rate(self):
        return self.attributes['hit_rate']

    @hit_rate.setter
    def hit_rate(self, value):
        self.attributes['hit_rate'] = value

    @property
    def maxhp_rate(self):
        return self.attributes['maxhp_rate']

    @maxhp_rate.setter
    def maxhp_rate(self, value):
        self.attributes['maxhp_rate'] = value

    @property
    def maxsp_rate(self):
        return self.attributes['maxsp_rate']

    @maxsp_rate.setter
    def maxsp_rate(self, value):
        self.attributes['maxsp_rate'] = value

    @property
    def str_rate(self):
        return self.attributes['str_rate']

    @str_rate.setter
    def str_rate(self, value):
        self.attributes['str_rate'] = value

    @property
    def dex_rate(self):
        return self.attributes['dex_rate']

    @dex_rate.setter
    def dex_rate(self, value):
        self.attributes['dex_rate'] = value

    @property
    def agi_rate(self):
        return self.attributes['agi_rate']

    @agi_rate.setter
    def agi_rate(self, value):
        self.attributes['agi_rate'] = value

    @property
    def int_rate(self):
        return self.attributes['int_rate']

    @int_rate.setter
    def int_rate(self, value):
        self.attributes['int_rate'] = value

    @property
    def atk_rate(self):
        return self.attributes['atk_rate']

    @atk_rate.setter
    def atk_rate(self, value):
        self.attributes['atk_rate'] = value

    @property
    def pdef_rate(self):
        return self.attributes['pdef_rate']

    @pdef_rate.setter
    def pdef_rate(self, value):
        self.attributes['pdef_rate'] = value

    @property
    def mdef_rate(self):
        return self.attributes['mdef_rate']

    @mdef_rate.setter
    def mdef_rate(self, value):
        self.attributes['mdef_rate'] = value

    @property
    def eva(self):
        return self.attributes['eva']

    @eva.setter
    def eva(self, value):
        self.attributes['eva'] = value

    @property
    def battle_only(self):
        return self.attributes['battle_only']

    @battle_only.setter
    def battle_only(self, value):
        self.attributes['battle_only'] = value

    @property
    def hold_turn(self):
        return self.attributes['hold_turn']

    @hold_turn.setter
    def hold_turn(self, value):
        self.attributes['hold_turn'] = value

    @property
    def auto_release_prob(self):
        return self.attributes['auto_release_prob']

    @auto_release_prob.setter
    def auto_release_prob(self, value):
        self.attributes['auto_release_prob'] = value

    @property
    def shock_release_prob(self):
        return self.attributes['shock_release_prob']

    @shock_release_prob.setter
    def shock_release_prob(self, value):
        self.attributes['shock_release_prob'] = value

    @property
    def guard_element_set(self):
        return self.attributes['guard_element_set']

    @guard_element_set.setter
    def guard_element_set(self, value):
        self.attributes['guard_element_set'] = value

    @property
    def plus_state_set(self):
        return self.attributes['plus_state_set']

    @plus_state_set.setter
    def plus_state_set(self, value):
        self.attributes['plus_state_set'] = value

    @property
    def minus_state_set(self):
        return self.attributes['minus_state_set']

    @minus_state_set.setter
    def minus_state_set(self, value):
        self.attributes['minus_state_set'] = value

class Animation(RubyObject):
    ruby_class_name = "RPG::Animation"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def animation_name(self):
        return self.attributes['animation_name']

    @animation_name.setter
    def animation_name(self, value):
        self.attributes['animation_name'] = value

    @property
    def animation_hue(self):
        return self.attributes['animation_hue']

    @animation_hue.setter
    def animation_hue(self, value):
        self.attributes['animation_hue'] = value

    @property
    def position(self):
        return self.attributes['position']

    @position.setter
    def position(self, value):
        self.attributes['position'] = value

    @property
    def frame_max(self):
        return self.attributes['frame_max']

    @frame_max.setter
    def frame_max(self, value):
        self.attributes['frame_max'] = value

    @property
    def frames(self):
        return self.attributes['frames']

    @frames.setter
    def frames(self, value):
        self.attributes['frames'] = value

    @property
    def timings(self):
        return self.attributes['timings']

    @timings.setter
    def timings(self, value):
        self.attributes['timings'] = value

class AnimationFrame(RubyObject):
    ruby_class_name = "RPG::Animation::Frame"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@cell_data'] = Table()._load(self.attributes['@cell_data']._private_data)

    @property
    def cell_max(self):
        return self.attributes['cell_max']

    @cell_max.setter
    def cell_max(self, value):
        self.attributes['cell_max'] = value

    @property
    def cell_data(self):
        return self.attributes['cell_data']

    @cell_data.setter
    def cell_data(self, value):
        self.attributes['cell_data'] = value

class AnimationTiming(RubyObject):
    ruby_class_name = "RPG::Animation::Timing"

    @property
    def frame(self):
        return self.attributes['frame']

    @frame.setter
    def frame(self, value):
        self.attributes['frame'] = value

    @property
    def se(self):
        return self.attributes['se']

    @se.setter
    def se(self, value):
        self.attributes['se'] = value

    @property
    def flash_scope(self):
        return self.attributes['flash_scope']

    @flash_scope.setter
    def flash_scope(self, value):
        self.attributes['flash_scope'] = value

    @property
    def flash_color(self):
        return self.attributes['flash_color']

    @flash_color.setter
    def flash_color(self, value):
        self.attributes['flash_color'] = value

    @property
    def flash_duration(self):
        return self.attributes['flash_duration']

    @flash_duration.setter
    def flash_duration(self, value):
        self.attributes['flash_duration'] = value

    @property
    def condition(self):
        return self.attributes['condition']

    @condition.setter
    def condition(self, value):
        self.attributes['condition'] = value

class CommonEvent(RubyObject):
    ruby_class_name = "RPG::CommonEvent"

    @property
    def id(self):
        return self.attributes['id']

    @id.setter
    def id(self, value):
        self.attributes['id'] = value

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        self.attributes['name'] = value

    @property
    def trigger(self):
        return self.attributes['trigger']

    @trigger.setter
    def trigger(self, value):
        self.attributes['trigger'] = value

    @property
    def switch_id(self):
        return self.attributes['switch_id']

    @switch_id.setter
    def switch_id(self, value):
        self.attributes['switch_id'] = value

    @property
    def list(self):
        return self.attributes['list']

    @list.setter
    def list(self, value):
        self.attributes['list'] = value

class System(RubyObject):
    ruby_class_name = "RPG::System"

    @property
    def magic_number(self):
        return self.attributes['magic_number']

    @magic_number.setter
    def magic_number(self, value):
        self.attributes['magic_number'] = value

    @property
    def party_members(self):
        return self.attributes['party_members']

    @party_members.setter
    def party_members(self, value):
        self.attributes['party_members'] = value

    @property
    def elements(self):
        return self.attributes['elements']

    @elements.setter
    def elements(self, value):
        self.attributes['elements'] = value

    @property
    def switches(self):
        return self.attributes['switches']

    @switches.setter
    def switches(self, value):
        self.attributes['switches'] = value

    @property
    def variables(self):
        return self.attributes['variables']

    @variables.setter
    def variables(self, value):
        self.attributes['variables'] = value

    @property
    def windowskin_name(self):
        return self.attributes['windowskin_name']

    @windowskin_name.setter
    def windowskin_name(self, value):
        self.attributes['windowskin_name'] = value

    @property
    def title_name(self):
        return self.attributes['title_name']

    @title_name.setter
    def title_name(self, value):
        self.attributes['title_name'] = value

    @property
    def gameover_name(self):
        return self.attributes['gameover_name']

    @gameover_name.setter
    def gameover_name(self, value):
        self.attributes['gameover_name'] = value

    @property
    def battle_transition(self):
        return self.attributes['battle_transition']

    @battle_transition.setter
    def battle_transition(self, value):
        self.attributes['battle_transition'] = value

    @property
    def title_bgm(self):
        return self.attributes['title_bgm']

    @title_bgm.setter
    def title_bgm(self, value):
        self.attributes['title_bgm'] = value

    @property
    def battle_bgm(self):
        return self.attributes['battle_bgm']

    @battle_bgm.setter
    def battle_bgm(self, value):
        self.attributes['battle_bgm'] = value

    @property
    def battle_end_me(self):
        return self.attributes['battle_end_me']

    @battle_end_me.setter
    def battle_end_me(self, value):
        self.attributes['battle_end_me'] = value

    @property
    def gameover_me(self):
        return self.attributes['gameover_me']

    @gameover_me.setter
    def gameover_me(self, value):
        self.attributes['gameover_me'] = value

    @property
    def cursor_se(self):
        return self.attributes['cursor_se']

    @cursor_se.setter
    def cursor_se(self, value):
        self.attributes['cursor_se'] = value

    @property
    def decision_se(self):
        return self.attributes['decision_se']

    @decision_se.setter
    def decision_se(self, value):
        self.attributes['decision_se'] = value

    @property
    def cancel_se(self):
        return self.attributes['cancel_se']

    @cancel_se.setter
    def cancel_se(self, value):
        self.attributes['cancel_se'] = value

    @property
    def buzzer_se(self):
        return self.attributes['buzzer_se']

    @buzzer_se.setter
    def buzzer_se(self, value):
        self.attributes['buzzer_se'] = value

    @property
    def equip_se(self):
        return self.attributes['equip_se']

    @equip_se.setter
    def equip_se(self, value):
        self.attributes['equip_se'] = value

    @property
    def shop_se(self):
        return self.attributes['shop_se']

    @shop_se.setter
    def shop_se(self, value):
        self.attributes['shop_se'] = value

    @property
    def save_se(self):
        return self.attributes['save_se']

    @save_se.setter
    def save_se(self, value):
        self.attributes['save_se'] = value

    @property
    def load_se(self):
        return self.attributes['load_se']

    @load_se.setter
    def load_se(self, value):
        self.attributes['load_se'] = value

    @property
    def battle_start_se(self):
        return self.attributes['battle_start_se']

    @battle_start_se.setter
    def battle_start_se(self, value):
        self.attributes['battle_start_se'] = value

    @property
    def escape_se(self):
        return self.attributes['escape_se']

    @escape_se.setter
    def escape_se(self, value):
        self.attributes['escape_se'] = value

    @property
    def actor_collapse_se(self):
        return self.attributes['actor_collapse_se']

    @actor_collapse_se.setter
    def actor_collapse_se(self, value):
        self.attributes['actor_collapse_se'] = value

    @property
    def enemy_collapse_se(self):
        return self.attributes['enemy_collapse_se']

    @enemy_collapse_se.setter
    def enemy_collapse_se(self, value):
        self.attributes['enemy_collapse_se'] = value

    @property
    def words(self):
        return self.attributes['words']

    @words.setter
    def words(self, value):
        self.attributes['words'] = value

    @property
    def test_battlers(self):
        return self.attributes['test_battlers']

    @test_battlers.setter
    def test_battlers(self, value):
        self.attributes['test_battlers'] = value

    @property
    def test_troop_id(self):
        return self.attributes['test_troop_id']

    @test_troop_id.setter
    def test_troop_id(self, value):
        self.attributes['test_troop_id'] = value

    @property
    def start_map_id(self):
        return self.attributes['start_map_id']

    @start_map_id.setter
    def start_map_id(self, value):
        self.attributes['start_map_id'] = value

    @property
    def start_x(self):
        return self.attributes['start_x']

    @start_x.setter
    def start_x(self, value):
        self.attributes['start_x'] = value

    @property
    def start_y(self):
        return self.attributes['start_y']

    @start_y.setter
    def start_y(self, value):
        self.attributes['start_y'] = value

    @property
    def battleback_name(self):
        return self.attributes['battleback_name']

    @battleback_name.setter
    def battleback_name(self, value):
        self.attributes['battleback_name'] = value

    @property
    def battler_name(self):
        return self.attributes['battler_name']

    @battler_name.setter
    def battler_name(self, value):
        self.attributes['battler_name'] = value

    @property
    def battler_hue(self):
        return self.attributes['battler_hue']

    @battler_hue.setter
    def battler_hue(self, value):
        self.attributes['battler_hue'] = value

    @property
    def edit_map_id(self):
        return self.attributes['edit_map_id']

    @edit_map_id.setter
    def edit_map_id(self, value):
        self.attributes['edit_map_id'] = value

class SystemWords(RubyObject):
    ruby_class_name = "RPG::System::Words"

    @property
    def gold(self):
        return self.attributes['gold']

    @gold.setter
    def gold(self, value):
        self.attributes['gold'] = value

    @property
    def hp(self):
        return self.attributes['hp']

    @hp.setter
    def hp(self, value):
        self.attributes['hp'] = value

    @property
    def sp(self):
        return self.attributes['sp']

    @sp.setter
    def sp(self, value):
        self.attributes['sp'] = value

    @property
    def str(self):
        return self.attributes['str']

    @str.setter
    def str(self, value):
        self.attributes['str'] = value

    @property
    def dex(self):
        return self.attributes['dex']

    @dex.setter
    def dex(self, value):
        self.attributes['dex'] = value

    @property
    def agi(self):
        return self.attributes['agi']

    @agi.setter
    def agi(self, value):
        self.attributes['agi'] = value

    @property
    def int(self):
        return self.attributes['int']

    @int.setter
    def int(self, value):
        self.attributes['int'] = value

    @property
    def atk(self):
        return self.attributes['atk']

    @atk.setter
    def atk(self, value):
        self.attributes['atk'] = value

    @property
    def pdef(self):
        return self.attributes['pdef']

    @pdef.setter
    def pdef(self, value):
        self.attributes['pdef'] = value

    @property
    def mdef(self):
        return self.attributes['mdef']

    @mdef.setter
    def mdef(self, value):
        self.attributes['mdef'] = value

    @property
    def weapon(self):
        return self.attributes['weapon']

    @weapon.setter
    def weapon(self, value):
        self.attributes['weapon'] = value

    @property
    def armor1(self):
        return self.attributes['armor1']

    @armor1.setter
    def armor1(self, value):
        self.attributes['armor1'] = value

    @property
    def armor2(self):
        return self.attributes['armor2']

    @armor2.setter
    def armor2(self, value):
        self.attributes['armor2'] = value

    @property
    def armor3(self):
        return self.attributes['armor3']

    @armor3.setter
    def armor3(self, value):
        self.attributes['armor3'] = value

    @property
    def armor4(self):
        return self.attributes['armor4']

    @armor4.setter
    def armor4(self, value):
        self.attributes['armor4'] = value

    @property
    def attack(self):
        return self.attributes['attack']

    @attack.setter
    def attack(self, value):
        self.attributes['attack'] = value

    @property
    def skill(self):
        return self.attributes['skill']

    @skill.setter
    def skill(self, value):
        self.attributes['skill'] = value

    @property
    def guard(self):
        return self.attributes['guard']

    @guard.setter
    def guard(self, value):
        self.attributes['guard'] = value

    @property
    def item(self):
        return self.attributes['item']

    @item.setter
    def item(self, value):
        self.attributes['item'] = value

    @property
    def equip(self):
        return self.attributes['equip']

    @equip.setter
    def equip(self, value):
        self.attributes['equip'] = value

class SystemTestBattler(RubyObject):
    ruby_class_name = "RPG::System::TestBattler"

    @property
    def actor_id(self):
        return self.attributes['actor_id']

    @actor_id.setter
    def actor_id(self, value):
        self.attributes['actor_id'] = value

    @property
    def level(self):
        return self.attributes['level']

    @level.setter
    def level(self, value):
        self.attributes['level'] = value

    @property
    def weapon_id(self):
        return self.attributes['weapon_id']

    @weapon_id.setter
    def weapon_id(self, value):
        self.attributes['weapon_id'] = value

    @property
    def armor1_id(self):
        return self.attributes['armor1_id']

    @armor1_id.setter
    def armor1_id(self, value):
        self.attributes['armor1_id'] = value

    @property
    def armor2_id(self):
        return self.attributes['armor2_id']

    @armor2_id.setter
    def armor2_id(self, value):
        self.attributes['armor2_id'] = value

    @property
    def armor3_id(self):
        return self.attributes['armor3_id']

    @armor3_id.setter
    def armor3_id(self, value):
        self.attributes['armor3_id'] = value

    @property
    def armor4_id(self):
        return self.attributes['armor4_id']

    @armor4_id.setter
    def armor4_id(self, value):
        self.attributes['armor4_id'] = value

# Load all classes into registry
# Python moment
def load_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if issubclass(obj, RubyObject):
                #print(obj)
                registry.register(obj)