'''
Defines different agents e.g, human, maybe in the future more agent e.g police / attacker etc.
'''
class Agent:
    def __init__(self, id, alive, health, size, behaviour = 'normal'):
        self.id = id
        self.alive = alive
        self.health = health
        self.size = size
        self.behaviour = behaviour
class Human(Agent):
    ''' Defines a human'''
    def __init__(self,id = 1, alive = True, health = 100, size = 10, behaviour='normal'):
        super().__init__(id, alive, health, size)
        self.id = id
        self.alive = alive
        self.health = health
        # Just some starting ideas, size could be used randomly 
        # so that every agent is not the same size, like Viktor is two times the
        # size of me (Felix) and will probably survive longer
        self.size = size
        # I was thinking that depending on the type of person their reactions to events might differ, 
        #self.behaviour = behaviour
    def __str__(self) -> str:
        return f'Type: Human. Id: {self.id} Behaviour: {self.behaviour}'