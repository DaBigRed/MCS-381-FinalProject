import json

#open the file which has urls as keys and what the url links to as values
with open("graph.json", "r") as input_file:
	data = json.load(input_file)

#this prints the value (list of urls) for a certain page
# print(data["https://www.reddit.com/"]) 

#make a list of tuples to hold all of the clustering coefficient values
cluster_co_list = []

#now for each key
for key in data.keys():
	#calculate the cluster coefficient score for the key

	#K will be degree of a node v (a certain key) and N will be the number 
	#of connections between neighbors of v
	
	#calculate how many outgoing links v has
	K = len(data[key])
	#no divide by zero allowed!
	if K == 1 or K == 0:
		continue

	#now we calculate N
	N = 0

	#for each url that the current key links to 
	for url in data[key]:
		#make a list of all the other urls that the current key links to
		other_urls = data[key]
		other_urls.remove(url)

		#if the url does not link to anything, then there is no way
		#that it could link to something that the current key links to, 
		#so go to the next url
		if url not in data.keys():
			continue

		url_links = data[url]

		#intersect between other_urls and url_links to find the 
		#urls that both the key and the current url from the value of the 
		#key link to
		intersect = []

		for element in url_links:
			if element in other_urls:
				intersect.append(element)

		#the number of values in the intersect list is added to the N value
		N = N + len(intersect)

	#now that we have K and N, we can calculate the clustering coefficient of the 
	#current key
	cluster_co = (2 * N) / (K * (K - 1))
	
	#append the cluster coefficient value to cluster_co_list
	cluster_co_list.append((key, cluster_co))

#now we sort

#initialize the top_5 list with zeros
top_5 = [("null", 0),("null", 0),("null", 0),("null", 0),("null", 0)]

#iterate through every value in cluster_co_list starting with the one at index 5
for x in range(len(cluster_co_list)):

	#determine if the current node's cluster coefficient is in the top five
	#if it is, assign n to the spot it should take
	if cluster_co_list[x][1] > top_5[0][1]:
		n = 0
	elif cluster_co_list[x][1] > top_5[1][1]:
		n = 1
	elif cluster_co_list[x][1] > top_5[2][1]:
		n = 2
	elif cluster_co_list[x][1] > top_5[3][1]:
		n = 3
	elif cluster_co_list[x][1] > top_5[4][1]:
		n = 4
	else:
		continue

	#now we have n, a value which we can use to update our top_5 list
	if n == 0:
		top_5[4] = top_5[3]
		top_5[3] = top_5[2]
		top_5[2] = top_5[1]
		top_5[1] = top_5[0]
		top_5[0] = cluster_co_list[x]
	elif n == 1:
		top_5[4] = top_5[3]
		top_5[3] = top_5[2]
		top_5[2] = top_5[1]
		top_5[1] = cluster_co_list[x]
	elif n == 2:
		top_5[4] = top_5[3]
		top_5[3] = top_5[2]
		top_5[2] = cluster_co_list[x]
	elif n == 3:
		top_5[4] = top_5[3]
		top_5[3] = cluster_co_list[x]
	#n == 4
	else:
		top_5[4] = cluster_co_list[x] 
		
#print sorted list
for item in top_5:
	print(item)

	

