#嵌套循环
print("         MuliplicationTable.py")
print(" ",end="")
for i in range(1,10):
    print("  ",i,end='')
print() #换行
print("--------------------------------------")
for i in range(1,10):      #i循环1次,i1循环10次
    print(i,"|",end = '')
    for i1 in range(1,10):
        print(format(i*i1,"2d"),end="  ")
    print()