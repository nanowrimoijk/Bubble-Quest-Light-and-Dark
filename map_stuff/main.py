from player import Player
from bubble import Bubble, Move
from tile import tiles
from battle import wild_battle
from os import system
import random


cut = Move("Cut", 20, 120)
jab = Move("Jab", 15, 160)
xcannon = Move("X-Cannon", -25, 240)
slash = Move("Slash", 30, 80)
spin = Move("Spin", 25, 120)
rollout = Move("Rollout", -20, 180)
mow = Move("Mow", 25, 80)
plow = Move("Plow", 5, 120)
lawnmow = Move("Lawnmow", -25, 250)

jab = Bubble("Jab", [cut, jab, xcannon], 3, 640, 35)
mow = Bubble("Mow", [mow, plow, lawnmow], 1, 680, 30)
spin = Bubble("Spin", [slash, spin, rollout], 7, 520, 40)


player = Player([jab])


world = """
               ˶˶˶˶˶˶˶˶
      #########˶˶˶˶˶˶˶˶
      #       #˶˶˶˶˶˶˶˶
      #       #˶˶˶˶˶˶˶˶
      # #######˶˶˶˶˶˶˶˶
               ˶˶˶˶˶˶˶˶
               ˶˶˶˶˶˶˶˶"""
#


world_encounter_chance = 50
world_encounters = [mow, spin]

world = world.split("\n")


def split(word):
	return list(word)
#

def collide(char):
	found = False
	for i in tiles:
		if ((i.char == char and i.collision == True) or char == None):
			found = True
		#
	#

	return found if True else False
#

def encounter():
	chance = random.randint(0, 100)

	if(chance < world_encounter_chance):
		return world_encounters[random.randint(0, len(world_encounters) - 1)]
	else:
		return False
	#
#




while(True):
	system('clear')
	moved = False

	#find character under player
	world[player.y] = split(world[player.y])
	last = player.under
	player.under = world[player.y][player.x]
	if(player.under == player.char):
		player.under = last
	#
	world[player.y][player.x] = player.char
	#west of player
	if(player.x + 1 < len(world[player.y])):
		if(player.x <= len(world[player.y])):
			player.right = world[player.y][player.x + 1]
		#
	else:
		player.right = None
	#
	#east of player
	if(not player.x == 0):
		player.left = world[player.y][player.x - 1]
	else:
		player.left = None
	#

	world[player.y] = "".join(world[player.y])
	
	#north of player
	world[player.y - 1] = split(world[player.y - 1])
	if(not len(world[player.y - 1]) == 0):
		player.up = world[player.y - 1][player.x]
	else:
		player.up = None
	#
	world[player.y - 1] = "".join(world[player.y - 1])
	#south of player
	if(player.y + 1 < len(world)):
		world[player.y + 1] = split(world[player.y + 1])
		if(not len(world[player.y + 1]) == 0):
			player.down = world[player.y + 1][player.x]
		#
		world[player.y + 1] = "".join(world[player.y + 1])
	else:
		player.down = None
	#


	print("\n".join(world))
	action = input('> ')
	
	if(action in ['w', 's', 'a', 'd']):
		world[player.y] = split(world[player.y])
		world[player.y][player.x] = player.under
		world[player.y] = "".join(world[player.y])
		moved = True
	#

		if(action == 'w'):
			if(not collide(player.up)):
				player.y -= 1
		elif(action == 's'):
			if(not collide(player.down)):
				player.y += 1
		elif(action == 'a'):
			if(not collide(player.left)):
				player.x -= 1
		elif(action == 'd'):
			if(not collide(player.right)):
				player.x += 1
		elif(action == 'e'):
			#main_menu()
			False
	#

	#check for an encounter
	if(moved):
		fight = False
		for i in tiles:
			if(i.char == player.under and i.encounter):
				fight = True
			#
		#
		if(fight):
			fight = encounter()
			if(fight != False):
				wild_battle(player, fight)
			#
		#
	#
#