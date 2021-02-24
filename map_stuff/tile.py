class Tile:
	def __init__(self, name, char, collision, encounter):
		self.name = name
		self.char = char
		self.collision = collision
		self.encounter = encounter
#

wall = Tile("wall", "#", True, False)
dirt = Tile("dirt", ' ', False, False)
grass = Tile("grass", '˶', False, True)

tiles = [
	wall, 
	dirt, 
	grass
]
