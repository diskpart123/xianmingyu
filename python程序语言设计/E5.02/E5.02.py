import random
import time

correctcount = 0
count = 0
numberofquestions = 2

starttime = time.time()

while count < numberofquestions:
    number1 = random.randint(0,15)
    number2 = random.randint(0,15)
    
    answer = eval(input("What is" + str(number1) + "+" + str(number2) + "?"))
    
    if number1 + number2 == answer:
        print("You are correct!")
        correctcount += 1
    else:
        print("Your answer is wrong.\n",umber1,"+",number2,"is",number1 + number2)

    count += 1

endtime = time.time()
testtime = int( endtime - starttime )

print("Correct count is", correctcount,"out of", numberofquestions,"\nTest time is",testtime,"seconds")