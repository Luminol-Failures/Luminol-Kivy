from src.ruby_loader import DataLoader
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel

class MapList(TreeView):
    def __init__(self, **kwargs):
        super(MapList, self).__init__(**kwargs)

        self.mapinfos = DataLoader().load_data('Data/MapInfos.rxdata')
        self.mapinfos_sorted = {}
        self.nodes = {}
        self.order_mapinfos()
        self.load_mapinfos()
        self.root_options = {'text': 'Maps'}

        self.size_hint_y = None
        self.bind(on_node_expand = self.set_height, on_node_collapse = self.set_height)
        

    def order_mapinfos(self):
        self.mapsinfos_sorted = {}
        ord = 1
        while True:
            for key, value in self.mapinfos.items():
                if value.order == ord:
                    ord += 1
                    self.mapinfos_sorted[key] = value
            if len(self.mapinfos_sorted) + 1 == len(self.mapinfos):
                break
    
    def load_mapinfos(self):
        self.nodes = {}
        for key, value in self.mapinfos_sorted.items():
            if type(value.name) == bytes:
                self.nodes[int(key)] = TreeViewLabel(text=value.name.decode())
            else:
                self.nodes[int(key)] = TreeViewLabel(text=value.name.text)

        for key, value in self.mapinfos_sorted.items():
            if value.parent_id == 0:
                self.add_node(self.nodes[key])
            else:
                self.add_node(self.nodes[key], self.nodes[value.parent_id])
            
            if value.expanded:
                self.toggle_node(self.nodes[key])
        self.select_node(self.nodes[list(self.mapinfos_sorted.keys())[0]])
        self.set_height()
    
    def set_height(self, *args):
        self.height = 28
        for node in self.iterate_open_nodes():
            self.height += 28
        
    def get_selected_map(self):
        selected_node = self.selected_node
        for key, value in self.nodes.items():
            if value == selected_node:
                return key
        return 1
