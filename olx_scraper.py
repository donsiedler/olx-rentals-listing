import requests
from bs4 import BeautifulSoup


class OLXScraper:
    def __init__(self, url):
        self.response = requests.get(url).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.listings = None

    def __str__(self):
        return f"Found {len(self.listings)} listings."

    def get_listings(self):
        self.listings = self.soup.findAll(name="div", class_="css-1sw7q4x", attrs={"data-cy": "l-card"})

    def get_link(self, listing):
        url = listing.find(name="a", class_="css-rc5s2u")["href"]
        if url[0] == "/":
            url = f"https://olx.pl{url}"
        return url

    def get_price(self, listing):
        try:
            price = listing.find(name="p", class_="css-10b0gli").text
        except AttributeError:
            price = "n/a"
        return price

    def get_address(self, listing):
        address = listing.find(name="p", class_="css-veheph", attrs={"data-testid": "location-date"})
        address = address.text.split("-")[0].rstrip()
        return address
