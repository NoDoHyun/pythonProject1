import csv

f = open("C:\pythonProject\pythonProject\pythonProject\data.csv", "r",encoding='utf-8')
reader = csv.reader(f)

for row in reader:
    print(row[0],row[3],row[6])


