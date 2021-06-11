from random import randint
class Move: 
  def __init__(self, name, energy, damage, effect, move_type, status, chance):
    self.name = str(name)
    self.energy = int(energy)
    self.damage = int(damage)
    self.effect = str(effect)
    self.move_type = str(move_type)
    self.status = str(status)
    self.chance = int(chance)
    def special_effect(effect):
      effect_success = False #first set it to false
      #True = effect will go on opponent
      #False = effect won't
      status_chance = randint(1,100)
      #check if effect is going to succeed:
      if status_chance < self.chance:
        effect_success = True
        #now effect can successfully go on opponent
        #if it doesn't succeed then nothing happens and it is kept as false
      shield_enabled = [False]
      shield_enabled.clear()
      heal = [False]
      heal.clear()
      steal_energy = [False]
      take_health = [False]
      kill_both = [False]
      drain = [False]
      energy = ''
      opponent_energy = ''
      percent = ''
      health = ''
      opponent_health = ''
      damage_taken = '' #find out how much damage was taken somehow... 
      if effect == 'stun':
        randint(1,status_chance)
      if effect == 'reduce_dmg1':
        if shield_enabled == True and damage_taken > 5:
          damage = 10
          damage_taken = damage_taken/2
          shield_enabled = False
          pass 
      if effect == 'reduce_dmg2': #Also gains energy
        if shield_enabled == True and damage_taken > 5:
          damage = 0
          damage_taken = damage_taken/2
          energy += 2
          shield_enabled = False
          pass
      if effect == 'heal1': #Also deals dmg
        if heal == True:
          damage = 10
          health += 15
          heal = False
          pass
      if effect == 'heal2': #A lot healed and energy cost is high
        if heal == True:
          health += 50
          energy -= 8
          heal = False
          pass
      if effect == 'deal_%_of_recived_dmg' or effect == "Deflect" or effect == "Deflection": #Does x times the amount of damage your opponent did to you
        if percent == True:
          damage = damage_taken * 1.5
          percent = False
          pass
      if effect == 'take_energy': #Takes opponent's energy
        if steal_energy == True:
          opponent_energy -= 5
          energy += 5
          steal_energy = False
          pass
      if effect == 'take_health_from_both': #Takes the same amount of health from both bubbles until your bubble has x health left
        if take_health == True: 
          opponent_health-(health-health-damage)
          health = damage
          take_health = False
          pass
      if effect == 'kill_both': #Takes the same amount of health from both bubbles until one dies
        while opponent_health>0 and health>0 and kill_both == True:
          opponent_health -= 1
          health -= 1
          kill_both = False
          pass
      if effect == 'switch_bubbles': #Switches your bubble while doing some damage
        pass
      if effect == 'drain_health': #Takes a certain amount of health from opponent to heal your bubble
        if drain == True:
          opponent_health -= damage
          health += damage
          drain = False
          pass
      if effect == 'attract_attention': #Makes all opposing bubbles attack it no matter where they aim, kinda like a meat shield. Has a limit to how much damage it can take.
        pass
	
  def effectivness(self, target):
    effect1 = target.type1.type_adv(self.move_type)
    effect2 = None
    effect3 = None
    if(not target.type2 == None):
      effect2 = target.type2.type_adv(self.move_type)
    if(not target.type3 == None):
      effect3 = target.type3.type_adv(self.move_type)
			
    return {
			"ef1": effect1, 
			"ef2": effect2, 
			"ef3": effect3
		}