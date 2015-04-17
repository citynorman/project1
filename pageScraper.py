from bs4 import BeautifulSoup
from bs4 import Tag

import urllib2
import MySQLdb

from dataSheetItem import DataSheetItem

class PageScraper ():


    def scrape(self, url, holdingDate): #Change this name to reportDate.

        holdingCompanyCIK = url.split("/")[6] #This is the CIK number via which the company is identified in the EDGAR database.

        page = urllib2.urlopen(url)

        soup = BeautifulSoup (page.read(), "xml")

        entries = soup.findAll('infoTable')

        #dsi = DataSheetItem() #This should be done VERY differently, though Python init's are different from Java/etc. constructors.

        # Open database connection
        db = MySQLdb.connect("localhost","testuser","password","mytestdb")


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
            otherManager = entry.find('otherManager')
            soleVotingAuthority = entry.find('Sole') #This is a bit of a hack.
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
                dsi.saveToDB(db) #Not the most efficient way to deal with database connections!
            except Exception, e:
                print str(e)
                print("Failed to save to DB.")

                # disconnect from server
        db.close()
                   
