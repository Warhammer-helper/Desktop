from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import StringProperty


class PopupBox(Label):
    textContent = StringProperty("")

    def display_error(text: str):
        show = PopupBox()
        show.textContent = text
        popup = Popup(title='Error',
                      content=show,
                      size_hint=(0.3, 0.3),
                      pos_hint={'x': 0.35, 'y': 0.6},
                      separator_color=[139 / 255, 0 / 255, 0 / 255, 1],
                      auto_dismiss=True)
        popup.open()

    def display_info(text: str):
        show = PopupBox()
        show.textContent = text
        popup = Popup(title='Information',
                      content=show,
                      size_hint=(0.3, 0.3),
                      pos_hint={'x': 0.35, 'y': 0.6},
                      separator_color=(90 / 255, 190 / 255, 90 / 255, 1),
                      auto_dismiss=True)
        popup.open()
