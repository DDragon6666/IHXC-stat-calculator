
from calculator.stat_finder import get_stats, BASE_STATS, BACKEND_STATS
from calculator.stones import STONES
from calculator.heroes import HERO_STATS
from calculator.artifacts import ARTIFACTS


def convert_from_str(hero_str: str):
    hero = ''
    stone = ''
    artifact = ''
    weapon = ''
    armour = ''
    boots = ''
    accesory = ''
    position = 0
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get hero name
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            hero += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get stone num
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            stone += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get artifact name
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            artifact += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get weapon number
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            weapon += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get armour number
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            armour += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get boots number
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            boots += letter
        except IndexError:
            break
    # remove spaces
    while True:
        try:
            letter = hero_str[position]
            if letter != ' ': break
            position += 1
        except IndexError:
            break
    # get accesory number
    while True:
        try:
            letter = hero_str[position]
            position += 1
            if letter == ',': break
            accesory += letter
        except IndexError:
            break

    # full class gear
    if weapon == 'c':
        weapon = '18'
        armour = '18'
        boots = '18'
        accesory = '18'

    return hero, stone, artifact, weapon, armour, boots, accesory

def get_hero_stats(hero_str: str):
    try:
        hero, stone, artifact, weapon, armour, boots, accesory = convert_from_str(hero_str)
        # check hero
        if HERO_STATS.get(hero) is None: raise ValueError(f'The hero ({hero}) is not possible')
        # check stone
        try: stone = int(stone)
        except: raise ValueError(f'The stone ({stone}) is not possible')
        stone -= 1
        if stone < 0 or stone > 23: raise ValueError(f'The stone ({stone+1}) is not possible')
        # check artifact
        if ARTIFACTS.get(artifact) is None: raise ValueError(f'The artifact ({artifact}) is not possible')
        # check weapon
        try: weapon = int(weapon)
        except: raise ValueError(f'The weapon ({weapon}) is not possible')
        if weapon < 0 or weapon > 19: raise ValueError(f'The weapon ({weapon}) is not possible')
        # check armour
        try: armour = int(armour)
        except: raise ValueError(f'The armour ({armour}) is not possible')
        if armour < 0 or armour > 19: raise ValueError(f'The armour ({armour}) is not possible')
        # check boots
        try: boots = int(boots)
        except: raise ValueError(f'The boots ({boots}) is not possible')
        if boots < 0 or boots > 19: raise ValueError(f'The boots ({boots}) is not possible')
        # check accesory
        try: accesory = int(accesory)
        except: raise ValueError(f'The accesory ({accesory}) is not possible')
        if accesory < 0 or accesory > 19: raise ValueError(f'The accesory ({accesory}) is not possible')
    except ValueError as e:
        print(e)
        return
    # get stats
    stats = get_stats(hero, artifact, stone, weapon, armour, boots, accesory)
    stats['name'] = hero
    return stats

equipment_names = ('None', '1* yellow', '2* yellow',
                   '1* purple', '2* purple',
                   '1* green', '2* green', '3* green',
                   '1* red', '2* red', '3* red', '4* red',
                   '1* orange', '2* orange', '3* orange', '4* orange',
                   '5* orange', '6* orange', 'class gear', 'wrong class gear')
print('Equipment: ')
for i, name in enumerate(equipment_names):
    print(f'{i}: {name}')

print('Stones: ')
for i, stone_type in enumerate(STONES):
        text = str(i+1) + ': '
        for stat in stone_type:
            text += stat + ': ' + str(stone_type.get(stat)) + ', '
        print(text)

print('Inputs should be hero_name, stone_number, artifact, weapon, armour, boots, accesory')
print('to have full class gear you can do c for the weapon and ignore the rest of the equipment')

hero1_stats = None
while hero1_stats is None:
    hero1 = input('Hero 1: ').lower()
    hero1_stats = get_hero_stats(hero1)

hero2_stats = None
while hero2_stats is None:
    hero2 = input('Hero 2: ').lower()
    hero2_stats = get_hero_stats(hero2)

hero3_stats = None
while hero3_stats is None:
    hero3 = input('Hero 3: ').lower()
    hero3_stats = get_hero_stats(hero3)

hero4_stats = None
while hero4_stats is None:
    hero4 = input('Hero 4: ').lower()
    hero4_stats = get_hero_stats(hero4)

hero5_stats = None
while hero5_stats is None:
    hero5 = input('Hero 5: ').lower()
    hero5_stats = get_hero_stats(hero5)

hero6_stats = None
while hero6_stats is None:
    hero6 = input('Hero 6: ').lower()
    hero6_stats = get_hero_stats(hero6)

all_hero_stats = [hero1_stats, hero2_stats, hero3_stats, hero4_stats, hero5_stats, hero6_stats]
sorted_all_hero_stats = [hero1_stats, hero2_stats, hero3_stats, hero4_stats, hero5_stats, hero6_stats]

print('Command options are sort or hero(number) then a stat or for a specific hero all or changed')
while True:
    print()
    command = input('Command: ')
    if command[:4] == 'sort':
        stat = command[5:]
        if hero1_stats.get(stat) is None or stat in BACKEND_STATS:
            print(f'Stat ({stat}) not found')
            continue
        sorted_all_hero_stats.sort(key = lambda x: x.get(stat))
        for i in range(6):
            print(f'{sorted_all_hero_stats[i].get("name")}: {sorted_all_hero_stats[i].get(stat)}')
    elif command[:4] == 'hero':
        num = command[4]
        try:
            num = int(num)
            if num < 1 or num > 6: raise ValueError
            stat = command[6:]
            hero = all_hero_stats[num-1]
            if stat == 'all':
                print()
                for stat in BASE_STATS:
                    if stat in BACKEND_STATS: continue
                    print(f'{stat}: {hero.get(stat)}')
            elif stat == 'changed':
                print()
                for stat in BASE_STATS:
                    if stat in BACKEND_STATS: continue
                    if BASE_STATS.get(stat) != hero.get(stat): print(f'{stat}: {hero.get(stat)}')
            else:
                if hero.get(stat) is None or stat in BACKEND_STATS:
                    print(f'Stat ({stat}) not found')
                    continue
                print(f'{hero.get("name")}: {hero.get(stat)}')
        except:
            print(f'{command[:5]} is not a valid option')
    else:
        print('invalid command')

