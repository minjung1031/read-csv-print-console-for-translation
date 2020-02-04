import csv
import re

result = ''
keys = []
englishes = []
frenches = []
newFrenches = []

# read csv file
with open('test.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';')
  for row in spamreader:
    for line in row:
      Type = line.split(",")
      englishes.append(Type[0])
      frenches.append(Type[1])
englishes.pop(0)
frenches.pop(0)

# generate keys from English
for e in englishes:
  tempKey = ''
  for letter in e:
    if re.match(r'^[a-zA-Z0-9_.-]*$', letter):
      tempKey += letter
    else:
      tempKey += '_'
  keys.append(tempKey.lower())

# manage apostrophe in French
for f in frenches:
  tempFrench = ''
  for letter in f:
    if re.match(r'[a-zA-Z]+\'?s', letter):
      tempFrench += '\\'+letter
    else:
      tempFrench += letter
  newFrenches.append(tempFrench)

# print out result on console
result += '===== ENGLISH =====\n'
for i in xrange(0, len(keys)):
  result += keys[i]+': \''+englishes[i]+'\''
  if i < len(keys)-1:
    result += ',\n'
  else:
    result += '\n'
result += '\n===== FRENCH =====\n'
for i in xrange(0, len(keys)):
  result += keys[i]+': \''+newFrenches[i]+'\''
  if i < len(keys)-1:
    result += ',\n'
  else:
    result += '\n'
print result

