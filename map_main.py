from map_stuff.player import Player
from bubblesNmoves import *
from map_stuff.tile import tiles
from helper.battle import battle
from getkey import getkey, keys
from os import system
import random
import copy

player = Player([copy.copy(jab)], 10, 10, [])
player.deck[0].id = 12345

map_1 = {
	"string": """
               ˶˶˶˶˶˶˶˶
      #########˶˶˶˶˶˶˶˶
      #       #˶˶˶˶˶˶˶˶
      #       #˶˶˶˶˶˶˶˶
      # #######˶˶˶˶˶˶˶˶
               ˶˶˶˶˶˶˶˶
               ˶˶˶˶˶˶˶˶""", 
	"encounter_chance": 50, 
	"encounters": [copy.copy(mow), copy.copy(jab)]
}


world = map_1

world["string"] = world["string"].split("\n")


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

	if(chance < world["encounter_chance"]):
		x = world["encounters"][random.randint(0, len(world["encounters"]) - 1)]
		x.id = 00000
		return x
	else:
		return False
	#
#




while(True):
	system('clear')
	moved = False

	#find character under player 
	world["string"][player.y] = split(world["string"][player.y])
	last = player.under
	player.under = world["string"][player.y][player.x]
	if(player.under == player.char):
		player.under = last
	#
	world["string"][player.y][player.x] = player.char
	#west of player
	if(player.x + 1 < len(world["string"][player.y])):
		if(player.x <= len(world["string"][player.y])):
			player.right = world["string"][player.y][player.x + 1]
		#
	else:
		player.right = None
	#
	#east of player
	if(not player.x == 0):
		player.left = world["string"][player.y][player.x - 1]
	else:
		player.left = None
	#

	world["string"][player.y] = "".join(world["string"][player.y])
	
	#north of player
	world["string"][player.y - 1] = split(world["string"][player.y - 1])
	if(not len(world["string"][player.y - 1]) == 0):
		player.up = world["string"][player.y - 1][player.x]
	else:
		player.up = None
	#
	world["string"][player.y - 1] = "".join(world["string"][player.y - 1])
	#south of player
	if(player.y + 1 < len(world["string"])):
		world["string"][player.y + 1] = split(world["string"][player.y + 1])
		if(not len(world["string"][player.y + 1]) == 0):
			player.down = world["string"][player.y + 1][player.x]
		#
		world["string"][player.y + 1] = "".join(world["string"][player.y + 1])
	else:
		player.down = None
	#


	print("\n".join(world["string"]))
	key = getkey()
	
	if(key in ['w', 'a', 's', 'd', keys.UP, keys.DOWN, keys.RIGHT, keys.LEFT]):
		world["string"][player.y] = split(world["string"][player.y])
		world["string"][player.y][player.x] = player.under
		world["string"][player.y] = "".join(world["string"][player.y])
		moved = True

		if(key == 'w'):
			if(not collide(player.up)):
				player.y -= 1
		elif(key == 's'):
			if(not collide(player.down)):
				player.y += 1
		elif(key == 'a'):
			if(not collide(player.left)):
				player.x -= 1
		elif(key == 'd'):
			if(not collide(player.right)):
				player.x += 1
		elif(key == 'e'):
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
				winner = battle(1, player, fight, True)
				system('clear')
				print(f"{winner} won the battle!")
				input('press enter')
				for i in player.deck:
					i.health = i.health_MAX
					i.energy = i.energy_MAX
				fight.health = fight.health_MAX
				fight.energy = fight.energy_MAX
			#
		#
	#
#