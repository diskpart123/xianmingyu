num = eval(input("Enter a decimal value (0 to 15):"))

if num < 10:
    print("The hex value is",num)
elif num >= 10 and num <= 15:
    num = 65 + num - 10
    print("The hex value is",chr(num))
else:
    print("Invalid input")