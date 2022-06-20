#!/usr/bin/python

"""
This module displays a roulette game. The player is asked to choose a number between 
0 and 50 and make a money bet. A random number is drawn and the player wins or 
loses money according to the game rules. 

Example:
    $ python casino.py

Attributes:
    bet(int): the number between 1 and 50 on which the player bets
    ball(int): the winning number picked randomly between 0 and 50
    wallet(int): the money available for the player to bet, equals 100$ at the beginning of the game
    betamount(int): the money bet by the player on a round
    history(list): the previous winning numbers

"""

import random

import time

import math

#import os

import getpass

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

history = []

time.sleep(1)

#print(f"\nHello {os.environ.get('USERNAME')}\n")
print(f"\nHello {getpass.getuser()}\n")

while wallet > 0:
    #obligé de mettre variable ball dans boucle sinon ne va pas s'update
    ball = random.randrange(1,50)
    # math.ceil arrondit un float à l'entier supérieur
    retry = ""
    if history == []:
        print(f"You have {math.ceil(wallet)}$\n")
    else:
        print(f"You now have {math.ceil(wallet)}$\n")
    while retry != "y" and retry != "n":
        if history == []:
            retry = input("Do you want to try your luck? (y/n)\n")
        else:
            retry = input("Do you still want to play? (y/n)\n")
        if retry == "n":
            print("You don't know what you're missing... Bye")
            exit()
        elif retry == "y":
            break

    #si input n'est pas un integer --> erreur / stacktrace
    bet = 0
    while bet < 1 or bet > 50:
        try:
            bet = int(input("\nChoose a number between 1 and 50 to bet on\n"))
        except ValueError:
            print("Invalid value") 
            continue

    betamount = 0
    while betamount < 1 or betamount > wallet:
        try:    
            #j'ai essayé le f dans le input, ça marche! pourquoi bleu et pas violet?
            betamount = int(input(f"\nHow much do you want to bet on {bet} ({givecolor(bet)})?\n"))
            if betamount == wallet:
                print("! ALL IN !")
        except ValueError:
            continue
        if betamount > wallet:
            print("You do not have enough in your wallet")

    # print("You bet on the " + str(ball) + " " + "(" + givecolor(ball) + ")")
    print(f"\nYou bet {betamount}$ on {bet} ({givecolor(bet)})\n")

    time.sleep(1)

    print("*Spins*")

    time.sleep(2)

    print(f"The winning number is {ball} {givecolor(ball)} !")
    
    history.append(ball)

    time.sleep(2)

    if ball == bet:
        wallet = wallet + betamount*4
        time.sleep(1)
        print("Well done. You win 3 times your bet\n")
    else:
        wallet = wallet - betamount
        if givecolor(ball) == givecolor(bet):
            time.sleep(1)
            print("\n==> You missed... but you guessed the color, you win half your bet\n")
            wallet = wallet + betamount*1.5
        else:
            print ("\n==> You missed\n")

print("OUT!")
exit()




