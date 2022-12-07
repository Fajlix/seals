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
def run():
    agents = []
    
    for i in range(10):
        x = random.randint(8/2, 200 - 8/2)
        y = random.randint(8/2, 200 - 8/2)
        # make sure that the agents are not in radius of each other
        while any([np.sqrt(np.power(x - agent.position[0],2) + np.power(y - agent.position[1],2)) < 16 for agent in agents]):
            x = random.randint(8/2, 200 - 8/2)
            y = random.randint(8/2, 200 - 8/2)
        
        agents.append(Agent(x,y))

    env = Environment(agents)

    graphic = Graphics(200, 200)

    graphic.drawHuman(env.getAgentInfo())
    running = True
    last_update_time = 0
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        env.update()
        if env.time - last_update_time > 0.5:
            graphic.drawHuman(env.getAgentInfo())
            last_update_time = env.time
if __name__ == "__main__":
    run()
