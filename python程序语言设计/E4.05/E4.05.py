today = eval(input("Enter today's day:"))
future = eval(input("Enter the number of days elapsed since today:"))
future = (future + today) % 7
if today == 0 and future == 0:
    print("today is Sunday and the future day is Sunday")
elif today == 0 and future == 1:
    print("today is Sunday and the future day is Monday")
elif today == 0 and future == 2:
    print("today is Sunday and the future day is Tuesday")
elif today == 0 and future == 3:
    print("today is Sunday and the future day is Wednesday")
elif today == 0 and future == 4:
    print("today is Sunday and the future day is Thursday")
elif today == 0 and future == 5:
    print("today is Sunday and the future day is Friday")
elif today == 0 and future == 6:
    print("today is Sunday and the future day is Saturday")
elif today == 1 and future == 0:
    print("today is Monday and the future day is Sunday")
elif today == 1 and future == 1:
    print("today is Monday and the future day is Monday")
elif today == 1 and future == 2:
    print("today is Monday and the future day is Tuesday")
elif today == 1 and future == 3:
    print("today is Monday and the future day is Wednesday")
elif today == 1 and future == 4:
    print("today is Monday and the future day is Thursday")
elif today == 1 and future == 5:
    print("today is Monday and the future day is Friday")
elif today == 1 and future == 6:
    print("today is Monday and the future day is Saturday")
elif today == 2 and future == 0:
    print("today is Tuesday and the future day is Sunday")
elif today == 2 and future == 1:
    print("today is Tuesday and the future day is Monday")
elif today == 2 and future == 2:
    print("today is Tuesday and the future day is Tuesday")
elif today == 2 and future == 3:
    print("today is Tuesday and the future day is Wednesday")
elif today == 2 and future == 4:
    print("today is Tuesday and the future day is Thursday")
elif today == 2 and future == 5:
    print("today is Tuesday and the future day is Friday")
elif today == 2 and future == 6:
    print("today is Tuesday and the future day is Saturday")
elif today == 3 and future == 0:
    print("today is Wednesday and the future day is Sunday")
elif today == 3 and future == 1:
    print("today is Wednesday and the future day is Monday")
elif today == 3 and future == 2:
    print("today is Wednesday and the future day is Tuesday")
elif today == 3 and future == 3:
    print("today is Wednesday and the future day is Wednesday")
elif today == 3 and future == 4:
    print("today is Wednesday and the future day is Thursday")
elif today == 3 and future == 5:
    print("today is Wednesday and the future day is Friday")
elif today == 3 and future == 6:
    print("today is Wednesday and the future day is Saturday")
elif today == 4 and future == 0:
    print("today is Thursday and the future day is Sunday")
elif today == 4 and future == 1:
    print("today is Thursday and the future day is Monday")
elif today == 4 and future == 2:
    print("today is Thursday and the future day is Tuesday")
elif today == 4 and future == 3:
    print("today is Thursday and the future day is Wednesday")
elif today == 4 and future == 4:
    print("today is Thursday and the future day is Thursday")
elif today == 4 and future == 5:
    print("today is Thursday and the future day is Friday")
elif today == 4 and future == 6:
    print("today is Thursday and the future day is Saturday")
elif today == 5 and future == 0:
    print("today is Friday and the future day is Sunday")
elif today == 5 and future == 1:
    print("today is Friday and the future day is Monday")
elif today == 5 and future == 2:
    print("today is Friday and the future day is Tuesday")
elif today == 5 and future == 3:
    print("today is Friday and the future day is Wednesday")
elif today == 5 and future == 4:
    print("today is Friday and the future day is Thursday")
elif today == 5 and future == 5:
    print("today is Friday and the future day is Friday")
elif today == 5 and future == 6:
    print("today is Friday and the future day is Saturday")
elif today == 6 and future == 0:
    print("today is Saturday and the future day is Sunday")
elif today == 6 and future == 1:
    print("today is Saturday and the future day is Monday")
elif today == 6 and future == 2:
    print("today is Saturday and the future day is Tuesday")
elif today == 6 and future == 3:
    print("today is Saturday and the future day is Wednesday")
elif today == 6 and future == 4:
    print("today is Saturday and the future day is Thursday")
elif today == 6 and future == 5:
    print("today is Saturday and the future day is Friday")
else :
    print("today is Saturday and the future day is Saturday")
