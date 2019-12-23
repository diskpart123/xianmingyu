num = eval(input("Enter an integer:"))
isand = ( num % 5 == 0 and num % 6 == 0 )
isor = ( num % 5 == 0 or num % 6 == 0 )
isboth = ( num % 5 == 0 or num % 6 == 0 ) and ( num % 5 != 0 or num % 6 != 0 )

print("Is", num, "divisible by 5 and 6?",isand)
print("Is", num, "divisible by 5 or 6?",isor)
print("Is", num, "divisible by 5 or 6,but not both?",isboth)
