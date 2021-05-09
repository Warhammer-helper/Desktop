from kivy.app import App
from kivy.lang import Builder
from kivi_custom import widgets
from kivi_custom import screen_manager

from kivy.core.window import Window
from kivy.config import Config

kv_layout = Builder.load_file('main.kv')


class MyApp(App):

    def build(self):
        Window.size = (960, 540)
        Window.minimum_width = 960
        Window.minimum_height = 540
        Config.set('graphics', 'resizable', False)
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        return kv_layout


if __name__ == '__main__':
    MyApp().run()
