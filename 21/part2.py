# AoC: Day 21

with open("input") as f:
    lines = f.readlines()

lines = map(lambda x: x.strip(), lines)

boss_hp     = int(lines[0].split(":")[1])
boss_damage = int(lines[1].split(":")[1])
boss_armor  = int(lines[2].split(":")[1])


"""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""
weapons = [ ( 8, 4)
          , (10, 5)
          , (25, 6)
          , (40, 7)
          , (74, 8)
          ]

"""
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""
armor = [ ( 13, 1)
        , ( 31, 2)
        , ( 53, 3)
        , ( 75, 4)
        , (102, 5)
        , (  0, 0)
        ]

"""
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""
rings = [ ( 25, 1, 0)
        , ( 50, 2, 0)
        , (100, 3, 0)
        , ( 20, 0, 1)
        , ( 40, 0, 2)
        , ( 80, 0, 3)
        , (  0, 0, 0)
        , (  0, 0, 0)
        ]


def playerWins(player, boss, turn):

    """
    Damage dealt by an attacker each turn is equal to the
    attacker's damage score minus the defender's armor score.
    An attacker always does at least 1 damage.
    """

    if turn == "player":
        damage_dealt = max([1, player[ "Damage" ] - boss[ "Armor" ]])

        boss["Hit Points"] -= damage_dealt

        if boss[ "Hit Points" ] <= 0:
            return True

        else:
            return playerWins(player, boss, "boss")


    elif turn == "boss":

        damage_dealt = max([1, boss[ "Damage" ] - player[ "Armor" ]])

        player["Hit Points"] -= damage_dealt

        if player[ "Hit Points" ] <= 0:
            return False

        else:
            return playerWins(player, boss, "player")



# create all combinations
# 1 weapon
# 0 or 1 armor
# 0, 1, or 2 rings
# simple solution: encode in data

ring_choice = []

for i in range(len(rings)):
    for j in range(len(rings)):
        if i != j:
            if i < j:
                ring_choice.append((rings[i], rings[j]))
            elif i > j:
                ring_choice.append((rings[j], rings[i]))

# remove duplicates
ring_choice = list(set(ring_choice))

most_expensive = 0 # '-infinity'

# find cheapest equipment
for (cost_a, armor_a) in armor:

    for (cost_w, damage_w) in weapons:

        for (r1, r2) in ring_choice:
            (cost_r1, damage_r1, armor_r1) = r1
            (cost_r2, damage_r2, armor_r2) = r2

            total_cost   = sum([cost_a, cost_w, cost_r1, cost_r2])
            total_armor  = sum([armor_a, armor_r1, armor_r2]     )
            total_damage = sum([damage_w, damage_r1, damage_r2]  )

            player = dict()
            player[ "Hit Points" ] = 100
            player[ "Damage"     ] = total_damage
            player[ "Armor"      ] = total_armor

            # symmetrical, but not the most concise
            boss  = dict()
            boss[ "Hit Points" ] = boss_hp
            boss[ "Damage"     ] = boss_damage
            boss[ "Armor"      ] = boss_armor

            if not playerWins(player, boss, "player"):
                if total_cost > most_expensive:
                    most_expensive = total_cost


print most_expensive