from kivy.uix.screenmanager import ScreenManager, Screen
from kivi_custom.popup_box import PopupBox as Popup
from kivy.app import StringProperty

from database.realtime_handler import Handler
from database.account import Account


class WindowManager(ScreenManager):
    admin = StringProperty('')
    account = Account()
    pass


# Main menu
class MainMenu(Screen):
    text = StringProperty('')

    def updateText(self, text):
        self.text = text

    def changeScreen(self, screen):
        self.manager.current = screen

    def logout(self):
        self.text = ''
        self.manager.admin = ''
        self.manager.account.user = None

    pass


# Account
class Authorization(Screen):

    def submitLogin(self):
        if self.manager.account.login(self.loginEmail.text, self.loginPassword.text):

            if self.loginEmail.text == "admin@admin.com":
                self.manager.admin = 'True'

            menu_screen = self.manager.get_screen('Main')
            menu_screen.updateText(self.manager.account.getUsername())
            return True
        else:
            return False

    def submitRegister(self):
        if self.manager.account.register(self.registerEmail.text,
                                         self.registerPassword.text,
                                         self.registerPasswordConfirm.text):
            return True
        else:
            return False

    pass


# Admin panel
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
            Popup.display_error('Please fill all of the blank spots')

        elif (len(self.primaryStatistics.text) != 16 or
              len(self.secondaryStatistics.text) != 16 or
              len(self.wRoll.text) != 8 or
              len(self.fpRoll.text) != 3):
            Popup.display_error('Wrong format in one of the boxes')

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
            Popup.display_error('Please fill all of the blank spots')

        elif (len(self.primaryStatistics.text) != 16 or
              len(self.secondaryStatistics.text) != 16):
            Popup.display_error('Wrong format in one of the boxes')

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

            Popup.display_error('Please fill all of the blank spots')

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

            Popup.display_error('Please fill all of the blank spots')

        else:
            data = {'name': self.nameOfStarSign.text,
                    'description': self.description.text}
            Handler.push_data(data, 'StarSigns')
            self.clearInputBoxes()

    pass
