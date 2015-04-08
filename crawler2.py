#Copied from rahulrrixe's EDGAR project.
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
#from config import DEFAULT_DATA_PATH
#import re
import requests
#import os

from bs4 import BeautifulSoup



#class SecCrawler():

#	def __init__(self):
#		self.hello = "Welcome to Sec Crawler!"
		
#    def filing_13F(self, cik, count): #No need for company code if we've got CIK numbers. CIK numbers are unique for each company.


cik = '872573'
count = 40

#generate the url to crawl
base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+str(cik)+"&type=13F-HR&owner=exclude&output=xml&count="+str(count)
print ("started 13F"+str(cik))
r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data) # Initializing to crawl again
linkList=[] # List of all links from the CIK page


#soup.find_all("tr"). #perhaps reach for each row, and then grab the link and the date?
#Need to identify the link, the filing date, and the filing type; 13F-HR/A's are a problem, as will be avoiding 13F-NT's and the like.

# If the link is .htm convert it to .html
for link in soup.find_all('filinghref'): #Why filinghref?
    URL = link.string
    linkList.append(URL)

linkListFinal = linkList

#print(linkListFinal)


print ("Number of files to download %s", len(linkListFinal))
print ("Starting download....")

docList = [] # List of URL to the text documents
docNameList = [] # List of document names

# Get all the doc
for k in range(len(linkListFinal)):
    print str(linkListFinal[k])
    #What would this more properly be?
    requiredURL = str(linkListFinal[k])[0:(linkListFinal[k]).rfind("/")]
    xmldoc = requiredURL + "/form13fInfoTable.xml"
    #print xmldoc
    docname =xmldoc.split("/")[len(xmldoc.split("/"))-1]
#    print docname
    docList.append(xmldoc)
    docNameList.append(docname)

#From here, need to scrape the relevant XML files given the cik and the date.
    

#		try:
#			self.save_in_directory(companyCode, cik, priorto, docList, docNameList, '13-F')
#		except Exception,e:
#			print str(e)

#		print "Successfully downloaded all the files"
