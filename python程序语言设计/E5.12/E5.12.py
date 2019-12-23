count = 0
for i in range(100,1000):
    if i % 5 == 0 and i % 6 == 0:
        count += 1
        if count < 10:
            print(format(i,"d"),end = ' ')
        else:
            count = 0
            print(format(i,"d"),end = '\n')