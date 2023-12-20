from calculator.gear_stats import *



def add_gear_stats(stats: dict, equipment) -> None:

    weapon, armour, boots, accesory = equipment

    _class = stats.get('class')
    
    stats['atk'] += weapon_info[min(17, weapon)].get('atk')*(1+stats.get('atk_mult')/100)

    stats['hp'] += armour_info[min(17, armour)].get('hp')*(1+stats.get('hp_mult')/100)

    stats['hp'] += boots_info[min(17, boots)].get('hp')*(1+stats.get('hp_mult')/100)

    stats['atk'] += accesory_info[min(17, accesory)].get('atk')*(1+stats.get('atk_mult')/100)

    c = 0
    d = 0

    for i in range(4):
        for j in range(i+1, 4):
            a = weapon if i == 0 else armour if i == 1 else boots
            b = armour if j == 1 else boots if j == 2 else accesory

            if a > 17: continue
            if b > 17: continue

            if a == b:
                if a == c:
                    # has to be 3-1 or 4
                    if d == 2:
                        stats['atk'] *= 1+bonus_multipliers[a][1]/100
                        stats['atk'] = int(stats.get('atk'))
                    if d == 5:
                        stats['hp'] *= 1+bonus_multipliers[a][2]/100
                        stats['hp'] = int(stats.get('hp'))
                else:
                    stats['hp'] *= 1+bonus_multipliers[a][0]/100
                    stats['hp'] = int(stats.get('hp'))
                d += 1
                c = a

    # class gear/incorrect class gear both add the same 7% atk/hp
    if weapon > 17:
        stats['atk'] *= 1.07
        stats['atk'] = int(stats.get('atk'))
    if armour > 17:
        stats['hp'] *= 1.07
        stats['hp'] = int(stats.get('hp'))
    if boots > 17:
        stats['hp'] *= 1.07
        stats['hp'] = int(stats.get('hp'))
    if accesory > 17:
        stats['atk'] *= 1.07
        stats['atk'] = int(stats.get('atk'))

    # correct class gear gives an additional atk/hp buff
    if weapon == 18:
        stats['atk'] *= 1.06
        stats['atk'] = int(stats.get('atk'))
        if _class == 'priest':
            stats['atk'] *= 1.05
            stats['atk'] = int(stats.get('atk'))
        else:
            bonus_stat, bonus_amount = class_gear_additional_bonuses.get(_class)[0]
            stats[bonus_stat] += bonus_amount
    if armour == 18:
        stats['hp'] *= 1.06
        stats['hp'] = int(stats.get('hp'))
        bonus_stat, bonus_amount = class_gear_additional_bonuses.get(_class)[1]
        stats[bonus_stat] += bonus_amount
    if boots == 18:
        stats['hp'] *= 1.06
        stats['hp'] = int(stats.get('hp'))
        bonus_stat, bonus_amount = class_gear_additional_bonuses.get(_class)[2]
        stats[bonus_stat] += bonus_amount
    if accesory == 18:
        stats['atk'] *= 1.06
        stats['atk'] = int(stats.get('atk'))
        if _class == 'priest':
            stats['hp'] *= 1.05
            stats['hp'] = int(stats.get('hp'))
        else:
            bonus_stat, bonus_amount = class_gear_additional_bonuses.get(_class)[3]
            stats[bonus_stat] += bonus_amount
