from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from  kivy.uix.button import Button


class SmallTextInput(TextInput):
    def __init__(self, **kwargs):
        super(SmallTextInput, self).__init__(**kwargs)
        self.size_hint = (.2, None)
        self.height = 28
        self.multiline = False


class BigTextInput(TextInput):
    def __init__(self, **kwargs):
        super(BigTextInput, self).__init__(**kwargs)
        self.size_hint = (.8, None)
        self.height = 112
        self.multiline = True


class SmallLabel(Label):
    def __init__(self, **kwargs):
        super(SmallLabel, self).__init__(**kwargs)
        self.size_hint = (.2, None)
        self.height = 28


class BigLabel(Label):
    def __init__(self, **kwargs):
        super(BigLabel, self).__init__(**kwargs)
        self.size_hint = (.2, None)
        self.height = 112


class PrimaryButton(Button):
    def __init__(self, **kwargs):
        super(PrimaryButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [90/255, 190/255, 90/255, 1]


class SubmitButton(Button):
    def __init__(self, **kwargs):
        super(SubmitButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [3/255, 182/255, 252/255, 1]


class DeleteButton(Button):
    def __init__(self, **kwargs):
        super(DeleteButton, self).__init__(**kwargs)
        self.background_normal = ''
        self.background_color = [255/255, 0/255, 0/255, 1]
