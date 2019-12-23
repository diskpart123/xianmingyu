import math
x1 ,y1 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
x2 ,y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))
x3 ,y3 = eval(input("Enter point 3 (latitude and longitude) in degrees: "))
x4 ,y4 = eval(input("Enter point 4 (latitude and longitude) in degrees: "))
radius = 6371.01
distance1 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1)-math.radians(y2)))
distance2 = radius * math.acos(math.sin(math.radians(x2)) * math.sin(math.radians(x3)) + math.cos(math.radians(x2)) * math.cos(math.radians(x3)) * math.cos(math.radians(y2)-math.radians(y3)))
distance3 = radius * math.acos(math.sin(math.radians(x3)) * math.sin(math.radians(x4)) + math.cos(math.radians(x3)) * math.cos(math.radians(x4)) * math.cos(math.radians(y3)-math.radians(y4)))
distance4 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x4)) + math.cos(math.radians(x1)) * math.cos(math.radians(x4)) * math.cos(math.radians(y1)-math.radians(y4)))
distance5 = radius * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x3)) + math.cos(math.radians(x1)) * math.cos(math.radians(x3)) * math.cos(math.radians(y1)-math.radians(y3)))



s1 = (distance1 + distance2 + distance5) / 2
area1 = (s1 * (s1 - distance1) * (s1 - distance2) * (s1 - distance5)) ** 0.5
s2 = (distance3 + distance4 + distance5) / 2
area2 = (s2 * (s2 - distance3) * (s2 - distance4) * (s2 - distance5)) ** 0.5
area = area1 + area2
print("The area of the four cities is",area)
