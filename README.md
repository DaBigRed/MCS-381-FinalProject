# MCS-381-Paper

A research project and paper created by Robby Swenson and Corey Lundgren at Gustavus Adolphus College for MCS - 381, Social Computing.


File Descriptions:
BFS.py: Our breadth first search algorithm used to find the shortest path lengths of all possible connections between nodes
com.py: A small file to confirm that all pages link to “https://reddit.com/” to confirm that we only have 1 component
findIncoming.py: Using graph.json, make a dictionary where each key is a website url and each value is a list of the pages which link to the key.
graph.json: Our main data file. Each key is a website url and each value is a list of the pages the key links to.
incoming.json: The file found using findIncoming.py.
items.py: A file which defines a class “RedditPostItem” which is used to keep track of certain information about each Reddit page we visited. This class is used in scrapyReddit.py.
numNodesEdges.py: Finds and prints the number of nodes and edges in graph.json.
pageRank.py: Calculates page rank of all pages and prints the 100 highest in PR.json
scrapyReddit.py: Our scrapy scraper which sorted through reddit pages and exported data to graph.json.
smallerJSON: A smaller set of scraped data which we used for testing.
clusterC.py: Calculates and prints the top five cluster coefficient scores of nodes in graph.json.
