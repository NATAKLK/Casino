import random
import os

class Ruleta:
    def __init__(self, colors, number):
        self.colors_roulette  = colors
        self.number_roulette = number

    @staticmethod
    def colorsr():
        return ["Red", "Blue", "Green"]
    
    @staticmethod
    def random_roulette():
        return Ruleta(random.choice(Ruleta.colorsr()), random.randint(1, 36))
    

ruleta1 = Ruleta.random_roulette()

print(ruleta1.colors_roulette)
print(ruleta1.number_roulette)