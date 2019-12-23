import random

lottery = random.randint(0,999)

guess = eval(input("Enter your lottery pick (three digits): "))

lotterydigit1 = lottery // 100#百位数
lotterydigit2 = lottery % 100
lotterydigit3 = lotterydigit2 // 10#十位数
lotterydigit4 = lotterydigit2 % 10#个位数

guess1 = guess // 100#百位数
guess2 = guess % 100
guess3 = guess2 // 10#十位数
guess4 = guess2 % 10#个位数

two = ( lotterydigit3 == guess4 and lotterydigit4 == guess3 ) or \
      ( lotterydigit1 == guess3 and lotterydigit3 == guess1 ) or \
      ( lotterydigit1 == guess4 and lotterydigit3 == guess1 and lotterydigit4 == guess3 ) or \
      ( lotterydigit1 == guess3 and lotterydigit3 == guess4 and lotterydigit4 == guess1 ) or \
      ( lotterydigit1 == guess4 and lotterydigit4 == guess1 )

one = ( lotterydigit1 == guess1 ) or ( lotterydigit1 == guess3 ) or ( lotterydigit1 == guess4 ) or \
      ( lotterydigit3 == guess1 ) or ( lotterydigit3 == guess3 ) or ( lotterydigit3 == guess4 ) or \
      ( lotterydigit4 == guess1 ) or ( lotterydigit4 == guess3 ) or ( lotterydigit4 == guess4 )

print("The lottery number is",lottery)

if guess == lottery:
    print("Exact match: you win $10,000!")
elif two:
    print("Match all digits: you win $3,000!")
elif one:
    print("Match one digits: you win $1,000!")
else:
    print("Sorry ,on match!")