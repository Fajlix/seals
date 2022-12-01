'''
main file
'''
from draw import *
from crowdPhysics import *
from environment import *
import random

agents = []

for i in range(10):
    x = random.randint(8/2, 1000 - 8/2)
    y = random.randint(8/2, 1000 - 8/2)
    agents.append(Agent(x,y))

env = Environment(agents)

graphic = Graphics(1000, 1000)

graphic.drawHuman(env.getAgentPos())

time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pixels = graphic.getPixels()
    listOfCollisions = env.checkCollisions(pixels)
    print(listOfCollisions)
    env.update()
    graphic.drawHuman(env.getAgentPos())

