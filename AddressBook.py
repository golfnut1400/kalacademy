from tkinter import *

class AddressBook:
    '''
        This function constructos the Loan class
    '''
    def __init__(self):
        window = Tk()
        window.title("Address Book")

        #
        # self.canvas = Canvas(window, width=450, height=300, bg="blue")
        # self.canvas.pack()
        #
        # self.window = Canvas(window, width=450, height=300, bg="blue")
        # self.window.pack()

        #
        # frame = Frame(window)
        # frame.pack()

        Label(window, text="Name").grid(row=1, column=1, sticky=E)
        # Label(window, text="Street").grid(row = 2, column=1, sticky=W)
        # Label(window, text="City").grid(row = 3, column=1, sticky=W)
        # Label(window, text="Monthly Payment").grid(row = 4, column=1, sticky=W)
        # Label(window, text="Total Payment").grid(row = 5, column=1, sticky=W)

        # self.annualInterestRateVar = StringVar()
        # Entry(window, textvariable = self.annualInterestRateVar, justify=RIGHT).grid(row =1, column=2)
        #
        # self.numberOfYearsVar = StringVar()
        # Entry(window, textvariable = self.numberOfYearsVar, justify=RIGHT).grid(row=2, column=2)
        #
        # self.loanAmountVar = StringVar()
        # Entry(window, textvariable = self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)
        #
        # self.monthlyPaymentVar = StringVar()
        # Label(window, textvariable=self.monthlyPaymentVar).grid(row=4,column=2,sticky=E)
        #
        # self.totalPaymentVar = StringVar()
        # Label(window, textvariable=self.totalPaymentVar).grid(row=5,column=2, sticky=E)

        # command fires an event to fire off the fucnction
        # Button(window, text="Add", command=self.computePayment).grid(row=6, column=2)
        # Button(window, text="Find", command=self.computePayment).grid(row=6, column=3)
        #
        # Button(window, text="Add" .grid(row=6, column=2)
        # Button(window, text="Find" .grid(row=6, column=3)


        # imagine a game loop
        window.mainloop()

    #called by the Compute Payment button

    # def computePayment(self):
    #      # uset get() to get information
    #      # converting str to float or str
    #     monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
    #                                             float(self.annualInterestRateVar.get())/1200,
    #                                             int(self.numberOfYearsVar.get()))
    #
    #     # set to display
    #     self.monthlyPaymentVar.set(format(monthlyPayment, "10.2f"))  # 10 didgit with 2 place after floating point value
    #     # uset get() to get information
    #
    #      # total payment
    #     totalPayment = monthlyPayment * 12 * int(self.numberOfYearsVar.get())
    #      # set to diaplay
    #     self.totalPaymentVar.set(format(totalPayment, "10.2f"))
    #
    #   # calculate a monthly payment
    # def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
    #     monthlyPayment = loanAmount * monthlyInterestRate/ (1 - 1/(1 + monthlyInterestRate) ** (numberOfYears * 12))
    #     return monthlyPayment

AddressBook()

