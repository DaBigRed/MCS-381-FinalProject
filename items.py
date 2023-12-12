import scrapy

class RedditPostItem(scrapy.Item):
  node_id = scrapy.Field()
  post_name = scrapy.Field()
  links_from = scrapy.Field()
