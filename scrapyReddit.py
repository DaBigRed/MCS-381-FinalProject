import scrapy
from finalProj.items import RedditClassItem
import csv
import json

class RedditSpider(scrapy.Spider):

	name = "redditCrawler2"
	allowed_domains = ["reddit.com"]
	page_limit = 50
	#we will use an adjacency list to represent the graph
	#which will be stored as a dictionary
	graph = {}
	JSON_FILE_PATH = '/Users/robbyswenson/Desktop/CS/finalProj/finalproj/spiders/graph.json'

	def start_requests(self):

		start_urls = ['https://www.reddit.com/']

		#we are iterating here in order to futureproof this code
		for url in start_urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):

		#creates an instance of RedditClassItem
		item = RedditClassItem()

		#names the node_id the current url of what we are parsing
		item['node_id'] = response.url
		
		#gets the pages on reddit which the node links to (reccommended posts section)
		item['links_from'] = response.css('a::attr(href)').getall()

		#iterates through items to make links out of things that only start with /
		for index in range(len(item['links_from'])):
			if item['links_from'][index].startswith('/'):
				item['links_from'][index] = "https://www.reddit.com" + item['links_from'][index]

		#define a list to hold all links that need to be deleted
		delete_list = []	

		#add links to delete_list
		for index in range(len(item['links_from'])):	

			#gets all the bad links
			if item['links_from'][index].startswith('#'): 
				delete_list.append(item['links_from'][index])
			#gets all the external links
			elif not item['links_from'][index].startswith('https://www.reddit.com'):
				delete_list.append(item['links_from'][index])
			else: 
				continue

		#delete nodes
		for link in delete_list:
			item['links_from'].remove(link)

		#here we are adding edges from the current node in the adjacency graph
		if item['node_id'] not in self.graph:
			self.graph[item['node_id']] = set(item['links_from'])
		else:
			self.graph[item['node_id']].update(item['links_from'])

		#here we are following the links we have stored to parse new reddit posts
		for link in item['links_from']:
			if self.page_limit > 0:
				yield scrapy.Request(url=link, callback=self.parse)	
				self.page_limit -= 1
			else:
				self.log("Page limit reached. Stopping further extraction.")
				break

	def close(self, reason='finished', spider=None):
		if self.graph:
			graph_copy = {key: list(value) for key, value in self.graph.items()}
			with open(self.JSON_FILE_PATH, 'w') as json_file:
				json.dump(graph_copy, json_file, indent = 2)			
			self.log(f"Graph exported to {self.JSON_FILE_PATH}")
		super().close(reason = reason, spider = spider)
