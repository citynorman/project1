import urllib2

from pageScraper import PageScraper

URLS = ["http://www.sec.gov/Archives/edgar/data/872573/000087257315000003/form13fInfoTable.xml",
        "http://www.sec.gov/Archives/edgar/data/1574886/000142050615000171/Form13F_InfoTable.xml"]
DATES = ['2015-02-13',
         '2015-02-17'] #For testing. Need to have this provided somehow.


dateIndex = 0
ps = PageScraper()

for eachUrl in URLS:

    ps.scrape(eachUrl, DATES[dateIndex])
    dateIndex += 1
pass
