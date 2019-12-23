num = eval(input("请输入一个1到15的整数:"))

if num < 10:
    for i in range(1,num + 1):
        temp = 17 - i
        for a in range(1,temp):
            print(' ',end = ' ')
        for j in range(i,1,-1):
            print(j,end = ' ')
        for j in range(1,i + 1):
            print(j,end = ' ')
        print()
else:
    for i in range(1,num + 1):
        temp = 17 - i
        for a in range(1,temp):
              print('  ',end = ' ')
        for j in range(i,1,-1):
            print(format(j,"2d"),end = ' ')
        for j in range(1,i + 1):
            print(format(j,"2d"),end = ' ')
        print()