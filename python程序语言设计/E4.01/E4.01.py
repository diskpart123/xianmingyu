a, b, c = eval(input("Enter a, b, c: "))
r = b ** 2 - 4 * a * c
if r < 0:
    print("The equation has no real roots")
elif r > 0:
    r1 = ( -b + r ** 0.5 ) / (2 * a)
    r2 = ( -b - r ** 0.5 ) / (2 * a)
    print("The roots are:",round(r1,6),round(r2,5))
else:
    r3 = -b / ( 2* a )
    print("The root is:",r3)
