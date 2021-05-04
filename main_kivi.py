from kivy.app import App
from kivy.lang import Builder
from kivi_custom import widgets
from kivi_custom import screen_manager


kv_layout = Builder.load_file('main.kv')


class MyApp(App):
    def build(self):
        return kv_layout


if __name__ == '__main__':
    MyApp().run()
