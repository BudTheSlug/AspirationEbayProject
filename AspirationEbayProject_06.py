import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from locators import Locator
from homepage import Home
from signinpage import SignIn

#This test is a to use page objects and locators

driver = webdriver.Chrome()

driver.implicitly_wait(10)
#This wait is merely to visually verify the code runs correctly and to account for any internet slowness

driver.get("https://www.ebay.com/")

signinlink = Home(driver)
signinlink.sign_in
signinlink.getSignIn().click()

signinusername = SignIn(driver)
signinusername.username
signinusername.getUsername().send_keys("testuser")

signinpassword = SignIn(driver)
signinpassword.password
signinpassword.getPassword().send_keys("password123")

signinsubmitbutton = SignIn(driver)
signinsubmitbutton.submitbutton
signinsubmitbutton.getSubmitButton().click()

time.sleep(4)
driver.close()
