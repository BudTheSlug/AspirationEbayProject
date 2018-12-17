from locators import Locator
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Home(object):

    def __init__(self, driver):
        self.driver = driver

    #homepage locator will just be sign on for test
        self.sign_in = driver.find_element(By.XPATH, Locator.sign_in)

    def getSignIn(self):
        return self.sign_in
