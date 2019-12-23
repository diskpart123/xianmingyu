num = eval(input("Enter an integer: "))
num1= num % 10
num2 = num // 10
num3 = num2 % 10
num4 = num // 100
num5 = num4 % 10
num6 = num // 1000
num7 = num6 % 10
num8 = num1 * 1000 + num3 * 100 + num5 * 10 + num7
print("The reversed number is",num8)
