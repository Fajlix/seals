'''
main file
'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from draw import *
from crowdPhysics import *
from environment import *
import random
import multiprocessing as mp
from numpy import random
import matplotlib.pyplot as plt


import numpy as np

# Booleans:
agent_individual_mass = False
agent_individual_size = False
stage = True
split = False
variable_attraction=True


# Variables
dead_list=[]
time_list=[]
no_of_agents = 500

height_of_window, width_of_window = 1000, 1000


def run():
    
    time_st = 0
    no_of_dead_agents = 0
    agents = []

    if agent_individual_mass:
        mass = random.normal(loc=70, scale=10, size=no_of_agents)  # Mean = 70kg, Std = 10kg, feel free to change
    else:
        mass = np.full(no_of_agents, 70)
    if agent_individual_size and agent_individual_mass:
        r = random.normal(loc=0.006, scale=0.001, size=no_of_agents)  # Chosen s.t. 70*0.006=0.42, std arbitrary
        size = np.multiply(r, mass)
    elif agent_individual_size:
        size = random.normal(loc=0.42, scale=0.05, size=no_of_agents)  # Mean = 42cm, Std = 5cm, feel free to change
    else:
        size = np.full(no_of_agents, 2)
    if stage and not split:
        for i in range(no_of_agents):
            x = random.randint(50, width_of_window - 50)
            y = random.randint(50, height_of_window - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 18 for agent in agents]):

                x = random.randint(50, width_of_window - 50)
                y = random.randint(50, height_of_window - 50)
            if variable_attraction:
                attraction = np.random.randint(3, high=12, size=None, dtype=int)
                agents.append(Agent(x, y, attraction,mass[i], size[i]))
            else:
                agents.append(Agent(x, y, 5,mass[i], size[i]))
    elif stage and split:
        for i in range(int(no_of_agents/2)):
            x = random.randint(50, width_of_window - 550)
            y = random.randint(50, height_of_window - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 18 for agent in agents]):

                x = random.randint(50, width_of_window - 550)
                y = random.randint(50, height_of_window - 50)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x, y, attraction,mass[i], size[i]))
            else:
                agents.append(Agent(x, y, 5,mass[i], size[i]))
        for i in range(int(no_of_agents/2)):
            x = random.randint(550, width_of_window - 50)
            y = random.randint(50, height_of_window - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(550, width_of_window - 50)
                y = random.randint(50, height_of_window - 50)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x, y, attraction,mass[i], size[i]))
            else:
                agents.append(Agent(x, y, 5,mass[i], size[i]))
    else:
        for i in range(no_of_agents):
            x = random.randint(8/2, width_of_window - 8/2)
            y = random.randint(8/2, height_of_window - 8/2)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):

                x = random.randint(8/2, width_of_window - 8/2)
                y = random.randint(8/2, height_of_window - 8/2)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x, y, attraction,mass[i], size[i]))
            else:
                agents.append(Agent(x, y, 5,mass[i], size[i]))
    env = Environment(agents,stage,split)
    graphic = Graphics(width_of_window, height_of_window)
    graphic.drawSimulation(env.getAgentPositions(), env.getAgentHealth(), stage, split, env.time)

    running = True
    last_update_time = 0
    while running and time_st<1000:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        no_of_dead_agents = no_of_dead_agents + env.update()
        if env.time - last_update_time >= 0.5:
            time_st = time_st + 1
            time_list.append(time_st)
            dead_list.append(no_of_dead_agents)
            graphic.drawSimulation(env.getAgentPositions(), env.getAgentHealth(), stage, split, env.time)

            last_update_time = env.time
            
    pygame.display.quit()
    pygame.quit()
    
    plt.plot(time_list, dead_list, color ='r')
    plt.title(str(no_of_agents)+ " agents", fontsize=20)
    plt.xlabel("time steps", fontsize=15)
    plt.ylabel("Number of dead agents",fontsize=15)
    plt.ylim(bottom=0)
    plt.show()
   
if __name__ == "__main__":
    run()


   
