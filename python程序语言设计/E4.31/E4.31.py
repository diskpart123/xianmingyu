x1, y1, x2, y2, x3, y3 = eval(input("Enter coordinates for the three points p0, p1, and p2:\n"))

d = ( x2 - x1 ) * ( y3 - y1 ) - ( x3 - x1 ) * ( y2 - y1 )

if d > 0:
    print("p2 is on the left side of the line from p0 to p1.")
elif d == 0:
    print("p2 is on the same line from p0 to p1.")
else:
    print("p2 is on the right side of the line from p0 to p1.")
