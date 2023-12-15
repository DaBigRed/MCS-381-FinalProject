import json

with open("graph.json", "r") as f:
  data = json.load(f)
numNodes = 0
numEdges = 0
for node in data:
  numNodes+=1
  for connect in data[node]:
    numEdges += 1
print(numNodes)
print(numEdges)
