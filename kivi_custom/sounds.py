from kivy.core.audio import SoundLoader

class Sounds:

    @staticmethod
    def playSingle(source):
        sound = SoundLoader.load(source)
        sound.play()

