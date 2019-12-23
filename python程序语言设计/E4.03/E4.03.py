a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f:"))
num = a * d - b * c
if num == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / num
    y = (a * f - e * c) / num
    print("x is", x, "and","y is", y )
