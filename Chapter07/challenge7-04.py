list = [8, 9]
while True:
    anser = input("数を推測しましょう。'q'を押したら終了します")
    if anser == 'q':
        break   
    try:
        anser = int(anser)
    except valueError:
        print("数を推測しましょう。qを押したら終了します")
    if anser in list:
        print("正解！")
    else:
        print("不正解")
