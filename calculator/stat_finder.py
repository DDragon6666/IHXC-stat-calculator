
from calculator.guild_tech import add_guild_tech
from calculator.gear import add_gear_stats
from math import *
from calculator.stones import do_addition_stone, do_stone_percents
from calculator.artifacts import do_addition_artifact, do_artifact_percents
from calculator.heroes import HERO_STATS

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

BACKEND_STATS = ('hp_mult',
                 'atk_mult',
                 'armour_mult')

BOOL_STATS = ('stun immunity',
              'petrify immunity',
              'freeze immunity',
              'bleed immunity',
              'burn immunity')

def get_stats(hero: str, artifact: str, stone: int, weapon: int, armour: int, boots: int, accesory: int) -> list:

    stats = HERO_STATS.get(hero)

    for stat in BASE_STATS:
        if stats.get(stat) is None: stats[stat] = BASE_STATS.get(stat)

    do_addition_stone(stats, stone) # things like +1550 atk or +80% skill damage
    do_addition_artifact(stats, artifact)
    add_gear_stats(stats, (weapon, armour, boots, accesory))
    add_guild_tech(stats)
    do_stone_percents(stats, stone) # things like 26% atk
    do_artifact_percents(stats, artifact)

    for backend_stat in BACKEND_STATS:
        del stats[backend_stat]
        del BASE_STATS[backend_stat]
    for bool_stat in BOOL_STATS:
        stats[bool_stat] = bool(stats.get(bool_stat))

    return stats


'''
made by

     Y&###&PY?:       !####&BYY~.                                                                   
     ~Y@@@J?G&@@Y.    :7&@@G75#@@B^                                                                 
      J@@!    ^&@&.    .@@#    .5@@?   ..  ...       .....        ...         .!7~       77. ^?7^   
     .@@B      :@@!    G@@:      #@#   &@&&@&@@!  .?#@#&@@?    ~B&&&@&:    ^G@@@@@@~    G@@@&BG@@5  
     P@@:     .B@&    ^@@5      J@@~  ^@@@J. !7: 7@@5. 5@@.  ^#@^ .#@@.  .#@&7. .@@#   Y@@B7. :@@J  
    :@@5   .~B@@P.    #@&    ^Y@@&^   G@@.      Y@&.  Y@@Y  !@@! .&@@G  :@@5    ?@@7  ~@@?   .&@#   
   :B@@5JG&@@#J.    .J@@#J5&@@&P^    :@@J      .@@J:Y@@@@.  G@@5&@@@@^  P@@.  .G@@7  .&@B    &@&.   
 ?&@@@&B#Y7:      .#&@@@B#G7~.       ?@&.       ?#&#5?&@Y    ~7?~!@@G   ^&@@#&@&J    ~@@^   7@@^    
                                                                ^@@B                                
                                                            .YB&@&?                                 
'''
