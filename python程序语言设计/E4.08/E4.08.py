a, b, c = eval(input("Enter the three numbers:"))
if a < b:
    if b < c:
        None
    else:
        if a < c:
            t = b
            b = c
            c = t
        else:
            t = a
            a = c
            c = t
            t = b
            b = c
            c = t
    print(a, b, c)
else:
    if b > c:
        print(c, b, a)
    else:
        if c < a:
            t = b
            b = c
            c = t
            print(c, b, a)
        else:
            t = a
            a = b
            b = t
            print(a, b, c)