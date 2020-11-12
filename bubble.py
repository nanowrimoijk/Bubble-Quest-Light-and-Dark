import time
import sys
import random
#vars
capture_disc_count=[]
opponent_name = []
berries = [1,1,1,1,1,1,1,1,1,1]
lost_contest_1 = []
lost_grunt_1 = []
money = []
battle_valid_used = []
health_potion = []
strength_potion = []
revive = [1]
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

  CBLACK  = '\33[30m'
  CRED    = '\33[31m'
  CGREEN  = '\33[32m'
  CYELLOW = '\33[33m'
  CBLUE   = '\33[34m'
  CVIOLET = '\33[35m'
  CBEIGE  = '\33[36m'
  CWHITE  = '\33[37m'

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


def the_end():
  delay_print("\n...........     . .       .     ...........")
  delay_print("\n.               .  .      .     .          .")
  delay_print("\n.               .   .     .     .          .")
  delay_print("\n...........     .    .    .     .          .")
  delay_print("\n.               .     .   .     .          .")
  delay_print("\n.               .      .  .     .          .")
  delay_print("\n...........     .       . .     ...........")
  delay_print(f"{bcolors.FIRE_TYPE}\nThese are the people who helped with the code.\nCredits:\n")
  time.wait(10)
  delay_print(f"{bcolors.WATER_TYPE}Peyton Yang - peytony071@gmail.com")
  delay_print(f"{bcolors.GRASS_TYPE}Cameron Jiang - 22camerjian@gmail.com")
  delay_print(f"{bcolors.ELECTRIC_TYPE}")
  delay_print(f"{bcolors.WATER_TYPE}")

class Person:
  def __init__(self, name, berries, money):

    self.name = name
    self.berries = berries
    self.money = money


player_bubbles = []
bubble_names = []

player_deck = []
deck_name = []


###################################################


skip = input(f"{bcolors.ROCK_TYPE}Do you want to skip the credits? Type y to skip: {bcolors.ENDC}")
if skip == "MONEY":
  player_money = 1000
  begin_delay_timer = 0
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


#welcome


delay_print_begin(
    "\nHi! Welcome to BUBBLE QUEST: LIGHT AND DARK!\nThis is still in beta, so it might be buggy.\nIf you have troubles please email an editor.\n"
) 
delay_print_begin(
    f"{bcolors.OKGREEN}\nCREDITS\nHead Developers:\nCameron Jiang - 22camerjian@gmail.com\nPeyton Yang - peytony071@gmail.com\n\n{bcolors.ENDC}\n"
)
delay_print_begin(
    f"{bcolors.OKGREEN}\nOther Devs:\nRyan Li - liryan376@gmail.com\nKai Hsu - 22kaihsu@gmail.com\nHans Liu - supercellscrub3@gmail.com\n\n{bcolors.ENDC}\n"
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

def delay_print(s):
    # print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(msg_delay)

delay_print(f"{bcolors.NORMAL_AND_AIR_TYPE}What is your name?\n")
name = input("")

player = Person(name, 0, 0)

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
      if change_again != "y":
        done_changing_deck = 1
      else:
        done_changing_deck = False
        done_switching_out = False
        done_replacing = False
    else:
      print("You do not have any bubbles to switch out")

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
  health_potion_price += random.randint((luck*-20),(luck*50)
  )
  revive_price += random.randint((luck*-20),(luck*50)
  )
  buy = True
  while buy == True:
    delay_print(f"1.) Evolution Stone: ${evolution_stone_price}\n2.) Strength Potion: ${strength_potion_price}\n3.) Health Potion: ${health_potion_price}\n4.) Revive: ${revive_price}\n")
    delay_print("Which one do you want?(press n to leave the shop)\n")
    shop_item = input('')
    if shop_item == '2':
      buy = None
      if len(money) < strength_potion_price:
        delay_print("Sorry, you don't have enough money.\n")
        delay_print("Do you want to buy something from the shop?\nPress y for yes.\n")
        buy_or_not = input("")
        if buy_or_not == "y":
          buy_or_not = ""
          buy = True
        else:
          buy_or_not = ""
          buy = False
      else:
        strength_potion.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
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
        buy_or_not = input("")
        if buy_or_not == "y":
          buy_or_not = ""
          buy = True
        else:
          buy_or_not = ""
          buy = False
      else:
        health_potion.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
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
        buy_or_not = input("")
        if buy_or_not == "y":
          buy_or_not = ""
          buy = True
        else:
          buy_or_not = ""
          buy = False
      else:
        revive.append(1)
        delay_print("Do you want to buy something else?\nPress y for yes\n")
        buy_again = input("")
        shop_item == ""
        if buy_again == "y":
          buy_again = ""
          buy = True
        else:
          buy_again = ""
          buy = False
    elif shop_item == "":
      buy = False
    elif buy_again == "":
      buy = False
    else:
      delay_print("Please try again\n")
      shop_item = ""
      buy = True
  while buy == False:
    delay_print("\nYou left the shop.")
    break

class Item:
  def __init__(self, use):
    self.use = use

    def heal(heal_type, amount):
      if heal_type == 'normal':
        return(20)
      if heal_type == 'boosted':
        return(40)
      if heal_type == 'mega':
        return(100)
    def lvl(lvl_type, lvls):
      if lvl_type == 'normal':
        lvls == 1
      if lvl_type == 'boosted':
        lvls == 3
      if lvl_type == 'mega':
        lvls == 5
      if lvl_type == 'evol':
        pass


class Bubble:
  def __init__(self, name, energy, move1, move2, move3, move4, move1_damage, move2_damage, move3_damage, move4_damage, move1_energy, move2_energy, move3_energy, move4_energy, move1_type, move2_type, move3_type, move4_type, speed, health, level, XP, bubble_type, max_moves, total_moves, energyc, healthc,evolution,evolution_level):
    # save variables as attributes

    self.name = name
    self.energy = float(energy)
    self.move_one = move1
    self.move_two = move2
    self.move_three = move3
    self.move_four = move4
    self.move_one_energy = float(move1_energy)
    self.move_two_energy = float(move2_energy)
    self.move_three_energy = float(move3_energy)
    self.move_four_energy = float(move4_energy)
    self.move_one_damage = float(move1_damage)
    self.move_two_damage = float(move2_damage)
    self.move_three_damage = float(move3_damage)
    self.move_four_damage = float(move4_damage)
    self.move_one_type = move1_type
    self.move_two_type = move2_type
    self.move_three_type = move3_type
    self.move_four_type = move4_type
    self.total_moves = float(total_moves)
    self.speed = float(speed)
    self.bars = float(health) # Amount of health bars
    self.level = float(level)
    self.level_MAX = float(100)
    self.XP = float(XP)
    self.XP_MAX = float(20)
    self.healthc = float(healthc)
    self.energyc = float(energyc)
    self.evolution = evolution
    try:
      self.evolution_level = float(evolution_level)
    except TypeError:
      self.evolution_level = 100
    except ValueError:
      self.evolution_level = 100

    self.moves = [self.move_one, self.move_two, self.move_three, self.move_four]

    self.moves_damage = [self.move_one_damage, self.move_two_damage, self.move_three_damage, self.move_four_damage]
    
    self.moves_energy = [self.move_one_energy, self.move_two_energy, self.move_three_energy*-1, self.move_four_energy*-1]


    self.max_moves = float(max_moves)
    self.bubble_type = bubble_type

    if self.move_four == "":
      self.move_four == "NOT AVAILABLE"
    
    if self.move_four_damage == "":
      self.move_four_damage == 0

    if self.move_four_energy == "":
      self.move_four_energy == 0

    self.stats = f"\n{self.name}:\nType: {self.bubble_type}\nHealth: {self.bars}\nLevel: {self.level}\nSpeed: {self.speed}\n{self.move_one} ({self.move_one_type}): Does {self.move_one_damage} damage + {self.move_one_energy} energy\n{self.move_two} ({self.move_two_type}): Does {self.move_two_damage} + {self.move_two_energy} energy\n{self.move_three} ({self.move_three_type}): Does {self.move_three_damage} damage - {self.move_three_energy} energy\n{self.move_four} ({self.move_four_type}): Does {self.move_four_damage} - {self.move_four_energy}\nThis bubble starts with {self.energy} energy."


  def multiple_fight_v(your_bubbles_amount,opponents_bubbles_amount,kind,opponents_first_bubble,second,third,fourth,fifth):
    list_of_bubbles = []
    done = False
    repeating = False
    index_error = False
    for i in range(len(player_deck)):
        print(i+1,deck_name[i])
    while done == False:
      bubble = input("Which bubbles do you want to use in the fight?\nEX: 1234 (no spaces in between)\n")
      list_of_bubbles.clear()
      repeating = False
      index_error = False
      for char in bubble:
        try:
          char = int(char)
          if char > len(player_deck):
            print("There are errors in your responce")
            index_error = True
          elif char-1 in list_of_bubbles:
            print("You cannot have repeating bubbles")
            repeating = True
          list_of_bubbles.append(char-1)
        except ValueError:
          pass
      if index_error == False and repeating == False:
        if len(list_of_bubbles) < your_bubbles_amount:
          print("You do not have enough bubbles")
        elif len(list_of_bubbles) > your_bubbles_amount:
          print("You have too many bubbles")
        else:
          done = True
      else:
        print("You have errors in your text")
    bubble_amount = f"{your_bubbles_amount}-{opponents_bubbles_amount}"
    if len(list_of_bubbles) == 2:
      player_deck[list_of_bubbles[0]].multiple_fight(player_deck[list_of_bubbles[1]],None,None,None,opponents_first_bubble,second,third,fourth,fifth,bubble_amount,kind)
    if len(list_of_bubbles) == 3:
      player_deck[list_of_bubbles[0]].multiple_fight(player_deck[list_of_bubbles[1]],player_deck[list_of_bubbles[2]],None,None,opponents_first_bubble,second,third,fourth,fifth,bubble_amount,kind)
    if len(list_of_bubbles) == 4:
      player_deck[list_of_bubbles[0]].multiple_fight(player_deck[list_of_bubbles[1]],player_deck[list_of_bubbles[2]],player_deck[list_of_bubbles[3]],None,opponents_first_bubble,second,third,fourth,fifth,bubble_amount,kind)
    if len(list_of_bubbles) == 5:
      player_deck[list_of_bubbles[0]].multiple_fight(player_deck[list_of_bubbles[1]],player_deck[list_of_bubbles[2]],player_deck[list_of_bubbles[3]],player_deck[list_of_bubbles[4]],opponents_first_bubble,second,third,fourth,fifth,bubble_amount,kind)



    


  def battle_validation(tier, catch, fight, bubble, player, player_bubble_amt): 
    battle_valid_used.clear()
    if fight == True:
      done_choosing_fighting_bubble_in_battle_validation_1 = False #doing very long names so we can use shorter names of vars in the storyline

      while done_choosing_fighting_bubble_in_battle_validation_1 == False:
        delay_print("\nPick a bubble:\n")
        for i in range(len(deck_name)):
          print(i+1,": ",deck_name[i])
        delay_print("\n(Type the number of the bubble you want to use)\n")
        fighting_bubble = input("")
        try:
          fighting_bubble = int(fighting_bubble)
          if fighting_bubble > len(player_deck):
            print("That is not an option")
          elif fighting_bubble <= 0:
            print("That is not an option")
          else:
            fighting_bubble -= 1
            done_choosing_fighting_bubble_in_battle_validation_1 = True
        except ValueError:
          print("That is not an option")
      battle_valid_used.append(fighting_bubble)
      player_deck[fighting_bubble].fight(bubble,"battle",0)

    elif catch == True:
      done_choosing_attacking_bubble = False
      for i in range(len(deck_name)):
        print(i+1,": ", deck_name[i])
      delay_print("\nPick a bubble:\n(Type the number of the bubble you want to use)\n")
      while done_choosing_attacking_bubble == False:
        fighting_bubble = input("")
        try:
          fighting_bubble = int(fighting_bubble)
          if fighting_bubble > len(deck_name):
            print("That is too high")
          elif fighting_bubble <= 0:
            print("That is too small")
          else:
            fighting_bubble -= 1
            done_choosing_attacking_bubble = True
        except ValueError:
          print("Try again")
      battle_valid_used.append(fighting_bubble)
      player_deck[fighting_bubble].fight(tier[random.randint(0,len(tier)-1)],"capture",10)

    elif fight == "contest":
      delay_print("\nPick a bubble:\n")
      for i in range(len(deck_name)):
        print(i+1,": ",deck_name[i])
      delay_print("\n(Type the number of the bubble you want to use)\n")
      fighting_bubble = input("")

      while not fighting_bubble.isdigit():
        fighting_bubble=input("Type a number ")
        while not fighting_bubble.isdigit():
          break
        else:
          break
          break
      else:
        while int(fighting_bubble) > int(len(deck_name)):
          delay_print("\nSorry, that is not a valid choice, please try again.\n")
          delay_print("\nPick a bubble:\n")
          for i in range(len(deck_name)):
            print(i+1,": ",deck_name[i])
          delay_print("\n(Type the number of the bubble you want to use)\n")
          fighting_bubble = input("")

        while not fighting_bubble.isdigit():
          delay_print("Try again ")
          fighting_bubble = input("")
          while not fighting_bubble.isdigit():
            break
          else:
            fighting_bubble = int(fighting_bubble)-1
            break
        else:
          fighting_bubble = int(fighting_bubble)-1
        battle_valid_used.append(fighting_bubble)
        player_deck[fighting_bubble].fight(bubble,"contest",0)


  def fight(self, Bubble2, kind, chance): #fight ################

    accurate_level = random.randint(max(1,self.level-Bubble2.level),self.level+5)
    level_up = accurate_level - Bubble2.level
    Bubble2.healthc+=level_up
    for i in range(int(Bubble2.total_moves)):
      Bubble2.moves_damage[i] += level_up
    Bubble2.level = accurate_level


    self.bars = self.healthc
    self.energy = self.energyc

    self_health = [self.bars]
    self_energy = [self.energy]

    Bubble2.bars = Bubble2.healthc
    Bubble2.energy = Bubble2.energyc

    oppo_health = [Bubble2.bars]
    oppo_energy = [Bubble2.energy]

    kind.lower()
    win = ""
    if (self.level > 99):
      self.level_MAX = True
    else:
      self.level_MAX=False


  
    
    # Allow two Bubbles to fight each other

    # Print fight information
    print("\n-----BATTLE-----")
    animation = random.randint(1,3)
    print(f"\n{self.name}:\nType: {self.bubble_type}\n{bcolors.GRASS_TYPE}Health: {self.bars}\n{bcolors.FIRE_TYPE}Level: {self.level}\n{bcolors.ELECTRIC_TYPE}Speed: {self.speed}{bcolors.NORMAL_AND_AIR_TYPE}\n{self.move_one} ({self.move_one_type}): Does {self.move_one_damage} damage + {self.move_one_energy} energy\n{self.move_two} ({self.move_two_type}): Does {self.move_two_damage} + {self.move_two_energy} energy\n{self.move_three} ({self.move_three_type}): Does {self.move_three_damage} damage - {self.move_three_energy} energy\n{self.move_four} ({self.move_four_type}): Does {self.move_four_damage} - {self.move_four_energy}\nThis bubble starts with {self.energy} energy.")
    if (animation == 1):
      delay_print("\            /     —————————— \n")
      delay_print(" \          /     |           \n")
      delay_print("  \        /      |           \n")
      delay_print("   \      /        —————————— \n")
      delay_print("    \    /                   |\n")
      delay_print("     \  /                    |\n")
      delay_print("      \/     <>    —————————— \n")
    elif (animation == 2):
      delay_print("|||            |||     |||||||||||||||\n")
      delay_print(" |||          |||      |||            \n")
      delay_print("  |||        |||       |||            \n")
      delay_print("   |||      |||        |||||||||||||||\n")
      delay_print("    |||    |||                     |||\n")
      delay_print("     |||  |||                      |||\n")
      delay_print("      ||||||   <<>>    |||||||||||||||\n")
    elif(animation == 3):
      delay_print("–––––––––––V.S–––––––––––")
    print(f"\n{Bubble2.name}:\nType: {Bubble2.bubble_type}\n{bcolors.GRASS_TYPE}Health: {Bubble2.bars}\n{bcolors.FIRE_TYPE}Level: {Bubble2.level}{bcolors.ELECTRIC_TYPE}\nSpeed: {Bubble2.speed}{bcolors.NORMAL_AND_AIR_TYPE}\n{Bubble2.move_one} ({Bubble2.move_one_type}): Does {Bubble2.move_one_damage} damage + {Bubble2.move_one_energy} energy\n{Bubble2.move_two} ({Bubble2.move_two_type}): Does {Bubble2.move_two_damage} + {Bubble2.move_two_energy} energy\n{Bubble2.move_three} ({Bubble2.move_three_type}): Does {Bubble2.move_three_damage} damage - {Bubble2.move_three_energy} energy\n{Bubble2.move_four} ({Bubble2.move_four_type}): Does {Bubble2.move_four_damage} - {Bubble2.move_four_energy}\nThis bubble starts with {Bubble2.energy} energy.")
    time.sleep(2)

    # Print the health and name of each Bubble
    print(f"{self.name}\t\tHP\t{self.bars}")
    print(f"{Bubble2.name}\t\tHP\t{Bubble2.bars}")
    print(f"Go, {Bubble2.name}!\n")
    print(f"Go, {self.name}!\n")

    if(self.speed>Bubble2.speed):
      delay_print("Your bubble is faster, so it goes first!\n")
      turn=0 #turn 0 is your turn
      
    if(self.speed<Bubble2.speed):
      delay_print(f"{Bubble2.name} is faster, so it goes first!\n")
      turn=1 #this means it is the computer's turn
      
    if(self.speed == Bubble2.speed):
      delay_print("The speeds are the same, so the first attacker is declared randomly, please wait \n\n")
      turn=random.randint(0,1) #returns a random number in the range of 1 and 2
      


    # Now for the actual fighting...
    # Continue when each Bubble still has health
    while (self_health[0] > 0) and (oppo_health[0] > 0):
      indent = ' '*max(0,len(self.name)-len(Bubble2.name)) #these two indents are here to even out the spaces between the two names and the health
      indent2 = ' '*max(0,len(Bubble2.name)-len(self.name)+4)
      while turn == 0: #your turn
        if(oppo_energy[0] < 0):
          oppo_health[0] -= 5
          delay_print(f"{Bubble2.name} used up all its energy and lost 5 health!\n")
        delay_print("It is your turn!\n\n")
        delay_print(f"{Bubble2.name}: {indent}{oppo_health[0]} Health\n\nYour {self.name}: {indent2}{self_health[0]} Health\n\n")
        delay_print("Please Choose Your Move:\n\n")
        self.total_moves = int(self.total_moves)
        for i in range(self.total_moves):
          print(f"{i+1}: {self.moves[i]}.    (Gives {self.moves_energy[i]} energy. Does {self.moves_damage[i]} damage)\n")
        done_attacking = False
        while done_attacking == False:
          attack=input("(Type the number)\n" )
          try:
            attack = int(attack)
            if float(attack) > float(self.total_moves):
              delay_print("\nThat is not a valid choice, please try again.\n")
            else:
              done_attacking = True
          except ValueError:
            abcdefg = 0
            for i in range(self.total_moves):
              move_now = self.moves[i]
              if attack.lower() == move_now.lower():
                abcdefg = i+1
                done_attacking = True
            attack = abcdefg
            if done_attacking == False:
              print("That is not an option")

        
        attack = int(attack)-1 #subtracts one because all lists start from 0
        oppo_health[0]-=self.moves_damage[attack]
        self_energy[0]+=self.moves_energy[attack] #this will subtract the energy from the third and forth move because the third and forth move from the list is multiplied by -1
        delay_print(f"{self.name} used {self.moves[attack]} and did {self.moves_damage[attack]} damage!\n{self.name} has {self_energy[0]} energy left.\n")
        if(oppo_health[0]>0):
          turn=1 
          break
        else:
          break
      while turn == 1 and Bubble2.bars>0: #computer's turn
        if(self_energy[0] < 0):
          self_health[0] -= 5
          delay_print(f"{self.name} used up all of its energy and lost 5 health!\n")
        if oppo_health[0] <= 0:
          break
        move=random.randint(0,Bubble2.total_moves - 1)
        oppo_energy[0]+=Bubble2.moves_energy[move]
        self_health[0]-=Bubble2.moves_damage[move]
        delay_print(f"{Bubble2.name} used {Bubble2.moves[move]} and did {Bubble2.moves_damage[move]} damage!\n{Bubble2.name} has {oppo_energy[0]} energy left!\n")
        turn=0
        break
    if(self_health[0]<=0 or oppo_health[0]<=0):
      if(self_health[0]<=0):
        delay_print("You lost...\n\n")
        win = False
        if kind == "battle":
          amount_of_money = random.randint(15, 20)
          amount_of_money *= 10
          for i in range(amount_of_money):
            money.remove(money[0])
            if len(money) == 0:
              money.clear()
          delay_print(f"You paid the opponent ${amount_of_money}.\n")
        self.XP + 10
        if self.XP >= self.XP_MAX:
          self.XP - self.XP_MAX
          self.XP_MAX * 1.1
          self.level + 1
          delay_print(f"\n{self.name} has leveled up!\nNow it is on level {self.level}!\n")

          self.level_MAX = False

          if self.level == 100:
            self.level_MAX = True
              
            delay_print(f"\n{self.name} is at level 100.\nIt cannot level up anymore because 100 is the maximum level that a bubble can attain.\n")
              
            self.level_MAX = True
              
            while self.level_MAX == True:
              self.XP = 0
        print(f"Good job! {self.name} needs {self.XP_MAX - self.XP} more XP to reach level {self.level+1}!")
      else:
        if(kind=="battle"):
          delay_print("You Won!\n\n")
          amount_of_money = random.randint(15, 20)
          amount_of_money * 10
          for i in range(amount_of_money):
            money.append(1)
          delay_print(f"The opponent paid you ${amount_of_money}!\n")
          self.XP += 20
          if random.randint(1,2) == 1:
            shop(random.randint(10,15), random.randint(10,15))
          win == True
          if self.XP >= self.XP_MAX:
            self.XP -= self.XP_MAX
            self.XP_MAX *= 1.1
            self.level += 1
            self.healthc += 1
            self.move_one_damage += 1
            self.move_two_damage += 1
            if self.total_moves == 3: #in case you have like fake or something
              self.move_three_damage += 1
            if self.total_moves == 4:
              self.move_four_damage += 1
              self.move_three_damage += 1
            delay_print(f"\n{self.name} has leveled up!\nNow it is on level {self.level}!\n")

            self.level_MAX = False

            if self.level == 100:
              self.level_MAX = True
                
              delay_print(f"\n\n{self.name} is at level 100.\nIt cannot level up anymore because 100 is the maximum level that a bubble can attain.\n")
                
              while self.level_MAX == True:
                self.XP = 0

            if self.level >= self.evolution_level:
              delay_print(f"WOW! {self.name} is evolving to {self.evolution.name} because it reached level {self.evolution_level}\n")
              delay_print(f"{self.evolution.stats}\n")
              player_deck.append(self.evolution)
              deck_name.append(self.evolution.name)
              player_deck.remove(self)
              deck_name.remove(self.name)
            else:
              delay_print(f"\nGood job! {self.name} needs {self.XP_MAX - self.XP} more XP to reach level {self.level+1}!")
        if(kind=="capture"):
          attempts = 0
          delay_print(f"You won, do you want to capture the bubble, the chances are 1 in {chance}.\nPress y to capture\n")
          print(f"You have {len(capture_disc_count)} capture discs")
          capture=input("")
          done_catching = False
          berry_done = False
          if(capture=='y'):
            while(len(capture_disc_count) > 0 and done_catching == False):
              capture_disc_count.remove(capture_disc_count[0])
              while berry_done == False:
                berry_amount=input(f"How many berries do you use?\n(You have {len(berries)} berries)\n")
                try:
                  berry_amount = int(berry_amount)
                  if berry_amount > len(berries):
                    print("You do not have this many...")
                  elif berry_amount < 0:
                    print("Sorry, you must enter a number 0 or greater")
                  else:
                    for i in range(berry_amount):
                      berries.remove(berries[0])
                    print(f"Now you have {len(berries)} berries left!")
                    berry_done = True
                except ValueError:
                  delay_print("Sorry, that is not an option\n")
              chance -= berry_amount
              if chance <= 1:
                chance = 1
              berry_amount = 0
              print(f"Now the chances are 1 in {chance}!")
              captured = random.randint(1,chance)
              if captured == 1 or captured == chance:
                player_bubbles.append(Bubble2)
                bubble_names.append(Bubble2.name)
                print("You caught the bubble!")

                if len(player_bubbles) > 5:
                  delay_print(f"\nYou do not have enough space in your party to add {Bubble2.name} to your party.\n")
                  change_deck()
                else:
                  delay_print(f"\nYou added {Bubble2.name} to your party!\n")
                  player_deck.append(Bubble2)
                  deck_name.append(Bubble2.name)
                done_catching = True
              else:
                if attempts <= 5:
                  print("The bubble escaped...")
                  catch_again = input(f"Try again? (The berries haven't worn off! You have {len(capture_disc_count)} capture discs.) y/n\n")
                  if catch_again == "y":
                    attempts += 1
                    if attempts > 5:
                      print("The bubble ran away!\n")
                      done_catching = True
                  if catch_again != "y":
                    done_catching = True
            if len(capture_disc_count) <= 0:
              delay_print("You do not have any more capture discs.\n")
              done_catching = True

        if (kind.lower() == "contest"):
          if self.bars <= 0:
            lost_contest_1.append(0)
      if(self_health[0] > oppo_health[0]):
        delay_print(f"\n{self.name} is happy that it won!\n\n")
        actions = input(f"\n1: Change Name (current: {self.name} Cost: $100)\n\n2: Upgrade base energy (Cost: $1500 = +2 base energy)\n3: Upgrade base health (Cost $1500 = +2 base health)\n(Warning: Base Energy and Base Health will reset once a bubble evolves)\n\n4: Level up Bubble (Cost: ${(self.XP_MAX-self.XP)*30})\n(Type the number of the action you want to make)\n")
        if actions == "1":
          if len(money) >= 100:
            for i in range(100):
              money.remove(money[0])
            name = input("What should the new name of your bubble be?\n")
            self.name = name
            deck_name.remove(deck_name[battle_valid_used[0]])
            deck_name.insert(battle_valid_used[0],name)
          else:
            print(f"Sorry, you only have ${len(money)}\n")
        if actions == "2":
          if len(money) >= 1500:
            for i in range(1500):
              money.remove(money[0])
            self.energyc += 2
            print(f"Your bubble's base energy rose to {self.energyc}\n")
          else:
            print(f"Sorry, you only have ${len(money)}\n")
        if actions == "3":
          if len(money) >= 1500:
            for i in range(1500):
              money.remove(money[0])
            self.healthc += 2
            print(f"Your bubble's health capacity is now {self.healthc}!\n")
          else:
            print(f"Sorry, you only have ${len(money)}\n")
        if actions == "4":
          if len(money) > (self.XP_MAX-self.XP)*30:
            for i in range(int((self.XP_MAX-self.XP)*30)):
              money.remove(money[0])
            self.level += 1
            self.XP = 0
            self.XP_MAX*=1.1
            self.XP_MAX = round(self.XP_MAX,1)
            print(f"Your bubble is now on level {self.level}! (If it is at evolution level, it will evolve during the next battle you win.)\n")
            delay_print(f"{self.name} needs {self.XP_MAX-self.XP} more XP to level up!\n")
          else:
            print(f"Sorry, you only have ${len(money)}")
  def multiple_fight(self1,self2,self3,self4,self5,bubble1,bubble2,bubble3,bubble4,bubble5,bubbles_battling,battle_type):
    money_bet = random.randint(15,20)*10
    print(f"You agreed to bet {money_bet}")

    try:
    
      if not bubbles_battling.isdigit():
        odds = True
    except AttributeError:
      odds = False

    if battle_type == 'contest':
      contest = True
    else:
      contest = False
    
    if battle_type == 'EVIL_Grunt':
      print("You are battling a grunt from E.V.I.L!!!")
      grunt = True
    else:
      grunt = 1


    if odds == False:

      if(bubbles_battling == 1):

        accurate_level = random.randint(max(1,self1.level-bubble1.level),self1.level+5)
        level_up = accurate_level - bubble1.level
        bubble1.healthc+=level_up
        for i in range(int(bubble1.total_moves)):
          bubble1.moves_damage[i] += level_up
        bubble1.level = accurate_level

        self1.bars = self1.healthc

        self1.energy = self1.energyc

        bubble1.bars = bubble1.healthc

        bubble1.energy = bubble1.energyc

        self_bubbles = [self1.name]
        self_bubbles_health = [self1.bars]
        self_bubbles_energy = [self1.energy]
        self_bubbles_moves = [self1.moves]
        self_bubbles_moves_energy = [self1.moves_energy]
        self_moves_damage = [self1.moves_damage]
        self_bubbles_total_moves = [self1.total_moves]

        oppo_bubbles = [bubble1.name]
        oppo_bubbles_health = [bubble1.bars]
        oppo_bubbles_energy = [bubble1.energy]
        oppo_bubbles_moves = [bubble1.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage]
        oppo_bubbles_total_moves = [bubble1.total_moves]

      if(bubbles_battling == 2):

        accurate_level = random.randint(max(1,self1.level-bubble1.level),self1.level+5)
        level_up = accurate_level - bubble1.level
        bubble1.healthc+=level_up
        for i in range(int(bubble1.total_moves)):
          bubble1.moves_damage[i] += level_up
        bubble1.level = accurate_level

        accurate_level = random.randint(max(1,self2.level-bubble2.level),self2.level+5)
        level_up = accurate_level - bubble2.level
        bubble2.healthc+=level_up
        for i in range(int(bubble2.total_moves)):
          bubble2.moves_damage[i] += level_up
        bubble2.level = accurate_level

        self1.bars = self1.healthc
        self2.bars = self2.healthc

        self1.energy = self1.energyc
        self2.energy = self2.energyc

        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc

        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc

        self_bubbles = [self1.name,self2.name]
        self_bubbles_health = [self1.bars, self2.bars]
        self_bubbles_energy = [self1.energy, self2.energy]
        self_bubbles_moves = [self1.moves, self2.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage]
        self_bubbles_total_moves = [self1.total_moves, self2.total_moves]

        oppo_bubbles = [bubble1.name,bubble2.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage]
        oppo_bubbles_total_moves = [bubble1.total_moves, bubble2.total_moves]

      if(bubbles_battling == 3):

        accurate_level = random.randint(max(1,self1.level-bubble1.level),self1.level+5)
        level_up = accurate_level - bubble1.level
        bubble1.healthc+=level_up
        for i in range(int(bubble1.total_moves)):
          bubble1.moves_damage[i] += level_up
        bubble1.level = accurate_level

        accurate_level = random.randint(max(1,self2.level-bubble2.level),self2.level+5)
        level_up = accurate_level - bubble2.level
        bubble2.healthc+=level_up
        for i in range(int(bubble2.total_moves)):
          bubble2.moves_damage[i] += level_up
        bubble2.level = accurate_level

        accurate_level = random.randint(max(1,self3.level-bubble3.level),self3.level+5)
        level_up = accurate_level - bubble3.level
        bubble3.healthc+=level_up
        for i in range(int(bubble3.total_moves)):
          bubble3.moves_damage[i] += level_up
        bubble3.level = accurate_level

        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc


        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc



        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc


        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc

        self_bubbles = [self1.name,self2.name,self3.name]
        self_bubbles_health = [self1.bars, self2.bars, self3.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage]
        

        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage]
        oppo_bubbles_total_moves = [bubble1.total_moves,bubble2.total_moves,bubble3.total_moves]

      if(bubbles_battling == 4):

        accurate_level = random.randint(max(1,self1.level-bubble1.level),self1.level+5)
        level_up = accurate_level - bubble1.level
        bubble1.healthc+=level_up
        for i in range(int(bubble1.total_moves)):
          bubble1.moves_damage[i] += level_up
        bubble1.level = accurate_level

        accurate_level = random.randint(max(1,self2.level-bubble2.level),self2.level+5)
        level_up = accurate_level - bubble2.level
        bubble2.healthc+=level_up
        for i in range(int(bubble2.total_moves)):
          bubble2.moves_damage[i] += level_up
        bubble2.level = accurate_level

        accurate_level = random.randint(max(1,self3.level-bubble3.level),self3.level+5)
        level_up = accurate_level - bubble3.level
        bubble3.healthc+=level_up
        for i in range(int(bubble3.total_moves)):
          bubble3.moves_damage[i] += level_up
        bubble3.level = accurate_level

        accurate_level = random.randint(max(1,self4.level-bubble4.level),self4.level+5)
        level_up = accurate_level - bubble4.level
        bubble4.healthc+=level_up
        for i in range(int(bubble4.total_moves)):
          bubble4.moves_damage[i] += level_up
        bubble4.level = accurate_level

        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc
        self4.bars = self4.healthc

        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc
        self4.energy = self4.energyc


        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc
        bubble4.bars = bubble4.healthc

        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc
        bubble4.energy = bubble4.energyc

        self_bubbles = [self1.name,self2.name,self3.name,self4.name]
        self_bubbles_health = [self1.bars, self2.bars, self3.bars, self4.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy, self4.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves, self4.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy, self4.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage, self4.moves_damage]
        self_bubbles_total_moves = [self1.total_moves, self2.total_moves, self3.total_moves, self4.total_moves]
        
        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name,bubble4.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars, bubble4.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy, bubble4.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves, bubble4.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy, bubble4.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage, bubble4.moves_damage]
        oppo_bubbles_total_moves = [bubble1.total_moves,bubble2.total_moves,bubble3.total_moves,bubble4.total_moves]

      if bubbles_battling == 5:

        accurate_level = random.randint(max(1,self1.level-bubble1.level),self1.level+5)
        level_up = accurate_level - bubble1.level
        bubble1.healthc+=level_up
        for i in range(int(bubble1.total_moves)):
          bubble1.moves_damage[i] += level_up
        bubble1.level = accurate_level

        accurate_level = random.randint(max(1,self2.level-bubble2.level),self2.level+5)
        level_up = accurate_level - bubble2.level
        bubble2.healthc+=level_up
        for i in range(int(bubble2.total_moves)):
          bubble2.moves_damage[i] += level_up
        bubble2.level = accurate_level

        accurate_level = random.randint(max(1,self3.level-bubble3.level),self3.level+5)
        level_up = accurate_level - bubble3.level
        bubble3.healthc+=level_up
        for i in range(int(bubble3.total_moves)):
          bubble3.moves_damage[i] += level_up
        bubble3.level = accurate_level

        accurate_level = random.randint(max(1,self4.level-bubble4.level),self4.level+5)
        level_up = accurate_level - bubble4.level
        bubble4.healthc+=level_up
        for i in range(int(bubble4.total_moves)):
          bubble4.moves_damage[i] += level_up
        bubble4.level = accurate_level

        accurate_level = random.randint(max(1,self5.level-bubble5.level),self5.level+5)
        level_up = accurate_level - bubble5.level
        bubble5.healthc+=level_up
        for i in range(int(bubble5.total_moves)):
          bubble5.moves_damage[i] += level_up
        bubble5.level = accurate_level

        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc
        self4.bars = self4.healthc
        self5.bars = self5.healthc
        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc
        self4.energy = self4.energyc
        self5.energy = self5.energyc

        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc
        bubble4.bars = bubble4.healthc
        bubble5.bars = bubble5.healthc
        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc
        bubble4.energy = bubble4.energyc
        bubble5.energy = bubble5.energyc

        self_bubbles = [self1.name,self2.name,self3.name,self4.name,self5.name] 
        self_bubbles_health = [self1.bars, self2.bars, self3.bars, self4.bars, self5.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy, self4.energy, self5.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves, self4.moves, self5.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy, self4.moves_energy, self5.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage, self4.moves_damage, self5.moves_damage]
        self_bubbles_total_moves = [self1.total_moves, self2.total_moves, self3.total_moves,self4.total_moves,self5.total_moves]


        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name,bubble4.name,bubble5.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars, bubble4.bars, bubble5.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy, bubble4.energy, bubble5.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves, bubble4.moves, bubble5.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy, bubble4.moves_energy, bubble5.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage, bubble4.moves_damage, bubble5.moves_damage]
        oppo_bubbles_total_moves = [bubble1.total_moves,bubble2.total_moves,bubble3.total_moves,bubble4.total_moves,bubble5.total_moves]
    else:
      char_num = 0
      for char in bubbles_battling:
        char_num += 1
        if char_num == 1:
          oppo_bubbles_amount = int(char)
        if char_num == 3:
          your_bubbles_amount = int(char)
      if your_bubbles_amount == 5:
        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc
        self4.bars = self4.healthc
        self5.bars = self5.healthc
        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc
        self4.energy = self4.energyc
        self5.energy = self5.energyc
        self_bubbles = [self1.name,self2.name,self3.name,self4.name,self5.name] 
        self_bubbles_health = [self1.bars, self2.bars, self3.bars, self4.bars, self5.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy, self4.energy, self5.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves, self4.moves, self5.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy, self4.moves_energy, self5.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage, self4.moves_damage, self5.moves_damage]

      if your_bubbles_amount == 4:
        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc
        self4.bars = self4.healthc

        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc
        self4.energy = self4.energyc
        self_bubbles = [self1.name,self2.name,self3.name,self4.name]
        self_bubbles_health = [self1.bars, self2.bars, self3.bars, self4.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy, self4.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves, self4.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy, self4.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage, self4.moves_damage]
      if your_bubbles_amount == 3:

        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self3.bars = self3.healthc


        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self3.energy = self3.energyc
        self_bubbles = [self1.name,self2.name,self3.name]
        self_bubbles_health = [self1.bars, self2.bars, self3.bars]
        self_bubbles_energy = [self1.energy, self2.energy, self3.energy]
        self_bubbles_moves = [self1.moves, self2.moves, self3.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy, self3.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage, self3.moves_damage]
      if your_bubbles_amount == 2:
        self1.bars = self1.healthc
        self2.bars = self2.healthc
        self1.energy = self1.energyc
        self2.energy = self2.energyc
        self_bubbles = [self1.name,self2.name]
        self_bubbles_health = [self1.bars, self2.bars]
        self_bubbles_energy = [self1.energy, self2.energy]
        self_bubbles_moves = [self1.moves, self2.moves]
        self_bubbles_moves_energy = [self1.moves_energy, self2.moves_energy]
        self_moves_damage = [self1.moves_damage, self2.moves_damage]

      if your_bubbles_amount == 1:
        self1.bars = self1.healthc
        self1.energy = self1.energyc
        self_bubbles = [self1.name]
        self_bubbles_health = [self1.bars]
        self_bubbles_energy = [self1.energy]
        self_bubbles_moves = [self1.moves]
        self_bubbles_moves_energy = [self1.moves_energy]
        self_moves_damage = [self1.moves_damage]
      


      #time for your opponent's bubbles
      if oppo_bubbles_amount == 5:
        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc
        bubble4.bars = bubble4.healthc
        bubble5.bars = bubble5.healthc
        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc
        bubble4.energy = bubble4.energyc
        bubble5.energy = bubble5.energyc

        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name,bubble4.name,bubble5.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars, bubble4.bars, bubble5.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy, bubble4.energy, bubble5.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves, bubble4.moves, bubble5.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy, bubble4.moves_energy, bubble5.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage, bubble4.moves_damage, bubble5.moves_damage]

      if oppo_bubbles_amount == 4:
        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc
        bubble4.bars = bubble4.healthc

        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc
        bubble4.energy = bubble4.energyc
        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name,bubble4.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars, bubble4.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy, bubble4.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves, bubble4.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy, bubble4.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage, bubble4.moves_damage]
      if oppo_bubbles_amount == 3:

        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc
        bubble3.bars = bubble3.healthc

        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        bubble3.energy = bubble3.energyc
        oppo_bubbles = [bubble1.name,bubble2.name,bubble3.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars, bubble3.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy, bubble3.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves, bubble3.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy, bubble3.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage, bubble3.moves_damage]

      if oppo_bubbles_amount == 2:

        bubble1.bars = bubble1.healthc
        bubble2.bars = bubble2.healthc

        bubble1.energy = bubble1.energyc
        bubble2.energy = bubble2.energyc
        oppo_bubbles = [bubble1.name,bubble2.name]
        oppo_bubbles_health = [bubble1.bars, bubble2.bars]
        oppo_bubbles_energy = [bubble1.energy, bubble2.energy]
        oppo_bubbles_moves = [bubble1.moves, bubble2.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy, bubble2.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage, bubble2.moves_damage]

      if oppo_bubbles_amount == 1:

        bubble1.bars = bubble1.healthc
        bubble1.energy = bubble1.energyc
        oppo_bubbles = [bubble1.name]
        oppo_bubbles_health = [bubble1.bars]
        oppo_bubbles_energy = [bubble1.energy]
        oppo_bubbles_moves = [bubble1.moves]
        oppo_bubbles_moves_energy = [bubble1.moves_energy]
        oppo_moves_damage = [bubble1.moves_damage]


    lost_bubble = []
    lost_bubble.clear()
    if odds == False:
      for i in range(bubbles_battling):
        print(self_bubbles[i])
      print("----------VS----------")
      for i in range(bubbles_battling):
        print(oppo_bubbles[i])
    else:
      for i in range(len(self_bubbles)):
        print(self_bubbles[i])
      print("----------VS----------")
      for i in range(len(oppo_bubbles)):
        print(oppo_bubbles[i])


    turn = "0"
    input("\nWhen you battle multiple bubbles, the first attacker is decided by a coin flip.\nHeads or tails?\n")
    coin_result = random.randint(0,1)
    delay_print("The coin is flipping")
    for i in range(random.randint(3,5)):
      print(".")
      time.sleep(1)
    if(coin_result == 1):
      delay_print("You won!")
    else:
      delay_print("You lost...")
    turn = coin_result
    while len(self_bubbles_health)>0 and len(oppo_bubbles_health) >0:
      while turn == 1:
        for i in range(len(self_bubbles_energy)):
          if self_bubbles_energy[i] < 0:
            self_bubbles_health[i] -= 5
            print(self_bubbles[i], " lost 5 health because it has lower than 0 energy!")
        for i in range(len(self_bubbles_health)):
          if self_bubbles_health[i] <= 0:
            print(self_bubbles[i] , "has fainted!")
            lost_bubble.append(eval(self_bubbles[i].lower()))
            self_bubbles.remove(self_bubbles[i])
            self_bubbles_energy.remove(self_bubbles_energy[i])
            self_bubbles_health.remove(self_bubbles_health[i])
            self_bubbles_moves.remove(self_bubbles_moves[i])
            self_bubbles_moves_energy.remove(self_bubbles_moves_energy[i])
            break
        print(bcolors.WATER_TYPE)
        done_choosing = 1
        done_choosing_move = 1
        done_choosing_target = 1

        no_undo = False
        target_pass = False
        bubble_pass = False
        move_pass = False

        while no_undo == False:
          if bubble_pass == False:
            done_choosing = False
          bubble_pass = False
          while done_choosing == False:
            for i in range(len(self_bubbles)):
              print("\n",i+1,self_bubbles[i],"      Health: ",self_bubbles_health[i],"    (",self_bubbles_energy[i]," Energy)")
            if len(lost_bubble) >= 1 and len(revive) > 0:
              revive_bubble = input("\nUse U to revive a bubble.\n")
              if revive_bubble.lower() == 'u':
                if len(lost_bubble) == 1:
                  revive.remove(-1)
                  self_bubbles.append(lost_bubble[0].name)
                  self_bubbles_health.append(lost_bubble[0].health)
                  self_bubbles_energy.append(lost_bubble[0].energy)
                  self_bubbles_moves_energy.append(lost_bubble[0].moves_energy)
                if len(lost_bubble) > 1:
                  number = 0
                  for ele in lost_bubble:
                    print((int(number) + 1),':',ele.name)
                    number += 1
                  reviving_bubble = input("Which one do you want to revive?\n")
                  try:
                    reviving_bubble = int(reviving_bubble)-1
                    if reviving_bubble < 0:
                      print("That is not an option.\n")
                    else:
                      try:
                        revive.remove(-1)
                        self_bubbles.append(lost_bubble[reviving_bubble].name)
                        self_bubbles_health.append(lost_bubble[reviving_bubble].health)
                        self_bubbles_energy.append(lost_bubble[reviving_bubble].energy)
                        self_bubbles_moves_energy.append(lost_bubble[reviving_bubble].moves_energy) 
                      except IndexError:
                        print("Sorry, that was not an option.\n")
                  except ValueError:
                    print("Sorry that was not an option")
            attacking_bubble = input("\nWhich bubble do you use?\n")
            try:
              attacking_bubble = int(attacking_bubble)-1
              if attacking_bubble > len(self_bubbles) - 1:
                print("That is too high")
              elif attacking_bubble < 0:
                print("That is too small")
              else:
                done_choosing = True
            except ValueError:
              print("That is not an option")
          if target_pass == False:
            done_choosing_target = False
          target_pass = False
          done_choosing_target = False
          while done_choosing_target == False:
            for i in range(len(oppo_bubbles)):
              print("\n",i+1,oppo_bubbles[i],"    Health: ",oppo_bubbles_health[i]," Energy: ",oppo_bubbles_energy[i])
            attacking_who = input("\nWho do you attack? (Press k to undo the last move)\n")
            try:
              attacking_who = int(attacking_who)-1
              if(attacking_who > len(oppo_bubbles)-1):
                print("That is too high")
              elif attacking_who < 0:
                print("That is too small")
              else:
                done_choosing_target = True
            except ValueError:
              if attacking_who == "k":
                done_choosing = False
                done_choosing_target = True
                move_pass = True
              else:
                print("That is not an option")

          if move_pass == False:
            done_choosing_move = False
          move_pass = False
          while done_choosing_move == False:
            for i in range(len(self_bubbles_moves[attacking_bubble])):
              print("\n",i+1,self_bubbles_moves[attacking_bubble][i],"    Damage: ",self_moves_damage[attacking_bubble][i], f"  Gives: {self_bubbles_moves_energy[attacking_bubble][i]} energy")
            attacking_move = input("\nWhich move do you use?(Press k to re-choose your bubble, press r to re-choose target)\n")
            try:
              attacking_move = int(attacking_move)-1
              if(attacking_move == 3 and self_moves_damage[attacking_bubble][3] == 0):
                print("That is too high")
              elif attacking_move < 0:
                print("That is too small")
              else:
                done_choosing_move = True
                no_undo = True
            except ValueError:
              if attacking_move == "k":
                done_choosing_move = True
                done_choosing = False
                target_pass = True
              elif attacking_move == "r":
                done_choosing_move = True
                done_choosing_target = False
                bubble_pass = True
              else:
                print("That is not an option")


        oppo_bubbles_health[attacking_who] -= self_moves_damage[attacking_bubble][attacking_move]
        self_bubbles_energy[attacking_bubble] += self_bubbles_moves_energy[attacking_bubble][attacking_move]

        print(f"{self_bubbles[attacking_bubble]} used {self_bubbles_moves[attacking_bubble][attacking_move]} and left {oppo_bubbles[attacking_who]} with {oppo_bubbles_health[attacking_who]} health!")
        for i in range(len(oppo_bubbles_health)):
          if oppo_bubbles_health[i] <= 0:
            print("Your opponent's ",oppo_bubbles[i]," has fainted!")
            oppo_bubbles.remove(oppo_bubbles[i])
            oppo_bubbles_energy.remove(oppo_bubbles_energy[i])
            oppo_bubbles_health.remove(oppo_bubbles_health[i])
            oppo_bubbles_moves.remove(oppo_bubbles_moves[i])
            oppo_bubbles_moves_energy.remove(oppo_bubbles_moves_energy[i])
            break
        turn = 0
        break
      while turn == 0 and len(oppo_bubbles) != 0: #computer's turn
        for i in range(len(oppo_bubbles_health)):
          if oppo_bubbles_energy[i] < 0:
            oppo_bubbles_health[i] -= 5
            print(oppo_bubbles[i], " lost 5 health because it has lower than 0 energy!")
        print(bcolors.FIRE_TYPE)
        delay_print(f"\nIt is {opponent_name[0]}'s turn! ")
        random_bubble = random.randint(0,len(oppo_bubbles)-1) #the bubble the cpu chooses
        random_move = random.randint(0,len(oppo_bubbles_moves)-1) #the move the cpu uses
        while oppo_moves_damage[random_bubble][random_move] == 0 and random_move == 3 or oppo_moves_damage[random_bubble][random_move] == 0 and random_move == 4:
          random_move = random.randint(0,len(oppo_bubbles_moves)-1)
        random_target = random.randint(0,len(self_bubbles)-1) #the bubble the computer is attacking
        self_bubbles_health[random_target] -= oppo_moves_damage[random_bubble][random_move]
        oppo_bubbles_energy[random_bubble] += oppo_bubbles_moves_energy[random_bubble][random_move]
        delay_print(f"Your opponent's {oppo_bubbles[random_bubble]} used {oppo_bubbles_moves[random_bubble][random_move]} on {self_bubbles[random_target]}! Now your bubble has {self_bubbles_health[random_target]} health left\n")
        delay_print(f"{opponent_name[0]}'s attacking bubble now has {oppo_bubbles_energy[random_bubble]} energy left!\n")
        for i in range(len(self_bubbles_health)):
          if self_bubbles_health[i] <= 0:
            print(self_bubbles[i] , "has fainted!") 
            lost_bubble.append(eval(self_bubbles[i].lower()).health)
            print(lost_bubble)
            self_bubbles.remove(self_bubbles[i])
            self_bubbles_energy.remove(self_bubbles_energy[i])
            self_bubbles_health.remove(self_bubbles_health[i])
            self_bubbles_moves.remove(self_bubbles_moves[i])
            self_bubbles_moves_energy.remove(self_bubbles_moves_energy[i])
            break

        turn = 1
    if len(oppo_bubbles_health) > len(self_bubbles_health):
      print("\nYou lost...\n")
      print("\n'Haha! I beat you!'\n")
      print(f"You paid your opponent {money_bet} dollars")
      for i in range(money_bet):
        money.remove(money[0])
      delay_print(f"\nYou walked away with ${len(money)} ...")
      if contest == True:
        lost_contest_1.append(1)
    elif len(oppo_bubbles_health) < len(self_bubbles_health):
      print("\nYou win!\n")
      if odds != True:
        if bubbles_battling == 2:
          self2.XP += 20
          self1.XP += 20
          if self2.XP >= self2.XP_MAX:
            self2.level += 1
            print(f"{self2.name} is now on level {self2.level}!")
            over_level = self2.XP - self2.XP_MAX
            self2.XP = 0
            self2.XP_MAX *= 1.1
            self2.XP += over_level
            print(f"Now it needs {self2.XP_MAX-self2.XP} more XP to reach level {self2.level-1}!")
          if self1.XP >= self1.XP_MAX:
            self1.level += 1
            print(f"{self1.name} is now on level {self1.level}!")
            over_level = self1.XP - self1.XP_MAX
            self1.XP = 0
            self1.XP_MAX *= 1.1
            self1.XP += over_level
            print(f"Now it needs {self1.XP_MAX-self1.XP} more XP to reach level {self1.level-1}!")
        if bubbles_battling == 3:
          self2.XP += 20
          self1.XP += 20
          self2.XP += 20
          if self2.XP >= self2.XP_MAX:
            self2.level += 1
            print(f"{self2.name} is now on level {self2.level}!")
            over_level = self2.XP - self2.XP_MAX
            self2.XP = 0
            self2.XP_MAX *= 1.1
            self2.XP += over_level
            print(f"Now it needs {self2.XP_MAX-self2.XP} more XP to reach level {self2.level-1}!")
          if self1.XP >= self1.XP_MAX:
            self1.level += 1
            print(f"{self1.name} is now on level {self1.level}!")
            over_level = self1.XP - self1.XP_MAX
            self1.XP = 0
            self1.XP_MAX *= 1.1
            self1.XP += over_level
            print(f"Now it needs {self1.XP_MAX-self1.XP} more XP to reach level {self1.level-1}!")
        if bubbles_battling == 3:
          self2.XP += 20
          self1.XP += 20
          if self1.XP >= self1.XP_MAX:
            self1.level += 1
            print(f"{self1.name} is now on level {self1.level}!")
            over_level = self1.XP - self1.XP_MAX
            self1.XP = 0
            self1.XP_MAX *= 1.1
            self1.XP += over_level
            print(f"Now it needs {self1.XP_MAX-self1.XP} more XP to reach level {self1.level-1}!")
          if self2.XP >= self2.XP_MAX:
            self2.level += 1
            print(f"{self2.name} is now on level {self2.level}!")
            over_level = self2.XP - self2.XP_MAX
            self2.XP = 0
            self2.XP_MAX *= 1.1
            self2.XP += over_level
            print(f"Now it needs {self2.XP_MAX-self2.XP} more XP to reach level {self2.level-1}!")
          if self3.XP >= self3.XP_MAX:
            self3.level += 1
            print(f"{self3.name} is now on level {self3.level}!")
            over_level = self3.XP - self3.XP_MAX
            self3.XP = 0
            self3.XP_MAX *= 1.1
            self3.XP += over_level
            print(f"Now it needs {self3.XP_MAX-self3.XP} more XP to reach level {self3.level-1}!")
        if bubbles_battling == 4:
          self2.XP += 20
          self1.XP += 20
          if self2.XP >= self2.XP_MAX:
            self2.level += 1
            print(f"{self2.name} is now on level {self2.level}!")
            over_level = self2.XP - self2.XP_MAX
            self2.XP = 0
            self2.XP_MAX *= 1.1
            self2.XP += over_level
            print(f"Now it needs {self2.XP_MAX-self2.XP} more XP to reach level {self2.level-1}!")
          if self1.XP >= self1.XP_MAX:
            self1.level += 1
            print(f"{self1.name} is now on level {self1.level}!")
            over_level = self1.XP - self1.XP_MAX
            self1.XP = 0
            self1.XP_MAX *= 1.1
            self1.XP += over_level
            print(f"Now it needs {self1.XP_MAX-self1.XP} more XP to reach level {self1.level-1}!")
          if self3.XP >= self3.XP_MAX:
            self3.level += 1
            print(f"{self3.name} is now on level {self3.level}!")
            over_level = self3.XP - self3.XP_MAX
            self3.XP = 0
            self3.XP_MAX *= 1.1
            self3.XP += over_level
            print(f"Now it needs {self3.XP_MAX-self3.XP} more XP to reach level {self3.level-1}!")
          if self4.XP >= self4.XP_MAX:
            self4.level += 1
            print(f"{self4.name} is now on level {self4.level}!")
            over_level = self4.XP - self4.XP_MAX
            self4.XP = 0
            self4.XP_MAX *= 1.1
            self4.XP += over_level
            print(f"Now it needs {self4.XP_MAX-self4.XP} more XP to reach level {self4.level-1}!")
      print("\n'No! How did I lose?'\n")
      print(f"{opponent_name[0]} paid you ${money_bet}")
      for i in range(money_bet):
        money.append(1)
      print(f"Now you have ${len(money)}!")
      if grunt == True:
        lost_grunt_1.append(1)
    else:
      print("\nIt is a draw!\n")
      print("\n'I thought I was going to win!'\n")
    time.sleep(1)
    print(bcolors.NORMAL_AND_AIR_TYPE)


