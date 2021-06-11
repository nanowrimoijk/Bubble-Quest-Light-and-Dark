import random

class Bubble:
	def __init__(self, name, moves, speed, health, energy, level, xp, evolution, evolution_level, bubble_type):
		self.name = name
		self.moves = moves
		self.speed = speed
		self.health = health
		self.max_health = health
		self.energy = energy
		self.max_energy = energy
		self.id = random.randint(0, 1000000)# so if you have multiple of the same bubble, we can still tell them apart
		self.level = level
		self.xp = xp
		self.evolution = evolution
		self.evolution_level = evolution_level
		self.bubble_type = bubble_type
	#	
#