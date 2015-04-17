import pandas as pd

#wget ftp://ftp.sec.gov/edgar/full-index/2015/QTR1/master.zip
#unzip master.zip
#=> delete extra header lines to read in pandas
#wget ftp://ftp.sec.gov/edgar/full-index/2015/QTR2/master.zip
#unzip master.zip
#=> delete extra header lines to read in pandas

data=pd.read_csv(r'C:\UBS\Dev\Temp\master.idx',sep='|')
data['ftplink']='ftp://ftp.sec.gov/'+data['Filename']

data_13f=data.ix[(data['Form Type']=='13F-HR') | (data['Form Type']=='13F-HR/A')]
#funds=data_13f['Company Name'].unique()

data_13f[data_13f['Company Name'].str.contains("OCONNOR")]
data_13f[data_13f['Company Name'].str.contains("CAXTON ASSOCIATES")]
data_13f[data_13f['Company Name'].str.contains("MILLENNIUM CAPITAL")]
data_13f[data_13f['Company Name'].str.contains("Point72 Asset Management")] #SAC
data_13f[data_13f['Company Name'].str.contains("Bridgewater Associates")]
data_13f[data_13f['Company Name'].str.contains("Marshall Wace")]


#http://stackoverflow.com/questions/11573817/how-to-download-a-file-via-ftp-with-python-ftplib
import ftplib

fh=open('test-13f.txt')
for link in data_13f['ftplink'].ix[data_13f['Company Name'].str.contains("OCONNOR")]:
    print link

#ftp.retrbinary('RETR %s' % filename, file.write)
