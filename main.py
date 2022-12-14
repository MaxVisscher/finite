import finite as m
import state as s
import coffee as c

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
    machine = c.CoffeeMachine(beverages)
    q4 = s.State(machine.start, 'q4')
    q0 = s.State(machine.press_go, 'q0')
    q1 = s.State(machine.get_input, 'q1')
    q2 = s.State(machine.payment, 'q2')
    q3 = s.State(machine.give_beverage, 'q3')
    k = [(q4,1,q0),(q1,0,q0),(q0,1,q1),(q0,0,q4),(q1,1,q2),(q2,0,q0),(q2,1,q3),(q3,0,q0),(q3,1,q4),(q2, 5, q2),(q0, 5, q0),(q4, 0, q4),(q4, 5, q4),(q1,5,q1)]  
    delta = [q0,q1,q2,q3]
    sigma = [0,1,2,3,4, 5]
    f= [q0]
    finite_state = m.FiniteStateMachine(q4, delta, sigma, k,f)
    finite_state.start()

main()