from random import *
import random


wished = 0
fourStarDropPity = 0
wishPity = 0
fourStarPityWished = 0

wishes = 0
primogems = 160000000000

fiveStarCharacterDrop = "5* Character"
fourStarCharacterDrop = "4* Character"
weaponDrop = "Weapon"


print("Genshin Wish Simulator by Ducky. Version 1.1\n\n")
print("Welcome to Genshin Impact Wish Simulator!\n")
print('Type 1 to buy one wish, or 2 to buy ten wishes.\nType 3 to wish once, or 4 to wish ten times.\n')

while True:
    action = int(input())
    
    if action == 1:
        if primogems >= 160:
            primoGems = primogems - 160
            wishes = wishes + 1
            print("You bought one wish!\n")
            print("Primogems left:", primoGems)
            print("Wishes:", wishes, "\n")
        else:
            print("Sorry! You don't have enough Primogems!\n")
    elif action == 2:
        if primogems >= 1600:
            primoGems = primogems - 1600
            wishes = wishes + 10
            print("You bought ten wishes!\n")
            print("Primogems left:", primoGems)
            print("Wishes:", wishes, "\n")
        else:
            print("Sorry! You don't have enough Primogems!\n")
    elif action == 3:
        if wishes > 0:
            wished = wished + 1
            fourStarPityWished = fourStarPityWished + 1
            if fourStarPityWished == 10:
                fourStarPityWished = 0
                fourStarDropPity = 1
            if wished >= 90:
                print("You got:", fiveStarCharacterDrop, "!\n")
                wished = 0
            elif wished >= 75:
                if random.randint(1, 1000) < 200:
                    print("You got:", fiveStarCharacterDrop, "!\n")
                    wished = 0
                else:
                    if fourStarDropPity == 1:
                        print("You got:", fourStarCharacterDrop, "!\n")
                    else:
                        print("You got:", weaponDrop, "!\n")
            else:
                if random.randint(1, 1000) < 6:
                    print("You got:", fiveStarCharacterDrop, "!\n")
                    wished = 0
                else:
                    if fourStarDropPity == 1:
                        print("You got:", fourStarCharacterDrop, "!\n")
                    else:
                        print("You got:", weaponDrop, "!\n")
            wishes = wishes - 1
            fourStarDropPity = 0
        else:
            print("Sorry! You don't have enough Wishes!\n")
        print("Wishes left:", wishes)
        print("Total wishes wished(Before 5*):", wished)
    elif action == 4:
        if wishes >= 10:
            for i in range(10):
                wished = wished + 1
                fourStarPityWished = fourStarPityWished + 1
                if fourStarPityWished == 10:
                    fourStarPityWished = 0
                    fourStarDropPity = 1
                if wished >= 90:
                    print("You got:", fiveStarCharacterDrop, "!\n")
                    wished = 0
                elif wished >= 75:
                    if random.randint(1, 1000) < 200:
                        print("You got:", fiveStarCharacterDrop, "!\n")
                        wished = 0
                    else:
                        if fourStarDropPity == 1:
                            print("You got:", fourStarCharacterDrop, "!\n")
                        else:
                            print("You got:", weaponDrop, "!\n")
                else:
                    if random.randint(1, 1000) < 6:
                        print("You got:", fiveStarCharacterDrop, "!\n")
                        wished = 0
                    else:
                        if fourStarDropPity == 1:
                            print("You got:", fourStarCharacterDrop, "!\n")
                        else:
                            print("You got:", weaponDrop, "!\n")
                wishes = wishes - 1
                fourStarDropPity = 0
        else:
            print("Sorry! You don't have enough Wishes!\n")
        print("Wishes left:", wishes)
        print("Total wishes wished(Before 5*):", wished)

    else:
        print("Sorry! Action is not recognized, try again!\n")
