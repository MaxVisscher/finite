class State:
    def __init__(self, func, name):
        self.func = func
        self.name = name
        
    def run(self):
        return self.func()

    def __str__(self):
        return self.name

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

    def addToK(self, k : tuple(State, int, State)):
        self.k.append(k)
    
    def addToDelta(self, state : State):
        self.delta.append(state)

class CoffeeMachine:
    def __init__(self, beverages : list):
        self.beverages = beverages
        self.selectedBeverage = None

    def pressStart(self):
        """
        This function simulates the "go" button on the coffee machine.
        """
        temp = input("choose your options \n\4 make beverage: 1 \n\4 turn machine off: 2 \n")
        if int(temp) == 1:
            return 1
        else:
            exit()

    def getInput(self):
        """
        This function asks the user to select the beverage they want to buy. It expects integers ranging from 1 to 4. 
        This function does not catch invalid inputs since this application simulates a coffee machine which has buttons,
        So invalid inputs are impossible in this scenario.

        If the selected beverage is no longer available due to insufficient stock, it refuses the option.
        """
        order = int(input("choose your beverage: \n\4 coffee: 1\n\4 tea: 2\n\4 water: 3\n\4 chocolate milk: 4 \n"))
        self.selectedBeverage = self.beverages[int(order) -1]
        if self.selectedBeverage['stock'] == 0:
            print('out of stock')
            return 0
        return order

    def payment(self):
        """
        This function asks the user to pay. Since the machine only accepts digital payments the user is given the option for successful payment, for failed payment.
        To give the user the ability to test both scenario's.
        """
        print(f"please pay $ {self.selectedBeverage['price']}")
        return int(input("Did the payment succeed?\n\4 No: 0\n\4 Yes: 1\n"))

    def giveBeverage(self):
        """
        This function gives the user the requested beverage and updates the stock.
        """
        print(f"here is your {self.selectedBeverage['beverage']}")
        self.selectedBeverage['stock'] =  self.selectedBeverage['stock'] -1
        self.beverages[self.beverages.index(self.selectedBeverage)] = self.selectedBeverage
        return 1

def main():
    coffee = {
        'beverage':'coffee',
        'stock':10,
        'price':0.30 
    }

    tea = {
        'beverage':'tea',
        'stock':1,
        'price':0.25
    }

    water = {
        'beverage':'water',
        'stock':100,
        'price':0.06
    }

    choco = {
        'beverage':'choco',
        'stock':10,
        'price':0.42,
    }

    beverages = [coffee, tea, water, choco]
    machine = CoffeeMachine(beverages)
    q0 = State(machine.pressStart, 'q0')
    q1 = State(machine.getInput, 'q1')
    q2 = State(machine.payment, 'q2')
    q3 = State(machine.payment, 'q3')
    q4 = State(machine.payment, 'q4')
    q5 = State(machine.payment, 'q5')
    q6 = State(machine.giveBeverage, 'q6')
    k = [(q1,0,q0),(q0,1,q1),(q0,0,q0),(q1,1,q2),(q1,2,q3),(q1,3,q4),(q1,4,q5),(q2,0,q0),(q3,0,q0),(q5,0,q0),(q2,1,q6),(q3,1,q6),(q4,1,q6),(q5,1,q6),(q6,0,q0),(q6,1,q0)]  
    delta = [q0,q1,q2,q3,q4,q5,q6]
    sigma = [0,1,2,3,4]
    f= [q0]
    finiteState = FiniteStateMachine(q0, delta, sigma, k,f)
    finiteState.start()

main()