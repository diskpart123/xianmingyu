import math
num = eval(input("Enter the number of sides: "))
side = eval(input("Enter the side: "))
area = 5 * math.pow(side,2) / (4 * math.tan(math.pi / num))
print("The area of the pentagon is",area)
