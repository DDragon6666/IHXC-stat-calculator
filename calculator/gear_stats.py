
weapon_info = [
    {'atk': 0},
    {'atk': 32},
    {'atk': 38},
    {'atk': 66},
    {'atk': 85},
    {'atk': 168},
    {'atk': 218},
    {'atk': 267},
    {'atk': 414},
    {'atk': 502},
    {'atk': 590},
    {'atk': 678},
    {'atk': 914},
    {'atk': 1116},
    {'atk': 1317},
    {'atk': 1519},
    {'atk': 2464, 'crit damage': 3},
    {'atk': 3704, 'crit damage': 5}
]

armour_info = [
    {'hp': 0},
    {'hp': 141},
    {'hp': 169},
    {'hp': 337},
    {'hp': 434},
    {'hp': 970},
    {'hp': 1255},
    {'hp': 1541},
    {'hp': 2645},
    {'hp': 3207},
    {'hp': 3770},
    {'hp': 4333},
    {'hp': 6401},
    {'hp': 7811},
    {'hp': 9222},
    {'hp': 10632},
    {'hp': 32455, 'damage reduction': 1},
    {'hp': 52449, 'damage reduction': 2}
]

boots_info = [
    {'hp': 0},
    {'hp': 94},
    {'hp': 113},
    {'hp': 225},
    {'hp': 289},
    {'hp': 647},
    {'hp': 837},
    {'hp': 1027},
    {'hp': 1763},
    {'hp': 2138},
    {'hp': 2513},
    {'hp': 2889},
    {'hp': 4267},
    {'hp': 5207},
    {'hp': 6148},
    {'hp': 7088},
    {'hp': 20146, 'block': 2},
    {'hp': 32367, 'block': 4}
]

accesory_info = [
    {'atk': 0},
    {'atk': 21},
    {'atk': 25},
    {'atk': 44},
    {'atk': 57},
    {'atk': 112},
    {'atk': 145},
    {'atk': 178},
    {'atk': 276},
    {'atk': 335},
    {'atk': 393},
    {'atk': 452},
    {'atk': 610},
    {'atk': 744},
    {'atk': 878},
    {'atk': 1013},
    {'atk': 1643, 'skill damage': 3},
    {'atk': 2469, 'skill damage': 5}
]

bonus_multipliers = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [2, 3, 1],
    [4, 5, 2],
    [5, 7, 4],
    [7, 9, 4],
    [8, 11, 5],
    [10, 13, 5],
    [11, 15, 6],
    [12, 17, 7],
    [14, 19, 7],
    [15, 20, 8],
    [16, 21, 8]
]


# important for later
class_gear_additional_bonuses = {
    'warrior': [
        ['block', 10],
        ['damage reduction', 5],
        ['speed', 20],
        ['control immunity', 5]
    ],
    'mage': [
        ['crit', 5],
        ['precision', 10],
        ['speed', 20],
        ['skill damage', 10]
    ],
    'ranger': [
        ['crit', 5],
        ['block', 5],
        ['speed', 20],
        ['damage reduction', 5]
    ],
    'assassin': [
        ['crit', 5],
        ['armour break', 10],
        ['speed', 20],
        ['crit damage', 5]
    ],
    'priest': [
        ['atk', 5],
        ['damage reduction', 5],
        ['speed', 20],
        ['hp', 5]
    ]
}