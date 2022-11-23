class CoffeeMachine:
    def __init__(self, beverages : list):
        self.beverages = beverages
        self.selectedBeverage = None
    def start(self):
        start = int(input("Do you want to use the coffee machine?\n\4 yes: 1 \n\4 no: 0 \n"))
        if start ==1:
            print("You feel thirsty and walk to the coffee machine.")
        else:
            print("You have an appointment and dont have time for a drink.")
        return start

    def pressGo(self):
        """
        This function simulates the "go" button on the coffee machine.
        """
        temp = input("Choose your options \n\4 make beverage: 1 \n\4 time expired: 0 \n")

        if int(temp) == 1:
            print("You pressed go.")
            return 1
        print("The machine was inactive and returned to its idle state.")
        return 0

    def getInput(self):
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
        print(f"you have selected {self.selectedBeverage['beverage']}")
        return order

    def payment(self):
        """
        This function asks the user to pay. Since the machine only accepts digital payments the user is given the option for successful payment, for failed payment.
        To give the user the ability to test both scenario's.
        """
        print(f"Please pay $ {self.selectedBeverage['price']}.")
        payment =int(input("Did the payment succeed?\n\4 No: 0\n\4 Yes: 1\n"))
        if payment == 1:
            print("The payment has been approved.")
        else:
            print("Your card has been declined.")
        return payment
    def giveBeverage(self):
        """
        This function gives the user the requested beverage and updates the stock.
        """
        print(f"Here is your {self.selectedBeverage['beverage']}")
        self.selectedBeverage['stock'] =  self.selectedBeverage['stock'] -1
        self.beverages[self.beverages.index(self.selectedBeverage)] = self.selectedBeverage
        print(f"You walk away satisfied with your {self.selectedBeverage['beverage']} ")
        return 1
