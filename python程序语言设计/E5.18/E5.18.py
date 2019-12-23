num = eval(input("Enter an integer:"))
d = num

for i in range(d-1,1,-1):
    if d % i == 0:
        a = d // i
        d = i
        print(a,end = ',')
        i = d - 1

print(d)