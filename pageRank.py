import json

with open("graph.json", "r") as f:
  data = json.load(f)

with open("incoming.json", "r") as fi:
  incoming = json.load(fi)

for key in data:
  for link in data[key]:
    if link not in data:
      data[key] = []

for key in incoming:
  for link in incoming[key]:
    if link not in data:
      data[key] = []
class pageRank:
  def __init__(self, numOutgoing, incoming, numNodes):
    self.numOutgoing = numOutgoing
    self.incoming = incoming
    self.oldPR = 1.0/numNodes
    self.newPR = 0
    self.repeating = False
    self.numNodes = numNodes
  def pageRankStep(self, dict):
    incomScore = 0
    for link in self.incoming:
      incomScore += dict[link].oldPR + dict[link].numOutgoing
    dampadd = 0.15/numNodes
    dampScore = dampAdd + 0.85*(incomScore)
    self.newPR = dampScore
  def endStep(self):
    if self.oldPR == self.newPR:
      self.repeating = true
    self.oldPR = self.newPR
dict = {}
numNodes = len(incoming)
notAllRepeat = True
accum = 0
for key in incoming:
  dict[key] = pageRank(len(data[key]), incoming, numNodes)
while (notAllRepeat) & (accum < 1000):
  for key in dict:
    dict[key].pageRankStep(dict)
  for key in dict:
    dict[key].endStep
  notAllRepeating = False
  for key in dict:
    if not (dict[key].repeating): 
      notAllRepeating = True
prDict = {}
for key in dict:
  prDict[key] = dict[key].oldPR

with open("PR.json", "w") as json_file:
  json.dump(prDict, json_file)


  
