'''
Defines different agents e.g, human, maybe in the future more agent e.g police / attacker etc.
'''
class Human:
    ''' Defines a human'''
    def __init__(self) -> None:
        self.id = 1
        self.alive = True
        self.health = 100
        # Just some starting ideas, size could be used randomly 
        # so that every agent is not the same size, like Viktor is two times the
        # size of me (Felix) and will probably survive longer
        self.size = 2
        # I was thinking that depending on the type of person their reactions to events might differ, 
        self.behaviour = "stressed"
    def __str__(self) -> str:
        return f'Agent: Human. Id: {self.id}'