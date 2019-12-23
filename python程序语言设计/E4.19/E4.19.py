a, b, c = eval(input("Enter three edges: "))

ture = ( ( a + b ) > c ) and ( ( a + c ) > b ) and ( ( b + c ) > a )

if ture:
    print("The perimeter is",a +b + c)
else:
    print("The input is invalid")
