x, y = eval(input("Enter a point with two coordinate: "))
line = ( x * x + y * y ) ** 0.5

if line < 10:
    print("point (", x, ",", y, ") is in the circle.")
else:
    print("point (", x, ",", y, ") is not in the circle.")