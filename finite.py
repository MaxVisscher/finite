from state import State

class FiniteStateMachine:
    def __init__(self, startState, delta,sigma, k , f):
        self.delta = delta # all states
        self.currentState = startState #current state
        self.f = f #stop staten
        self.sigma = sigma # alphabet
        self.k = k # all possible states and paths
        self.startState = startState

    def run(self, condition, state):
        """
        This function loops through the K of the finite state machine to find the next state it needs to load. 
        It finds the correct state by checking if the condition and state are the same as in the current tuple.  
        
        parameters:
        condition -> the return value of the previous function : int
        state -> the 
        """
        k = self.k
        for path in k:
            if condition == int(path[1]) and state == path[0]:
                self.currentState = path[2]
                self.run(self.currentState.run(), self.currentState)

    def start(self): 
        self.run(self.startState.run(),self.startState)

    def addToSigma(self, value: int):
        self.sigma.append(value)

    def addToK(self, k : tuple):
        self.k.append(k)
    
    def addToDelta(self, state : State):
        self.delta.append(state)