from form_bot import FormBot
from olx_scraper import OLXScraper

OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"


scraper = OLXScraper(OLX_URL)
scraper.get_listings()
scraper.get_links()
scraper.get_prices()
scraper.get_addresses()
