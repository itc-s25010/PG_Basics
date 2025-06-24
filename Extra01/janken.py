import random


a = ("グー","チョキ","パー")
b = input("ジャンケンしてください")
c = random.choice(a)

print (f"あなた:{b}",f"CP:{c}")

if b == "グー":
    if c == "グー":
        print("あいこです")

    elif c == "チョキ":
        print("勝ちです")

    else:
        print("負けです")

if b == "チョキ":
    if c == "グー":
        print("負けです")

    elif c == "チョキ":
        print("あいこです")

    else:
        print("勝ちです")

if b == "パー":
    if c == "グー":
        print("勝ちです")

    elif c == "チョキ":
        print("負けです")

    else:
        print("あいこです")

