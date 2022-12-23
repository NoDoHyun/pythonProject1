import csv
f = open('flower.csv', 'r')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()
