from player import Player
import bubblesNmoves
from tile import tiles
from battle import wild_battle
from os import system
import random

lab = """

      ##########       
      #        #       
      #        #       
      # ########      
                      
                      """
#


lab_encounter_chance = 0
lab_encounters = [None]

lab = lab.split("\n")