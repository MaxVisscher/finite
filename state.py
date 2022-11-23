class State:
    def __init__(self, func, name):
        """
        func is the function bound to the state. 

        func: def 
        """
        self.func = func
        self.name = name
        
    def run(self):
        return self.func()

    def __str__(self):
        return self.name