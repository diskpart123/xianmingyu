pounds = eval(input("Enter weight in pounds: "))
inches = eval(input("Enter height in inches: "))
kg = pounds * 0.45359237
m = inches * 0.0254
print("BMI is",round(kg / m ** 2 , 4))
