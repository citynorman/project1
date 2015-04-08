from bs4 import BeautifulSoup
from bs4 import Tag

import urllib2

from dataSheetItem import DataSheetItem

class PageScraper ():

    def scrape(self, url, holdingDate): #Change this name to reportDate. The date needs to be provided.

        holdingCompanyCIK = url.split("/")[6] #This is the CIK number via which the company is identified in the EDGAR database.

        page = urllib2.urlopen(url)

        soup = BeautifulSoup (page.read(), "xml")

        entries = soup.findAll('infoTable')

        for entry in entries:
            #try:
            nameOfIssuer = entry.find('nameOfIssuer')
            titleOfClass = entry.find('titleOfClass')
            cusip = entry.find('cusip')
            valueInThousands = entry.find('value')
            shrsOrPrn = entry.find('sshPrnamt')
            shPrn = entry.find('sshPrnamtType')
            putCall = entry.find('putCall') #This may often be a None.
            investmentDiscretion = entry.find('investmentDiscretion')
            otherManager = entry.find('otherManager') #Most often a None.
            soleVotingAuthority = entry.find('Sole') 
            sharedVotingAuthority = entry.find('Shared')
            noneVotingAuthority = entry.find('None')
            #except:
            #print("Missing data item in xml file.")
            #continue
            dsi = DataSheetItem(
                holdingDate,
                holdingCompanyCIK,
                nameOfIssuer,
                titleOfClass,
                cusip,
                valueInThousands,
                shrsOrPrn,
                shPrn,
                putCall,
                investmentDiscretion,
                otherManager,
                soleVotingAuthority,
                sharedVotingAuthority,
                noneVotingAuthority
                )
            try:
                dsi.saveToDB() #Not the most efficient way to deal with database connections.
            except Exception, e:
                print str(e)
                print("Failed to save to DB.")
                
