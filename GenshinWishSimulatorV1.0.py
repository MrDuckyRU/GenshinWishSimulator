from random import *
import random


wished = 0
wishes = 0
primogems = 160000000000


while True:       
    print("Welcome to Genshin Impact Wish Simulator!")
    print('\nType 1 to buy wish, and type 2 to wish!\n')
    
    action = int(input())
    
    if action == 1:
        if primogems >= 160:
            primoGems = primogems - 160
            wishes = wishes + 1
            print("You bought one wish!\n")
            print("Primogems left:", primoGems)
            print("Wishes:", wishes)
        else:
            print("Sorry! You don't have enough Primogems!\n")
    elif action == 2:
        if wishes > 0:
            wished = wished + 1
            if wished == 90:
                print("You got [5*Character]!\n")
                wished = 0
            elif wished >= 75:
                if random.randint(1, 1000) < 200:
                    print("You got [5*Character]!")
                    wished = 0
                else:
                    print("You got [Weapon]!\n")
            else:
                if random.randint(1, 1000) < 6:
                    print("You got [5*Character]!\n")
                    wished = 0
                else:
                    print("You got [Weapon]!\n")
        else:
            print("Sorry! You don't have enough Wishes!\n")
        print("Wishes left:", wishes)
    else:
        print("Sorry! Action is not recognized, try again!\n")