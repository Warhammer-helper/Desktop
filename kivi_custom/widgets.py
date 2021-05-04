from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


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
