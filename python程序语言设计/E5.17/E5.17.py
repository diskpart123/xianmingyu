count = 0
for i in range(33,127):
        count += 1
        if count < 10:
            print(chr(i),end = ' ')
        else:
            count = 0
            print(chr(i),end = '\n')