#!/usr/bin/python

"""
This module displays a roulette game. The player is asked to choose a number between 
1 and 50 and make a bet. A random number is picked and the player wins or 
loses money according to the game rules. 

Example:
    $ python casino.py --number 44 --bet 75
    
Attributes:
    number(int): the number between 1 and 50 on which the player bets
    ball(int): the winning number picked randomly between 1 and 50
    wallet(int): the money available for the player to bet, equals 100$ at the beginning of the game
    bet(int): the money bet by the player on a number
    history(list): the previous winning numbers

"""

import random

import time

import math

import getpass

import argparse

def givecolor(number):
    """
    Returns the color of a given number according to the game rules   

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

parser = argparse.ArgumentParser()

#parser.add_argument("-number", help="on which number you set your bet", type=int) 
parser.add_argument("number", help="on which number you set your bet", type=int) 

#parser.add_argument("-bet", help="how much dollars you wish to bet", type=int)
parser.add_argument("bet", help="how much dollars you wish to bet", type=int)

args = parser.parse_args()

time.sleep(1)

#pour ne pas avoir à mettre des "if args / if input" tout au long du code*****
if args.number:
    number = args.number
    bet = args.bet
else:
    number = 0
    bet = 0

print(f"\nHello {getpass.getuser()}")

time.sleep(1)

while wallet > 0:
    ball = random.randrange(1,50)

    if args.number == None: 
        retry = ""
        if history == []:
            print(f"\nYou have {math.ceil(wallet)}$\n")
        else:
            time.sleep(2)
            print(f"\nYou now have {math.ceil(wallet)}$\n")
        while retry != "y" and retry != "n":
            if history == []:
                retry = input("Do you want to try your luck? (y/n)\n")
            else:
                time.sleep(1)
                retry = input("Do you still want to play? (y/n)\n")
            if retry == "n":
                print("You don't know what you're missing... Bye")
                exit()
            elif retry == "y":
                break

        number = 0
        while number < 1 or number > 50:
            try:
                number = int(input("\nChoose a number between 1 and 50 to bet on\n"))
            except ValueError:
                print("Invalid value") 
                continue
            
        bet = 0
        while bet < 1 or bet > wallet:
            try:    
                bet = int(input(f"\nHow much do you want to bet on {number} ({givecolor(number)})?\n"))
                if bet == wallet:
                    print("!!! ALL IN !!!")
            except ValueError:
                continue
            if bet > wallet:
                print("You do not have enough in your wallet")

    print(f"\nYou bet {bet}$ on {number} ({givecolor(number)})\n")

    time.sleep(1)

    print("*Spins*")

    time.sleep(2)

    print(f"The winning number is {ball} {givecolor(ball)} !")
    
    history.append(ball)

    time.sleep(2)

    if ball == number:
        wallet = wallet + bet*4
        print("Well done. You win 3 times your bet\n")
    else:
        wallet = wallet - bet
        if givecolor(ball) == givecolor(number):
            print("\n==> Missed... but you guessed the color, you win half your bet\n")
            wallet = wallet + bet*1.5
        else:
            print ("\n==> You lose your bet\n")

#si args, pas de possibilité de rejouer
    if args.number:
        time.sleep(2)
        print(f"You now have {math.ceil(wallet)}$\n")
        time.sleep(2)
        print("Bye\n")
        time.sleep(2)
        exit()
    
print("You're broke. Out!")

time.sleep(2)

exit()




