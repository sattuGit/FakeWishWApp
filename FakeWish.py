'''
URLs : 	https://github.com/zvovov/whatsapp-web/blob/bc2041fed5883e2dc6a5a9e65baba4ae970c9056/chat.py#L31
	https://www.geeksforgeeks.org/whatsapp-using-python/
	https://stackoverflow.com/questions/49831933/eliminate-entering-qr-whatsapp-web-automated-by-selenium-java
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('./chromedriver_linux64/chromedriver_2.44')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"AnoopShukla"'

# Replace the below string with your own message
string = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
print(x_arg)
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
print(group_title)
group_title.click()
inp_xpath = '//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"][@dir="ltr"]'
#<div class="_3u328 copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div>

input_box = wait.until(EC.presence_of_element_located((
	By.XPATH, inp_xpath)))
print(input_box)
for i in range(10):
	input_box.send_keys('test automation' + Keys.ENTER)
	print(i)
	time.sleep(1)
