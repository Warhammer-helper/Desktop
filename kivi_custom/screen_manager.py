from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner

from kivi_custom.popup_box import PopupBox as Popup
from kivi_custom.widgets import *
from kivi_custom.widgets_creator import WidgetsCreator

from kivy.app import StringProperty
from kivy.properties import NumericProperty

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


# Character creation
class CharacterCreatePrimary(Screen):

    def form(self):
        form = [self.nameOfCharacter, self.age, self.weight, self.eyeColour, self.hairColour, self.race, self.origin,
                self.sex, self.starSign]
        return form

    def press(self):
        if self.filledCorrectly():
            self.manager.transition.direction = "left"
            self.manager.current = "CharacterCreateRoll"

    def filledCorrectly(self):
        for entity in self.form():
            if entity.text == '' \
                    or entity.text == 'Gender' \
                    or entity.text == 'Race' \
                    or entity.text == 'Star sign':
                Popup.display_info("Please fill all input boxes")
                return False
            else:
                pass
        return True

    def setDropdowns(self):
        sex = Handler.get_data("Sex")
        starSigns = Handler.get_data("Starsigns")
        races = Handler.get_data("Races")

        for entity in sex:
            self.sex.values.append(entity["name"])
        for entity in starSigns:
            self.starSign.values.append(entity["name"])
        for entity in races:
            self.race.values.append(entity["name"])

    pass


class CharacterCreateRoll(Screen):

    primary_statistics = ""
    secondary_statistics = ""

    def press(self):
        self.manager.transition.direction = "left"
        self.manager.current = "CharacterCreateProfession"

    def clearBoxes(self):
        WidgetsCreator.clearStatisticsWidget(self.primaryStatistics,
                                            self.secondaryStatistics)

    def setBoxes(self):
        self.primary_statistics = WidgetsCreator.getMergedPrimary(self.manager.screens[2].ids.race.text)
        self.secondary_statistics = WidgetsCreator.getMergedSecondary(self.manager.screens[2].ids.race.text, self.primary_statistics)

        WidgetsCreator.setCharacterStatisticsWidget(self.primaryStatistics,
                                                    self.secondaryStatistics,
                                                     self.primary_statistics,
                                                    self.secondary_statistics)

    pass


class CharacterCreateProfession(Screen):
    professions = Handler.get_data("Professions")

    def press(self):
        if self.profession.text == "Professions":

            Popup.display_error('Please choose a desired profession')

        else:
            data = {'name': self.manager.screens[2].nameOfCharacter.text,
                    'age': self.manager.screens[2].age.text,
                    'weight': self.manager.screens[2].weight.text,
                    'eye_colour': self.manager.screens[2].eyeColour.text,
                    'hair_colour': self.manager.screens[2].hairColour.text,
                    'race': self.manager.screens[2].race.text,
                    'origin': self.manager.screens[2].origin.text,
                    'sex': self.manager.screens[2].sex.text,
                    'star_sign': self.manager.screens[2].starSign.text,
                    'primary_statistics': self.manager.screens[3].primary_statistics,
                    'secondary_statistics': self.manager.screens[3].secondary_statistics,
                    'profession': self.profession.text}
            Handler.push_data(data, 'Character')
            #self.manager.screens[2].clearBoxes()
            self.manager.screens[3].clearBoxes()
            self.clearBoxes()

            self.manager.transition.direction = "up"
            self.manager.current = "Main"

    def setBoxes(self):
        for entity in self.professions:
            if self.profession.text == entity["name"]:
                self.description.text = entity["description"]
                self.equipment.text = entity["equipment"]
                self.weapon.text = entity["weapon"]
                self.armor.text = entity["armor"]
                WidgetsCreator.setStatisticsWidget(entity["primaryStatistics"],
                                                    entity["secondaryStatistics"],
                                                    self.primaryStatistics,
                                                    self.secondaryStatistics)
        pass

    def clearBoxes(self):
        self.profession.text = "Professions"
        self.description.text = ""
        self.equipment.text = ""
        self.weapon.text = ""
        self.armor.text = ""
        self.primaryStatistics.text = ""
        self.secondaryStatistics.text = ""

        WidgetsCreator.clearStatisticsWidget(self.primaryStatistics,
                                            self.secondaryStatistics)

    def setDropdowns(self):
        self.profession.values = []
        for entity in self.professions:
            if self.raceAllowance(entity["availableFor"]):
                self.profession.values.append(entity["name"])

    def raceAllowance(self, availableFor):
        # Current race
        race = self.manager.screens[2].ids.race.text
        if race != "Race":
            index = 0
            # Get index
            for entity in Handler.get_data("Races"):
                if race != entity["name"]:
                    index += 1
                else:
                    break
            # Check if allowed
            if availableFor[index] == "1":
                return True
            else:
                return False

    pass


pass


# Character board
class CharacterBoard(Screen):
    # This var is required because of nasty bug which throws table too high on the first open
    # It just counts to two, to negate this effect
    openedTimes = NumericProperty(0)
    createdNames = []

    def refresh(self):
        character = Handler.get_data("Character")
        self.clear()
        #self.fill(self.layout, character)
        if self.openedTimes != 2:
            self.openedTimes += 1

    def clear(self):
        for child in [child for child in self.layout.children]:
            if not isinstance(child, PrimaryButton):
                self.layout.remove_widget(child)
        self.createdNames = []

    def fill(self, layout, character):
        for entity in character:
            if entity['name'] not in self.createdNames:
                s = Spinner(text=entity['name'],

                            values=["Age : " + str(entity['age']),
                                    "Statistics primary : " + str(entity['primary_statistics']),
                                    "Statistics secondary : " + str(entity['secondary_statistics']),
                                    "Eyes : " + str(entity['eye_colour']),
                                    "Hair : " + str(entity['hair_colour']),
                                    "Money : " + str(entity['money']),
                                    "Origin : " + str(entity['origin']),
                                    "Profession : " + str(entity['profession']),
                                    "Race : " + str(entity['race']),
                                    "Gender : " + str(entity['sex']),
                                    "Star sign : " + str(entity['star_sign']),
                                    "Equipment : " + str(entity['equipment']),
                                    "Weapon : " + str(entity['weapon']),
                                    "Weight : " + str(entity['weight'])],

                            height=30, size_hint=(1, None),

                            background_normal='', background_color=[90 / 255, 190 / 255, 90 / 255, 1])
                layout.add_widget(s)
                self.createdNames.append(entity['name'])

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
