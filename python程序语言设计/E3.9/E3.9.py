name = input("Enter employee's name: ")
workhour = eval(input("Enter number of hours worked in a week: "))
payrate = eval(input("Enter hourly pay rate: "))
fedrate = eval(input("Enter federal tax withholding rate: "))
staterate = eval(input("Enter state tax withholding rate: "))

grosspay = workhour * payrate

fedpay = fedrate * grosspay
statepay = staterate * grosspay
totaldeduction = fedpay + statepay
netpay = grosspay - totaldeduction

print("Employee Name: ",name)
print("Hours Worked: ",format(workhour,".1f"))
print("Pay Rate: ",chr(36),payrate)
print("Gross Pay: ",chr(36),grosspay)
print("Deductions: ")
print("  Federal Withholding (",format(fedrate,".1%"),"):",chr(36),fedpay)
print("  State Withholding (",format(staterate,".1%"),"):",chr(36),format(statepay,".2f"))
print("  Total Dedution:",chr(36),format(totaldeduction,".2f"))
print("Net Pay:",chr(36),format(netpay,".2f"))
