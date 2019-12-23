num = eval(input("Enter an integer, the input ends if it is 0:"))

if num == 0:
    print("You didn't enter any number.")
else:
    count1 = 0
    count2 = 0
    sum = 0

    while num != 0:
        if num < 0:
            count1 += 1
        else:
            count2 += 1
        sum = num + sum
        num = eval(input("Enter an integer, the input ends if it is 0:"))

    print("The number of positives is", count2)
    print("The number of negatives is", count1)
    print("The total is", sum)
    print("The average is", sum / ( count1 + count2 ))