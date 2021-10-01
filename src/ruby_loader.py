from rubymarshal.reader import loads, load
from rubymarshal.writer import writes, write
from rubymarshal.classes import RubyObject
import classes
classes.load_classes()

class DataLoader():

    def load_data(self, filename: str):
        with open(filename, 'rb') as tset:
            content = load(tset)
        return content

    # Define different RXDATA loaders
    def map(self, id = 1):
        rjust_id = str(id).rjust(3, "0")
        map = self.load_data(f"Data/Map{rjust_id}.rxdata")
        return map
    
    def tileset(self, id = 1):
        tilesets = self.load_data("Data/Tilesets.rxdata")
        return tilesets[id]

    def commonevent(self, id = 1):
        commonevents = self.load_data("Data/CommonEvents.rxdata")
        return commonevents[id]
    
    def actor(self, id = 1):
        actors = self.load_data("Data/Actors.rxdata")
        return actors[id]
    
    def item(self, id = 1):
        items = self.load_data("Data/Items.rxdata")
        return items[id]
    
    def armor(self, id = 1):
        armors = self.load_data("Data/Armors.rxdata")
        return armors[id]
    
    def animation(self, id = 1):
        animations = self.load_data("Data/Animations.rxdata")
        return animations[id]
    
    def rpgclass(self, id = 1):
        classes = self.load_data("Data/Classes.rxdata")
        return classes[id]
    
    def enemy(self, id = 1):
        enemies = self.load_data("Data/Enemies.rxdata")
        return enemies[id]
    
    def skill(self, id = 1):
        skills = self.load_data("Data/Skills.rxdata")
        return skills[id]
    
    def state(self, id = 1):
        states = self.load_data("Data/States.rxdata")
        return states[id]
    
    def system(self):
        system = self.load_data("Data/System.rxdata")
        return system
    
    def troop(self, id = 1):
        troops = self.load_data("Data/Troops.rxdata")
        return troops[id]
    
    def weapon(self, id = 1):
        weapons = self.load_data("Data/Weapons.rxdata")
        return weapons[id]

class DataWriter():

    def write_data(self, filename: str, data):
        with open(filename, 'wb') as tset:
            contents = writes(data)
            tset.write(contents)