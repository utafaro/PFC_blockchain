import random


class Player:

    def __init__(self, pseudo,  balance=0, points=0):
        self.pseudo = pseudo
        self.points = points
        self.balance = balance
        self.choice = None

    def getChoix(self):
        return self.choice
    def setChoix(self, choice):
        self.choice = choice

    def generateNonce(self):
        return random.randint(2**10, 2**256)


