import random

class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.name = "D" + str(sides)

    def roll(self, number_of_dice):
        dice_rolls = []
        while len(dice_rolls) != number_of_dice:
            roll = random.randint(1, self.sides)
            dice_rolls.append(roll)
        return f"You rolled {number_of_dice}x {self.name}.\nThe results are: {dice_rolls}"

class Percentile(Dice):
    def roll(self, number_of_dice):
        dice_rolls = []
        second_digit = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
        while len(dice_rolls) != number_of_dice:
            first_number = random.randint(0, 9)
            second_number = random.choice(second_digit)
            if (first_number + int(second_number)) == 0:
                dice_rolls.append(100)
            else:
                dice_rolls.append(first_number + int(second_number))
        return f"You rolled {number_of_dice}x {self.name}.\nThe results are: {[i for i in dice_rolls]}"

def choose_dice_and_roll():
    get_dice = int(input("Which die do you need?\nD"))
    if get_dice == 100:
        dice_type = Percentile(get_dice)
    else:
        dice_type = Dice(get_dice)
    dice_amount = int(input("How many?\n"))
    return dice_type.roll(dice_amount)


print(choose_dice_and_roll())
