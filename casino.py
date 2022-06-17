#!/usr/bin/python

"""
This module displays a roulette game. The player is asked to choose a number between 
0 and 50 and make a money bet. A random number is drawn and the player wins or 
loses money according to the game rules. 

Example:
    $ python casino.py

Attributes:
    bet(int): the number between 1 and 50 on which the player bets
    #color(string): the color associated with a given number, black for even, red for odd
    bille(int): the winning number picked randomly between 0 and 50
    wallet(int): the money available for the player to bet, equals 100$ at the beginning of the game
    betamount(int): the money bet by the player on a round

"""

import random

def givecolor(number):
    """
    Ce que ça fait    

        Args:
            number: integer between 1 and 50
        
        Return:
            string: two possible values "black" if the integer is even and "red" if the integer is odd

    """
    if number % 2 == 0:
        return("black")
    else:
        return("red")


wallet = 100

bille = random.randrange(1,50)

#while wallet > 0 

print("You have " + str(wallet) + "$")

bet = int(input("Choose a number between 1 and 50 to bet on "))

betamount = input("How much do you want to bet on " + str(bet) + " (" + givecolor(bille) + ")" )

print("*Roule*")

print("The number drawn is...")

# print(bille + "(" + givecolor(bille) + ")")
# print("{} ({})".format(bille, givecolor(bille)))
print(f"{bille} ({givecolor(bille)})")

# print("You bet on the " + str(bille) + " " + "(" + givecolor(bille) + ")")
print(f"You bet on the {bille} ({givecolor(bille)})")

