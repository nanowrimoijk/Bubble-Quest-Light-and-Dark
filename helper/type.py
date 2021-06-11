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

class Type:
	def __init__(self, name, weaknesses, resistances, null):
		self.weaknesses = weaknesses
		self.resistances = resistances
		self.null = null #null damage
		pass
	
	def type_adv(self, attacker):
		if(attacker.name in self.weaknesses):
			return 'weak'
		elif(attacker.name in self.resistances):
			return 'resist'
		elif(attacker.name in self.null):
			return 'null'
		else:
			return 'nuetral'

    

fire = Type('Fire', ['Water', 'Rock'], ['Grass', 'Steel', 'Ice'], [])
water = Type('Water', ['Grass', 'Electric'], ['Fire', 'Poison', 'Rock'], [])
grass = Type('Grass', ['Fire', 'Dark', 'Poison'], ['Water', 'Rock', 'Air'], [])
electric = Type('Electric', ['Rock', 'Psychic'], ['Water', 'Air'], [])
rock = Type('Rock', ['Water', 'Fighting', 'Grass'], ['Fire', 'Electric', 'Air'], [])
poison = Type('Poison', ['Psychic', 'Rock', 'Water'], ['Grass', 'Steel', 'Fighting'], [])
dark = Type('Dark', ['Fighting', 'Light'], ['Psychic'], [])
light = Type('Light', ['Fighting', 'Dark'], ['Psychic'], [])
psychic = Type('Psychic', ['Dark', 'Light', 'Steel'], ['Poison', 'Fighting', 'Electric'], [])
fighting = Type('Fighting', ['Air', 'Poison', 'Psychic'], ['Dark', 'Light', 'Normal'], [])
normal = Type('Normal', ['Fighting', 'Steel'], [], [])
steel = Type('Steel', ['Fire', 'Poison'], ['Normal', 'Psychic'], [])
air = Type('Air', ['Electric', 'Grass', 'Rock'], ['Fighting', 'Poison'], [])