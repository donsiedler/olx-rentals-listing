import requests
from bs4 import BeautifulSoup

OTODOM_URL = "https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/wroclaw?ownerTypeSingleSelect=ALL&distanceRadius=0" \
             "&locations=%5Bcities_6-39%5D&viewType=listing&limit=72&page=1"


class OtodomScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")

    def get_links(self):
        pass

    def get_prices(self):
        pass

    def get_addresses(self):
        pass


scraper = OtodomScraper(OTODOM_URL)
