def displaypattern(num):

    if num < 10:
        for i in range(1,num + 1):
            temp = num + 2 - i
            for a in range(1,temp):
                print(' ',end = ' ')
            for j in range(i,0,-1):
                print(j,end = ' ')
            print()
    else:
        for i in range(1,num + 1):
            temp = num + 2 - i
            for a in range(1,temp):
                print('  ',end = ' ')
            for j in range(i,0,-1):
                print(format(j,"2d"),end = ' ')
            print()

num = eval(input("Enter an integer:"))

displaypattern(num)