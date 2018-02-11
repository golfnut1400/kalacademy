class Loan:
    '''
        This function constructos the Loan class
    '''
    def __init__(self, annualInterestRate = 2.5, numberOfYears = 5,
                 loanAmount = 10000, borrower = ""):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount
        self.__borrower = borrower

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def getBorrower(self):
        return self.__borrower

    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = self.__loanAmount * monthlyInterestRate / (1 - (1/(1 + monthlyInterestRate)** (self.__numberOfYears * 12)))
        return monthlyPayment

#Creating an object = instantiating a class
loan1 = Loan(2.5, 5, 10000.10, "Kal")

print(loan1.getAnnualInterestRate())
print("The monthly payment is ", loan1.getMonthlyPayment())
loan2 = Loan(5, 10, 5000, "Kal")

print("The monthly payment is ", loan2.getMonthlyPayment())

loan3 = Loan(loanAmount = 20000, numberOfYears=2)
print("The monthly payment is ", loan3.getMonthlyPayment())
