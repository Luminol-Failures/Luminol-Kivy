import rubymarshal
import classes
from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write
from rubymarshal.classes import RubyObject

class DataLoader():

    def load_data(self, filename):
        with open(filename, 'rb') as tset:
            content = load(tset)
        return content

    def map(self, id = 1):
        rjust_id = str(id).rjust(3, "0")
        map = self.load_data(f"Data/Map{rjust_id}.rxdata")
        return map
    
    def tileset(self, id):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id]

from classes import Event
loader = DataLoader()
map = Event()
print(map)