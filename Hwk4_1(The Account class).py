
'''
Introduction to Programming
Homework 2
Created by: Stan Corpuz
Jan 28, 2018

#Homework 4 - the Account Class
'''




# Account class will track the balance, deposits, withdrawls and montly interest rates

annualInterestRate = 0
monthlyInterestRate = 0


class Account:
    def __init__(self, name, id = 0, balance=100):
        self.id = id        #account id
        self.name = name    #name on the account
        self.balance = balance

        global annualInterestRate   # 4.5%
        self.annualInterestRate = annualInterestRate
        self.monthlyInterestRate = monthlyInterestRate


    def deposit(self, amount):
        """make a deposit"""
        self.balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def get_balance(self): #are accessor methods needed in Python?
        """check the balance"""
        return self.balance

    # the (annualInterestRate/100)/12 months
    # returns monthly interest rate
    def getMonthlyInterestRate(self, annualInterestRate):
        self.monthlyInterestRate = (annualInterestRate/100)/12  # (4.5/12)/100
        return self.monthlyInterestRate

    #returns monthly iterest
    def getMonthlyInterest(self):
        self.monthlyInterest = self.balance * self.monthlyInterestRate
        return self.monthlyInterest




def main():
    print("\n Customer1: ")
    customer1 = Account('Siri ''&',1122)
    print("Customer name and Account ID: ", customer1.name, customer1.id)
    print("Your current balance: ",customer1.balance)
    # deposit $ to customer 1 account

    customer1.deposit(3000)
    print("Current balance after deposit: ",customer1.balance)

    customer1.withdraw(2500)
    print("Current balance after withdraw: ",customer1.balance)

    customer1.getMonthlyInterestRate(5.0)
    print("Monthly interest rate: " '{:.5f}'.format(customer1.monthlyInterestRate))
    print("Monthly interest earned base-off current balance: $", customer1.balance * customer1.monthlyInterestRate)
    Finalbalance  = customer1.balance  + (customer1.balance * customer1.monthlyInterestRate)
    print("Total balance (monthly interest plus balance): $", Finalbalance)


    print("\n Customer2: ")
    customer2 = Account('Alexa ''&',1122)
    print("Customer name and Account ID: ", customer2.name, customer2.id)
    print("Your current balance: $",customer2.balance)
    # deposit $ to customer 1 account

    customer2.deposit(10000)
    print("Current balance after deposit: $",customer2.balance)

    customer2.withdraw(2500)
    print("Current balance after withdraw: $",customer2.balance)

    customer2.getMonthlyInterestRate(5.0)
    print("Mnthly interest rate: " '{:.5f}'.format(customer2.monthlyInterestRate))
    print("Monthly interest earned base-off current balance: $", '{:.2f}'.format(customer2.balance * customer2.monthlyInterestRate))
    Finalbalance  = customer2.balance  + (customer2.balance * (customer2.monthlyInterestRate))
    print("Total balance (monthly interest plus balance): $", '{:.2f}'.format(Finalbalance))





if __name__ == "__main__":
    main()
