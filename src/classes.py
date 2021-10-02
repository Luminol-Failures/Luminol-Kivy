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

    #attr_accessor :id
    #attr_accessor :name
    #attr_accessor :position
    #attr_accessor :weapon_set
    #attr_accessor :armor_set
    #attr_accessor :element_ranks
    #attr_accessor :state_ranks
    #attr_accessor :learnings

class Learning(RubyObject):
    ruby_class_name = "RPG::Class::Learning"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@element_ranks'] = Table()._load(self.attributes['@element_ranks']._private_data)
        self.attributes['@state_ranks'] = Table()._load(self.attributes['@state_ranks']._private_data)

class Skill(RubyObject):
    ruby_class_name = "RPG::Skill"

class Item(RubyObject):
    ruby_class_name = "RPG::Item"

class Weapon(RubyObject):
    ruby_class_name = "RPG::Weapon"

class Armor(RubyObject):
    ruby_class_name = "RPG::Armor"

class Enemy(RubyObject):
    ruby_class_name = "RPG::Enemy"

class EnemyAction(RubyObject):
    ruby_class_name = "RPG::Enemy::Action"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@element_ranks'] = Table()._load(self.attributes['@element_ranks']._private_data)
        self.attributes['@state_ranks'] = Table()._load(self.attributes['@state_ranks']._private_data)

class Troop(RubyObject):
    ruby_class_name = "RPG::Troop"

class TroopMember(RubyObject):
    ruby_class_name = "RPG::Troop::Member"

class TroopPage(RubyObject):
    ruby_class_name = "RPG::Troop::Page"

class TroopPageCondition(RubyObject):
    ruby_class_name = "RPG::Troop::Page::Condition"

class State(RubyObject):
    ruby_class_name = "RPG::State"

class Animation(RubyObject):
    ruby_class_name = "RPG::Animation"

class AnimationFrame(RubyObject):
    ruby_class_name = "RPG::Animation::Frame"
    def __init__(self, ruby_class_name=None, attributes=None):
        super().__init__(ruby_class_name=ruby_class_name, attributes=attributes)
        self.attributes['@cell_data'] = Table()._load(self.attributes['@cell_data']._private_data)

class AnimationTiming(RubyObject):
    ruby_class_name = "RPG::Animation::Timing"

class CommonEvent(RubyObject):
    ruby_class_name = "RPG::CommonEvent"

class System(RubyObject):
    ruby_class_name = "RPG::System"

class SystemWords(RubyObject):
    ruby_class_name = "RPG::System::Words"

class SystemTestBattler(RubyObject):
    ruby_class_name = "RPG::System::TestBattler"

# Load all classes into registry
# Python moment
def load_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            if issubclass(obj, RubyObject):
                #print(obj)
                registry.register(obj)