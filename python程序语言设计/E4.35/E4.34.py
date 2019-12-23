num = input("Enter a hex character:")

if ord(num) >= 65 and ord(num) <= 71:
    print("The decimal value is",ord(num) - 55)
elif ord(num) >= 97 and ord(num) <= 103:
    print("The decimal value is",ord(num) - 87)
elif int(num) <=9 and int(num) >= 0:
    print("The decimal value is",int(num))
else:
    print("Invalid input")