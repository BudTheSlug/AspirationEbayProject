import time
from selenium import webdriver
from selenium.webdriver import ActionChains

#This test is a check of carousel buttons

driver = webdriver.Firefox()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

categoryexpand = driver.find_element_by_id('gh-shop-a')
categoryexpand.click()


subcategoryitem = driver.find_element_by_xpath('//*[@id="gh-sbc"]/tbody/tr/td[3]/ul[2]/li[3]/a')
subcategoryitem.click()

categoryshop = driver.find_element_by_xpath('//*[@id="mainContent"]/section[3]/div[2]/a[10]/div[1]/img')
categoryshop.click()

sidebuttonright = driver.find_element_by_xpath('//*[@id="w10-xCarousel-next"]')
action = ActionChains(driver)
action.move_to_element(sidebuttonright)

i = 0
while i <= 3:
    sidebuttonright.click()
    i += 1

sidebuttonleft = driver.find_element_by_xpath('//*[@id="w10-xCarousel-previous"]')
action = ActionChains(driver)
action.move_to_element(sidebuttonleft)

j = 0
while j <= 3:
    sidebuttonleft.click()
    j += 1

time.sleep(4)

driver.close()

