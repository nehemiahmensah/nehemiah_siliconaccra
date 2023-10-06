import csv

with open("./resources/movies.csv", "r") as movies:
    info = csv.reader(movies)
    for record in info:
        title, rating , year , runtime = record
        print(f"{title, rating ,year ,runtime}")