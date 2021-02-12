from move import Move
from bubble import Bubble

#Bubbles:

#Create a Bubble

#Format Example: bubble = Bubble('Name', 'Bubble Energy', 'First Move Name', 'Second Move Name', 'Third Move Name', 'Fourth Move Name', 'First Move Damage', 'Second Move Damage', 'Third Move Damage', 'Fourth Move Damage', 'First Move Energy', 'Second Move Energy', 'Third Move Energy', 'Fourth Move Energy', 'Bubble Speed', 'Bubble Health', 'level', 'XP', 'type')

none = Move('NOT_AVAILABLE', 0, 0, 'None', 'None', 'None', 0)

bump_fake = Move('Bump', 0, 1, 'None', 'Type', 'None', 0)

crash_fake = Move('Crash', 0, 2, 'None', 'Type', 'None', 0)

cut = Move('Cut', 20, 120, 'None', 'Normal', 'Bleeding', 5)

jab = Move('Jab', 15, 160, 'None', 'Normal', 'Bleeding', 5)

xcannon = Move('X-Cannon', 25, 240, 'None', 'Normal', 'Paralysis', 5)

spike = Move('Spike', 10, 180, 'None', 'Normal', 'Bleeding', 2)

spike_ring = Move('Spike Ring', 10, 240, 'None', 'Steel', 'None', 0)

spike_beam = Move('Spike Beam', 35, 280, 'None', 'Steel', 'None', 0)

slash = Move('Slash', 30, 80, 'None', 'Normal', 'Bleeding', 5)

spin = Move('Spin', 25, 120, 'None', 'Normal', 'Bleeding', 5)

block = Move("Block", 15, 80, "Shield", "Normal", "None", 0)

screen_slash = Move("Screen Slash", 0 ,120, "None", "Normal", "None", 0)

spike_screen = Move("Spike Screen", 15, 160, "None", "Normal", "Bleeding", 9)

screen_ram = Move("Screen Ram", 30, 280, "None", "Normal", "None", 0)

mow = Move("Mow", 25, 80, "None", "Normal", "None", 0)

plow = Move("Plow", 5, 120, "None", "Normal", "None", 0)

lawnmow = Move("Lawnmow", 25, 250, "None", "Normal", "Bleeding", 5)

tear = Move("Tear", 10, 80, "None", "Normal", "None", 0)

rip = Move("Rip", 5, 120, "None", "Fighting", "None", 0)

shred = Move("Shred", 20, 200, "Rage", "Fighting", "None", 0)

ram = Move("Ram", 20, 30, "None", "Normal", "None", 0)

crash = Move("Crash", 10, 80, "None", "Normal", "None", 0)

shield = Move("Shield", 15, 120, "Shield", "Steel", "None", 0)

deflection_shield = Move("Deflection Shield", 25, 240, "Deflect", "Steel", "None", 0)

rollout = Move('Rollout', 20, 180, 'None', 'Normal', 'Bleeding', 5)

xslash = Move('X-Slash', 20, 200, 'None', 'Normal', 'Bleeding', 5)

slash_charge = Move('Slash Charge', 25, 260, 'None', 'Fighting', 'Bleeding', 6)

mad = Move('Mad', 10, 80,'None','Fighting','None',0)

rage = Move('Rage', 0, 120,'Rage','Fighting','None',0)

trigger = Move('Trigger', 35, 240,'None','Fighting','None',0)

uppercut = Move('Uppercut', 10, 120, 'None', 'Fighting', 'None', 0)

quake_smash = Move('Quake Smash', 5, 160, 'None', 'Fighting', 'None', 0)

orbit_smash = Move('Orbit Smash', 45, 240, 'None', 'Rock', 'None', 0)

deadly_torando_smash = Move('Deadly Tornado Smash', 50, 360, 'None', 'Air', 'None', 0)

fire_blast = Move('Fire Blast', 10, 140, 'None', 'Fire', 'Burn', 6)

water_cannon = Move('Water Cannon', 10, 160, 'None', 'Water', 'None', 0)

fusion_beam = Move('Fusion Beam', 35, 280, 'None', 'Psychic', 'None', 0)

pebble_rain = Move('Pebble Rain', 5, 120, 'None', 'Rock', 'None', 0)

earthquake = Move('Earthquake', 5, 160, 'None', 'Ground', 'None', 0)

rock_toss = Move('Rock Toss', 25, 240, 'None', 'Rock', 'None', 0)

swipe = Move('Swipe', 15, 40, "None", "Normal", "None", 0)

rollout_shield = Move("Rollout Shield", 0, 160, "None", "Steel", "None", 0)

ram = Move("Ram", 20, 200, "None", "Normal", "None", 0)

fiery_smash = Move("Fiery Smash", 25, 240, "None", "Fire", "Burn", 10)

bite = Move("Bite", 15, 100, "None", "Dark", "Bleeding", 5)

headbutt = Move("Headbutt", 10, 150, "None", "Normal", "None", 0)

rock_slice = Move("Rock Slice", 10, 240, "None", "Rock", "None", 0)

bash = Move("Bash", 15, 160, "None", "Normal", "None", 0)

blast = Move("Blast", 5, 240, "None", "Steel", "None", 0)

laser = Move("Laser", 45, 440, "None", "Electric", "None", 0)

bullet_wave = Move("Bullet Wave", 55, 520, "None", "Steel", "None", 0)

shoot = Move("Shoot", 15, 120, "None", "Steel", "None", 0)

rapid_fire = Move("Rapid Fire", 5, 160, "None", "Steel", "None", 0)

laser_beam = Move("Laser Beam", 25, 280, "None", "Electric", "None", 0)

tracking_laser = Move("Tracking Laser", 40, 360, "None", "Electric", "None", 0)

gunfire = Move("Gunfire", 15, 80, "None", "Steel", "None", 0)

sniper_shot = Move("Sniper Shot", 5, 120, "None", "Steel", "None", 0)

bulletstorm = Move("Bulletstorm", 15, 200, "None", "Steel", "None", 0)

#
#
#
#
#
#

penta_spike = Bubble('Penta-Spike', '45', jab, spike, spike_ring, spike_beam, '7', '880', '20', '0', 'Normal', '4', '4', '45', '880', 'None_Yet', 'Unkown_For_Now')

jab = Bubble('Jab', '35', cut, jab, xcannon, none, '3', '640', '1', '0', 'Normal', '3', '3', '35', '640', penta_spike, '20')

slasher = Bubble('Slasher', '55', spin, rollout, xslash, slash_charge, '13', '760', '20', '0', 'Normal', '4', '4', '55', '760','None_Yet','Unkown_For_Now')

spin = Bubble('Spin', '40', slash, spin, rollout, none, '7', '520', '1', '0', 'Normal', '3', '3', '40', '520', slasher, '20')

screen = Bubble('Screen', '40', block, screen_slash, spike_screen, screen_ram, '5', '960', '20', '0', 'Normal', '4', '4', '40', '960','None_Yet', 'Unkown_For_Now')

mow = Bubble('Mow', '30', mow, plow, lawnmow, none, '1', '680', '1', '0', 'Normal', '3', '3', '30', '680', screen, '20') 

fake = Bubble('Fake', '0', bump_fake, crash_fake, none, none, '0', '1', '1', '0', 'Normal', '2', '2', '1', '1', None, None)

rip = Bubble('Rip', '35', tear, rip, shred, none, '5', '560', '1', '0', 'Fighting', '4', '3', '35', '560','None_Yet', 'Unkown_For_Now')

shield = Bubble('Shield', '25', ram, crash, shield, deflection_shield, '3', '680', '1', '0', 'Steel', '4', '4', '25', '680','None_Yet', 'Unkown_For_Now')

smasher = Bubble('Smasher', '10', uppercut, quake_smash, orbit_smash, deadly_torando_smash, '1', '1200', '1', '0', 'Fighting', '4', '4', '10', '1200','None_Yet', 'Unkown_For_Now')

rager = Bubble('Rager', '15', mad, rage, trigger, none, '5', '640', '1', '0', 'Fighting', '3', '3', '15', '640', smasher, '30')

twin = Bubble('Twin', '35', fire_blast, water_cannon, fusion_beam, none,'7', '680', '1', '0', 'Psychic', '3', '3', '35', '680','None_Yet', 'Unkown_For_Now')

miner = Bubble('Miner', '25', pebble_rain, earthquake, rock_toss, none, '5', '560', '1', '0', 'Rock', '3', '3', '25', '560','None_Yet', 'Unkown_For_Now')

cannonball = Bubble('Cannonball', '20', swipe, rollout_shield, ram, fiery_smash, '5', '680', '1', '0',
'Steel', '4', '4', '20', '680','None_Yet', 'Unkown_For_Now')

antser = Bubble('Antser', '25', bite, headbutt, rock_slice, none, '3', '640', '1', '0', 'Rock', '3', '3', '25', '640','None_Yet', 'Unkown_For_Now')

tank = Bubble('Tank', '60',bash, blast, laser, bullet_wave, '11', '1280', '65', '0', 'Steel', '4', '4', '60', '1280','None_Yet', 'Unkown_For_Now')

laser = Bubble('Laser', '50', shoot, rapid_fire, laser_beam, tracking_laser, '7', '920', '30', '0', 'Steel', '4', '4', '50', '920',tank,'65')

gunner = Bubble('Gunner', '30', gunfire, sniper_shot, bulletstorm, none, '3', '560', '1', '0', 'Steel', '3', '3', '30', '560',laser,'30')



#Make the bubble above this comment
#Format Example: bubble = Bubble('Name', 'Bubble Energy', First Move, Second Move, Third Move, Fourth Move, 'Bubble Speed', 'Bubble Health', 'level', 'XP', 'type','amount of moves', 'total moves', 'base energy', 'base health', Evolves to, 'Evolution level') 

