from os import system
import time
from bubblesNmoves import *


#if you want them in aphebetical order:
#all_bubbles=sorted(all_bubbles)
#all_bubbles=sorted(all_bubbles)


def search():

    print("These are the bubbles in the Bubble-DEX")

    for i in range(len(all_bubbles)):

        print(f"{1 + i}: {all_bubbles[i].name}")
    searching = input("")

    while not searching.isdigit():

        print("Please Type the number, not the name ")
        searching = input("")

        while not searching.isdigit:
            break

        else:
            searching = int(searching)
            delay_print(all_bubbles[searching])
            again = input("Search again? y/n ")

            if (again == "y"):
                time.sleep(1)
                system('clear')
                search()

            break
            break

    else:
        searching = int(searching)
        print(all_bubbles[searching - 1].stats)
        again = input("Search again? y/n ")
        if (again == "y"):
            time.sleep(1)
            system('clear')
            search()