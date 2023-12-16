import json
import csv
with open("graph.json", "r") as f:
  data = json.load(f)

with open("incoming.json", "r") as fi:
  incoming = json.load(fi)

numOut =  {}
numIn = {}

for key in data:
  if len(data[key]) not in numOut:
    numOut[len(data[key])] = 1
  else:
    numOut[len(data[key]] += 1
for key in incoming:
  if len(incoming[key] not in numIn:
    numIn[len(incoming[key])] = 1
  else:
    numIn[len(incoming[key])] += 1

header = ["url", "Number of Outgoing Links"]
header2 = ["url", "Number of Incoming Links"]

filename = "inDegree.csv"
with open(filename, 'w', newline="") as file:
  w = csv.writer(file)
  w.writerow(header)
  w.writerows(numOut)

filename2 = "outDegree.csv"
with open(filename2, 'w', newline="") as file:
  w = csv.writer(file)
  w.writerow(header2)
  w.writerows(numIn)
