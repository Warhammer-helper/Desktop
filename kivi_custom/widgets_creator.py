from kivi_custom.widgets import *

from random import randint

from database.realtime_handler import Handler


class Rolls:

    @staticmethod
    def statRoll():
        stats = ""
        for i in range(0, 8):
            number = randint(1, 20)
            if number < 10:
                number = "0" + str(number)
            stats += str(number)
        return stats

    @staticmethod
    def fpRoll(race_name):
        fp = ""
        number = randint(0, 2)
        for entity in Handler.get_data("Races"):
            if entity["name"] == race_name:
               fp += "0" + entity['fpRoll'][number]
        return fp

    @staticmethod
    def vitalityRoll(race_name):
        vitality = ""
        number = randint(0, 3)
        for entity in Handler.get_data("Races"):
            if entity["name"] == race_name:
                vitality += (entity['wRoll'][number*2] + entity['wRoll'][number*2+1])
        return vitality

class WidgetsCreator:

    @staticmethod
    def clearStatisticsWidget(first_grid,
                            second_grid):
        first_grid.clear_widgets()
        second_grid.clear_widgets()

    @staticmethod
    def setStatisticsWidget(primary_statistics,
                            secondary_statistics,
                            first_grid,
                            second_grid):
        # Reformat statistics
        primary_names = ["WS", "BS", "S", "T", "AG", "INT", "WP", "FEL"]
        secondary_names = ["A", "W", "SB", "TB", "M", "MAG", "IP", "FP"]
        primary_reformated = []
        secondary_reformated = []
        for i in range(0, 8):
            primary_reformated.append(primary_statistics[i * 2] +
                                     primary_statistics[(i * 2) + 1])
            secondary_reformated.append(secondary_statistics[i * 2] +
                                       secondary_statistics[(i * 2) + 1])

        # Create widgets
        first_grid.clear_widgets()
        second_grid.clear_widgets()
        for entity, name in zip(primary_reformated, primary_names):
            first_grid.add_widget(Label(text=name))
            first_grid.add_widget(TextInput(text=entity))
        for entity, name in zip(secondary_reformated, secondary_names):
            second_grid.add_widget(Label(text=name))
            second_grid.add_widget(TextInput(text=entity))

    @staticmethod
    def setCharacterStatisticsWidget(first_grid,
                                     second_grid,
                                     primary_statistics,
                                     secondary_statistics):
        # Reformat statistics
        primary_names = ["WS", "BS", "S", "T", "AG", "INT", "WP", "FEL"]
        secondary_names = ["A", "W", "SB", "TB", "M", "MAG", "IP", "FP"]
        primary_reformated = []
        secondary_reformated = []
        primary_statistics = str(primary_statistics)
        for i in range(0, 8):
            primary_reformated.append(primary_statistics[i * 2] +
                                     primary_statistics[(i * 2) + 1])
            secondary_reformated.append(secondary_statistics[i * 2] +
                                       secondary_statistics[(i * 2) + 1])

        # Create widgets
        first_grid.clear_widgets()
        second_grid.clear_widgets()
        for entity, name in zip(primary_reformated, primary_names):
            first_grid.add_widget(Label(text=name))
            first_grid.add_widget(TextInput(text=entity))
        for entity, name in zip(secondary_reformated, secondary_names):
            second_grid.add_widget(Label(text=name))
            second_grid.add_widget(TextInput(text=entity))

    @staticmethod
    def getMergedPrimary(race_name):
        stats = ""
        for entity in Handler.get_data("Races"):
            if entity["name"] == race_name:
               stats = int(Rolls.statRoll()) + int(entity["primaryStatistics"])
        stats = str(stats)
        while len(stats) < 16:
            stats = "0" + stats
        return stats

    @staticmethod
    def getMergedSecondary(race_name, primary):
        stats = ""
        for entity in Handler.get_data("Races"):
            if entity["name"] == race_name:
                stats = entity["secondaryStatistics"]
        # Rulebook changes
        addition = "00" \
                   + Rolls.vitalityRoll(race_name) + "0" \
                   + primary[4] + "0" \
                   + primary[6] + "000000" + Rolls.fpRoll(race_name)
        stats = int(stats) + int(addition)

        stats = str(stats)
        while len(stats) < 16:
            stats = "0" + stats

        return stats









