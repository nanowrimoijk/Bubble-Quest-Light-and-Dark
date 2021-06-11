from os import system
import random

def choose_bubble(player):
	system('clear')
	print('choose the number of the bubble you would like to fight with:')

	num = 1
	for i in player.deck:
		print(f"[{num}]{i.name}")
		num += 1
  #

	return input('> ')
#

def compare_speed(player, enemy):
	if(player.speed > enemy.speed):
		return [player.id, enemy.id]
	elif(player.speed < enemy.speed):
		return [enemy.id, player.id]
	else:
		num = random.randint(0, 2)
		if(num == 0):
			return [player.id, enemy.id]
		else:
			return [enemy.id, player.id]
		#
	#
#

def faint_check(bubble):
	return bubble.health <= 0 if True else False
#

def enemy_choose(bubble):
	return bubble.moves[random.randint(0, len(bubble.moves) - 1)]
#

def player_choose(bubble, enemy):
	system('clear')
	print(f"Your {bubble.name} - {bubble.health}/{bubble.health_MAX} health ({bubble.energy} energy)")
	print
	print(f"Enemy {enemy.name} - {enemy.health}/{enemy.health_MAX}")
	print
	print

	num = 1
	for i in bubble.moves:
		print(f"[{num}]{i.name} - {i.damage} damage, {i.energy} energy")
		num += 1
	#

	return input('> ')
#

def use_move(move, attacker, target):
	system('clear')
	attacker.energy += move.energy
	target.health -= move.damage

	print(f"{attacker.name} used {move.name}!")
	print(f"{attacker.name} has {attacker.energy} energy left!")
	if(attacker.energy < 0):
		attacker.health -= 200
		print(f"{attacker.name} ran out of energy, and got hurt!")
	#

	input('press enter')
#

def battle_loop(player, enemy):
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	move = False
	while(move == False):
		move = player_choose(player, enemy)
		if(move == '' or (not move in numbers) or int(move) == 0 or player.moves[int(move) - 1] == None):
			move = False
		#
	#
	move = player.moves[int(move) - 1]

	use_move(move, player, enemy)

	e = faint_check(enemy)
	if(e):
		return('enemy')
	#
	p = faint_check(player)
	if(p):
		return('player')
	#

	
	use_move(enemy_choose(enemy), enemy, player)

	p = faint_check(player)
	if(p):
		return('player')
	#
	e = faint_check(enemy)
	if(e):
		return('enemy')
	#
#