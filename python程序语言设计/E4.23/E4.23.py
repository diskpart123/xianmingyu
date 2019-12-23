x, y = eval(input("Enter a point with two coordinate: "))

x1 = ( x * x ) ** 0.5
y1 = ( y * y ) ** 0.5

if x1 <= 5 and y1 <= 2.5:
    print("point (", x, ",", y, ") is in the rectangle.")
else:
    print("point (", x, ",", y, ") is not in the rectangle.")