import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from src.tilemap import TileMap
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class EditorLayout(GridLayout):

    def __init__(self, **kwargs):
        super(EditorLayout, self).__init__(**kwargs)

        self.cols = 1
        t = TileMap()
        root = ScrollView(size_hint=(None, None), size=(Window.width, Window.height))
        root.add_widget(t)
        self.add_widget(root)

class LuminolApp(App):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def build(self):
            return EditorLayout()

if __name__ == '__main__':
    LuminolApp().run()