from kivy.uix.splitter import Splitter
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.uix.boxlayout import BoxLayout

from src.mapinfo import MapList
from src.tilepicker import TilePicker

class LeftLayout(Splitter):
    def __init__(self, root, **kwargs):
        super(LeftLayout, self).__init__(**kwargs)

        self.root = root

        self.sizable_from = 'right'
        self.min_size = 15
        self.max_size = 270

        self.layout = BoxLayout(orientation ='vertical')
        self.add_widget(self.layout)
        
        self.maplist = MapList()
        self.maplist.bind(on_touch_up=self.root.on_map_select)

        maplist_scroller = ScrollView(scroll_type = ['bars', 'content'], bar_width = 10)
        maplist_scroller.add_widget(self.maplist)

        maplist_splitter = Splitter(sizable_from = 'top')
        maplist_splitter.add_widget(maplist_scroller)

        maplist_splitter.add_widget(maplist_scroller)

        mappicker_scroller = ScrollView(scroll_type = ['bars', 'content'], bar_width = 10, effect_cls = ScrollEffect)

        self.tilepicker = TilePicker(self.root.map_id)
        mappicker_scroller.add_widget(self.tilepicker)

        self.layout.add_widget(mappicker_scroller)
        self.layout.add_widget(maplist_splitter)