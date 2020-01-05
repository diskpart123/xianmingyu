#加法
for i in range(1,10):
    for j in range(1,10):
        print(format(j),"+",format(i),"=",format(i+j,"<2d"),end="   ")
    print()
