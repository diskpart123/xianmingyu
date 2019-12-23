x1, y1, r1 = eval(input("Enter circle1's x-, y-coordinates, and radius:\n"))
x2, y2, r2 = eval(input("Enter circle2's x-, y-coordinates, and radius:\n"))

d = ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 ) ** 0.5
r = ( ( r1 - r2 ) * ( r1 - r2 ) ) ** 0.5

if d <= r:
    print("circle2 is inside circle1")
elif d <= r1 + r2:
    print("circle2 overlaps circle1")
elif d > r1 + r2:
    print("circle2 does not overlaps circle1")
else:
    None