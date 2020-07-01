from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
from PIL import Image
import requests
from io import BytesIO
class TinderBot():
    def __init__(self,email,password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.tinder.com")
        self.waitTime = 15 # 15 seconds to wait the page load
        self.makeLogin(email,password)
        print('login sucessful')
    def waitElementToLoadAndClickByXPATH(self,XPATH):
         WebDriverWait(self.driver, self.waitTime).until(
                 EC.element_to_be_clickable((By.XPATH, XPATH))
        ).click()
    def makeLogin(self,email,password):
        # Accept the cookies of website
        self.waitElementToLoadAndClickByXPATH('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        # Login with email and password depending on the email
        try :
            if 'gmail' in email : # it is a gmail type email 
                self.gmailLogin(email,password)
            else: # It is a different email type, tries to log in with facebook  
                self.facebookLogin(email,password)
            #allow to use location
            self.waitElementToLoadAndClickByXPATH('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            # disable notifications
            self.waitElementToLoadAndClickByXPATH('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]') 
        except  Exception as e:
            print(f'The login attempt failed, excpetion: {e} ')
    def gmailLogin(self,email,password):
            self.waitElementToLoadAndClickByXPATH('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button').click()
            tinderNormalWindow = self.driver.window_handles[0]
            gmailLogInWindow = self.driver.window_handles[1]
            self.driver.switch_to_window(gmailLogInWindow)
            self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
            self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/span').click()
            self.waitElementToLoadAndClickByXPATH('//*[@id="password"]/div[1]/div/div[1]/input')
            self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/span').click()
            self.driver.switch_to_window(tinderNormalWindow)

    def facebookLogin(self,email,password):
            self.waitElementToLoadAndClickByXPATH('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            time.sleep(3)
            tinderNormalWindow = self.driver.window_handles[0]
            facebookLogInWindow = self.driver.window_handles[1]
            self.driver.switch_to_window(facebookLogInWindow)
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)            
            self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
            self.driver.switch_to_window(tinderNormalWindow)

    def like(self):
         self.waitElementToLoadAndClickByXPATH('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
    def dislike(self):
        self.waitElementToLoadAndClickByXPATH('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
    
    def getProfileImage(self):
        imageElement = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]/div/div') 
        completeImageString = imageElement.get_attribute('style')
        imageUrl = self._getURLFromStyle(completeImageString)
        return  self._getImageFromUrl(imageUrl)

     #Internal function   
    def _getImageFromUrl(self,imageUrl):
        response = requests.get(imageUrl)
        image = Image.open(BytesIO(response.content))
        return image
    #Internal function
    def _getURLFromStyle(self,completeImageString) :
        regularExpressionPattern = re.compile('(?<= url\(\")(.*)(?=\"\))')
        resultOfSearch = regularExpressionPattern.search(completeImageString)
        return   resultOfSearch[0]
       