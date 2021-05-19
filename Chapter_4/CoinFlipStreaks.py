import random
from itertools import groupby
numberOfStreaks = 0
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipList = []
    coinFlip = random.randint(0, 1)
    for flip in range(100):
        if coinFlip == 0:
            flipList.append('H')
        else:
            flipList.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(flipList)):
        if i == 0:
            pass
        elif flipList[i] == flipList[i-1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1


print('Chance of streak: %s%%' % (numberOfStreaks / 100))
