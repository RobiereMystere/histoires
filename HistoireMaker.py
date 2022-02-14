import random


class HistoireMaker:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.protagoniste = {"Qui":random.choice(self.dictionary["Qui"])}
        self.situation_initiale = {
            "Ou": random.choice(self.dictionary["Ou"]),
            "Quand": random.choice(self.dictionary["Quand"]),
            "Quoi": random.choice(self.dictionary["Quoi"]),
                                }

