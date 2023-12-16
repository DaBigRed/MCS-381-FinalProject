import json
import sys
with open("graph.json", "r") as f:
  data = json.load(f)

with open("incoming.json", "r") as fi:
  incoming = json.load(fi)
sys.setrecursionlimit(100000)
newKeys = []
for key in data:
  for link in data[key]:
    if link not in data:
      newKeys.append(link)
for link in newKeys:
    data[link] = ["https://www.reddit.com"]


newKeys1 = []
for key in incoming:
  for link in incoming[key]:
    if link not in incoming:
      newKeys1.append(link)
for link in newKeys:
    incoming[link] = ["https://www.reddit.com"]
print("https://www.reddit.com/r/Minecraft" in data)
class pageRank:
  def __init__(self, numOutgoing, incoming, numNodes):
    self.numOutgoing = numOutgoing
    if(self.numOutgoing ==0):
      self.numoutgoing = 1
    self.incoming = incoming
    self.oldPR = 1.0/numNodes
    self.newPR = 0
    self.repeating = False
    self.numNodes = numNodes
  def getIncoming(self):
      return self.incoming
  def getoldPR(self):
      return self.oldPR
  def getnumOutgoing(self):
      return self.numOutgoing
  def pageRankStep(self):
    #print(self.incoming)
    incomScore = 0
    for link in self.incoming:
      incomScore += dict[link].getoldPR() / dict[link].getnumOutgoing()
      #print("one step")
    #print(incomScore)
    dampAdd = 0.15/numNodes
    dampScore = dampAdd + 0.85*(incomScore)
#    print(dampScore)
    self.newPR = dampScore
  def endStep(self):
    if self.oldPR == self.newPR:
      self.repeating = True
    self.oldPR = self.newPR
def partition(array, low, high, dict):
  pivot = dict[array[high]]
  i = low -1
  for j in range(low, high):
    if dict[array[j]] <= pivot:
      i = i+1
      (array[i], array[j]) = (array[j], array[i])
  (array[i+1], array[high]) = (array[high], array[i+1])
  return i + 1    
def quicksort(array, low, high, dict):
  if low<high:
    pi = partition(array, low, high, dict)
    print(pi)
    
    quicksort(array, low, pi - 1, dict)
    
    quicksort(array, pi +1, high, dict)
dict = {}
numNodes = len(incoming)
notAllRepeat = True
accum = 0
for key in incoming:
  dict[key] = pageRank(len(data[key]), incoming[key], numNodes)
  #print(dict[key].numOutgoing)
#print("keys Created")
while (accum < 100):
  for key in dict:
    dict[key].pageRankStep()
  print(accum)
  for key in dict:
    dict[key].endStep()
  notAllRepeating = False
  for key in dict:
    if not (dict[key].repeating): 
      notAllRepeating = True
  accum += 1
prDict = {}
keyList = []
for key in dict:
  keyList.append(key)
  prDict[key] = dict[key].getoldPR()
  #print(dict[key].getoldPR())
quicksort(keyList, 0, len(keyList) -1,prDict)
finalDict = {}
for index in range(-100, 0):
  key = str(-index) + ": " + keyList[index]
  finalDict[key] = prDict[keyList[index]]
with open("PR.json", "w") as json_file:
  json.dump(finalDict, json_file)


  
