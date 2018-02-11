from tkinter import *

class InvestmentCalculator:
    '''
        This function constructs the Loan class
    '''
    def __init__(self):
        window = Tk()
        window.title("Investment-Value-Calculator")

        Label(window, text="Investment Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Years").grid(row = 2, column=1, sticky=W)
        Label(window, text="Annual Interest Rate").grid(row = 3, column=1, sticky=W)
        Label(window, text="Future Value").grid(row = 4, column=1, sticky=W)
        #Label(window, text="Total Payment").grid(row = 5, column=1, sticky=W)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar, justify=RIGHT).grid(row =1, column=2)

        self.YearsVar = StringVar()
        Entry(window, textvariable = self.YearsVar, justify=RIGHT).grid(row=2, column=2)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify=RIGHT).grid(row=3, column=2)

        self.futureValueVar = StringVar()
        Label(window, textvariable=self.futureValueVar).grid(row=4,column=2,sticky=E)


        
        Button(window, text="Calculate", command=self.calculateInvestment).grid(row=6, column=2, sticky=E)

        window.mainloop()

    def calculateInvestment(self):
        futureValue = self.getfutureValue(float(self.investmentAmountVar.get()),float(self.annualInterestRateVar.get()),int(self.YearsVar.get()))
        # display onto the Future Value lable
        self.futureValueVar.set(format(futureValue, "5.2f"))


    # Calculates the future value of the investment
    def getfutureValue(self,investmentAmount, annualInterestRate, Years):
        # 1200 for the 12 months and correcting for the use of float above
        monthlyInterestRate = annualInterestRate /1200
        futureValue = (investmentAmount * ((1 + monthlyInterestRate) ** (Years * 12)))

        return futureValue



InvestmentCalculator()
