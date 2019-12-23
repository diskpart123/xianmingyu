fah = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
v = eval(input("Enter the wind speed in miles per hour: "))
print("The wind chill index is",round(35.74 + 0.6215 * fah - 35.75 * v ** 0.16 + 0.4275 * fah * v ** 0.16,5))
