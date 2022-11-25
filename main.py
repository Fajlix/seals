'''
main file
'''
from draw import *
import random

positions = []
for i in range(10):
    x = random.randint(8/2, 1000 - 8/2)
    y = random.randint(8/2, 1000 - 8/2)
    positions.append((x,y))

graphic = Graphics(1000, 1000)

graphic.drawHuman(positions)
