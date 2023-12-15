import json

with open("graph.json", "r") as f:
  data = json.load(f)

visited = []
queue = []
def bfs(graph, node1,node2):
  path_list = [[node1]]
  path_index = 0
  previous_nodes = {node1}
  if node1 == node2:
    return path_list[0]
  while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = graph[last_node]
    if node2 in next_nodes:
      current_path.append(node2)
      return current_path
    if next_node in next_nodes:
      if not next_node in previous_nodes:
        new_path = current_path[:]
        new_path.append(next_node)
        path_list.append(new_path)
    path_index += 1
  return []

dict = {}
paths = []
for node in data:
  dict[node] = 0
  for node1 in data:
    if node != node1:
      paths.append(bfs(data, node, node1)

for path in paths:
  for node in path:
      dict[node] += 1

with open("betweenness.json", "w") as json_file:
  json.dump(dict, json_file)
      
