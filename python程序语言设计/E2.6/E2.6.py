num = eval(input("Enter a number between 0 and 1000: "))
num1 = num%10
num2 = num//10
num3 = num2%10
num4= num//100
print("The sum of the digits is",num1 + num3 + num4)
