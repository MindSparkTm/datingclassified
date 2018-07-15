import requests
import urllib2
from bs4 import BeautifulSoup as soup
udata = urllib2.urlopen('https://www.sportpesa.co.ke/?sportId=1')
htmlsource = udata.read()
ssoup = soup(htmlsource,'html.parser')
file = open("file.txt","wb") #open file in binary mode
file.writelines(htmlsource)
file.close()

