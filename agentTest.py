from agents import Agent
import numpy as np
import matplotlib.pyplot as plt

def update_agent(agent,dt=0.1):
    agent.step(dt)
    return agent
def run_simulation():
    num_agents = 10000
    #Random x y positions for each agent
    xmax = 100
    ymax = 100
    xmin = -100
    ymin = -100
    x = np.random.uniform(xmin,xmax,num_agents)
    y = np.random.uniform(ymin,ymax,num_agents)
    dt = 0.1
    sime_time = 50
    #Create agents
    agents = [Agent(x[i],y[i]) for i in range(num_agents)]
    #Plot position of each agent
    positions = [agent.position for agent in agents]
    x = [position[0] for position in positions]
    y = [position[1] for position in positions]
    # randomly set agents external force to between -1 and 1

    for agent in agents:
        agent.external_force = np.random.uniform(-1,1,2)
    time = 0
    while(time < sime_time):
        # step each agent with dt using process
        agents = [update_agent(agent,dt) for agent in agents]
        time += dt
        #Plot position of each agent
        plt.clf()
        plt.xlim(-1000,1000)
        plt.ylim(-1000,1000)
        plt.title(f"t = {time:.2f}")
        plt.scatter([agent.position[0] for agent in agents],[agent.position[1] for agent in agents], s=0.5)
        plt.pause(0.01)

if __name__ == "__main__":
    run_simulation()