import json
def findPaths(data, node1, node2):
  return recFindPath(data, node1, node2, node1, [])
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
      nodebuilder = pastNodes + [currNode] + recFindPaths(data, node1, node2, node, [pastNodes + currNode]) 
      pastNodes.append(nodeBuilder)
      paths.append(pastNodes.append(currNode))
    return paths
#Save dictionary with url as keys and number of appearances in shortest paths as values, variable name = data
with open("graph.json", "r") as f:
  data = json.load(f)
for page in data:
  for page2 in data:
    findPaths(data, page1, page2)
      

#Export new dictionary to a json file
with open("betweenness.json", "w") as json_file:
  json.dump(incoming_dict, json_file)
