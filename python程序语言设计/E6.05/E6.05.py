def displaysortednumber(num1,num2,num3):
    t = 0
    if num1 < num2:
        t = num1
        num1 = num2
        num2 = t
    if num1 < num3:
        print( num3, num1, num2 )
    else:
        if num2 > num3:
            print( num1, num2, num3 )
        else:
            print( num1, num3, num2 )

num1, num2, num3 = eval(input("Enter three numbers: "))

displaysortednumber(num1,num2,num3)