import requests
from bs4 import BeautifulSoup


OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"


class OLXScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.listings = None
        self.links = []

    def get_listings(self):
        self.listings = self.soup.findAll(name="div", class_="css-1sw7q4x", attrs={"data-cy": "l-card"})
        print(len(self.listings))

    def get_links(self):
        for listing in self.listings:
            url = listing.find(name="a", class_="css-rc5s2u")["href"]
            if url[0] == "/":
                url = f"https://olx.pl{url}"
            self.links.append(url)
        print(self.links)

    def get_prices(self):
        pass

    def get_addresses(self):
        pass


scraper = OLXScraper(OLX_URL)
scraper.get_listings()
scraper.get_links()
