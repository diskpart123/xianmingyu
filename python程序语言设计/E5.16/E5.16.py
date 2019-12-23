n1 = eval(input("Enter first integer:"))
n2 = eval(input("Enter second integer:"))
d = 0

if n1 < n2:
    d = n1
else:
    d = n2

for i in range(d-1,1,-1):
    if n1 % i == 0 and n2 % i == 0:
        break
print("The greatest common divisor for",n1,"and",n2,"is",i)