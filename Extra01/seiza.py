month = int(input("誕生月を入力してください"))
days = int(input("誕生日を入力を入力してください"))

if month == int(1):
    if days <= 21:
        print("山羊座です")
    else:
        print("水瓶座です")

if month == int(2):
    if days < 19:
        print("水瓶座です")
    else:
        print("魚座です")

if month == int(3):
    if days < 21:
        print("魚座です")
    else:
        print("牡羊座です")

if month == int(4):
    if days < 20:
        print("牡羊座です")
    else:
        print("牡牛座です")

if month == int(5):
    if days < 21:
        print("牡牛座です")
    else:
        print("双子座です")

if month == int(6):
    if days < 22:
        print("双子座です")
    else:
        print("かに座です")

if month == int(7):
    if days < 23:
        print("蟹座です")
    else:
        print("獅子座になる")

if month == int(8):
    if days < 23:
        print("獅子座になる")
    else:
        print("乙女座になる")
        
if month == int(9):
    if days < 23:
        print("乙女座になる")
    else:
        print("天秤座になる")

if month == int(10):
    if days <23:
        print("てんびん座になる")
    else:
        print("蠍座です")

if month == int(11):
    if days < 23:
        print("蠍座になる")
    else:
        print("射手になる")

if month == int(12):
    if days < 22:
        print("射手座になる")
    else:
        print("山羊座になる")
