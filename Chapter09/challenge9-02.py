a = input("好きな数字は？")
with open("c.txt", "w+") as f:
    f.write(a)
    print(f.read())
