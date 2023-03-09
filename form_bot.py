import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps the browser open!
chrome_options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())


class FormBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def complete_form(self, url, listing_address, listing_price, listing_url):
        self.driver.get(url)

        time.sleep(1)  # Wait for the form to load

        # Locate inputs
        address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                           '2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
        url_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                       '2]/div/div[1]/div/div[1]/input')
        submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        # Fill out the form and submit
        address_input.send_keys(listing_address)
        price_input.send_keys(listing_price)
        url_input.send_keys(listing_url)
        submit_btn.click()
