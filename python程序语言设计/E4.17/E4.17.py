import random

num = eval(input("scissor(0), rock(1), paper(2) :"))
com = random.randint(0,2)

if com == num == 0:
    print("The computer is scissor. You are scissor too. It's a draw.")

if com == num == 1:
    print("The computer is rock. You are rock too. It's a draw.")

if com == num == 2:
    print("The computer is paper. You are paper too. It's a draw.")

if com == 0 and num == 1:
    print("The computer is scissor. You are rock. You won.")

if com == 0 and num == 2:
    print("The computer is scissor. You are paper. The computer won.")

if com == 1 and num == 0:
    print("The computer is rock. You are scissor. The computer won.")

if com == 1 and num == 2:
    print("The computer is rock. You are paper. You won.")

if com == 2 and num == 0:
    print("The computer is paper. You are scissor. You won.")

if com == 2 and num == 1:
    print("The computer is paper. You are rock. The computer won.")