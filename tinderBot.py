from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class TinderBot():
    def __init__(self,email,password):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.tinder.com")
        self.makeLogin(email,password)
    def makeLogin(self,email,password):
        # Accept the cookies of website
        WebDriverWait(self.driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button'))
            ).click()
        # Login with email and password
 
        if 'gmail' in email : # it is a gmail type email 
            WebDriverWait(self.driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button'))
            )
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button').click()
            tinderNormalWindow = self.driver.window_handles[0]
            gmailLogInWindow = self.driver.window_handles[1]
            self.driver.switch_to_window(gmailLogInWindow)
            self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/span').click()
            WebDriverWait(self.driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
            self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/span').click()
            time.sleep(30)
            self.driver.switch_to_window(tinderNormalWindow)
        else: # It is a different email type, tries to log in with facebook  
            WebDriverWait(self.driver, 20).until(
                 EC.element_to_be_clickable((By.XPATH, ''))
            ).click()
            