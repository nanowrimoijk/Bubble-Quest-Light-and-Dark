import random
import sys
import time
from os import system
from helper.bubble import *

money = []

for i in range(10000): #change back to 1000 later
  money.append(1)

class bcolors:
  HEADER = '\033[95m'
  OKGREEN = '\033[1;32;40m'
  OKBLUE = '\033[94m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  DEFAULT = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

  BLACK  = '\33[30m'
  RED    = '\33[91m'
  GREEN  = '\33[32m'
  YELLOW = '\33[93m'
  BLUE   = '\33[34m'
  VIOLET = '\33[35m'
  BEIGE  = '\33[36m'
  WHITE  = '\33[37m'
  BOLD = '\033[1m'
  END = '\033[0m'

  STEEL_TYPE    = '\33[90m'
  FIRE_TYPE   = '\33[91m'
  GRASS_TYPE  = '\33[92m'
  ELECTRIC_TYPE = '\33[93m'
  WATER_TYPE  = '\33[94m'
  PSYCHIC_AND_POISON_TYPE = '\33[95m'
  CBEIGE2  = '\33[96m'
  NORMAL_AND_AIR_TYPE  = '\33[97m'
  ROCK_TYPE = '\033[033m'
  LIGHT_TYPE = ''

  CGREYBG    = '\33[100m'
  CREDBG2    = '\33[101m'
  CGREENBG2  = '\33[102m'
  CYELLOWBG2 = '\33[103m'
  CBLUEBG2   = '\33[104m'
  CVIOLETBG2 = '\33[105m'
  CBEIGEBG2  = '\33[106m'
  CWHITEBG2  = '\33[107m'


skip = input(f"{bcolors.ROCK_TYPE}Do you want to skip the intro? Type y to skip: {bcolors.ENDC}")
if skip ==  "y":
  begin_delay_timer = 0
  msg_delay = 0
else:
  begin_delay_timer = 0.03

def delay_print_begin(s):
    # print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(begin_delay_timer)

delay_print_begin(
    "\nHi! Welcome to BUBBLE QUEST: LIGHT AND DARK!\nThis is still in beta, so it might be buggy.\nIf you have troubles, comment down below.\n||\n\/"
)
# Lets player choose how long the message delay is
delay_print_begin(
    "\nHow many seconds/100 do you want your message delay to be?\n(A message delay is the number of seconds before the engine prints out another letter).\nTHIS CANNOT BE CHANGED UNLESS YOU ARE WILLING TO RESTART THE GAME.\n(It has to be positive.)\n(recommended 2-5):\n"
)
msg_done = False
while msg_done == False:
  msg_delay = input("What do you want your message delay to be?\n")
  msg_confirm = msg_delay
  try:
    msg_delay = int(msg_delay)/100
    if(msg_delay < 0):
      msg_delay *= -1
      delay_print_begin("The negative sign has been removed from your response")
    confirm = input("Type that again to confirm\n")
    if(confirm != msg_confirm):
      print("That is not what you typed before")
    else:
      msg_done = True
  except ValueError or OverflowError:
    print("That is not an option\n")

time.sleep(1)
system('clear')

def delay_print(s):
    # print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(msg_delay)


def shop(item_amount,luck):
  #
  #item amount is the max quantity of an item they have, so the player can't spam berries or something.
  #luck is not how lucky in this function, the higher the luck, the more dramatic the prices will be from the standard/accurate price, both in a good way or in a bad way.
  evolution_stone_price = 5000
  strength_potion_price = 1000
  health_potion_price = 1000
  revive_price = 1000
  evolution_stone_price += random.randint((luck*-20),(luck*50))
  strength_potion_price += random.randint((luck*-20),(luck*50))
  health_potion_price += random.randint((luck*-20),(luck*50)) 
  revive_price += random.randint((luck*-20),(luck*50))
  buy = True
  while buy == True:
    delay_print(f"{bcolors.OKGREEN}You have ${len(money)}, what would you like to buy?\n")
    delay_print(f"{bcolors.DEFAULT}1.) Evolution Stone: ${evolution_stone_price}\n2.) Strength Potion: ${strength_potion_price}\n3.) Health Potion: ${health_potion_price}\n4.) Revive: ${revive_price}\n")
    delay_print("Which one do you want?(press n to leave the shop)\n")
    shop_item = input('')
    if shop_item == '2':
      buy = None
      if len(money) < strength_potion_price:
        delay_print("Sorry, you don't have enough money.\n")
        delay_print("Do you want to buy something from the shop?\nPress y for yes.\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
      else:
        strength_potion.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False

    elif shop_item == '3':
      buy == None
      if len(money) < health_potion_price:
        delay_print("Sorry, you don't have enough money.\n")
        shop_item == ""
        delay_print("Do you want to buy something from the shop?\nPress y for yes.\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
      else:
        health_potion.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        shop_item = ""
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
    elif shop_item == '4':
      if len(money) < revive_price:
        delay_print("Sorry, you don't have enough money.\n")
        shop_item == ""
        delay_print("Do you want to buy something from the shop?\nPress y for yes.\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
      else:
        revive.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
        time.sleep(1)
        system('clear')
        shop_item == ""
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
    elif shop_item == "":
      buy_again = ""
      buy = False
    elif shop_item == "n":
      buy_again = ""
      buy = False
  if buy_again == "":
    buy = False
  else:
    delay_print("Please try again\n")
    shop_item = ""
    buy = True
  while buy == False:
    delay_print("\nYou left the shop.")
    time.sleep(1)
    system('clear')
    break

def change_deck():
  done_changing_deck = False
  done_switching_out = False
  done_replacing = False
  while done_changing_deck == False:
    while done_switching_out == False:
      for i in range(len(player_deck)):
        print(i+1,deck_name[i])
      switch_out = input("Which one do you want to switch out?\n")
      try:
        switch_out = int(switch_out)
        if switch_out > len(player_deck):
          print("That is not a valid option")
        elif switch_out <= 0:
          print("That is not a valid option")
        else:
          done_switching_out = 1
          switch_out -= 1
      except ValueError:
        print("That is not a valid responce.")
    switched_out_bubble = player_deck[switch_out]
    while done_replacing==False:
      for i in range(len(player_bubbles)):
        print(i+1,bubble_names[i])
      replace_with = input("Which one do you want to replace it with?\n")
      try:
        replace_with = int(replace_with)
        if replace_with > len(player_bubbles):
          print("That is not a valid option")
        elif replace_with <= 0:
          print("That is not a valid option")
        else:
          replace_with -= 1
          done_replacing = 1
      except ValueError:
        print("That is not a valid responce")
    player_deck.remove(player_deck[switch_out])
    player_deck.append(player_bubbles[replace_with])
    deck_name.remove(deck_name[switch_out])
    deck_name.append(bubble_names[replace_with])
    player_bubbles.remove(player_bubbles[replace_with])
    player_bubbles.append(switched_out_bubble)
    bubble_names.remove(bubble_names[replace_with])
    bubble_names.append(switched_out_bubble.name)
    change_again = input("Do you want to repeat this process?\n(y/n)\n")
    time.sleep(1)
    system('clear')
    if change_again != "y":
      done_changing_deck = 1
    else:
      done_changing_deck = False
      done_switching_out = False
      done_replacing = False
  else:
    print("You do not have any bubbles to switch out")
    time.sleep(1)
    system('clear')




def list_splice(target, start, delete_count=None, *items):
	"""Remove existing elements and/or add new elements to a list.

	target        the target list (will be changed)
	start         index of starting position
	delete_count  number of items to remove (default: len(target) - start)
	*items        items to insert at start index

	Returns a new list of removed items (or an empty list)
	"""
	if delete_count == None:
		delete_count = len(target) - start

	# store removed range in a separate list and replace with *items
	total = start + delete_count
	removed = target[start:total]
	target[start:total] = items

	return removed