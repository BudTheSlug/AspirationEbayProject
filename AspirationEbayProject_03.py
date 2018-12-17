import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#This test scrolls to an element to select

driver = webdriver.Firefox()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

funkodeal = driver.find_element_by_xpath('//*[@id="events_list1"]/div[2]/div[1]/div/div/ul/li[3]/a/div[1]/div/div')
action = ActionChains(driver)
action.move_to_element(funkodeal)
funkodeal.click()

time.sleep(4)

driver.close()
