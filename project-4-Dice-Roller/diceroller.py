#Project 4: Dice Roller
import random
import matplotlib.pyplot as plt

diceSides = int(input("Enter how many sides you want the dice to have: "))
rolls = int(input("Enter how many times you want to roll the dice: "))
dice = {}
rollCount = 0
graphX = []
graphY = []

for side in range(diceSides):
    dice[side+1] = 0
while rollCount < rolls:
    dice[random.randint(1,diceSides)] += 1
    rollCount += 1
for key in dice:
    graphY.append(dice[key])
graphX = list(dice)

for key in dice:
    print("Side " + str(key) + ": " + str(dice[key]))

fig, ax = plt.subplots()
ax.bar(graphX, graphY, width=1)
ax.set(xticks=graphX)
plt.show()