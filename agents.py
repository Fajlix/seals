import numpy as np
'''
Defines different agents e.g, human, maybe in the future more agent e.g police / attacker etc.
'''
class Agent:
    ''' Defines a agent'''
    def __init__(self,x,y,mass=70,p_max =1,area =1,health = 100):
        self.position = np.array([float(x),float(y)])
        self.mass = mass
        self.velocity = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])
        self.external_force = np.array([0.0,0.0])
        # Towards ex stage, exit, etc
        self.attractive_force_magnitude = 0
        self.attraction_angle = 0
        #For example friction, other
        self.internal_force = np.array([0.0,0.0])
        self.p_max = p_max
        # Area of lung for pressure
        self.area = area
        self.alive = True
        #Instead of timer I though we could use health. Ex, we lose health over time depending on how high the pressure is
        # Or how many is in its radius. 
        self.health = health
        self.max_health = health
        # Just some starting ideas, size could be used randomly 
        # so that every agent is not the same size, like Viktor is two times the
        # size of me (Felix) and will probably survive longer
        self.size = 2
        # I was thinking that depending on the type of person their reactions to events might differ, 
        self.behaviour = "stressed"
    def apply_pressure(self,dt):
        if(np.linalg.norm(self.external_force/self.area) > self.p_max):
            #TODO DAMAGE SHOULD NOT BE A CONSTANT!
            damage = 1
            self.health -= damage
        elif(self.health < self.max_health):
            #TODO HEALING SHOULD NOT BE A CONSTANT!
            healing = 0.1
            healing = np.min([self.health + healing,self.max_health])
    def step(self,dt):
        self.attraction_towards_stage((500,500), 5)
        self.acceleration = (self.external_force + self.internal_force)/self.mass
        self.velocity += self.acceleration*dt
        # set max velocity in x and y direction
        self.velocity[0] = np.min([np.max([self.velocity[0], -2]), 2])
        self.velocity[1] = np.min([np.max([self.velocity[1], -2]), 2])
        
        self.position += self.velocity*dt
        self.apply_pressure(dt)
    def attraction_towards_stage(self, point_of_attraction, attractive_force_magnitude):
        # get the angle between the agent and the point of attraction
        self.attraction_angle = np.arctan2(point_of_attraction[1] - self.position[1], point_of_attraction[0] - self.position[0])
        self.attractive_force_magnitude = attractive_force_magnitude
        # calculate the attractive force
        self.internal_force = np.array([self.attractive_force_magnitude*np.cos(self.attraction_angle), self.attractive_force_magnitude*np.sin(self.attraction_angle)])







