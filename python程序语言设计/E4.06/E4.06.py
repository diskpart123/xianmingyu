weight = eval(input("Enter weight in pounds:"))
feet = eval(input("Enter weight in feet:"))
inches = eval(input("Enter weight in inches:"))

perpound = 0.45359237
perinch = 0.0254

weightinkilograms = weight * perpound
heightinmeters = ( feet * 12 + inches ) * perinch

bmi = weightinkilograms / (heightinmeters *heightinmeters)

print("BMI is",format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
