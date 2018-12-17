import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#This test is a multistep addition of an item to a cart and to check the cart

driver = webdriver.Chrome()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

searchbox = driver.find_element_by_id('gh-ac')
searchbox.clear();
searchbox.send_keys("funko");
searchbox.send_keys(Keys.RETURN);

gotofirstitem = driver.find_element_by_xpath('//*[@id="srp-river-results-listing1"]/div/div[1]/div/a/div/img')
gotofirstitem.click()

addtocartbutton = driver.find_element_by_id('atcRedesignId_btn')
addtocartbutton.click()

webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

checkcart = driver.find_element_by_id('gh-cart-i')
checkcart.click()

time.sleep(4)

driver.close()
