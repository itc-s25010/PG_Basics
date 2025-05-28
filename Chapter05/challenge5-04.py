dir = {"身長": 165, "体重": 61}
a = input("キーを入力してください:")
if a in dir:
    b = dir[a]
    print(b)
else:
    print("そんなキーはございません")
