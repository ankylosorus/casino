#!/usr/bin/python

"""
This module displays a roulette game. The player is asked to choose a number between 
0 and 50 and make a money bet. A random number is drawn and the player wins or 
loses money according to the game rules. 

Example:
    $ python casino.py --number 44 --bet 75
    
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

import getpass

import argparse

def givecolor(number):
    """
    Returns color of a given number according to the game rules   

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

parser.add_argument("-number", help="on which number you set your bet", type=int) 

parser.add_argument("-bet", help="how much dollars you wish to bet", type=int)

args = parser.parse_args()

time.sleep(1)

#*****pour ne pas avoir à mettre des "if args / if input" tout au long du code*****
if args.number:
    bet = args.number
    betamount = args.bet
else:
    bet = 0
    betamount = 0

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
                betamount = int(input(f"\nHow much do you want to bet on {bet} ({givecolor(bet)})?\n"))
                if betamount == wallet:
                    print("! ALL IN !")
            except ValueError:
                continue
            if betamount > wallet:
                print("You do not have enough in your wallet")

    print(f"\nYou bet {betamount}$ on {bet} ({givecolor(bet)})\n")

    time.sleep(1)

    print("*Spins*")

    time.sleep(2)

    print(f"The winning number is {ball} {givecolor(ball)} !")
    
    history.append(ball)

    time.sleep(2)

    if ball == bet:
        wallet = wallet + betamount*4
        print("Well done. You win 3 times your bet\n")
    else:
        wallet = wallet - betamount
        if givecolor(ball) == givecolor(bet):
            print("\n==> Missed... but you guessed the color, you win half your bet\n")
            wallet = wallet + betamount*1.5
        else:
            print ("\n==> You lose your bet\n")

    # if ball == bet:
    #     wallet = wallet + betamount*4
    # else:
    #     wallet = wallet - betamount
    #     if givecolor(ball) == givecolor(bet):
    #         wallet = wallet + betamount*1.5
            
    # time.sleep(1)

    # print(result(bet, betamount))

#car si args, pas de possibilité de rejouer
    if args.number:
        time.sleep(2)
        print(f"You now have {math.ceil(wallet)}$\n")
        time.sleep(3)
        exit()
    
print("You're broke. Out!")

time.sleep(1)

exit()




