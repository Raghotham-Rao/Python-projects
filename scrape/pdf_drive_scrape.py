from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib
import json

# initializing the driver
driver = webdriver.Chrome('/home/raghu/chromedriver')

driver.get('https://www.pdfdrive.com/')
sleep(2)

branch_topics = {"CSE":['python', 'Web development', 'java'], "EC": ['analog circuits', 'communication systems', 'circuit design'], "ME":['Fluid Mechanics', 'Thermodynamics', 'Automobile Engineering']}

for branch in branch_topics:
	search_box = driver.find_element_by_id('q')
	for topic in branch_topics[branch]:
		search_box.send_keys(topic)
		search_box.send_keys(Keys.ENTER)
		books_list = driver.find_elements_by_class_name("ai-search")
		url = driver.current_url
		print(len(books_list))
		for book in books_list[1:]:
			book.click()
			sleep(1)
			author = driver.find_elements_by_class_name('card-author')[0].find_element_by_tag_name('span').text
			print(author)
			# driver.get(url)
			break
		break
	break

print('done')
driver.close()