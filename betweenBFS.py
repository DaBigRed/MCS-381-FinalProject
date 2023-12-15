import json

with open("graph.json", "r") as f:
  data = json.load(f)
newKeys = []
for key in data:
  for link in data[key]:
    if link not in data:
      newKeys.append(link)
for link in newKeys:
    data[link] = ["https://www.reddit.com"]

def bfs(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return [start]
    while queue:
        path= queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(node)
    return []
print("made it passed cleaning")
dict = {}
paths = []
for node in data:
  dict[node] = 0
  for node1 in data:
    if node != node1:
      paths.append(bfs(data, node, node1))
      print("path added")
print("made it passed BFS")
for path in paths:
  for index in range(len(path-2)):
      dict[path[index+1]] += 1
print("made it past dictionary accumulating")
with open("betweenness.json", "w") as json_file:
  json.dump(dict, json_file)
      
      
