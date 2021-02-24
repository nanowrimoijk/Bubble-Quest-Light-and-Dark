class Player:
	def __init__(self, deck):
		self.char = '@'
		self.x = 1
		self.y = 1
		self.under = ''
		self.right = ''
		self.left = ''
		self.up = ''
		self.down = ''
		
		self.deck = deck