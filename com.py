import json

with open("graph.json", "r") as f:
  data = json.load(f)

for node in data:
  if "https://www.reddit.com/" not in data:
    final = "false"
  else:
    final = "true"
    
print(final)
