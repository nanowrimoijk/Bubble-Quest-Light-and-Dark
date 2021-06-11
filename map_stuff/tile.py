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
jab = Tile("jab", "(J)", True, False)
spin = Tile("spin", "(S)", True, False)
mow = Tile("mow", "(M)", True, False)
tiles = [
	wall, 
	dirt, 
	grass,
  jab,
  spin,
  mow
]
