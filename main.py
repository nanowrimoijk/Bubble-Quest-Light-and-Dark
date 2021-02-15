#Tools
#Ctrl + G lets you input a line to go to
#Ctrl + H lets you find and replace
#Ctrl + F lets you find anything

'''
UPDATES:


'''


'''
Goals:
Finish evolstone and potion and revive

Bubble Attack Effects:
1. Reduces the amount of damage done by the opponent on the next turn while doing a little damage.
2. Reduces the amount of damage done by the opponent on the next turn while gaining energy
3. Heals your bubble while doing a little bit of damage
4. Heals your bubble but uses your energy
5. Does x times the amount of damage your opponent did to you on his last turn.
6. Subtracts energy from opponent
7. Subtracts health from both bubbles until your bubble reaches 10 health
8. Subtracts health from both bubbles until one faints.
9. Switches bubble with another while doing a little damage.
10. Draining health from other bubble.
11. 
'''

'''
Bugs:
  Multi Battle (Revive):
    trouble adding variable (not variable name) into the list of knocked out bubbles because the name isn't defined in Bubble.py, only main.
    Other leaks are likely but can't be found until bug above gets patched.

	Battles in general: 
		when upgrading the stats of your own bubbles, it keeps those boosts when fighting that same bubble.
		example: upgraded the health of your "fake" to 41, next time you fight a "fake" it also has 41 health

  Typos:
    You agreed to bet 160
    change to:
      You agreed to bet [$]160 [for the battle]

		you get 10,000$
		change to:
			$10,000
'''
#
#
#
'''
Types:
Water
Fire
Electric
Grass
Rock
Poison
Dark
Light
Psychic
Fighting
Normal
Steel
Air

'''
from bubble import *
from bubblesNmoves import *
from search import *
import time
import sys
import random
#from move import Move
from os import system

#saving progress

#import save function here


#other stuff
confirm = ""
begin_delay_timer = 0.04




def float_txt(txt):
    txt = float(txt)


def string_txt(txt):
    txt = str(txt)


def int_txt(txt):
    txt = int(txt)


'''class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRASS_TYPE = '\033[32m'
    FIRE_TYPE = '\033[31m'
    WATER_TYPE = '\033[94m'
    ELECTRIC_TYPE = '\033[33m'
    PSYCHIC_AND_POISON_TYPE = '\033[35m'
    NORMAL_TYPE = "\033[0;37m'


#format
print(f"{bcolors.WARNING} <message here> {bcolors.ENDC}")
'''

#other vars
walk_around1 = False
answer = []
#player money
player_money = 0
#places
places = {
  'Professors lab': '(Starting)',
  'Ocean': '(Water types)',
  'Volcano': '(Fire types)',
  'Clouds': '(Electric types)',
  'Forest': '(Grass types)',
  'Mountains': '(Rock and Grass types)',
  'Swamps': '(Poison and Grass types)',
  'Town': '(Normal and Steel types)',
  'Castle': '(Pyschic and Dark types)',
  'Arena': '(Steel types and Battles)',
  'Shop': '(Where you buy stuff)'
}





def ask(question,return1,return2):
  done_answering = False
  answer.clear()
  while done_answering == False:
    delay_print(f"{question} {return1} or {return2}")
    no_name = input("\n")
    if no_name != return1 and no_name!= return2:
      if no_name == "c":
        change_deck()
        done_answering = True
      else:
        print("That is not a valid answer")
    elif no_name == return1:
      return return1
      done_answering = True
    elif no_name == return2:
      return return2
      done_answering = True


'''
#Bubble DEX
BUBBLE_DEX = {
  jab.stats,
  penta_spike.stats,
  spin.stats,
  slasher.stats,
  mow.stats,
  wall.stats,
  fake.stats,
  rip.stats,
  shield.stats,
  twin.stats,
  miner.stats,
  rager.stats,
  smasher.stats,
  cannonball.stats,
  gunner.stats,
  laser.stats,
  tank.stats,
}''' #uncomment if needed



def random_trainer(name, bubble1, bubble2, bubble3, bubble4, bubble5, bubbles, bubble6, bubble7, bubble8, bubble9, bubble10):
  accept_challenge = random.randint(1,4)
  trainer2_request = False
  try:
  	bubbles = int(bubbles)

  except ValueError:
    pass


  def random_bubble(bubble):
	  if(bubble == "f"):
		  bubble = tierf[random.randint(0,len(tierf)-1)]
	  if(bubble == "c"):
		  bubble = tierc[random.randint(0,len(tierc)-1)]
	  if(bubble == "b"):
		  bubble = tierb[random.randint(0,len(tierb)-1)]
	  if(bubble == "a"):
		  bubble = tiera[random.randint(0,len(tiera)-1)]
	  if(bubble == "s"):
		  bubble = tiers[random.randint(0,len(tiers)-1)]
	  if(bubble == "l"):
		  bubble = tierl[random.randint(0,len(tierl)-1)]
	  return bubble

  bubble1 = random_bubble(bubble1)
  bubble2 = random_bubble(bubble2)
  bubble3 = random_bubble(bubble3)
  bubble4 = random_bubble(bubble4)
  bubble5 = random_bubble(bubble5)

  delay_print(f"You are challenged by Trainer {name}!\n\n")
  opponent_name.clear()
  opponent_name.append(name)

  if "Grunt" in name:

      bubble6.multiple_fight(bubble7,bubble8,bubble9,bubble10,bubble1,bubble2,bubble3,bubble4,bubble5,bubbles,"EVIL_Grunt")

  elif bubbles == 2 or bubbles == 3 or bubbles == 4 or bubbles == 5:

    if "Grunt" in name:

      Bubble.multiple_fight_v(1,5,"EVIL_Grunt",bubble1,bubble2,bubble3,bubble4,bubble5)

    else:

      bubble6.multiple_fight(bubble7,bubble8,bubble9,bubble10,bubble1,bubble2,bubble3,bubble4,bubble5,bubbles,"")

  elif bubbles == 1:
    Bubble.battle_validation("f",False,True,bubble1,Person,len(player_deck))

  elif bubbles == "x":
    bubble_amount = input(f"Since this is a contest, you get to choose how many bubbles to battle with\n(max: {min(len(player_deck),5)})\n")
    try:
      bubble_amount = int(bubble_amount)
      if bubble_amount > len(player_deck) or bubble_amount > 5:
        print(f"{bubble_amount} was too high")
        trainer2_request = True
      else:
        if accept_challenge != 1:
          print(f"{opponent_name[0]} accepted!")
          time.sleep(1)
          system('clear')
          if bubble_amount == 1:
            Bubble.battle_validation("t",False,"contest",bubble1,Person,player_bubble_amt)
          elif bubble_amount == 2:
            Bubble.multiple_fight_v(2,2,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
          elif bubble_amount == 3:
            Bubble.multiple_fight_v(3,3,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
          elif bubble_amount == 4:
            Bubble.multiple_fight_v(4,4,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
          elif bubble_amount == 5:
            Bubble.multiple_fight_v(5,5,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
        else:
          print(f"They do not want a {bubble_amount} V {bubble_amount}")
          
          
    except ValueError:
      delay_print(f"When the judge asked you, you didn't say a number but said: '{bubble_amount}'. Since this was not a number, you lost your opportunity of choice.\n")
      time.sleep(1)
      system('clear')
      trainer2_request = True

    if accept_challenge == 1 or trainer2_request == True:
      random_vs = random.randint(1,len(player_deck))
      while random_vs == bubble_amount:
        random_vs = random.randint(1,min(len(player_deck),5))
      print(f"They want a {random_vs} V {random_vs}!")
      accept_challange_or_not = ask("Do you accept?","y","n")
      time.sleep(1)
      system('clear')
      if accept_challange_or_not == "y":
        if bubble_amount == 1:
            Bubble.battle_validation("t",False,"contest",bubble1,Person,player_bubble_amt)
        elif random_vs == 2:
          Bubble.multiple_fight_v(2,2,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
        elif random_vs == 3:
          Bubble.multiple_fight_v(3,3,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
        elif random_vs == 4:
          Bubble.multiple_fight_v(4,4,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
        elif random_vs == 5:
          Bubble.multiple_fight_v(5,5,"contest",bubble1,bubble2,bubble3,bubble4,bubble5)
      else:
        delay_print("No one agreed!\nNow we will be doing a 1 V 1 ! (but there's a twist! A random bubble is chosen from your 5 bubble deck and is used to fight!")
        time.sleep(1)
        system('clear')
        random_bubble_used_to_challenge = random.randint(0,len(player_deck)-1)
        player_deck[random_bubble_used_to_challenge].fight(bubble1,"contest",0)



'''def catch_wild_bubbles(tier,starting_point):
  if "grass" in starting_point.lower():
    wording = ["You followed some trail that led into a mysterious open area and heard some noises around you.","Some grass seemed to be flattened while something was passing by, you decide to follow the half hidden trail.","The grassland that you arrived at had very open space, but tall grass."]
    delay_print(random.choice(wording))
    delay_print("Just then, a bubble showed up!")

''' #idk if we need this, its kinda like battle validation

'''
def search():

    print("These are the bubbles in the Bubble-DEX")

    for i in range(len(search_names)):

        print(f"{1 + i}: {search_names[i]}")
    searching = input("")

    while not searching.isdigit():

        print("Please Type the number, not the name ")
        searching = input("")

        while not searching.isdigit:
            break

        else:
            searching = int(searching)
            delay_print(search_results[searching])
            again = input("Search again? y/n ")

            if (again == "y"):
                time.sleep(1)
                system('clear')
                search()

            break
            break

    else:
        searching = int(searching)
        print(search_results[searching - 1])
        again = input("Search again? y/n ")
        if (again == "y"):
            time.sleep(1)
            system('clear')
            search()
'''


def delay_print_begin(s):
    # print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(begin_delay_timer)


#############################################################
delay_print(
    f"Do you want to start the storyline?\nPress {bcolors.GREEN}y for yes{bcolors.WHITE} and {bcolors.RED}n for no.{bcolors.WHITE}\n"
)
storyline_start = input("")
storyline_start.lower()

while storyline_start != "y":
    delay_print(
        f"You have exited the storyline.\nYou can view the Bubble-DEX but {bcolors.BOLD}you cannot play the game unless you enter the storyline.{bcolors.END}\nDo you want to re-enter the storyline?\n(y or n)\n"
    )
    storyline_start_confirm = input("")

    if storyline_start_confirm == "y":
        storyline_start = "y"
        time.sleep(1)
        system('clear')

    if storyline_start_confirm != "y":
        delay_print(f"\nDo you want to view the {bcolors.YELLOW}BUBBLE_DEX?{bcolors.END}\n(y or n)\n")
        bubble_dex_start = input("")
        if bubble_dex_start == "y":
          time.sleep(1)
          system('clear')
          search()

    break

#Now for the storyline
while storyline_start == "y":
    game_start = True

    #Tiers

    tierf = [fake]

    tierc = [jab, mow, spin, rip, rager]

    tierb = [shield, cannonball, antser, gunner]

    tiera = [penta_spike, slasher, screen, miner, twin, smasher, laser]

    tiers = [tank]

    tierl = []


    delay_print(
        f"\n{bcolors.WATER_TYPE}BUBBLE QUEST:\n{bcolors.NORMAL_AND_AIR_TYPE}LIGHT {bcolors.WATER_TYPE}AND {bcolors.PSYCHIC_AND_POISON_TYPE}DARK\n{bcolors.WATER_TYPE}"
    )
    delay_print("---\n")
    delay_print("  ____            _       _       _              ____                         _ \n")
    delay_print(" |  _ \          | |     | |     | |            / __ \                       | |\n")
    delay_print(" | |_) |  _   _  | |__   | |__   | |   ___     | |  | |  _   _    ___   ___  | |_ \n")
    delay_print(" |  _ <| | | | | | '_ \  | '_ \  | |  / _ \    | |  | | | | | |  / _ \ / __| |  _|\n")
    delay_print(" | |_) | | |_| | | |_) | | |_) | | | |  __/    | |__| | | |_| | |  __/ \__ \ |  |_ \n")
    delay_print(" |____/   \__._| |_.__/  |_.__/  |_|  \___|     \___\_\  \__._|  \___| |___/  \___|\n")
    print(bcolors.NORMAL_AND_AIR_TYPE)
    print("\n5")
    time.sleep(1)
    print("\n4")
    time.sleep(1)
    print("\n3")
    time.sleep(1)
    print("\n2")
    time.sleep(1)
    print("\n1")
    time.sleep(1)
    print("\nSTARTING...")
    time.sleep(5)
    system('clear')

    player_bubble_amt = 0
    delay_print(f"Do you want to skip the tutorial?({bcolors.RED}Y{bcolors.END} or {bcolors.GREEN}N{bcolors.END})\n")
    skip_tutorial = input(str(''))
    time.sleep(1)
    system('clear')
    
    while skip_tutorial == 'N':


      delay_print(
          "Bubbles are mysterious creatures with magical powers.\nOur world is filled with these wonderful and powerful creatures.\nOnly three people every year are chosen to start their Bubble Quest here in my labratory.\n"
      )

      delay_print(
          "\nI am Professor 2.\nToday I will be helping you start your very own Bubble Quest, the same way I have helped many trainers before you.\n"
      )


      delay_print(
          "\nBefore you start your Bubble Quest, you will need a bubble to help you.\nYou can choose one from the three bubbles I have here.\n"
      )
      time.sleep(1)
      system('clear')

      delay_print("-You reach towards the bubbles.-\n")

      time.sleep(3)

      delay_print(
          "\nDon't choose yet! I need to tell you more about the rules!\nThe bubble with the higher speed goes first in a battle, but if they have the same speed the first attacker is declared randomly.\n"
      )

      delay_print(
          "\nWhen it's your turn, you use a move.\nLess powerful moves do less damage, but give you energy, the opposite happens for stronger moves, they do more damage, but use your energy.\nSpeaking of energy, if you don't have any energy left during a battle, your bubble loses health. In this region, they only lose 5 health.\n"
      )

      time.sleep(2)
      system('clear')

      delay_print(
          "Some bubbles can also evolve.\nFor example, Gunner bubble can evolve into Laser bubble once it reaches a certain level.\nAlso, once a bubble reaches a certain level, it can even learn a new move!\n"
      )

      delay_print(
          "\nNow that you know more about the rules of bubble quest, I think it is time for you to choose your bubble.\n"
      )
      break
    system('clear')

    delay_print("Please pick a bubble:")

    delay_print(f"\n{jab.stats}\n")

    delay_print(f"\n{spin.stats}\n")

    delay_print(f"\n{mow.stats}\n")

    delay_print("\nPlease choose a bubble --\n")
    bubble1 = input("")

    bubble1 = bubble1.lower()
    while bubble1.lower() != "jab" and bubble1.lower() != "spin" and bubble1.lower() != "mow":

      delay_print("That is not one of the bubbles")
      bubble1 = input(" ")

      while bubble1 != "jab" and bubble1!= "spin" and bubble1 != "mow":

        break

      else:

        bubble1.lower()

        player_bubbles == [
          None, None, None, None, None
        ]

        if (bubble1 == "mow"):
            player_deck.append(mow)
            deck_name.append("Mow")
            delay_print('You choose MOW!\n')
            player_bubble_amt += 1
        if (bubble1 == "jab"):
            player_deck.append(jab)
            deck_name.append("Jab")
            delay_print('You choose JAB!\n')
            player_bubble_amt += 1
        if (bubble1 == "spin"):
            player_deck.append(spin)
            deck_name.append("Spin")
            delay_print('You choose SPIN!\n')
            player_bubble_amt += 1

        break
    else:
      bubble1.lower()

      if (bubble1 == "mow"):
          player_deck.append(mow)
          deck_name.append("Mow")
          player_bubble_amt += 1
      if (bubble1 == "jab"):
          player_deck.append(jab)
          deck_name.append("Jab")
          player_bubble_amt += 1
      if (bubble1 == "spin"):
          player_deck.append(spin)
          deck_name.append("Spin")
          player_bubble_amt += 1

      delay_print(f"\n-You picked {bubble1.upper()}!-\n")
      time.sleep(1)
      system('clear')



    delay_print(
        "Now that you have a bubble, you should learn more about it.\nI have a device here called a Bubble-DEX that can tell you the stats of any bubble once you scan it.\nTry it.\n"
    )

    time.sleep(1)

    delay_print(
        "\n-You scanned the bubble you choose with your Bubble-DEX.-\n"
    )

    if bubble1 == 'jab':
      delay_print(f"{jab.stats}\n")

    if bubble1 == 'spin':
      delay_print(f"{spin.stats}\n")

    if bubble1 == 'mow':
      delay_print(f"{mow.stats}\n")

    delay_print(
        "\n-The professor gave you the Bubble-DEX and 50 capture discs to catch bubbles and sends you off on your journey.-\n"
    )

    time.sleep(1)
    system('clear')

    #updating the vars
    for i in range(50):
      capture_disc_count.append(1)


    delay_print("-You walk outside the room.-\n")

    delay_print(
        "-Just as you walk out of the lab somebody walks up to you.-\n")

    delay_print("Aha!\nA trainer!\nLet's battle!\n")

    delay_print("I choose you!\nFake bubble!\n")

    delay_print("-You scanned it with your Bubble-DEX.-\n")

    delay_print(f"{fake.stats}")

    time.sleep(3)
    system('clear')

    random_trainer('Jack', "f", "t", "t", "t", "t", 1, player_deck[0], None, None, None, None)
    
    delay_print(
        "\n-After beating the trainer, you headed forward on the path to continue your Bubble Quest.-\n"
    ) 



    left_or_right = ask(
      "-Soon, you arrived at a fork in the road.\nFrom what you see, you know that the left side leads to a forest and the right side leads to a clearing.\nFrom the map the professor gave you, you know that the roads will lead to the same place, but the paths are different.\nDo you go left or right?"
      ,"l","r"
    )

    time.sleep(1)
    system('clear')

    if left_or_right == 'l':
        delay_print(
            f"-You walked down the path that heads into the {bcolors.GREEN}forest{bcolors.END} and entered it.-\n"
        )

        delay_print("Inside the forest, you met some bubbles!\n")
        Bubble.battle_validation(tierb, True, False, None, Person, player_bubble_amt)
        Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)

        delay_print(
            "-After encountering the bubbles, you kept walking and saw something shiny on the ground!\nDo you pick it up?\n(y or n)-\n"
        )
        item1 = input("")

        if str(item1) == "y":
          delay_print("\nYou found a berry!\n")
          berries.append(1)

        else:
          delay_print("\n-You ignored the shiny thing and continued on your journey.-\n")

    time.sleep(1)
    system('clear')

    if left_or_right == 'r':
        delay_print(
            "-You walked down the path that heads into the clearing and entered it.-\n"
        )
        
        delay_print(
          "Two bubbles jumped out of the grass!\n"
        )
        Bubble.battle_validation(tierf, True, False, None, Person, player_bubble_amt)
        Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)

    delay_print(
      "There is a merchant sitting underneath a tree.\nDo you go to him?\n(y or n)\n"
    )
    merchant = input('')
    time.sleep(1)
    system('clear')
    if merchant == 'y':
      delay_print("He saw you and opened his shop.\n")
      shop(random.randint(10,15), random.randint(5,15))
      merchant == ''
    else:
      delay_print("You kept on walking.")
    delay_print(
        "-After a while, you see a building in the distance.\nDo you want to go there?\n(y or n)-\n"
    )
    building1 = str(input(""))

    while (building1 != 'y' and building1 != 'n'):
        delay_print("That is not a vaild answer please try again ")
        building1 = str(input(""))
        while (building1 != 'y' and building1 != 'n'):
            break
        else:
            break
            break

    contest1 = ""

    if building1 == 'y':
        delay_print(
            "\n-You head towards the building but a bubble jumps out of the grass!-\n"
        )

        time.sleep(1)
        system('clear')

        Bubble.battle_validation(tierb, True, False, None, Person, player_bubble_amt)

        delay_print(
            "\n-You continued to the building and once you got there, you saw a sign that showed that the building was home to a contest.-\n"
        )

        delay_print("-Do you want to join the contest?-\n-If you win, you get $10,000 and a lot of items!\n-")
        contest1 = str(input(""))

        time.sleep(1)
        system('clear')

    while building1 == 'n' or contest1 == 'n':
        delay_print(
            "\n-You decide to keep walking around and hopefully find some bubbles to catch.-\n"
        )
        walk_around1 = True
        break

    if walk_around1 == True:
      delay_print("\n-Two bubbles jump out of the grass!-\n")

      time.sleep(1)
      system('clear')

      Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)

      delay_print("\n Phew, one more to go...")

      time.sleep(1)
      system('clear')
      
      Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)

      print("You kept walking around and someone pulled you inside a building")

      contest1 = "y"

      time.sleep(1)
      system('clear')


    if contest1 == 'y' or contest1 == "yes":
      
      delay_print("-You entered the contest!-\n")
      delay_print(f"\n{player.name}, please go to Arena {random.randint(1, 10)}. Your match is about to begin.\n")
      delay_print("--------------------")

      delay_print(f"\n{player.name} V.S. Amy! Let the battle begin!\n")

      time.sleep(1)
      system('clear')

      random_trainer('Amy', 'c', "f", "f", "f", "f", "x", player_deck[0], None, None, None, None)

      if len(lost_contest_1) == 0:
        delay_print("\nCongrats!\nYou have now advanced to the next stage of the tournament!\n")
        delay_print("Do you want to start the next battle?\nIf you press c, you will be given an opportunity to change your deck before the fight begins. Or press y to continue to next battle (if you don't want to, press n)\n")
        start = input("\n")

        time.sleep(1)
        system('clear')
        
        if start == 'y':
          delay_print(f"\n{player.name}, please report to Arena {random.randint(1, 10)}. Your match is about to begin.\n")
          delay_print("--------------------")

          delay_print(f"\n{player.name} V.S. Ken! Let the battle begin!\n")

          time.sleep(1)
          system('clear')

          random_trainer('Ken', 'b', "c", "c", "b", "a", "x", player_deck[0], None, None, None, None)
          
        elif start != "n" and start != "y":
          change_deck()
          delay_print(f"\n{player.name}, please go to Arena {random.randint(1, 10) } Your match is about to begin.\n")
          delay_print("--------------------")

          delay_print(f"\n{player.name} V.S. Ken! Let the battle begin!\n")

          time.sleep(1)
          system('clear')

          random_trainer('Ken', 'b', "c", "f", "b", "a", "x", player_deck[0], None, None, None, None) 
          lost_contest_1.clear()

        if start != "n":
          if len(lost_contest_1) == 0:

            delay_print("Wow! You are such a strong trainer! There are only 8 trainers left in this contest!\n")
            read_tournament_1_sign = input("There is a sign ahead, would you like to read it?\nY or N\n")
            time.sleep(1)
            system('clear')
            if read_tournament_1_sign != "Y":
              delay_print("The next day, you finish breakfast and wait for your name to be called, but it never got called.\n")
              delay_print("You decide to wait a little longer.\n")
              delay_print("Waiting...")
              time.sleep(10)
              system('clear')
              delay_print("Finally, you give up waiting and walk around the propery and try to find someone who can knows what is happening, before you met someone, you encountered the same sign from yester day, you walk up to it and start reading.")

            time.sleep(1)
            system('clear')
              
            delay_print("\n\nThere are factors delaying the tournament, everyone's next round will be delayed until further notice. Sorry for your inconvenience\n\n")
          
            closed_down_contest = ask("Because there contest has tempoarily closed down, you have a chance to catch some more bubbles.\nDo you want to go?", 'Y', 'N')
          
            time.sleep(1)
            system('clear')

          if closed_down_contest == 'Y':
            delay_print("\nYou headed outside and met a thug bending some of the water pipes!")
            delay_print("\nYou walk towards him to talk.")
            delay_print("\n'Whaddaya want, punk?'")
            time.sleep(1)
            system('clear')
            random_trainer("Grunt A", 'c', 'f', 'f', 'f', 'f', "5" , player_deck[0], None, None, None, None)

            if len(lost_grunt_1) == 0:
              delay_print("\n'Gonna retreat back to H.Q. for now...'")
              delay_print("\nThe grunt ran away...")

            elif len(lost_grunt_1) == 1:
              delay_print("\n'Yes! I have defeated a trainer on behalf of E.V.I.L!'")
              delay_print("\nThe grunt ran away dancing...")
              lost_grunt_1.clear()

            time.sleep(1)
            system('clear')

            delay_print("\nThe loudspeaker buzzed and announced that the contests will resume tomorrow, telling everyone to have a nice day.\n")
            print("The quest has ended for now")
            print("It will be continued soon...")
            time.sleep(10)
            system('clear')







        if start == 'n':
          delay_print("You chickened out and went back to the lobby...\n")
          delay_print("Press n when you are ready for the fight.\n")
          start = input("")

          #is this WIP?

          time.sleep(1)
          system('clear')
        
        

      elif len(lost_contest_1) >= 1:
        delay_print("\nSorry, you were eliminated...\n")
        delay_print("You can still get back in the contest, but you will not get the prizes if you win.\n")
        delay_print("Do you want to re-enter? y or n\n")
        re_enter_contest = input("")
        time.sleep(1)
        system('clear')
        if re_enter_contest == "y":
          get_reward = False
          lost_contest_1.remove(1)
          

