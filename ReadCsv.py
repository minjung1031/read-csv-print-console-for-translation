import csv
import re

result = ''
keys = []
englishes = []
frenches = []

# read csv file
with open('test.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';')
  for row in spamreader:
    for line in row:
      Type = line.split(",")
      englishes.append(Type[0])
      frenches.append(Type[1])
for e in englishes:
  tempKey = ''
  for letter in e:
    if re.match(r'\b[^\d\W]+\b', letter):
      tempKey += letter
    else:
      tempKey += '_'
  keys.append(tempKey.lower())
print keys