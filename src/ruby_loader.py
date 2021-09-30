from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write
from rubymarshal.classes import RubyObject

from classes import Tileset

class DataLoader():

    def load_data(self, filename):
        with open(filename, 'rb') as tset:
            content = load(tset)
        return content
    
    def tileset_names(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return Tileset(tilesets[id]).tileset_name
    
    def tileset_passages(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return Tileset(tilesets[id]).passages
    
    def tileset_priorities(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return Tileset(tilesets[id]).priorites

    def tileset_tags(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return Tileset(tilesets[id]).terrain_tags

print(DataLoader().tileset_priorities(2))