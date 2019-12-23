subtotal,gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = round(subtotal*gratuityRate*0.01,2)
total = round(subtotal + gratuity,2)
print("The gratuity is",gratuity,"and the total is",total)
