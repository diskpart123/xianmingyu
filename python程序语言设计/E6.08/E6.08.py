def celtofah(n):
    fah = ( 9 / 5 ) * n + 32
    return round(fah,1)

def fahtocel(n):
    cel = ( 5 / 9 ) * n - 32
    return round(cel,2)

print("___________________________________________________________________")
print("Celius     |     Fahrenheit     ||     Fahrenheit     |     Celsius")
print("-------------------------------------------------------------------")
for i in range(0,10):
    if 40 - i >37:
        print(40 - i,"        |    ",celtofah(40 - i),"         ||    ",120 - 10 * i,"           |    ",fahtocel(120 - 10 * i))
    else:
        print(40 - i,"        |    ",celtofah(40 - i),"          ||    ",120 - 10 * i,"            |    ",fahtocel(120 - 10 * i))

print("-------------------------------------------------------------------")