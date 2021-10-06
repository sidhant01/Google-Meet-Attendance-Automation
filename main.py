from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import CHROME_PROFILE_PATH
from pygame.time import Clock
import time

# enter the number of seconds after which you want to start looking for the meet link
time.sleep(<enter time>)

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://web.whatsapp.com')

time.sleep(5)
driver.find_element_by_xpath('//span[@title="<enter group/contact name>"]').click()

clock = Clock()

while True:

	clock.tick(4)

	messages = driver.find_elements_by_xpath('//div[@class="_1Gy50"]')
	recent = messages[-1].text

	if 'meet.google.com' in recent:
		driver.get(recent)
		time.sleep(5)
		driver.find_element_by_xpath('//div[@aria-label="Turn off camera (ctrl + e)"]').click()
		driver.find_element_by_xpath('//div[@aria-label="Turn off microphone (ctrl + d)"]').click()
		driver.find_element_by_xpath('//span[@class="NPEfkd RveJvd snByac"][text()="Join now"]').click()
		time.sleep(3)
		driver.find_element_by_xpath('//button[@aria-label="Chat with everyone"]').click()
		time.sleep(2)
		textarea = driver.find_element_by_xpath('//textarea[@jsname="YPqjbf"][@aria-label="Send a message to everyone"]')
		textarea.send_keys("<enter-your-roll-number>" + Keys.ENTER)
		break

# enter the number of seconds for which you want to attend the meet
time.sleep(<enter time>)
driver.quit()