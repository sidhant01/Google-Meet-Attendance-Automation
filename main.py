from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import CHROME_PROFILE_PATH
from pygame.time import Clock
import time
import sys

# enter the number of seconds after which you want to start looking for the meet link
time.sleep(<enter time>)

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get('https://web.whatsapp.com')

time.sleep(5)

try:
	driver.find_element_by_xpath('//span[@title="<enter group/contact name>"]').click()
except:
	driver.quit()
	sys.exit()

clock = Clock()

def sendMessage(message):
	chatButton = WebDriverWait(driver, 600).until(
		EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Chat with everyone"]'))
		)

	chatButton.click()

	time.sleep(2)
	textarea = driver.find_element_by_xpath('//textarea[@jsname="YPqjbf"][@aria-label="Send a message to everyone"]')
	textarea.send_keys(message + Keys.ENTER)

def joinMeet(link):

	driver.get(link)
	time.sleep(10)

	try:
		driver.find_element_by_xpath('//div[@aria-label="Turn off camera (ctrl + e)"]').click()
		driver.find_element_by_xpath('//div[@aria-label="Turn off microphone (ctrl + d)"]').click()
	except:
		driver.quit()
		sys.exit()

	joinXPATH = '//span[@class="NPEfkd RveJvd snByac"][text()="Join now"]'
	askXPATH = '//span[@class="NPEfkd RveJvd snByac"][text()="Ask to join"]'
	joined = false

	if (driver.findElement(By.XPATH(joinXPATH)).size() != 0):
		driver.find_element_by_xpath(joinXPATH).click()
		joined = True
	elif (driver.findElement(By.XPATH(askXPATH)).size() != 0):
		driver.find_element_by_xpath(askXPATH).click()
		joined = True

	if !joined:
		driver.quit()
		sys.exit()


while True:

	clock.tick(4)

	messages = driver.find_elements_by_xpath('//div[@class="_1Gy50"]')
	recent = messages[-1].text

	if 'meet.google.com' in recent:

		joinMeet(recent)
		sendMessage("2K19/CO/378")
		
		break

# enter the number of seconds for which you want to attend the meet
time.sleep(<enter time>)
driver.quit()