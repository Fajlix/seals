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

# Booleans:
agent_individual_mass = False
agent_individual_size = False

# Variables
no_of_agents = 300
height_of_window, width_of_window = 1000, 1000


def run(stage=True,split= True):
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
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(50, width_of_window - 50)
                y = random.randint(50, height_of_window - 50)
            agents.append(Agent(x, y, mass[i], size[i]))
    elif stage and split:
        for i in range(int(no_of_agents/2)):
            x = random.randint(50, width_of_window - 550)
            y = random.randint(50, height_of_window - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(50, width_of_window - 550)
                y = random.randint(50, height_of_window - 50)
            agents.append(Agent(x, y, mass[i], size[i]))
        for i in range(int(no_of_agents/2)):
            x = random.randint(550, width_of_window - 50)
            y = random.randint(50, height_of_window - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(550, width_of_window - 50)
                y = random.randint(50, height_of_window - 50)
            agents.append(Agent(x, y, mass[i], size[i]))
    else:
        for i in range(no_of_agents):
            x = random.randint(8/2, width_of_window - 8/2)
            y = random.randint(8/2, height_of_window - 8/2)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(8/2, width_of_window - 8/2)
                y = random.randint(8/2, height_of_window - 8/2)
            agents.append(Agent(x, y, mass[i], size[i]))
    


    env = Environment(agents,stage,split)
    #why is this different? 
    graphics_width_of_window, graphics_height_of_window = 200, 200
    graphic = Graphics(graphics_width_of_window, graphics_height_of_window)


    if stage and not split:    
        graphic.drawHuman_stage(env.getAgentPositions())
    elif stage and split:
        graphic.drawHuman_stage_split(env.getAgentPositions())
    else:
        graphic.drawHuman(env.getAgentInfo())

    running = True
    last_update_time = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        env.update()
        if env.time - last_update_time > 0.5:

            if stage and not split:    
                graphic.drawHuman_stage(env.getAgentPositions())
            elif stage and split:
                graphic.drawHuman_stage_split(env.getAgentPositions())
            else:
                graphic.drawHuman(env.getAgentInfo())


            last_update_time = env.time

if __name__ == "__main__":
    run()
   
