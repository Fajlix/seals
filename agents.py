import numpy as np
'''
Defines different agents e.g, human, maybe in the future more agent e.g police / attacker etc.
'''

#max_pressure = 0
class Agent:
    ''' Defines a agent'''

    def __init__(self, x, y, attractive_force_magnitude, mass=70, size=2, p_max=1, area=1, health=100):
        self.position = np.array([float(x),float(y)])
        self.mass = mass
        self.velocity = np.array([0.0, 0.0])
        self.acceleration = np.array([0.0, 0.0])
        self.external_forces = []
        # Towards ex stage, exit, etc
        self.attractive_force_magnitude = attractive_force_magnitude
        self.attraction_angle = 0
        # For example friction, other
        self.internal_force = np.array([0.0, 0.0])
        self.p_max = p_max
        # Area of lung for pressure
        self.area = area
        self.alive = True
        # Instead of timer I though we could use health. Ex, we lose health over time depending on how high the pressure is
        # Or how many is in its radius. 
        self.health = health
        self.max_health = health
        # Just some starting ideas, size could be used randomly 
        # so that every agent is not the same size, like Viktor is two times the
        # size of me (Felix) and will probably survive longer
        self.size = size
        # I was thinking that depending on the type of person their reactions to events might differ, 
        self.behaviour = "stressed"
    def apply_pressure(self,dt):
        # calculate the combined pressure from all agents
        # get magnitude of all external forces acting on the agent
        external_force_magnitudes = np.linalg.norm(self.external_forces, axis=1)
        # sum all the external forces
        total_external_force = np.sum(external_force_magnitudes)
        # calculate the pressure
        pressure = total_external_force/self.area
        # if the pressure is higher than the max pressure, set the max pressure to the current pressure
        global max_pressure
        #if pressure > max_pressure:
        #    max_pressure = pressure
            #print(max_pressure)
        if(pressure > self.p_max):
            #TODO DAMAGE SHOULD NOT BE A CONSTANT!
            damage = 10*dt*pressure/self.p_max
            self.health -= damage
            if(self.health <= 0):
                #print("Agent died")
                self.alive = False
        elif(self.health < self.max_health):
            #TODO HEALING SHOULD NOT BE A CONSTANT!
            healing = 0.1*dt
            healing = np.min([self.health + healing,self.max_health])
    def step(self,dt,stage,split):
        self.external_forces = np.array(self.external_forces)
        # make sure that the external forces are atleast 2D
        self.external_forces = np.atleast_2d(self.external_forces)

        if stage:
            self.attraction_towards_stage((500,10), self.attractive_force_magnitude)
        else:
            self.attraction_towards_stage((500,500), self.attractive_force_magnitude)


        # calculate the acceleration
        self.acceleration = (self.internal_force + np.sum(self.external_forces, axis=0))/self.mass
        self.velocity += self.acceleration*dt
        # set max velocity in x and y direction
        self.velocity[0] = np.min([np.max([self.velocity[0], -2]), 2])
        self.velocity[1] = np.min([np.max([self.velocity[1], -2]), 2])
        

        new_position = self.position+ self.velocity*dt
        if stage and split:  
            if new_position[1]<=30:
                self.position[1]= self.position[1]
            elif 515>new_position[0]>485:
                self.position[0] = self.position[0]
            else:
                self.position += self.velocity*dt
        elif stage:
            if new_position[1]<=30:
                self.position[1]= self.position[1]
            elif new_position[0] <=30:
                    self.position[0] = self.position[0]
            elif new_position[0] >=960:
                    self.position[0] = self.position[0]
            else:
                self.position += self.velocity*dt
            
        else:
            self.position += self.velocity*dt




        friction = 0.0001
        velocity_norm = np.linalg.norm(self.velocity)
        
        if velocity_norm > friction:
            velocity_direction = self.velocity / velocity_norm
            self.velocity -= velocity_direction * friction
        elif friction - velocity_norm > 0:
            self.velocity = self.velocity*0

        self.apply_pressure(dt)

    def attraction_towards_stage(self, point_of_attraction, attractive_force_magnitude):
        # get the angle between the agent and the point of attraction
        self.attraction_angle = np.arctan2(point_of_attraction[1] - self.position[1], point_of_attraction[0] - self.position[0])
        self.attractive_force_magnitude = attractive_force_magnitude
        # calculate the attractive force
        self.internal_force = np.array([self.attractive_force_magnitude*np.cos(self.attraction_angle), self.attractive_force_magnitude*np.sin(self.attraction_angle)])