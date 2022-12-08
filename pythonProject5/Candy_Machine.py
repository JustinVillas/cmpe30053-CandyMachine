
class CashRegister:
    # Set a default value for cashOnHand.
    # If the value of the cashOnHad is less than equal to zero. It will pass on a condition and will again become 500.
    def __init__(self,cashOnHand = 500):
        if cashOnHand <= 0:
             self.cashOnHand = 500
        else:
            self.cashOnHand = cashOnHand
    #When called it will give the value of the cashOnHand
    def currentBalance(self):
        return self.cashOnHand

    #For every transfaction made, the purchace product will added to the cashOnHand.
    def acceptAmount(self,cashIn ):
        self.cashOnHand += cashIn
        print(f"Current Balance is: {self.cashOnHand}")



class Dispenser:
    #Set a default value for cost and number of items.
    #If condtions are satisfied, the of the variable's value in the parameter  will again equate to 50.
    def __init__(self,cost=50, numberOfItems=50):
        self.cost = cost
        if self.cost <= 0:
            self.cost = 50
        else:
            self.cost = cost

        self.numberOfItems = numberOfItems
        if self.numberOfItems <= 0:
            self.numberOfItems = 50
        elif self.numberOfItems >= 1:
            self.numberOfItems = numberOfItems

    #When called it will give the value of the number of items.
    def getCount(self):
        return self.numberOfItems

    #When called it will give the value of cost the particular items.
    def getProductCost(self):
        return self.cost

    #Ever sell made it the numberOfItems will decrease.
    def makeSale(self):
        self.numberOfItems -= 1


class mainProgram:
    #It enables the program to sell the choosen product to the user.
    def sellProduct(self, Items, CashAccept): # Usint the userChoice the two parameter will be given a value.

        #This the try and catch mechanism.
        try:
            product_cost =  Items.getProductCost()#get the product_cost value through calling the getProductCost fucntion
            if Items.getCount():
                print(f"Product cost: {product_cost} cents")
                userPay = int(input("Insert coins: ")) #Ask the user for coins. (Int data type only).
                print(f"Coins Received: {userPay} \n")
                while userPay < product_cost: #Will only be satified if the user inserted insuffient coins.
                    #using the userPay it will ask for additional coins.
                    userPay = userPay + int(input(f'Insufficient cents (Insert {str(product_cost- userPay)} cents)' + ': '))
                print("Successfully bought the item \n" )
                userChange = userPay - product_cost
                addcoins = product_cost - userPay
                if userChange >= 1: #Will only be satisfied when the user inserted more coins that the items cost.
                     print(f"Change:( {userChange} cents)")# return the

                     return
                if userChange < 0:  #Will only be satified if the user inserted insuffient coins.
                     print(f"Insufficient payment:(Add {addcoins} cents)") #show the needed coins.
                     return
                else:
                    CashAccept.acceptAmount(product_cost)
                    Items.makeSale()
                    return

        except:
            print("\n Invalid Input: (Interger data type only)\n")#Will only trigger when user inserted a non Int datatype

    #Do actions according the the user respond.
    def userChoice(self,respond):
        Counter =CashRegister()
        Chips = Dispenser(30,0)
        Candy = Dispenser(10, 50)
        Gum = Dispenser(5, 50)
        Cookies = Dispenser(20,50)
        if respond == 1: #When satisfied it will proceed to sellProduct function containing the Chips and Counter variables
            print("You have chosen Chips")
            self.sellProduct(Chips, Counter)
            return True
        if respond == 2:#When satisfied it will proceed to sellProduct function containing the Candy and Counter variables
            print("You have chosen Candy")
            self.sellProduct(Candy, Counter)
            return True
        if respond == 3:#When satisfied it will proceed to sellProduct function containing the Gum and Counter variables
            print("You have chosen Gum")
            self.sellProduct(Gum, Counter)
            return self.run()
        if respond == 4:#When satisfied it will proceed to sellProduct function containing the Cookies and Counter variables
            print("You have chosen Cookies")
            self.sellProduct(Cookies, Counter)
            return True
        if respond == 0:#When satisfied it will proceed to cuurent Balance and show the value of the cashOnHand.
            q = Counter.currentBalance()
            print(q)
            return True
        if respond == 9:#When satisfied it will close the program.
            print("It's a pleasure serving you =)")
            return False
        else:
            print("Incorrect respond please respond correctly next time!")#Show only when user selected a number that is not include to the choices.
            return True

    # Show the choices in the Candy Machine.
    def run(self):
        running = True
        welcome = "Need some sugar? Justin's Candy Machine is at your service. "
        mainMenu = """Choose what you want to buy?
              |   1   | for Chips
              |   2   | for Candy
              |   3   | for Gum
              |   4   | for Cookies
              |   0   | to View Balance
              |   9   | to Exit"""
        print(welcome)
        while running:
            print(mainMenu)
            respond = int(input("Enter your choice: "))
            running = self.userChoice(respond)



CandyMachine = mainProgram()
CandyMachine.run()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
