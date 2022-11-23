from state import State

class FiniteStateMachine:
    def __init__(self, start_state, delta,sigma, k , f):
        self.delta = delta # all states
        self.current_state = start_state #current state
        self.f = f #stop staten
        self.sigma = sigma # alphabet
        self.k = k # all possible states and paths
        self.start_state = start_state

    def run(self, condition, state):
        """
        This function loops through the K of the finite state machine to find the next state it needs to load. 
        It finds the correct state by checking if the condition and state are the same as in the current tuple.  
        
        parameters:
        condition -> the return value of the previous function : int
        """
        k = self.k
        for path in k:
            if condition == int(path[1]) and state == path[0]:
                self.current_state = path[2]
                self.run(self.current_state.run(), self.current_state)

    def start(self): 
        self.run(self.start_state.run(),self.start_state)

    def add_to_sigma(self, value: int):
        self.sigma.append(value)

    def add_to_k(self, k : tuple):
        self.k.append(k)
    
    def add_to_delta(self, state : State):
        self.delta.append(state)