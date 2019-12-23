num = eval(input("Enter a three-digit integer:"))

num1 = num % 10
num2 = num // 100

if num1 == num2:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")