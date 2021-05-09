from kivy.app import App
from kivy.lang import Builder
from kivi_custom import widgets
from kivi_custom import screen_manager

from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.modules import inspector


kv_layout = Builder.load_file('main.kv')


class MyApp(App):
    def build(self):
        button = Button(text="Test")
        inspector.create_inspector(Window, button)
        return kv_layout


if __name__ == '__main__':
    MyApp().run()
