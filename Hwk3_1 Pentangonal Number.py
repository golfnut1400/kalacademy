

'''
Introduction to Programming
Homework 3
Created by: Stan Corpuz
Jan 27, 2018

Homework 3
'''

def getPentagonalNumber(n):
    #p = n(3*n-1) // 2
    p = n*(3*n-1) // 2
    print(p)

def printPentagonalNumber(numberOfPentagonal):
    numberOfPentagonal = 100
    NUMBER_OF_PENTAGONAL_PER_LINE = 10
    count = 0
    n = 1

    while count < numberOfPentagonal:
        if getPentagonalNumber(n):
            count += 1 # increase count

            if count % NUMBER_OF_PENTAGONAL_PER_LINE == 0:
                print()

        n =+1

def main():
    print("The first 100 pentagonal numbers are")
    printPentagonalNumber(100)

main()
