class State:
    pass



class FiniteStateMachine:
    def __init__(self, startState):
        self.delta = [] # all states
        self.currentState = startState #current state
        self.f = [] #stop staten
        self.sigma = [] # alphabet
        self.k = [] # all possible states and paths
        self.startState = startState

    def nextState(self, condition, state):
        k = self.k
        for path in k:
            if condition and state in path:
                self.currentState = path[2]
                break
    
    def addToSigma(self, state):
        self.sigma.append(state)

    def addToK(self, state):
        self.k.append(state)
    
    def addToDelta(self, state : str):
        self.delta.append(state)

class CoffeeMachine:
    def __init__(self, beverages : list):
        self.beverages = beverages
        self.selectedBeverage = None
    def pressStart(self):
        temp = input("type 1 to start")
        if temp == 1:
            return 1
        return 0

    def getInput(self):
        order = input("choose your beverage: \n\4coffee: 1\n\4thee: 2\n\4water: 3\n\4chocolate milk: 4 \n")
 
        self.selectedBeverage = self.beverages[int(order) -1]
        if self.selectedBeverage['stock'] == 0:
            print('out of stock')
            return 0
        # if timeout( == T)rue:
        #     return 0
        return 1
    # def timeout(self):
    #     if timePassed == True:
    #         self.selectedBeverage = None

    def payment(self):
        print(f"please pay $ {self.selectedBeverage['price']}")

        return input("Did the payment succeed?\n\4No: 0\n\4Yes: 1")

    def giveBeverage(self):
        print(f"here is your {self.selectedBeverage['beverage']}")
        return 1

coffee = {
    'beverage':'coffee',
    'stock':10,
    'price':0.30 
}

thee = {
    'beverage':'thee',
    'stock':10,
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

beverages = [coffee, thee, water, choco]

def main():
    q0 = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State
    cofi = CoffeeMachine(beverages)
    cofi.getInput()
    cofi.payment()
    
    nickus = FiniteStateMachine()
    [(q0,1,q1),(q0,0,q0),(q1,1,q2),(q1,2,q3),(q1,3,q4),(q1,4,q5),(q2,0,q0),(q3,0,q0),(q5,0,q0),(q2,0,q6),(q3,0,q6),(q4,0,q6),(q5,0,q6),(q6,0,q0),(q6,1,q7),(q7,1,q0)]  
    nickus.addToDelta()

main()