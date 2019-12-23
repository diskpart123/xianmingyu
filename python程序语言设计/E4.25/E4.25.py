x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4:\n"))

a = y1 - y2
b = -( x1 - x2 )
c = y3 - y4
d = -( x3 - x4 )
e = a * x1 + b * y1
f = c * x3 + d * y3

num = a * d - b * c

if num == 0:
    print("The two lines are parallel")
else:
    x = (e * d - b * f) / num
    y = (a * f - e * c) / num
    print("The intersecting point is at (", x, ",",y, ")")
