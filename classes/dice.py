import random

class Dice():
    def __init__(self) -> None:
        pass

    def roll(self):
        return random.randint(1, 6)

    def roll_multiple(self, num):
        rolls = []
        for i in range(num):
            rolls.append(self.roll())

        rolls.sort(reverse=True)
        if rolls[0] == rolls[1]:    
            rolls = self.roll_multiple(num)
        
        random.shuffle(rolls)

        return rolls