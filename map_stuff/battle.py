from battle_stuff import *

def wild_battle(player, enemy):
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	system('clear')

	print(f"a wild {enemy.name} attacked!")
	input('press enter')

	bubble = False

	while(bubble == False):
		system('clear')
		bubble = choose_bubble(player)

		if(bubble == '' or (not bubble in numbers) or int(bubble) == 0 or player.deck[int(bubble) - 1] == None):
			bubble = False
		#
	#
	bubble = player.deck[int(bubble) - 1]

	order = compare_speed(bubble, enemy)

	loser = None

	if(order[0] == enemy.id):
		use_move(enemy_choose(enemy), enemy, bubble)
	
		p = faint_check(bubble)
		if(p):
			loser = 'player'
		#
		e = faint_check(enemy)
		if(e):
			loser = 'enemy'
		#
	#

	while(bubble.health > 0 and enemy.health > 0):
		loser = battle_loop(bubble, enemy)
	#

	if(loser == 'enemy'):
		print(f"{bubble.name} won the battle!")
	elif(loser == 'player'):
		print(f"{bubble.name} lost the battle!")
	#

	input('press enter')

	bubble.health = bubble.max_health
	bubble.energy = bubble.max_energy
	enemy.health = enemy.max_health
	enemy.energy = enemy.max_energy
#