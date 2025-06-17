import csv

list = [["トップガン", "リスキービジネス", "マイノリティリポート"], ["タイタニック", "ザリベント", "インセプション"], ["トレーニングデイ", "マン オン ファイル", "ファイト"]]

with open("pt.csv","w")as f:
    a = csv.writer(f,delimiter=",")
    for movie_list in list:
        a.writerow(movie_list)
