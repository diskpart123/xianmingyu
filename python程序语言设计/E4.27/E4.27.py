x2, y2 = eval(input("Enter a point's x- and y-coordinates:"))

a = -y2
b = x2
c = 100
d = 200
e = 0
f = 20000

num = a * d - b * c
x = (e * d - b * f) / num
y = (a * f - e * c) / num

if x > x2 or y > y2:
   print("The point is in the triangle")
else:
    print("The point is not in the triangle")