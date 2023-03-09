from form_bot import FormBot
from olx_scraper import OLXScraper

OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSekeWndUp3RzGgcjjXngAlDLkCd9GQhOZKO7mAHf3Y_vbtndg/viewform"

scraper = OLXScraper(OLX_URL)
scraper.get_listings()
print(scraper)

bot = FormBot()

for listing in scraper.listings:
    address = scraper.get_address(listing)
    price = scraper.get_price(listing)
    url = scraper.get_link(listing)
    print(url, price, address)
    bot.complete_form(FORM_URL, address, price, url)

