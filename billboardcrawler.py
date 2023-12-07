#import scrapy #possible crawler/scraper to use
#This is mostly bum code
from urllib.request import urlopen

class page:
  def __init__ (self, url):
    self.url = url
    incoming = []
    outgoing = []
    oldPR = 0
    newPR = 0
  def getURL():
    return self.url
  def addIncoming(newURL):
    incoming += newURL
  def addOutgoing(newURL):
    outgoing += newURL
    
def getLinks(url, pageList):
  response = urlopen(url)
  data = response.read()
  dataList = data.split()
  linkList = []
  pageURLList = []
  for page in pageList:
    pageURLList.append(page.getURL())
  for data in dataList:
    if "http" in data:
      if data not in pageURLList:
        linkList.append(data)
  return linkList

pageList = []
while pageList.size() < 10:
  allLinks = []
  url = "https://www.reddit.com"
  allLinks += getLinks(url, allLinks)
  firstPage = Page(url)
  firstPage.addOutgoing(allLinks)
  for link in allLinks:
    tempLinks = getLinks(link, allLinks) 
    allLinks += tempLinks
    #going to have to add an "if doesnt exist"  in here somewhere
    tempPage = Page(link)
    tempPage.addOutgoing(tempLinks)
    pageList.append(tempPage)
    #add keep track of all outgoing links
    allLinks.remove(link)

