from kivy.uix.screenmanager import ScreenManager, Screen
from database.realtime_handler import Handler


class DatabaseManager(Screen):
    pass


class CreateRace(Screen):

    def clearInputBoxes(self):
        self.nameOfRace.text = ""
        self.description.text = ""
        self.primaryStatistics.text = ""
        self.secondaryStatistics.text = ""
        self.wRoll.text = ""
        self.fpRoll.text = ""

    def press(self):

        if (self.nameOfRace.text == "" or
                self.description.text == "" or
                self.primaryStatistics.text == "" or
                self.secondaryStatistics.text == "" or
                self.fpRoll.text == "" or
                self.wRoll.text == ""):
            print('Please fill all of the blank spots')

        elif (len(self.primaryStatistics.text) != 16 or
              len(self.secondaryStatistics.text) != 16 or
              len(self.wRoll.text) != 8 or
              len(self.fpRoll.text) != 3):
            print('Wrong format in one of the boxes')

        else:
            data = {'name': self.nameOfRace.text,
                    'description': self.description.text,
                    'primaryStatistics': self.primaryStatistics.text,
                    'secondaryStatistics': self.secondaryStatistics.text,
                    'wRoll': self.wRoll.text,
                    'fpRoll': self.fpRoll.text}
            Handler.push_data(data, 'Races')
            self.clearInputBoxes()

    pass


class CreateProfession(Screen):

    def clearInputBoxes(self):
        self.nameOfProfession.text = ""
        self.description.text = ""
        self.availableFor.text = ""
        self.primaryStatistics.text = ""
        self.secondaryStatistics.text = ""
        self.equipment.text = ""
        self.weapon.text = ""
        self.armor.text = ""

    def press(self):

        if (self.nameOfProfession.text == "" or
                self.description.text == "" or
                self.availableFor.text == "" or
                self.primaryStatistics.text == "" or
                self.secondaryStatistics.text == "" or
                self.equipment.text == "" or
                self.weapon.text == "" or
                self.armor.text == ""):
            print('Please fill all of the blank spots')

        elif (len(self.primaryStatistics.text) != 16 or
              len(self.secondaryStatistics.text) != 16):
            print('Wrong format in one of the boxes')

        else:
            data = {'name': self.nameOfProfession.text,
                    'description': self.description.text,
                    'availableFor': self.availableFor.text,
                    'primaryStatistics': self.primaryStatistics.text,
                    'secondaryStatistics': self.secondaryStatistics.text,
                    'equipment': self.equipment.text,
                    'weapon': self.weapon.text,
                    'armor': self.armor.text}
            Handler.push_data(data, 'Professions')
            self.clearInputBoxes()

    pass


class CreateSex(Screen):
    def clearInputBoxes(self):
        self.nameOfSex.text = ""

    def press(self):

        if self.nameOfSex.text == "":

            print('Please fill all of the blank spots')

        else:
            data = {'name': self.nameOfSex.text}
            Handler.push_data(data, 'Sex')
            self.clearInputBoxes()

    pass


class CreateStarSign(Screen):
    def clearInputBoxes(self):
        self.nameOfStarSign.text = ""
        self.description.text = ""

    def press(self):

        if (self.nameOfStarSign.text == "" or
                self.description.text == ""):

            print('Please fill all of the blank spots')

        else:
            data = {'name': self.nameOfStarSign.text,
                    'description': self.description.text}
            Handler.push_data(data, 'StarSigns')
            self.clearInputBoxes()

    pass


class WindowManager(ScreenManager):
    pass
