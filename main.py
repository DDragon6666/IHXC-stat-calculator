
from math import *
from calculator.stones import STONES
from calculator.artifacts import ARTIFACTS
from calculator.heroes import HERO_STATS
from calculator.stat_finder import get_stats


PRINTED_STATS = ('hp',
                 'atk',
                 'armour',
                 'speed',
                 'skill damage',
                 'precision',
                 'block',
                 'crit',
                 'crit damage',
                 'armour break',
                 'control immunity',
                 'damage reduction',
                 'holy damage')

BASE_STATS = {'banned': False,
              'hp': 0,
              'atk': 0,
              'class': 'warrior',
              'faction': 'shadow',
              'hp_mult': 0,
              'atk_mult': 0,
              'armour_mult': 0,
              'armour': 0,
              'speed': 0,
              'skill damage': 0,
              'precision': 0,
              'block': 0,
              'crit': 0,
              'crit damage': 0,
              'armour break': 0,
              'control immunity': 0,
              'damage reduction': 0,
              'holy damage': 0,
              'energy': 50,
              'dodge': 0,
              'heal effect': 0,
              'effect of being healed': 0,
              'stun immunity': 0, # cc immunities
              'petrify immunity': 0,
              'freeze immunity': 0,
              'bleed immunity': 0, # dot immunities
              'burn immunity': 0,
              'dot received reduction': 0,
              'all damage reduction': 0,
              'control precision': 0,
              'all damage dealt': 0,
              'crit damage reduction': 0,
              'damage against warrior': 0, # class damage mults
              'damage against mage': 0,
              'damage against ranger': 0,
              'damage against assasin': 0,
              'damage against priest': 0, # cc damage mults
              'damage against frozen': 0,
              'damage against petrified': 0,
              'damage against stunned': 0,
              'damage against bleeding': 0, # dot damage mults
              'damage against poison': 0,
              'crit against burning': 0, # weird shit
              'rounds of being controlled': 0
              }

# get hero
hero = None
while HERO_STATS.get(hero) is None:
    hero = input('Hero:   (? - shows the possible choices)\n').lower()
    if hero == '?':
        for hero_name in HERO_STATS: print(hero_name.capitalize())
    else:
        nhero = ''
        for letter in hero: nhero += letter if letter != '-' else ' ' # remove - from hero names
        hero = nhero
        if HERO_STATS.get(hero) is None: print('Please choose an available hero')

# get stone
stone = None
for i, stone_type in enumerate(STONES):
        text = str(i+1) + ': '
        for stat in stone_type:
            text += stat + ': ' + str(stone_type.get(stat)) + ', '
        print(text)
while stone is None:
    stone = input('Choose the stone: (use the number next to the stone)\n')
    try:
        stone = int(stone)
        stone -= 1
        if not(0 <= stone < len(STONES)):
            stone = None
            print(f'Please have the number between {1} and {len(STONES)}')
    except:
        stone = None
        print('Please use a number')

# get artifact
artifact = None
while ARTIFACTS.get(artifact) is None:
    artifact = input('Artifact:   (? - shows the possible choices)\n').lower()
    if artifact == '?':
        for artifact_name in ARTIFACTS: print(artifact_name.capitalize())
    else:
        nartifact = ''
        for letter in artifact: nartifact += letter if letter != "'" else '' # remove ' from artifact names
        artifact = nartifact
        if ARTIFACTS.get(artifact) is None: print('Please choose an available artifact')

# get equipment
weapon = None
armour = None
boots = None
accesory = None
equipment_names = ('None', '1* yellow', '2* yellow',
                   '1* purple', '2* purple',
                   '1* green', '2* green', '3* green',
                   '1* red', '2* red', '3* red', '4* red',
                   '1* orange', '2* orange', '3* orange', '4* orange',
                   '5* orange', '6* orange', 'class gear', 'wrong class gear')

for i, name in enumerate(equipment_names):
    print(f'{i}: {name}')

while weapon is None:
    weapon = input('Choose the weapon: (use the number next to the weapon)\n')
    try:
        weapon = int(weapon)
        if not(0 <= weapon <= 19):
            weapon = None
            print('Please have the number between 0 and 19')
    except:
        weapon = None
        print('Please use a number')
while armour is None:
    armour = input('Choose the armour: (use the number next to the armour)\n')
    try:
        armour = int(armour)
        if not(0 <= armour <= 19):
            armour = None
            print('Please have the number between 0 and 19')
    except:
        armour = None
        print('Please use a number')
while boots is None:
    boots = input('Choose the boots: (use the number next to the boots)\n')
    try:
        boots = int(boots)
        if not(0 <= boots <= 19):
            boots = None
            print('Please have the number between 0 and 19')
    except:
        boots = None
        print('Please use a number')
while accesory is None:
    accesory = input('Choose the accesory: (use the number next to the accesory)\n')
    try:
        accesory = int(accesory)
        if not(0 <= accesory <= 19):
            accesory = None
            print('Please have the number between 0 and 19')
    except:
        accesory = None
        print('Please use a number')


# get stats
stats = get_stats(hero, artifact, stone, weapon, armour, boots, accesory)

for stat in PRINTED_STATS:
    print(f'{stat}: {stats.get(stat)}')

while True:
    extra_printed_stat = input('Specific stat:  (all - prints all stats|changed - prints changed stats)\n').lower()
    if extra_printed_stat == 'all':
        print()
        for stat in BASE_STATS:
            print(f'{stat}: {stats.get(stat)}')
    elif extra_printed_stat == 'changed':
        print()
        for stat in BASE_STATS:
            if BASE_STATS.get(stat) != stats.get(stat): print(f'{stat}: {stats.get(stat)}')
    elif stats.get(extra_printed_stat) is None: print('Not a valid stat')
    else: print(f'{extra_printed_stat}: {stats.get(extra_printed_stat)}')
