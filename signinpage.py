from locators import Locator
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SignIn(object):

    def __init__(self, driver):
        self.driver = driver

    #signin locators from locator.py
        self.username = driver.find_element(By.XPATH, Locator.username)
        self.password = driver.find_element(By.XPATH, Locator.password)
        self.submitbutton = driver.find_element(By.XPATH, Locator.submitbutton)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getSubmitButton(self):
        return self.submitbutton

