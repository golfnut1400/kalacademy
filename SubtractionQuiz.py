import random
import time

NUMBER_OF_QUESTIONS = 5 # Total number of questions to give the user
correctCount = 0 # count the number of correct answers
count = 0 # Count the number of questions given

startTime = time.time() #Get the current time

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # If number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

    if number1 - number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong. \n", number1 , "-", number2, "is", number1-number2)

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS,
      "\nTest time is", testTime, "seconds")
    
