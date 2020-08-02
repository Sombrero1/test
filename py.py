import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
       r=urllib.request.urlopen(self.site)
       html=r.read()
       parser="html.parser"
       s=BeautifulSoup(html, parser)
       for tag in s.find_all("a"):
           url = tag.get("href")
           if url is None:
               continue
           if "http" in url:
               print("\n" + url)
        
            

       
       
news = "https://pythonru.com/baza-znanij/ustanovka-pip-dlja-python-i-bazovye-komandy"
Scraper(news).scrape()

