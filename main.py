import requests
from bs4 import BeautifulSoup
from pprint import pprint

OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"


class OLXScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.listings = None

    def get_listings(self):
        listings = self.soup.findAll(name="div", class_="css-1sw7q4x")
        pprint(listings)
        print(len(listings))

    def get_links(self):
        pass

    def get_prices(self):
        pass

    def get_addresses(self):
        pass


scraper = OLXScraper(OLX_URL)
scraper.get_listings()
