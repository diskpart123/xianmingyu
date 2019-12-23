import random

number1 = random.randint(0,100)
number2 = random.randint(0,100)

answer = eval(input("What is "+ str(number1) + "*" + str(number2) + "? " ))
number = number1 * number2

if answer == number:
    print("you are corret!")
else:
    print("Your answer is wrong.\n",number1, '*', number2, "is", number1 * number2, '.')