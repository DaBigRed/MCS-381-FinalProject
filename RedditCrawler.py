import scrapy
import pickle

class page:
  def __init__ (self, url):
    self.url = url
    incoming = []
    outgoing = []
    oldPR = 0
    newPR = 0
  def getURL():
    return self.url
  def getPR():
    return this.oldPR
  def getNumOutgoing():
    return len(this.outgoing)
  def addIncoming(newURL):
    this.incoming += newURL
  def addOutgoing(newURL):
    this.outgoing += newURL
  def initPR(numNodes):
    this.oldPR = 1.0/numNodes
  def PRStep(numNodes):
    income = 0
    for num in range(len(incoming)):
      income += incoming[i].getPR() + incoming[i].getNumOutgoing()
    dampAdd = .15/numNodes
    dampScore = dampAdd + 0.85*(income)
    this.oldPR = dampScore
  def endStep():
    this.newPR = this.oldPR
  def __str__ (self):
    return("URL: " + this.url + "Page Rank: " + this.oldPR)
  def savePage(fileName):
    with open(fileName, "wb") as file:
      pickle.dump(this, file)
    
def sort(pageLst):
  size = len(pageLst)
  for i in range(size-1):
    for j in range(size-i):
      if(pageLst[j-1].getPR() < pageLst.getPR(j):
        temp = pageLst[j-1]
        pageLst[j-1] = pageLst[j]
        pageLst[j] = temp
    #checks for 2 sided connection
  def checkConnection(pageA, pageB):
    if(pageB in this.incoming):
      if(this in pageB.getIncoming):
        return True  
  def checkTriangle(pageA, pageB, pageC):
    if(checkConnection(pageA, pageB)):
      if(checkConnection(pageA, pageC)):
        if(checkConenction(pageB, pageC)):
          return true
  def clusterCoeff(pageLst):
    totalTrip = 0 #total number of triple in system
    trueTrip = 0 #number of closed triple
    for num in range(len(pageLst)):
      for num2 in range(len(pageLst)-1):
        for num3 in range(len(pageLst)-2):
          totalTrip += 1
          if(checkTriangle(pageLst[num], pageLst[num2+1], pageLst[num3+2]):
            trueTrip += 1
    return trueTrip/totalTrip
  def betweenness():

  
      
#Depending on what output Scrapy gives us, we need to write the "main"
#Preferably we get a list of Strings me thinks
#Then we iterate through them
#then do if("http://reddit.com" in *whateverOurNameForString*)
#currentNode.addOutgoing(*nodeNewURL*), URL.addIncoming(*CurrentNode*)
#We will need to keep track of total connections, so totalConnections +=1
#We need 100 highest page rank nodes
#We need num nodes and num connections
#We need diameter (essentially how many levels we have crawled(reddit.com/ is our first level, all things that links to are 2nd level, etc)
      
#Things we should do while scraping
  #find outgoing links
  #find diameter
#Kind of a second step
  #Store URL and it's outgoing links in a dictionary
#Things for later
  #Find incoming links using outgoing links
  #Find total connections(add numOutgoing for all pages)
  #Use incoming links, numOutgoing, to determine page rank (print 100 highest)
  #num nodes (size of dictionary)
  #Find 5 nodes with highest cluster coefficient
  #Number of components (numNodes + numEdges)
  #top 5 for Betweenness Centrality (In the most paths between nodes)
  #average path length
  #Graph of in-degree out-degree from assignment 1 (export as CSV and put in excel) (requires numIncoming)
  #100 highest page rank nodes (requires incomingLinks as a list and numOutgoing)








    
  
