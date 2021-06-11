import copy
from bubblesNmoves import *
from helper.battle import battle

#using copy so we dont edit the original version of each bubble

player = {
	"deck": [copy.copy(fake), copy.copy(mow), copy.copy(jab)]
}

enemy = {
	"name": "that old man living under your bed", 
	"deck": [copy.copy(fake), copy.copy(fake)], 
}

winner = battle(2, player, enemy, False)

print(winner + " wins!")