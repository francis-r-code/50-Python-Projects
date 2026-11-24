# Project 4: Dice Roller
import random
import matplotlib.pyplot as plt

# Setup variables and determine dice sides & times to roll dice
dice_sides = int(input("Enter how many sides you want the dice to have: "))
rolls = int(input("Enter how many times you want to roll the dice: "))
dice = {}
roll_count = 0
graph_x = []
graph_y = []

# Roll the dice and track how many times each side was rolled
for side in range(dice_sides):
    dice[side + 1] = 0
while roll_count < rolls:
    dice[random.randint(1, dice_sides)] += 1
    roll_count += 1
for key in dice:
    graph_y.append(dice[key])
graph_x = list(dice)

# Print roll results
for key in dice:
    print("Side " + str(key) + ": " + str(dice[key]))

# Graph the rolls
fig, ax = plt.subplots()
ax.bar(graph_x, graph_y, width=1)
ax.set(xticks=graph_x)
plt.show()