from os import system
import random
import copy

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#number => how many bubbles are in this fight eg: 1 for 1v1, 2 for 2v2
#wild => boolean; true for wild encounter, or false for a trainer battle
def battle(number, player, enemy, wild):
	#set lists for all of a trainers active bubbles to go in so we dont 
	#		have to make an entirely new function for multi-battles
	chosen_bubbles = []
	enemy_bubbles = []
	for x in range(number):
		#player chooses bubbles 
		choice = choose_bubble(player, x)
		chosen_bubbles.append(choice)
		if(wild == False):
			#enemy gets random bubbles
			e_choice = random.randint(0, len(enemy['deck']) - 1)
			enemy_bubbles.append(enemy['deck'][e_choice])
			enemy['deck'].remove(enemy['deck'][e_choice])
		else: 
			#set wild enemy bubble
			enemy_bubbles.append(enemy)
	 
	if(number == 1):
		if(wild == False):
			system('clear')
			print(f"{enemy['name']} sent out {enemy_bubbles[0].name}")
		else: 
			system('clear')
			print(f"wild {enemy_bubbles[0].name} attacked!")
	else: 
		#multi battle
		print(f"{enemy['name']} sent out {enemy_bubbles[0].name} and {enemy_bubbles[1].name}")
	input("press enter")

	#check speeds and determine which bubble moves first
	who_goes_first = check_speed(number == 2 if False else chosen_bubbles[0], enemy_bubbles[0])
	enemy_win = False
	player_win = False

	#if enemy is first they move. a copy of this is inside of the loop below
	if(who_goes_first == 'enemy'):
		#choose attack and deal damage
		enemy_turn(enemy_bubbles, chosen_bubbles, number)
		#check if opponent is KO'd
		enemy_win = check_win(chosen_bubbles)
		if(enemy_win):
			#if opponent is defeated, exit the loop and battle function
			return 'enemy'
		#next check if you have been KO'd (recoil, negative energy, etc.)
		player_win = check_win(enemy_bubbles)
		if(player_win):
			return 'player'
	#im not explaining the entire process again, so figure it out

	#loop each trainer's turn until someone loses
	while(enemy_win == False and player_win == False):
		player_turn(chosen_bubbles, enemy_bubbles, number)
		player_win = check_win(enemy_bubbles)
		if(player_win):
			return 'player'
		enemy_win = check_win(chosen_bubbles)
		if(enemy_win):
			return 'enemy'

		enemy_turn(enemy_bubbles, chosen_bubbles, number)
		enemy_win = check_win(chosen_bubbles)
		if(enemy_win):
			return 'enemy'
		player_win = check_win(enemy_bubbles)
		if(player_win):
			return 'player'



def choose_bubble(player, number):
	choice = False
	deck = copy.copy(player.deck)
	while(choice == False):
		print("choose the number of the bubble you want to send out")
		print(f"bubble #{number + 1}")

		num = 1
		#for loop lists all of the player's bubbles
		for x in deck:
			print(f"[{num}]{x.name}")
			num += 1
		
		choice = input('> ')

		#check if input is a valid integer, if not list all moves bubbles
		if(choice == '' or (not choice in numbers) or int(choice) == 0 or deck[int(choice) - 1] == None):
			#log error 
			system('clear')
			print(f"{choice} is not a vaild bubble, please choose a valid deck number")
			choice = False
		else: 
			x = deck[int(choice) - 1]
			del deck[int(choice) - 1]
			return x

#change player_bubble to False for a multi battle
def check_speed(player_bubble, enemy_bubble):
	first = None
	if(player_bubble == False):
		print("It is a multi battle, so the start is decided by a coin flip")
		flip = random.randint(0, 1)
		if(flip == 0): 
			first = 'player'
		else:
			first = 'enemy'
		if(first == 'player'):
			print('You won!')
		else: 
			print('You lost.')
		input('press enter')
	else:
		if(player_bubble.speed > enemy_bubble.speed): #player is faster
			first = 'player'
		elif(player_bubble.speed < enemy_bubble.speed): #enemy is faster
			first = 'enemy'
		elif(player_bubble.speed == enemy_bubble.speed): #player and enemy have equal speed
			flip = random.randint(0, 1)
			if(flip == 0):
				first = 'player'
			else:
				first = 'enemy'
	
		system('clear')
		print(f"{first}'s bubble is faster, so it moves first!")
		input('press enter')
	return first


def enemy_turn(enemy_bubbles, player_bubbles, number):
	move = None
	chosen_bubble = None
	target_bubble = None

	if(number == 1):
		#if this is a single battle, set the attacking and defending to the first and only slot
		#print(enemy_bubbles)
		#input('<>')
		chosen_bubble = enemy_bubbles[0]
		target_bubble = player_bubbles[0]
	else:
		#if this is a multi battle, set random attacker and defender
		choice = 3
		target = 3
		#choose a random bubble
		while(choice > len(enemy_bubbles)):
			choice = random.randint(0, 1)
			if(enemy_bubbles[choice].health <= 0):
				choice = 3
		#choose a random target
		while(target > len(player_bubbles)):
			target = random.randint(0, 1)
			if(player_bubbles[target].health <= 0):
				target = 3
		chosen_bubble = enemy_bubbles[choice]
		target_bubble = player_bubbles[target]

	
	#keep getting a random move until you get a valid one
	while(move == None or move.name == 'NOT_AVAILABLE'):
		move = chosen_bubble.moves[random.randint(0, len(chosen_bubble.moves) - 1)]

	#deal damage
	deal_damage(chosen_bubble, target_bubble, move)


def player_turn(player_bubbles, enemy_bubbles, number):
	chosen_bubble = None
	target_bubble = None

	turn_choices = ['Attack', 'Items']
	turn_choice = None
	
	while(turn_choice == None or turn_choice == 0):
		system('clear')
		display_health_bars(player_bubbles, enemy_bubbles, number)
		print('choose an action:')
		num = 1
		for i in turn_choices:
			print(f"[{num}] {i}")
			num += 1

		turn_choice = input('> ')

		if(turn_choice == 0):
			print(f"'{turn_choice}' is not an option, please choose a valid number.")
			input('press enter')
			turn_choice = None


	def choose_bubble_attack():
		display_health_bars(player_bubbles, enemy_bubbles, number)

		print("choose a bubble to attack with:")

		#list all the player's bubbles
		num = 1
		for x in player_bubbles:
			print(f"[{num}]{x.name}")
			num += 1
		
		choice = input('> ')

		return choice
	
	def choose_target():
		display_health_bars(player_bubbles, enemy_bubbles, number)
		
		print("choose a bubble to attack:")

		#list all the enemy's bubbles
		num = 1
		for x in enemy_bubbles:
			print(f"[{num}]{x.name}")
			num += 1
		
		choice = input('> ')

		return choice
		
	def choose_attack():
		display_health_bars(player_bubbles, enemy_bubbles, number)

		print("choose an attack to use:")
		
		#list all the chosen bubble's moves
		num = 1
		for x in chosen_bubble.moves:
			# "operator" is only for the print function below to tell you if the move decreases or increases your energy
			operator = ' '
			if(x.energy < 0):
				operator = ''
			else: 
				operator = '+'
			print(f"[{num}]{x.name}: {operator}{x.energy} energy, {x.damage} damage")
			num += 1
		
		choice = input('> ')

		return choice


	if(int(turn_choice) == 1):
		system('clear')
		while(chosen_bubble == None):
			chosen_bubble = choose_bubble_attack()

			if(chosen_bubble == '' or (not chosen_bubble in numbers) or int(chosen_bubble) == 0 or player_bubbles[int(chosen_bubble) - 1] == None):
				chosen_bubble = None
			else: 
				chosen_bubble = player_bubbles[int(chosen_bubble) - 1]

			if(chosen_bubble.health <= 0):
				print(f"{player_bubbles[int(chosen_bubble) - 1].name} is unable to fight!")
				input('press enter')
				system('clear')
				chosen_bubble = None
		
		move_choice = None
		#keep choosing attack until player chooses a valid move
		while(move_choice == None):
			system('clear')
			#player chooses their attack
			move_choice = choose_attack()

		if(move_choice == '' or (not move_choice in numbers) or int(move_choice) == 0 or chosen_bubble.moves[int(move_choice) - 1] == None):
			move_choice = None
		else: 
			move_choice = chosen_bubble.moves[int(move_choice) - 1]
		
		system('clear')
		while(target_bubble == None):
			target_bubble = choose_target()

			if(enemy_bubbles[int(target_bubble) - 1].health <= 0):
				print(f"It won't affect enemy {enemy_bubbles[int(target_bubble) - 1]}.")
				input('press enter')
				system('clear')
				target_bubble = None

			if(target_bubble == '' or (not target_bubble in numbers) or int(target_bubble) == 0 or player_bubbles[int(target_bubble) - 1] == None):
				target_bubble = None
			else: 
				target_bubble = enemy_bubbles[int(target_bubble) - 1]
		
		#deal damage and increase/decrease energy
		deal_damage(chosen_bubble, target_bubble, move_choice)
	elif(turn_choice == 2): 
		print("bruh, this isn't finished yet")
#


def check_win(damaged):
	amount = 0
	#checks if bubble has health left
	if(damaged[0].health > 0):
		amount += 1
	#checks if a second bubble is in play, if so checks how much health it has
	if(len(damaged) == 2):
		if(damaged[1].health > 0):
			amount += 1

	if(amount == 0):
		return True #trainer is defeated
	else: 
		return False #trainer still has bubbles that can fight


def deal_damage(attacker, defender, move):
	defender.health -= move.damage
	attacker.energy += move.energy#this MUST be "+=". moves that decrease your energy must be a negative number

	print(f"{attacker.name} used {move.name}!")
	print(f"{attacker.name} has {attacker.energy} energy left!")
	#if attacking bubble has less than 0 energy left it loses health
	if(attacker.energy < 0):
		attacker.health -= 200
		print(f"your {attacker.name} ran out of energy and got hurt!")

	input('press enter')


def display_health_bars(player_bubbles, enemy_bubbles, number):
	#display player/enemy health and energy
	print(f"enemy {enemy_bubbles[0].name}: {enemy_bubbles[0].health} ({enemy_bubbles[0].energy})")
	print("")
	if(number == 2):
		print(f"enemy {enemy_bubbles[1].name}: {enemy_bubbles[1].health} ({enemy_bubbles[1].energy})")
		print("")
	print(f"your {player_bubbles[0].name}: {player_bubbles[0].health} ({player_bubbles[0].energy})")
	print("")
	if(number == 2):
		print(f"your {player_bubbles[1].name}: {player_bubbles[1].health} ({player_bubbles[1].energy})")
		print("")