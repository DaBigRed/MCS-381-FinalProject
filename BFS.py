import json
import networkx as nx

#reads in the info from our .JSON file
def read_json(file_path):
	with open(file_path, 'r') as file:
		data = json.load(file)
	return data

#makes a directed graph containing all of our information
def create_graph(data):
	#make a graph and name it G
	G = nx.DiGraph()
	#makes two variables, node and neighbors, which will hold key value pairs from the 
	#.JSON file

	#for each key value pair, assign node to be the key and 
	#neighbors to be the value
	for node, neighbors in data.items():
		G.add_node(node)
		#for each node that the key connects to
		for neighbor in neighbors:
			#add an edge from the current node to the current neighbor
			G.add_edge(node, neighbor)
	#return the graph
	return G

#a function to get all of the shortest paths from every node to every other node and 
#store the length of the paths in a dictionary in the form: shortest_paths[first_node][second_node]
def get_short_paths(graph):
	shortest_paths = dict(nx.all_pairs_shortest_path_length(graph))
	return shortest_paths

def get_between_cent(graph):
	betweenness_centrality = nx.betweenness_centrality(graph)
	return betweenness_centrality

def calculate_average_path_length(all_shortest_paths_dict):
	total_length = 0
	total_paths = 0

	for source, targets in all_shortest_paths_dict.items():
		for target, length in targets.items():
			if length != 0 and length != float('inf'):
				total_length += length
				total_paths += 1
	
	if total_paths == 0:
		return 0  

	average_path_length = total_length / total_paths
	return average_path_length

def print_top_n_betweenness_centrality(betweenness_centrality_dict, n=5):
    # Sort the dictionary by centrality values in descending order
    sorted_nodes = sorted(betweenness_centrality_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Take only the top n nodes
    top_n_nodes = sorted_nodes[:n]

    for node, centrality in top_n_nodes:
        print(f"Node {node}: Betweenness centrality = {centrality}")

def find_longest_path(all_shortest_paths_dict):
    max_path_length = 0

    for source, targets in all_shortest_paths_dict.items():
        max_path_length = max(max_path_length, max(targets.values()))

    return max_path_length

def main():
	print("running")

	#make a variable named file path, which will reference the .JSON
	file_path = 'graph.json'
	
	#read the file
	data = read_json(file_path)
	
	#create the graph
	graph = create_graph(data)

	print("calculating shortest paths")

	#get the dictionary of shortest paths
	shortest_paths_dict = get_short_paths(graph)

	#now find the average path length
	average_path = calculate_average_path_length(shortest_paths_dict)

	###
	#Important stuff
	###

	print("**********" * 10)

	print("average path length: " + str(average_path))

	#calculate betweenness centrality
	bet_cent_dict = get_between_cent(graph)

	#print betweenness centrality
	print_top_n_betweenness_centrality(bet_cent_dict)

	longest_path = find_longest_path(shortest_paths_dict)
	print("Longest path: " + str(longest_path))

if __name__ == "__main__":
    main()
