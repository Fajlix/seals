import pygame
from agents import Agent
import numpy as np

class Environment:
    def __init__(self, agents:Agent, dt=0.1, sime_time=1000, xMin=0, xMax=1000, yMin=0, yMax=1000):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.agents = agents
        self.dt = dt
        self.sime_time = sime_time

    def update(self):
        for agent in self.agents:
            agent.step(self.dt)

    def getAgentPos(self):
        return [agent.position for agent in self.agents]

    def checkCollisions(self, listOfPixels):
        listOfCollisions = []
        for i in range(len(listOfPixels)-1):
            for j in range(i+1,len(listOfPixels)):
                pos1 = listOfPixels[i].getPosition()
                pos2 = listOfPixels[j].getPosition()
                distance = np.sqrt(np.power(pos2[0]-pos1[0],2) + np.power(pos2[1]-pos1[1],2))
                if distance < listOfPixels[i].getSize() + listOfPixels[j].getSize():
                    listOfCollisions.append((i,j))
