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
7. Subtracts health from both bubbles until you bubble reaches 10 health
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
  Merchant:
    Forces you to buy stuff.
  Typos:
    You agreed to bet 160
    change to:
      You agreed to bet [$]160 [for the battle]
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
from bubble import lost_contest_1
from bubble import capture_disc_count
from bubble import berries
from bubble import opponent_name
from bubble import bubble_names
from bubble import player_bubbles
from bubble import delay_print
from bubble import bcolors
from bubble import Bubble
from bubble import Person
from bubble import player
from bubble import player_deck
from bubble import deck_name
from bubble import change_deck
from bubble import lost_grunt_1
from bubble import shop
from bubble import money
from bubble import health_potion
from bubble import strength_potion
from bubble import revive
import time
import sys
import random
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
      answer.append(return1)
      done_answering = True
    elif no_name == return2:
      answer.append(return2)
      done_answering = True



#Bubbles:

#Create a Bubble

#Format Example: bubble = Bubble('Name', 'Bubble Energy', 'First Move Name', 'Second Move Name', 'Third Move Name', 'Fourth Move Name', 'First Move Damage', 'Second Move Damage', 'Third Move Damage', 'Fourth Move Damage', 'First Move Energy', 'Second Move Energy', 'Third Move Energy', 'Fourth Move Energy', 'Bubble Speed', 'Bubble Health', 'level', 'XP', 'type')

penta_spike = Bubble('Penta-Spike', '9', 'Jab', 'Spike', 'Spike Ring',
                    'Spike Beam', '8', '16', '20', '28', '3', '2', '2', '7',
                    'Normal', 'Normal', 'Steel', 'Steel', '7', '88', '20',
                    '0', 'Normal', '4', '4', '9', '88','None_Yet', 'Unkown_For_Now')

jab = Bubble('Jab', '7', 'Cut', 'Jab', 'X-Cannon', 'NOT AVAILABLE', '12', '16',
            '24', '0', '4', '1', '5', '0', 'Normal', 'Normal', 'Normal',
            'NO TYPE', '3', '64', '1', '0', 'Normal', '3', '3', '7', '64', penta_spike, '20')

slasher = Bubble('Slasher', '11', 'Spin', 'Rollout', 'X-Slash', 'Slash Charge',
                '12', '16', '20', '32', '3', '0', '4', '5', 'Normal', 'Normal',
                'Steel', 'Normal', '13', '76', '20', '0', 'Normal', '4', '4', '11', '76','None_Yet', 'Unkown_For_Now')

spin = Bubble('Spin', '8', 'Slash', 'Spin', 'Rollout', 'NOT  AVAILABLE', '8',
              '12', '28', '0', '2', '1', '4', '0', 'Normal', 'Normal', 'Normal',
              'NO TYPE', '7', '52', '1', '0', 'Normal', '3', '3', '8', '52', slasher, '20')

screen = Bubble('Screen', '8', 'Block', 'Lawnmow', 'Spike Screen', 'Screen Ram','8',
              '16', '12', '28', '3', '0', '-3', '6', 'Normal', 'Normal', 'Normal',
              'Normal', '5', '96', '20', '0', 'Normal', '4', '4', '8', '96','None_Yet', 'Unkown_For_Now')

mow = Bubble('Mow', '6', 'Mow', 'Plow', 'Lawnmow', 'NOT AVAILABLE', '8', '12',
            '24', '0', '5', '1', '5', '0', 'Normal', 'Normal', 'Normal',
            'NO TYPE', '1', '68', '1', '0', 'Normal', '3', '3', '6', '68', screen, '20') 

fake = Bubble('Fake', '0', 'Bump', 'Crash', 'NOT AVAILABLE', 'NOT AVAILABLE',
              '1', '2', '0', '0', '0', '0', '0', '0', 'Normal', 'Normal',
              'NO TYPE', 'NO TYPE', '0', '1', '1', '0', 'Normal', '2', '2', '0', '1',None, None)

rip = Bubble('Rip', '7', 'Tear', 'Rip', 'Shred', 'NOT AVAILABLE', '8', '12',
            '20', '0', '2', '1', '4', '0', 'Normal', 'Fighting', 'Fighting',
            'NO TYPE', '5', '56', '1', '0', 'Fighting', '4', '3', '7', '56','None_Yet', 'Unkown_For_Now')

shield = Bubble('Shield', '5', 'Ram', 'Crash', 'Shield', 'Deflection Shield',
                '4', '8', '12', '24', '3', '2', '3', '5', 'Normal', 'Normal',
                'Steel', 'Steel', '3', '68', '1', '0', 'Steel', '4', '4', '5', '68','None_Yet', 'Unkown_For_Now')

smasher = Bubble('Smasher', '2', 'Uppercut', 'Quake Smash', 'Orbit Smash',
                'Deady Tornado Smash', '12', '16', '24', '36', '2', '1', '9',
                '10', 'Fighting', 'Fighting', 'Rock', 'Air', '1', '140', '1',
                '0', 'Fighting', '4', '4', '2', '140','None_Yet', 'Unkown_For_Now')

rager = Bubble('Rager', '3', 'Mad', 'Rage', 'Trigger', 'NOT AVAILABLE', '8',
              '12', '24', '0', '2', '0', '7', '0', 'Fighting', 'Fighting',
              'Fighting', 'NO TYPE', '5', '64', '1', '0', 'Fighting', '3', '3', '3', '64', smasher, '30')

twin = Bubble('Twin', '7', 'Fire Blast', 'Water Cannon', 'Fusion Beam',
              'NOT AVAILABLE', '16', '16', '28', '0', '2', '2', '7', '0', 'Fire',
              'Water', 'Psychic', 'NO TYPE', '7', '68', '1', '0', 'Psychic',
              '3', '3', '7', '68','None_Yet', 'Unkown_For_Now')

miner = Bubble('Miner', '5', 'Pebble Rain', 'Earthquake', 'Rock Toss',
              'NOT AVAILABLE', '12', '16', '24', '0', '3', '1', '5', '0', 'Rock',
              'Rock', 'Rock', 'NO TYPE', '5', '56', '1', '0', 'Rock', '3', '3', '5', '56','None_Yet', 'Unkown_For_Now')

cannonball = Bubble('Cannonball', '4', 'Swipe', 'Rollout Shield', 'Ram',
                    'Firey Smash', '4', '16', '20', '24', '3', '0', '4', '5',
                    'Normal', 'Steel', 'Normal', 'Fire', '5', '68', '1', '0',
                    'Steel', '4', '4', '4', '68','None_Yet', 'Unkown_For_Now')

antser = Bubble('Antser', '5', 'Bite', 'Crash', 'Slice', 'NOT ABAILABLE', '8',
                '12', '16', '0', '3', '2', '2', '0', 'Dark', 'Normal', 'Dark',
                'NO TYPE', '3', '64', '1', '0', 'Rock', '3', '3', '5', '64','None_Yet', 'Unkown_For_Now')

tank = Bubble('Tank', '12', 'Ram', 'Blast', 'Laser', 'Bullet Wave', '16', '24',
              '44', '56', '3', '1', '9', '11', 'Normal', 'Steel', 'Electric',
              'Steel', '11', '128', '65', '0', 'Steel', '4', '4', '12', '128','None_Yet', 'Unkown_For_Now')

laser = Bubble('Laser', '10', 'Shoot', 'Rapid Fire', 'Laser Beam',
              'Tracking Laser', '12', '16', '28', '36', '3', '1', '5', '8',
              'Steel', 'Steel', 'Electric', 'Electric', '7', '92', '30', '0',
              'Steel', '4', '4', '10', '92',tank,'65')

gunner = Bubble('Gunner', '6', 'Shoot', 'Blast', 'Bulletstorm',
                'NOT AVAILABLE', '8', '12', '20', '0', '3', '1', '3', '0',
                'Steel', 'Steel', 'Steel', 'NO TYPE', '3', '56', '1', '0',
                'Steel', '3', '3', '10', '56',laser,'30')



#Make the bubble above this comment
#Format Example: bubble = Bubble('Name', 'Bubble Energy', 'First Move Name', 'Second Move Name', 'Third Move Name', 'Fourth Move Name', 'First Move Damage', 'Second Move Damage', 'Third Move Damage', 'Fourth Move Damage', 'First Move Energy', 'Second Move Energy', 'Third Move Energy', 'Fourth Move Energy', 'First Move Type', 'Second Move Type', 'Third Move Type', 'Fourth Move Type', 'Bubble Speed', 'Bubble Health', 'level', 'XP', 'type','amount of moves', 'total moves', 'base energy', 'base health', Evolves to, 'Evolution level') 


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

#search:

search_names = [
    "Jab", "Penta-Spike", "Spin", "Slasher", "Mow", "Wall", "Fake", "Rip",
    "Shield", "Twin", "Miner", "Rager", "Smasher", "Cannonball", "Antser",
    "Gunner", "Laser", "Tank"
]

#just add a new bubble every time you make a new one

search_results = [
    jab.stats, penta_spike.stats, spin.stats, slasher.stats, mow.stats,
    screen.stats, fake.stats, rip.stats, shield.stats, rager.stats, twin.stats,
    miner.stats, smasher.stats, cannonball.stats, antser.stats, gunner.stats,
    laser.stats, tank.stats
]  #the search_results here are different to the search names

#if you want them in aphebetical order:
#search_names=sorted(search_names)
#search_results=sorted(search_results)

def random_trainer(name, bubble1, bubble2, bubble3, bubble4, bubble5, bubbles, bubble6, bubble7, bubble8, bubble9, bubble10):
  #[mccabe] Cyclomatic complexity too high: 54 (threshold 15)
  accept_challenge = random.randint(1,4)
  trainer2_request = False
  try:
    bubbles = int(bubbles)

  except ValueError:
    pass
    
  if(bubble1 == "f"):
    bubble1 = tierf[random.randint(0,len(tierf)-1)]
  if(bubble1 == "c"):
    bubble1 = tierc[random.randint(0,len(tierc)-1)]
  if(bubble1 == "b"):
    bubble1 = tierb[random.randint(0,len(tierb)-1)]
  if(bubble1 == "a"):
    bubble1 = tiera[random.randint(0,len(tiera)-1)]
  if(bubble1 == "s"):
    bubble1 = tiers[random.randint(0,len(tiers)-1)]
  if(bubble1 == "l"):
    bubble1 = tierl[random.randint(0,len(tierl)-1)]

  if(bubble2 == "f"):
    bubble2 = tierf[random.randint(0,len(tierf)-1)]
  if(bubble2 == "c"):
    bubble2 = tierc[random.randint(0,len(tierc)-1)]
  if(bubble2 == "b"):
    bubble2 = tierb[random.randint(0,len(tierb)-1)]
  if(bubble2 == "a"):
    bubble2 = tiera[random.randint(0,len(tiera)-1)]
  if(bubble2 == "s"):
    bubble2 = tiers[random.randint(0,len(tiers)-1)]
  if(bubble2 == "l"):
    bubble2 = tierl[random.randint(0,len(tierl)-1)]

  if(bubble3 == "f"):
    bubble3 = tierf[random.randint(0,len(tierf)-1)]
  if(bubble3 == "c"):
    bubble3 = tierc[random.randint(0,len(tierc)-1)]
  if(bubble3 == "b"):
    bubble3 = tierb[random.randint(0,len(tierb)-1)]
  if(bubble3 == "a"):
    bubble3 = tiera[random.randint(0,len(tiera)-1)]
  if(bubble3 == "s"):
    bubble3 = tiers[random.randint(0,len(tiers)-1)]
  if(bubble3 == "l"):
    bubble3 = tierl[random.randint(0,len(tierl)-1)]

  if(bubble4 == "f"):
    bubble4 = tierf[random.randint(0,len(tierf)-1)]
  if(bubble4 == "c"):
    bubble4 = tierc[random.randint(0,len(tierc)-1)]
  if(bubble4 == "b"):
    bubble4 = tierb[random.randint(0,len(tierb)-1)]
  if(bubble4 == "a"):
    bubble4 = tiera[random.randint(0,len(tiera)-1)]
  if(bubble4 == "s"):
    bubble4 = tiers[random.randint(0,len(tiers)-1)]
  if(bubble4 == "l"):
    bubble4 = tierl[random.randint(0,len(tierl)-1)]

  if(bubble5 == "f"):
    bubble5 = tierf[random.randint(0,len(tierf)-1)]
  if(bubble5 == "c"):
    bubble5 = tierc[random.randint(0,len(tierc)-1)]
  if(bubble5 == "b"):
    bubble5 = tierb[random.randint(0,len(tierb)-1)]
  if(bubble5 == "a"):
    bubble5 = tiera[random.randint(0,len(tiera)-1)]
  if(bubble5 == "s"):
    bubble5 = tiers[random.randint(0,len(tiers)-1)]
  if(bubble5 == "l"):
    bubble5 = tierl[random.randint(0,len(tierl)-1)]

  delay_print(f"\n\nYou are challenged by Trainer {name}!\n\n")
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
    bubble_amount = input(f"Since this is a contest, you get to choose how many bubbles to battle with\n(max: {len(player_deck)})\n")
    try:
      bubble_amount = int(bubble_amount)
      if bubble_amount > len(player_deck):
        print(f"{bubble_amount} was too high")
        trainer2_request = True
      else:
        if accept_challenge != 1:
          print(f"{opponent_name[0]} accepted!")
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
      delay_print(f"When the judge asked you, you didn't say a number but said: {bubble_amount}. Since this was not a number, you lost your opportunity of choice.\n")
      trainer2_request = True

    if accept_challenge == 1 or trainer2_request == True:
      random_vs = random.randint(1,len(player_deck))
      while random_vs == bubble_amount:
        random_vs = random.randint(1,len(player_deck))
      print(f"They want a {random_vs} V {random_vs}!")
      ask("Do you accept?","y","n")
      if answer[0] == "y":
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
        delay_print("\nNo one agreed!\nNow we will be doing a 1 V 1 ! (but there's a twist! A random bubble is chosen from your 5 bubble deck and is used to fight!")
        random_bubble_used_to_challenge = random.randint(0,len(player_deck)-1)
        player_deck[random_bubble_used_to_challenge].fight(bubble1,"contest",0)



'''def catch_wild_bubbles(tier,starting_point):
  if "grass" in starting_point.lower():
    wording = ["You followed some trail that led into a mysterious open area and heard some noises around you.","Some grass seemed to be flattened while something was passing by, you decide to follow the half hidden trail.","The grassland that you arrived at had very open space, but tall grass."]
    delay_print(wording[random.randint(0,len(wording)-1)])
    delay_print("Just then, a bubble showed up!")

''' #idk if we need this, its kinda like battle validation


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
                search()

            break
            break

    else:
        searching = int(searching)
        print(search_results[searching - 1])
        again = input("Search again? y/n ")
        if (again == "y"):
            search()


def delay_print_begin(s):
    # print one character at a time
    #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(begin_delay_timer)


#############################################################
delay_print(
    "\n\n\nDo you want to start the storyline?\nPress y for yes and n for no.\n"
)
storyline_start = input("")
storyline_start.lower()

while storyline_start != "y":
    delay_print(
        "You have exited the storyline.\nYou can view the Bubble-DEX but you cannot play the game unless you enter the storyline.\nDo you want to re-enter the storyline?\n(y or n)\n"
    )
    storyline_start_confirm = input("")

    if storyline_start_confirm == "y":
        storyline_start = "y"

    if storyline_start_confirm != "y":
        delay_print("\nDo you want to view the BUBBLE_DEX?\n(y or n)\n")
        bubble_dex_start = input("")
        if bubble_dex_start == "y":
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
    delay_print(
        "..........     .          .     ..........     ..........     .              ..........\n"
    )
    delay_print(
        ".        .     .          .     .        .     .        .     .              .         \n"
    )
    delay_print(
        ".        .     .          .     .        .     .        .     .              .         \n"
    )
    delay_print(
        "........       .          .     .........      .........      .              ..........\n"
    )
    delay_print(
        ".        .     .          .     .        .     .        .     .              .         \n"
    )
    delay_print(
        ".        .      .        .      .        .     .        .     .              .         \n"
    )
    delay_print(
        "........         ........       .........      ........       ..........     ..........\n"
    )
    delay_print("\n\n\n\n")
    delay_print(
        "   ....        .          .     ..........     ..........     ...........\n"
    )
    delay_print(
        " .      .      .          .     .              .                   .    \n"
    )
    delay_print(
        ".        .     .          .     .              .                   .    \n"
    )
    delay_print(
        ".    .   .     .          .     ..........     ..........          .    \n"
    )
    delay_print(
        " .    . .      .          .     .                       .          .    \n"
    )
    delay_print(
        "  .... .        .        .      .                       .          .    \n"
    )
    delay_print(
        "        .        ........       ..........     ..........          .")
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
    print("\nSTART!")

    player_bubble_amt = 0
    delay_print("\nDo you want to skip the tutorial?(Y or N)\n")
    skip_tutorial = input(str(''))
    
    while skip_tutorial == 'N':


      delay_print(
          "\n\n\n\n\nBubbles are mysterious creatures with magical powers.\nOur world is filled with these wonderful and powerful creatures.\nOnly three people every year are chosen to start their Bubble Quest here in my labratory.\n"
      )

      delay_print(
          "\nI am Professor 2.\nToday I will be helping you start your very own Bubble Quest, the same way I have helped many trainers before you.\n"
      )


      delay_print(
          "\nBefore you start your Bubble Quest, you will need a bubble to help you.\nYou can choose one from the three bubbles I have here.\n"
      )

      delay_print("\n-You reach towards the bubbles.-\n")

      delay_print(
          "\nDon't choose yet! I need to tell you more about the rules!\nThe bubble with the higher speed goes first in a battle, but if they have the same speed the first attacker is declared randomly.\n"
      )

      delay_print(
          "\nWhen it's your turn, you use a move.\nLess powerful moves do less damage, but give you energy, the opposite happens for stronger moves, they do more damage, but use your energy.\nSpeaking of energy, if you don't have any energy left during a battle, your bubble loses health. In this region, they only lose 5 health.\n"
      )

      delay_print(
          "\nSome bubbles can also evolve.\nFor example, Gunner bubble can evolve into Laser bubble once it reaches a certain level.\nAlso, once a bubble reaches a certain level, it can even learn a new move!\n"
      )

      delay_print(
          "\nNow that you know more about the rules of bubble quest, I think it is time for you to choose your bubble.\n"
      )
      break

    delay_print(f"\n{jab.stats}\n")

    delay_print(f"\n{spin.stats}\n")

    delay_print(f"\n{mow.stats}\n")

    delay_print("\nPlease choose a bubble.\n(Write the name in lowercase.)\n")
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



    delay_print(
        "\nNow that you have a bubble, you should learn more about it.\nI have a device here called a Bubble-DEX that can tell you the stats of any bubble once you scan it.\nTry it.\n"
    )

    delay_print(
        "\n-You scanned the bubble you choose with your Bubble-DEX.-\n")

    if bubble1 == 'jab':
        delay_print(f"{jab.stats}\n")

    if bubble1 == 'spin':
        delay_print(f"{spin.stats}\n")

    if bubble1 == 'mow':
        delay_print(f"{mow.stats}\n")

    delay_print(
        "\n-The professor gave you the Bubble-DEX and 50 capture discs to catch bubbles and sends you off on your journey.-\n"
    )

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

    random_trainer('Jack', "f", "t", "t", "t", "t", 1, player_deck[0], None, None, None, None)
    
    delay_print(
        "\n-After beating the trainer, you headed forward on the path to continue your Bubble Quest.-\n"
    ) 



    ask(
      "-Soon, you arrived at a fork in the road.\nFrom what you see, you know that the left side leads to a forest and the right side leads to a clearing.\nFrom the map the professor gave you, you know that the roads will lead to the same place, but the paths are different.\nDo you go left or right?"
      ,"l","r"
    )

    if answer[0] == 'l':
        delay_print(
            "-You walked down the path that heads into the forest and entered it.-\n"
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

    if answer[0] == 'r':
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
    if merchant == 'y':
      delay_print("\nHe saw you and opened his shop.\n")
      shop(random.randint(10,15), random.randint(5,15))
      merchant == ''
    else:
      delay_print("You kept on walking.")
    delay_print(
        "\n-After a while, you see a building in the distance.\nDo you want to go there?\n(y or n)-\n"
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

        Bubble.battle_validation(tierb, True, False, None, Person, player_bubble_amt)

        delay_print(
            "\n-You continued to the building and once you got there, you saw a sign that showed that the building was home to a contest.-\n"
        )

        delay_print("-Do you want to join the contest?-\n-If you win, you get 10,000$ and a lot of items!\n-")
        contest1 = str(input(""))

    while building1 == 'n' or contest1 == 'n':
        delay_print(
            "\n-You decide to keep walking around and hopefully find some bubbles to catch.-\n"
        )
        walk_around1 = True
        break

    if walk_around1 == True:
      delay_print("\n-Two bubbles jump out of the grass!-\n")

      Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)
      
      Bubble.battle_validation(tierc, True, False, None, Person, player_bubble_amt)

      print("You kept walking around and someone pulled you inside a building")

      contest1 = "y"


    if contest1 == 'y' or contest1 == "yes":
      
      delay_print("\n-You entered the contest!-\n")
      delay_print(f"\n{player.name}, please go to Arena {random.randint(1, 10)}. Your match is about to begin.\n")
      delay_print("--------------------")

      delay_print(f"\n{player.name} V.S. Amy! Let the battle begin!\n")
      random_trainer('Amy', 'c', "f", "f", "f", "f", "x", player_deck[0], None, None, None, None)

      if len(lost_contest_1) == 0:
        delay_print("\nCongrats!\nYou have now advanced to the next stage of the tournament!\n")
        delay_print("Do you want to start the next battle?\nIf you press c, you will be given an opportunity to change your deck before the fight begins. Or press y to continue to next battle (if you don't want to, press n)\n")
        start = input("\n")
        
        if start == 'y':
          delay_print(f"\n{player.name}, please report to Arena {random.randint(1, 10)}. Your match is about to begin.\n")
          delay_print("--------------------")

          delay_print(f"\n{player.name} V.S. Ken! Let the battle begin!\n")
          random_trainer('Ken', 'b', "c", "c", "b", "a", "x", player_deck[0], None, None, None, None)
          
        elif start != "n" and start != "y":
          change_deck()
          delay_print(f"\n{player.name}, please go to Arena {random.randint(1, 10) } Your match is about to begin.\n")
          delay_print("--------------------")

          delay_print(f"\n{player.name} V.S. Ken! Let the battle begin!\n")
          random_trainer('Ken', 'b', "c", "f", "b", "a", "x", player_deck[0], None, None, None, None) 
          lost_contest_1.clear()

        if start != "n":
          if len(lost_contest_1) == 0:

            delay_print("Wow! You are such a strong trainer! There are only 8 trainers left in this contest!\n")
            read_tournament_1_sign = input("There is a sign ahead, would you like to read it?\nY or N\n")
            if read_tournament_1_sign != "Y":
              delay_print("The next day, you finish breakfast and wait for your name to be called, but it never got called.\n")
              delay_print("You decide to wait a little longer.\n")
              time.sleep(10)
              delay_print("Finally, you give up waiting and walk around the propery and try to find someone who can knows what is happening, before you met someone, you encountered the same sign from yester day, you walk up to it and start reading.")
              
          

            delay_print("\n\nThere are factors delaying the tournament, everyone's next round will be delayed until further notice. Sorry for your inconvenience\n\n")
          
            ask("Because there contest has tempoarily closed down, you have a chance to catch some more bubbles.\nDo you want to go?", 'Y', 'N')
          

          if answer[0] == 'Y':
            delay_print("\nYou headed outside and met a thug bending some of the water pipes!")
            delay_print("\nYou walk towards him to talk.")
            delay_print("\n'Whaddaya want, punk?'")
            random_trainer("Grunt A", 'c', 'f', 'f', 'f', 'f', "5" , player_deck[0], None, None, None, None)

            if len(lost_grunt_1) == 0:
              delay_print("\n'Gonna retreat back to H.Q. for now...'")
              delay_print("\nThe grunt ran away...")

            elif len(lost_grunt_1) == 1:
              delay_print("\n'Yes! I have defeated a trainer on behalf of E.V.I.L!'")
              delay_print("\nThe grunt ran away dancing...")
              lost_grunt_1.clear()

            delay_print("\nThe loudspeaker buzzed and announced that the contests will resume tomorrow, telling everyone to have a nice day.\n")
            print("The quest has ended for now")
            print("It will be continued soon...")
            time.sleep(10)







        if start == 'n':
          delay_print("You chickened out and went back to the lobby...\n")
          delay_print("Press n when you are ready for the fight.\n")
          start == input("")
        
        

      elif len(lost_contest_1) >= 1:
        delay_print("\nSorry, you were eliminated...\n")
        delay_print("You can still get back in the contest, but you will not get the prizes if you win.\n")
        delay_print("Do you want to re-enter? y or n\n")
        re_enter_contest = input("")
        if re_enter_contest == "y":
          get_reward = False
          lost_contest_1.remove[1]
          

