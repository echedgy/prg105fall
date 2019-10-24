"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

import random
# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)


class Dice:  # note class names are capitalized
    def __init__(self):
        # TODO change side_up to '1'
        self.side_up = '1'

        # TODO change toss() to roll()
    def roll(self):
        # TODO get a random value and set side_up for the 6 sides of the dice
        if random.randint(1, 6) == 1:
            self.side_up = '1'
        elif random.randint(1,6) == 2:
            self.side_up = '2'
        elif random.randint(1,6) == 3:
            self.side_up = '3'
        elif random.randint(1,6) == 4:
            self.side_up = '4'
        elif random.randint(1,6) == 5:
            self.side_up = '5'
        else:
            self.side_up = '6'

    def get_side_up(self):
        return self.side_up


def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    my_dice_three = Dice()
    my_dice_four = Dice()
    my_dice_five = Dice()
    my_dice_six = Dice()
    print('This dice is 1, ', my_dice.get_side_up())
    print('This side is 2, ', my_dice_two.get_side_up())
    print('This side is 3, ', my_dice_three.get_side_up())
    print('This side is 4, ', my_dice_four.get_side_up())
    print('This side is 5, ', my_dice_five.get_side_up())
    print('This side is 6, ', my_dice_six.get_side_up())

    print('I am rolling the dice...')
    my_dice.toss()
    my_dice_two.toss()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())


main()
