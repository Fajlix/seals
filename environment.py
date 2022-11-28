import pygame
from agents import Agent

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