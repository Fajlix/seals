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


def run(stage,split,variable_attraction):
    
    agents = []
    
    if stage and not split:
        for i in range(100):
            x = random.randint(50, 1000 - 50)
            y = random.randint(50, 1000 - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(50, 1000 - 50)
                y = random.randint(50, 1000 - 50)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x,y,attraction))
            else:
                agents.append(Agent(x,y,5))
    elif stage and split:
        for i in range(50):
            x = random.randint(50, 1000 - 550)
            y = random.randint(50, 1000 - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(50, 1000 - 550)
                y = random.randint(50, 1000 - 50)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x,y,attraction))
            else:
                agents.append(Agent(x,y,5))
        for i in range(50):
            x = random.randint(550, 1000 - 50)
            y = random.randint(50, 1000 - 50)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(550, 1000 - 50)
                y = random.randint(50, 1000 - 50)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x,y,attraction))
            else:
                agents.append(Agent(x,y,5))
    else:
        for i in range(100):
            x = random.randint(8/2, 1000 - 8/2)
            y = random.randint(8/2, 1000 - 8/2)
            while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
                x = random.randint(8/2, 1000 - 8/2)
                y = random.randint(8/2, 1000 - 8/2)
            if variable_attraction:
                attraction = np.random.randint(1, high=7, size=None, dtype=int)
                agents.append(Agent(x,y,attraction))
            else:
                agents.append(Agent(x,y,5))
    


    env = Environment(agents,stage,split)

    graphic = Graphics(1000, 1000)


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
    run(stage=True,split=False,variable_attraction=True)
   
