#import scrapy #possible crawler/scraper to use
from urllib.request import urlopen
url = "https://www.reddit.com"
response = urlopen(url)
data = response.read()
dataList = data.split()
linkList = []
for data in dataList:
  if "http" in data:
    linkList.append(data)

    
