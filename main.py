from form_bot import FormBot
from olx_scraper import OLXScraper

OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSekeWndUp3RzGgcjjXngAlDLkCd9GQhOZKO7mAHf3Y_vbtndg/viewform"

scraper = OLXScraper(OLX_URL)
scraper.get_listings()
scraper.get_links()
scraper.get_prices()
scraper.get_addresses()
print(scraper)

bot = FormBot()
bot.complete_form(FORM_URL)

