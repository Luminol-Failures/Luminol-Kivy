import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from src.tilemap import TileMap
from kivy.uix.scrollview import ScrollView
from kivy.effects.scroll import ScrollEffect
from kivy.core.window import Window


class EditorLayout(GridLayout):

    def __init__(self, **kwargs):
        super(EditorLayout, self).__init__(**kwargs)

        self.cols = 1
        self.root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))
        self.root.bar_width = 5

        self.tilemap = TileMap()

        self.root.add_widget(self.tilemap)

        self.add_widget(self.root)
    
    def resize(self, *args):
        self.root.size = (Window.width, Window.height)

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.layout = EditorLayout()

        def build(self):
            Window.bind(on_resize=self.layout.resize)
            return self.layout

if __name__ == '__main__':
    LuminolApp().run()