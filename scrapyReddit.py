import scrapy
from mcs381final.items import RedditPostItem

#this will help us parse urls better by allowing us to chop them up
from urllib.parse import urlparse

class RedditSpider(scrapy.Spider):

	name = "redditCrawler"
	allowed_domains = ["reddit.com"]
	page_limit = 100
	#we will use an adjacency list to represent the graph
	#which will be stored as a dictionary
	graph = {}
	#this is how many layers we have went to
	layers = 1

	def start_requests(self):

		start_urls = ['https://www.reddit.com/r/pokemon/comments/18f8vzh/my_problem_with_scarlet_and_violet/']

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

		#iterates through items to make links out of things that only start with /
		for index in range(len(item.links_from)):
			if item.links_from[index].startswith('/'):
				item.links_from[index] = "https://www.reddit.com" + item.links_from[index]

		#define a list to hold all links that need to be deleted
		delete_list = []

		#add links to delete_list
		for index in range(len(item.links_from)):	

			#gets all the bad links
			if item.links_from[index].startswith('#'): 
				delete_list.append(item.links_from[index])
			#gets all the external links
			elif not item.links_from[index].startswith('https://www.reddit.com'):
				delete_list.append(item.links_from[index])
			else: continue

		#delete nodes
		for link in delete_list:
			item.links_from.remove(link)

		#here we are adding edges from the current node in the adjacency graph
		if item.node_id not in self.graph:
			self.graph[item.node_id] = set()
		for link in item.links_from:
			self.graph[item.node_id].add(link)

		#here we are following the links we have stored to parse new reddit posts
		for link in item.links_from:
			if self.page_limit > 0:
				yield scrapy.Request(url=link, callback=self.parse)
				self.layers += 1
				self.page_limit -= 1
			else:
				self.logger.info("Page limit reached. Stopping further extraction.")
				break			
