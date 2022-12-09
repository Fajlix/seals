from agents import Agent
import numpy as np
from itertools import combinations
import time
class Environment:
    def __init__(self, agents:list,stage,split, dt=0.01, sime_time=1000, xMin=0, xMax=1000, yMin=0, yMax=1000):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        if type(agents[0]) is not Agent:
            raise TypeError("agents should be of type Agent")
        self.agents = agents
        self.stage=stage
        self.split=split
        self.dt = dt
        self.time = 0
        self.sime_time = sime_time
    def repulsiveForceMagnitude(self, distance, magnitude):
        # shouod be exponential force ?
        if distance <= 0:
            distance = 10**-10
        return magnitude/(distance**2)


    def forcesBetweenAgents(self, listOfCollisions,agent_radius=8, magnitude=10): 
        # the force between the agents should exponential to the distance 
        # list of collisions is a list of agents that are colliding
        # between them
        start = time.time()
        for collision in listOfCollisions:
            # calculate the distance between the agents
            pos1 = collision[0].position
            pos2 = collision[1].position
            distance = np.sqrt(np.power(pos2[0]-pos1[0],2) + np.power(pos2[1]-pos1[1],2))
            distance = distance - 2*agent_radius
            # calculate the force between the agents
            force = self.repulsiveForceMagnitude(distance, magnitude)
            # calculate the direction of the force
            direction = np.array([pos2[0]-pos1[0], pos2[1]-pos1[1]])
            norm = np.sqrt(np.power(direction[0],2) + np.power(direction[1],2))
            direction = direction/norm
            # calculate the force vector
            forceVector = force*direction
            # apply the force to the agents
            collision[0].external_forces.append(-forceVector)
            collision[1].external_forces.append(forceVector)

            

    def update(self):
        # remove agents that are not alive
        self.agents = [agent for agent in self.agents if agent.alive]
        # set the external forces to zero

        for agent in self.agents:
            agent.external_forces = []
            agent.external_forces.append(np.array([0,0]))
        listOfCollisions = self.checkCollisions()
        self.forcesBetweenAgents(listOfCollisions, magnitude=10)
        #print(listOfCollisions)
        for agent in self.agents:
            agent.step(self.dt,self.stage,self.split)
        self.time += self.dt

    def getAgentPositions(self):
        return np.array([agent.position for agent in self.agents])
    
    def getAgentHealth(self):
        return np.array([agent.health for agent in self.agents])


    def getAgentInfo(self):
        return np.array([[agent.position, agent.health] for agent in self.agents])


    def checkCollisions(self, radius=16):
        # get positions of all agents
        
        positions = self.getAgentPositions()
        # get positions squared
        radiussquare = 2*radius**2
        start = time.time()
        # get the distance between all agents
        distances = np.sum(positions**2, axis=1)[:, None] + np.sum(positions**2, axis=1) - 2*np.dot(positions, positions.T)
        end = time.time()
        #print("time taken to check collisions: ", end-start)
        # calculate the distance between all
        # check if the distance is less than the radius
        # set the diagonal to be 1000
        np.fill_diagonal(distances, np.inf)
        collisions = np.where(distances < radiussquare)
        # get only the unique pairs
        collisions = np.unique(np.sort(collisions, axis=0), axis=1)
        
        # get the agents that are colliding
        agents = []
        for i in range(len(collisions[0])):
            agents.append([self.agents[collisions[0][i]], self.agents[collisions[1][i]]])
        
        return agents
