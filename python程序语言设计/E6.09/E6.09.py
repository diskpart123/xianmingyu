def foottometer(foot):
    meter = 0.305 * foot
    return "%.3f" % float(meter)

def metertofoot(meter):
    foot = meter / 0.305
    return "%.3f" % float(foot)

print("___________________________________________________________________")
print("Feet      |     Meters         ||     Meters        |     Feet")
print("-------------------------------------------------------------------")
for i in range(1,11):
    if i < 9:
        print(i,"        |    ",foottometer(i),"         ||    ",20 + 10 * ( i - 1 ),"           |    ",metertofoot(20 + 10 * ( i - 1 )))
    elif i == 9:
        print(40 - i,"       |    ",foottometer(40 - i),"         ||    ",120 - 10 * i,"           |    ",metertofoot(120 - 10 * i))
    else:
        print(i,"       |    ",foottometer(i),"         ||    ",20 + 10 * ( i - 1 ),"          |    ",metertofoot(20 + 10 * ( i - 1 )))

print("-------------------------------------------------------------------")