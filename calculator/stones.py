

STONES = [
    {'speed': 115,
     'percent hp': 32},
    {'speed': 115,
     'percent atk': 26},
    {'speed': 115,
     'crit': 23},
    {'speed': 115,
     'heal effect': 29},
    {'speed': 115,
     'precision': 23},
    {'atk': 4000,
     'percent atk': 37},
    {'hp': 25000,
     'percent hp': 46},
    {'atk': 1550,
     'percent atk': 24,
     'precision': 24},
    {'atk': 1550,
     'percent atk': 24,
     'armour break': 50},
    {'atk': 1550,
     'percent atk': 24,
     'holy damage': 36},
    {'atk': 1550,
     'percent atk': 24,
     'skill damage': 80},
    {'crit': 23,
     'crit damage': 55,
     'percent atk': 10},
    {'crit': 23,
     'precision': 23},
    {'crit': 23,
     'armour break': 50},
    {'percent hp': 33,
     'crit': 23},
    {'percent hp': 33,
     'percent atk': 26},
    {'percent hp': 33,
     'effect of being healed': 29},
    {'percent hp': 33,
     'precision': 33},
    {'block': 28,
     'percent hp': 35},
    {'block': 28,
     'percent atk': 28},
    {'skill damage': 80,
     'holy damage': 36},
    {'holy damage': 80,
     'precision': 23},
    {'atk': 1550,
     'percent hp': 28,
     'holy damage': 36},
    {'atk': 1550,
     'percent hp': 28,
     'heal effect': 28}
]


def do_addition_stone(stats, stone_num):
    stone = STONES[stone_num]
    print(stone)
    for i in stone:
        if i[:7] == 'percent': continue
        stats[i] += stone.get(i)

def do_stone_percents(stats, stone_num):
    stone = STONES[stone_num]
    for i in stone:
        if not(i[:7] == 'percent'): continue
        stat = i[8:]
        stats[stat] *= 1+stone.get(i)/100
        stats[stat] = int(stats.get(stat))