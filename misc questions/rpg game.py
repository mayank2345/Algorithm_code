"""
Problem Statement:

While playing an RPG game, you were assigned to complete one of the hardest quests in this game. There are n monsters you’ll need to defeat in this quest. Each monster i is described with two integer numbers – poweri and bonusi. To defeat this monster, you’ll need at least poweri experience points. If you try fighting this monster without having enough experience points, you lose immediately. You will also gain bonusi experience points if you defeat this monster. You can defeat monsters in any order.

The quest turned out to be very hard – you try to defeat the monsters but keep losing repeatedly. Your friend told you that this quest is impossible to complete. Knowing that, you’re interested, what is the maximum possible number of monsters you can defeat?

(Question difficulty level: Hardest)

Input:

The first line contains an integer, n, denoting the number of monsters. The next line contains an integer, e, denoting your initial experience.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, poweri, which represents power of the corresponding monster.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, bonusi, which represents bonus for defeating the corresponding monster.
"""


# Input code
# 1. Testcase
n = int(input("Enter Enemies Number:"))
exp = int(input("Enter Exp: "))
#2. Enemies
e,b = [],[]
for i in range(n):
    enemies = int(input("Enter enemy health "))
    e.append(enemies)
for i in range(n):
    bonus = int(input("Enter enemy score "))
    b.append(bonus)

# Sorting list
comb = list(zip(e,b))
comb.sort(key= lambda x: x[0])
ene, bon = zip(*comb)

count = 0
for i in range(n):
    if ene[i] <= exp:
        exp += bon[i]
        count += 1
    if ene[i] > exp:
        break
print("You defeated ",count)
print("Exp: ", exp)

