import requests
from bs4 import BeautifulSoup


OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"


class OLXScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.listings = None
        self.links = []
        self.prices = []
        self.addresses = []

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
        for listing in self.listings:
            try:
                price = listing.find(name="p", class_="css-10b0gli").text
            except AttributeError:
                price = "n/a"
            self.prices.append(price)

    def get_addresses(self):
        for listing in self.listings:
            address = listing.find(name="p", class_="css-veheph", attrs={"data-testid": "location-date"})
            address = address.text.split("-")[0].rstrip()
            self.addresses.append(address)


scraper = OLXScraper(OLX_URL)
scraper.get_listings()
scraper.get_links()
scraper.get_prices()
scraper.get_addresses()
