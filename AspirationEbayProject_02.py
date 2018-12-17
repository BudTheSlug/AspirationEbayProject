import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#This test is a check of the category dropdown selector

driver = webdriver.Firefox()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

categorybox = Select(driver.find_element_by_xpath('//*[@id="gh-cat"]'))
#I understand that xpath is not an ideal element locator, but wanted to include it for demonstration
categorybox.select_by_value("220")
#This will bring up the toys and hobbies page

searchbutton = driver.find_element_by_id("gh-btn")
searchbutton.click()

time.sleep(4)

driver.close()
