import json
def findPaths(data, node1, node2): 
  #Find all paths
  paths = recFindPath(data, node1, node2, node1, [])
  min = len(paths[0])
  max = 0
  for path in paths:
    #If the path did not reach the desired value
    if(path[-1] == -1):
      #remove it
      paths.remove(path)
    #else if length is less than min
    else if(len(path) < min):
      #set new min
      min = len(path)
    #else if length is greater than max
    else if(len(path) > max):
      #set new max
      max = len(path)
  for path in paths:
    #If a path's length is longer than the min
    if(len(path) != min):
      #remove it from paths
      paths.remove(path)
  #return all paths that are the minimum length
  return paths
#Recursive
def recFindPaths(data, node1, node2, currNode, pastNodes):
  #if destination is already is a direct connection to current node
  if(node2 in data[currNode]):
    #put current node in the path and return
    return pastNodes.append(currNode)
    #accumulator for nodes that arent already in the path (dont circle back)
  newNodes = []
  for node in data[currNode]:
    #if node is not a past node
    if(node not in pastNodes):
      #mark it as a new node
      newNodes.append(node)
  #If there are no new paths, mark this as not a valid path
  if (len(newNodes) = 0):
    return pastNodes.append(-1)
    #else continue down path
  else:
    #contains all new path possible
    paths = []
    #for all the nodes not already in path
    for node in newNodes:
      #create path with node in the final spot
      nodebuilder = pastNodes + [currNode] + recFindPaths(data, node1, node2, node, [pastNodes + currNode]) 
      #Add this to our sum of paths
      paths.append(pastNodes.append(currNode))
    return paths
#Save dictionary with url as keys and number of appearances in shortest paths as values, variable name = data
with open("graph.json", "r") as f:
  data = json.load(f)
dict = {}
paths = [] 
#Find shortest paths of all 1-2 node pairs
for page in data:
  for page2 in data:
    paths += findPaths(data, page1, page2)
#initialize all keys at 0
for key in data:
  dict[key] = 0
#Add 1 for everytime a stop appears in a path
for path in paths:
  for stop in path:
    dict[stop] += 1
  



#Export new dictionary to a json file
with open("betweenness.json", "w") as json_file:
  json.dump(incoming_dict, json_file)
