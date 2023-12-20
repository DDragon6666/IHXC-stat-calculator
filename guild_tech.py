
from math import floor

# Guild tech levels:
# all have the max of [60, 50, 40, 30, 20, 20, 20, 20] and have to have 8 numbers

# 30% hp, 25% atk, 20% crit, 15% block, 20% skill dmg, 80 spd, 20% hp/20% atk, 20% hp/20% skill dmg
warrior = [60, 50, 40, 30, 20, 20, 20, 20]

# 30% hp, 25% atk, 20% crit, 15% precision, 20% skill dmg, 80 spd, 20% hp/20% atk, 20% hp/20% skill dmg
mage = [60, 50, 40, 30, 20, 20, 20, 20]

# 30% hp, 25% atk, 20% block, 15% precision, 20% skill dmg, 80 spd, 20% hp/20% atk, 20% hp/20% skill dmg
ranger = [60, 50, 40, 30, 20, 20, 20, 20]

# 30% hp, 25% crit damage, 20% crit, 15% armour break, 20% skill dmg, 80 spd, 20% hp/20% atk, 20% hp/20% skill dmg
assassin = [60, 50, 40, 30, 20, 20, 20, 20]

# 30% hp, 25% block, 20% crit, 60 speed, 20% skill dmg, 20 spd 10% atk, 20% hp/20% atk, 20% hp/20% skill dmg
priest = [60, 50, 40, 30, 20, 20, 20, 20]



def add_warrior_guild_tech(stats: dict) -> None:

    stats['hp'] *= 1+(warrior[0])/200
    stats['hp'] = floor(stats.get('hp'))

    stats['atk'] *= 1+(warrior[1])/200
    stats['atk'] = floor(stats.get('atk'))

    stats['crit'] += (warrior[2])/2

    stats['block'] += (warrior[3])/2

    stats['skill damage'] += (warrior[4])

    stats['speed'] += (warrior[5])*4

    stats['hp'] *= 1+(warrior[6])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['atk'] *= 1+(warrior[6])/100
    stats['atk'] = floor(stats.get('atk'))

    stats['hp'] *= 1+(warrior[7])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['skill damage'] += (warrior[7])

def add_mage_guild_tech(stats: dict) -> None:

    stats['hp'] *= 1+(mage[0])/200
    stats['hp'] = floor(stats.get('hp'))

    stats['atk'] *= 1+(mage[1])/200
    stats['atk'] = floor(stats.get('atk'))

    stats['crit'] += (mage[2])/2

    stats['precision'] += (mage[3])/2

    stats['skill damage'] += (mage[4])

    stats['speed'] += (mage[5])*4

    stats['hp'] *= 1+(mage[6])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['atk'] *= 1+(mage[6])/100
    stats['atk'] = floor(stats.get('atk'))

    stats['hp'] *= 1+(mage[7])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['skill damage'] += (mage[7])

def add_ranger_guild_tech(stats: dict) -> None:

    stats['hp'] *= 1+(ranger[0])/200
    stats['hp'] = floor(stats.get('hp'))

    stats['atk'] *= 1+(ranger[1])/200
    stats['atk'] = floor(stats.get('atk'))

    stats['block'] += (ranger[2])/2

    stats['precision'] += (ranger[3])/2

    stats['skill damage'] += (ranger[4])

    stats['speed'] += (ranger[5])*4

    stats['hp'] *= 1+(ranger[6])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['atk'] *= 1+(ranger[6])/100
    stats['atk'] = floor(stats.get('atk'))

    stats['hp'] *= 1+(ranger[7])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['skill damage'] += (ranger[7])

def add_assassin_guild_tech(stats: dict) -> None:

    stats['hp'] *= 1+(assassin[0])/200
    stats['hp'] = floor(stats.get('hp'))

    stats['crit damage'] += (assassin[1])/2

    stats['crit'] += (assassin[2])/2

    stats['armour break'] += (assassin[3])/2

    stats['skill damage'] += (assassin[4])

    stats['speed'] += (assassin[5])*4

    stats['hp'] *= 1+(assassin[6])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['atk'] *= 1+(assassin[6])/100
    stats['atk'] = floor(stats.get('atk'))

    stats['hp'] *= 1+(assassin[7])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['skill damage'] += (assassin[7])

def add_priest_guild_tech(stats: dict) -> None:

    stats['hp'] *= 1+(priest[0])/200
    stats['hp'] = floor(stats.get('hp'))

    stats['block'] += (priest[1])/2

    stats['crit'] += (priest[2])/2

    stats['speed'] += (priest[3])*2

    stats['skill damage'] += (priest[4])

    stats['speed'] += (assassin[5])
    stats['atk'] *= 1+(priest[5])/200

    stats['hp'] *= 1+(priest[6])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['atk'] *= 1+(priest[6])/100
    stats['atk'] = floor(stats.get('atk'))

    stats['hp'] *= 1+(priest[7])/100
    stats['hp'] = floor(stats.get('hp'))
    stats['skill damage'] += (priest[7])

def add_guild_tech(stats):
    _class = stats.get('class')
    if _class == 'warrior':
        add_warrior_guild_tech(stats)
    if _class == 'mage':
        add_mage_guild_tech(stats)
    if _class == 'ranger':
        add_ranger_guild_tech(stats)
    if _class == 'assassin':
        add_assassin_guild_tech(stats)
    if _class == 'priest':
        add_priest_guild_tech(stats)