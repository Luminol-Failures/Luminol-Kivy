import json

class Config():
    def __init__(self):
        self.load_config()
        pass

    def load_config(self):
        with open("config.json") as f:
            self.data = json.load(f)

    def code_config(self, code):
        for key in self.data["special_commands"]:
            value  = self.data["special_commands"][key]
            for value in value:
                if (code == value[0]):
                    return [True, key, value[1]]
        return [False]
    
    #? Code config returns an array of values
    #* [0: Is code special?, 1: code special type, 2: special type position]
    #* This doesn't work with say arrays of special types, or multiple, but eh it works