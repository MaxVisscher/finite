from random import randint

class CoffeeMachine:
    def __init__(self, beverages : list):
        self.beverages = beverages
        self.selectedBeverage = None
        self.list_of_roasts = ["This input is invalid, maybe you should buy some glasses.", 
                            "Are you sure you want to do this? Or do you just have fat fingers.", 
                            "How many tries will it take to submit the correct input?", 
                            "This machine is sponsored by grade school counting", 
                            "At this rate you will have a better chance of winning the lottery then submitting the correct input", 
                            "Have you tried turning the machine off and on?", 
                            "Maybe you need a cup of coffee to get the right input",
                            "You should've provided a better coffee machine",
                            "Have you tried texting your mom for help?",
                            "Error 404 competence not found.",
                            "Please call 911, i am about to commit a murder.",
                            "Maybe Johnny Sins can \"repair\" this machine"]
    def start(self):
        start = int(input("Do you want to use the coffee machine?\n\4 yes: 1 \n\4 no: 0 \n"))
        if start ==1:
            print("You feel thirsty and walk to the coffee machine.")
            return start
        elif start == 0:
            print("You have an appointment and dont have time for a drink.")
            return start
        print(self.list_of_roasts[randint(0, 11)])
        return 5

    def press_go(self):
        """
        This function simulates the "go" button on the coffee machine.
        """
        temp = int(input("Choose your options \n\4 make beverage: 1 \n\4 time expired: 0 \n"))

        if temp == 1:
            print("You pressed go.")
            return temp
        elif temp == 0:
            print("The machine was inactive and returned to its idle state.")
            return temp
        else:
            print(self.list_of_roasts[randint(0, 11)])
            return 5
    def get_input(self):
        """
        This function asks the user to select the beverage they want to buy. It expects integers ranging from 1 to 4. 
        This function does not catch invalid inputs since this application simulates a coffee machine which has buttons,
        So invalid inputs are impossible in this scenario. 

        If the selected beverage is no longer available due to insufficient stock, it refuses the option.
        """
        order = int(input("Please choose your beverage: \n\4 coffee: 1\n\4 tea: 2\n\4 water: 3\n\4 chocolate milk: 4 \n"))
        self.selectedBeverage = self.beverages[int(order) -1]
        if self.selectedBeverage['stock'] == 0:
            print(f"{self.selectedBeverage['beverage']} is out of stock.")
            print("You cry a little on the inside.")
            return 0
        elif self.selectedBeverage['stock'] < 0 and self.selectedBeverage['stock'] < 5:
            print(f"you have selected {self.selectedBeverage['beverage']}")
            return order
        else:
            print(self.list_of_roasts[randint(0, 11)])
            return 5

    def payment(self):
        """
        This function asks the user to pay. Since the machine only accepts digital payments the user is given the option for successful payment, for failed payment.
        To give the user the ability to test both scenario's.
        """
        print(f"Please pay $ {self.selectedBeverage['price']}.")
        payment =int(input("Did the payment succeed?\n\4 No: 0\n\4 Yes: 1\n"))
        if payment == 1:
            print("The payment has been approved.")
            return payment
        elif payment == 0:
            print("Your card has been declined.")
            return payment
        else:
            print(self.list_of_roasts[randint(0, 11)])
            return 5

    def give_beverage(self):
        """
        This function gives the user the requested beverage and updates the stock.
        """
        print(f"Here is your {self.selectedBeverage['beverage']}")
        self.selectedBeverage['stock'] =  self.selectedBeverage['stock'] -1
        self.beverages[self.beverages.index(self.selectedBeverage)] = self.selectedBeverage
        print(f"You walk away satisfied with your {self.selectedBeverage['beverage']} ")
        return 1

