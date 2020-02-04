import csv

result = ''
english = []
french = []
with open('test.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';')
  for row in spamreader:
    for line in row:
      Type = line.split(",")
      english.append(Type[0])
      french.append(Type[1])
print english