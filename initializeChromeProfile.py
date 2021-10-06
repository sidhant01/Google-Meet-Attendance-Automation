from selenium import webdriver
from config import CHROME_PROFILE_PATH

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://web.whatsapp.com')