import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#This test will is a quick search and enter test for the searchbar

driver = webdriver.Firefox()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

searchbox = driver.find_element_by_id('gh-ac')
searchbox.clear();
searchbox.send_keys("funko");
searchbox.send_keys(Keys.RETURN);

time.sleep(4)

driver.close()

