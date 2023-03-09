from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSekeWndUp3RzGgcjjXngAlDLkCd9GQhOZKO7mAHf3Y_vbtndg/viewform"


class FormBot:
    def __init__(self, service, chrome_options):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def complete_form(self):
        self.driver.get(FORM_URL)


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open!
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())

bot = FormBot(service, chrome_options)
bot.complete_form()
