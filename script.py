import csv

with open('insurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader)