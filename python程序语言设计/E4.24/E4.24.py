num = eval(input("Enter a number from 1 to 52:"))
col = ""
card = ""

colour = ( num - 1 ) // 13
number = num % 13

if colour == 0:
    col = "Clubs"
elif colour == 1:
    col = "Heart"
elif colour == 2:
    col = "Dianmond"
else:
    col= "Spade"

if number == 0:
    card = "King"
elif number == 1:
    card = "Ace"
elif number == 2:
    card = "2"
elif number == 3:
    card = "3"
elif number == 4:
    card = "4"
elif number == 5:
    card = "5"
elif number == 6:
    card = "6"
elif number == 7:
    card = "7"
elif number == 8:
    card = "8"
elif number == 9:
    card = "9"
elif number == 10:
    card = "10"
elif number == 11:
    card = "Jack"
else:
    card = "Queen"

print("The card you picked is the",card,"of",col)
