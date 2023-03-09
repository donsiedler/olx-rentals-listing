import requests
from bs4 import BeautifulSoup


class OLXScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.listings = None
        self.links = []
        self.prices = []
        self.addresses = []

    def __str__(self):
        return (f"Found {len(self.listings)} listings. \n"
                f"Links ({len(self.links)}): {self.links} \n"
                f"Prices ({len(self.prices)}): {self.prices} \n"
                f"Addresses ({len(self.addresses)}): {self.addresses} \n")

    def get_listings(self):
        self.listings = self.soup.findAll(name="div", class_="css-1sw7q4x", attrs={"data-cy": "l-card"})

    def get_links(self):
        for listing in self.listings:
            url = listing.find(name="a", class_="css-rc5s2u")["href"]
            if url[0] == "/":
                url = f"https://olx.pl{url}"
            self.links.append(url)

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
