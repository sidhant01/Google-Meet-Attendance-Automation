from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pygame.time import Clock
from datetime import datetime
from datetime import timedelta
import re
import config
import time
import sys

def any_of(*expected_conditions):
    def any_of_condition(driver):
        for expected_condition in expected_conditions:
            try:
                result = expected_condition(driver)
                if result:
                    return result
            except Exception:
                pass
        return False
    return any_of_condition


def joinMeet(link):
	driver.get(link)
	print('heehe')
	joinXPATH = '//span[@class="NPEfkd RveJvd snByac"][text()="Join now"]'
	askXPATH = '//span[@class="NPEfkd RveJvd snByac"][text()="Ask to join"]'
	try:
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Turn off camera (ctrl + e)"]'))).click()
		print('here')
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Turn off microphone (ctrl + d)"]'))).click()
		WebDriverWait(driver, 20).until(
			any_of(EC.element_to_be_clickable((By.XPATH, joinXPATH)), 
				EC.element_to_be_clickable((By.XPATH, askXPATH)))).click()
	except Exception as e:
		print(e)
		driver.quit()
		sys.exit()


def sendMessage(message):
	WebDriverWait(driver, 300).until(
		EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Chat with everyone"]'))).click()
	textArea = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located(
			(By.XPATH, '//textArea[@jsname="YPqjbf"][@aria-label="Send a message to everyone"]')))
	textArea.send_keys(Message + Keys.ENTER)


def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


CHROME_PROFILE_PATH = config.CHROME_PROFILE_PATH
Duration = int(config.Duration)
GroupName = config.GroupName
Message = config.Message

WhatsappRefreshTime = 20

options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')

try:
	WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"][@data-tab="3"]'))).send_keys(GroupName)
	WebDriverWait(driver, 20).until(
		EC.presence_of_element_located(
			(By.XPATH, '//span[@class="matched-text i0jNr"][text()="{}"]'.format(str(GroupName))))).click()
except Exception as e:
	print(e)
	driver.quit()
	sys.exit()
	
clock = Clock()

messageArea = driver.find_element_by_xpath('//div[@role="textbox"][@data-tab="9"]')

n = Duration//WhatsappRefreshTime + 1
startTime = datetime.now()
timeStamps = [(startTime + timedelta(minutes=WhatsappRefreshTime*x)) for x in range(1, n+1)]
i = 0

while True:

	clock.tick(4)

	now = datetime.now()

	if i == n:
		driver.quit()
		sys.exit()

	if now >= timeStamps[i] and "web.whatsapp.com" in driver.current_url:
		messageArea.send_keys("time is " + now.strftime("%H:%M:%S") + ", ")
		i += 1

	messages = driver.find_elements_by_xpath('//div[@class="_1Gy50"]')
	recent = messages[-1].text

	if "meet.google.com" in recent:
		link = Find(recent)[0]
		joinMeet(link)

		if Message != None:
			sendMessage(Message)

		break

time.sleep(Duration * 60)
driver.quit()