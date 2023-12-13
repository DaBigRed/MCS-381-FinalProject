import json
#Save dictionary with url as keys and outgoing links as values, variable name = data
with open("graph.json", "r") as f:
  data = json.load(f)
#construct dictionary with url as key and outgoing links as value
#Constructor dictionary
incoming_dict = {}
#Initialize all the same keys we previously used
for key in data:
  incoming_dict[key] = []
#for each URL used as a key in data
for key in data:
  #For each outgoing link of that URL
  for url in data[key]:
    #If that link's URL is one of our keys(because we limited our crawler)
    if url in incoming_dict:
      #add the key URL to link's incoming list
      incoming_dict[url].append(key)
      #else if it isnt one we crawled through
    else:
      #add it as a new key with the value as a list containing original key
      incoming_dict[url] = [key]
#Export new dictionary to a json file
with open("incoming.json", "w") as json_file:
  json.dump(incoming_dict, json_file)
