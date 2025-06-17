import csv

list = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revent", "Inception"], ["Training day", "Man on fire", "Flighit"]]

with open("pt.csv","w")as f:
    a = csv.writer(f,delimiter=",")
    for movie_list in list:
        a.writerow(movie_list)
