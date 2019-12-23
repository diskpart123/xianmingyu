count = 0
for i in range(100,200):
    if ( i % 5 == 0 ) or ( i % 6 == 0 ) and not ( ( i % 5 == 0 ) and ( i % 6 == 0 ) ):
        count += 1
        if count < 10:
            print(format(i,"d"),end = ' ')
        else:
            count = 0
            print(format(i,"d"),end = '\n')