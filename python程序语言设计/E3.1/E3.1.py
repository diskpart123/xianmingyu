import math
center = eval(input("Enter the length from the center to a vertex: "))
side = 2 * center * math.sin(math.pi / 5)
area = 5 * math.pow(side,2) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is",format(area,".2f"))
