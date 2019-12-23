finacccountvalue = eval(input("Enter final account value: "))
rate = eval(input("Enter annual interest rate in percent: "))
years = eval(input("Enter number of years: "))
print("Initial deposit value is",finacccountvalue / (1 + rate / (12 * 100)) ** (years * 12))
