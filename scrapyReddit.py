import scrapy
from mcs381final.items import RedditPostItem
#this will help us parse urls better by allowing us to chop them up
from urllib.parse import urlparse

class RedditSpider(scrapy.Spider):

  name = "redditCrawler"
  allowed_domains = ["reddit.com"]

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

    #gets the title of the reddit page
    item['title'] = response.xpath('//embed-snippet-share-button [@postid="t3_18f8vzh"]/following:: text()').get()

    #gets the pages on reddit which the node links to (reccommended posts section)
    item['links_from'] = response.xpath('').get()

