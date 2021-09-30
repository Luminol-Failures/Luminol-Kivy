from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write
from rubymarshal.classes import RubyObject

from classes import Tileset
from classes import Map

class DataLoader():

    def load_data(self, filename):
        with open(filename, 'rb') as tset:
            content = load(tset)
        return content
    
    def tileset_names(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id].name
    
    def tileset_passages(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id].passages
    
    def tileset_priorities(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id].priorites

    def tileset_tags(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id].terrain_tags

    def map_bgm(self, id = 1):
        rjust_id = str(id).rjust(3, "0")
        map = self.load_data(f"Data/Map{rjust_id}.rxdata")
        return map.bgm
    
    def map_data(self, id = 1):
        rjust_id = str(id).rjust(3, "0")
        map = self.load_data(f"Data/Map{rjust_id}.rxdata")
        return map.data

print(DataLoader().map_data(1).xyz(1, 1, 0))