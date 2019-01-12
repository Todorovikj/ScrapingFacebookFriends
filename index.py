from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os
import requests
import shutil
from xlsxwriter import Workbook

# advice: use delays to avoid getting blocked, try torrequest for changing your IP
# driver.switch_to.window(driver.window_handles[1]) changig active tab in driver chrome
chromePath="D:\\neco skola i rabota\\rabota\\learning dollars\\ChromeDriver\\chromedriver"
# scrolling to bottom of window self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

class App:
    def __init__(self,username="leposava.10.02.1941@gmail.com",password='WebScraper'):
        self.username=username
        self.password=password
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver=webdriver.Chrome("D:\\neco skola i rabota\\rabota\\learning dollars\\ChromeDriver\\chromedriver",chrome_options=chrome_options)
        self.driver.get("https://facebook.com")
        self.error=False

        self.logIn()

        if self.error is False:
            self.driver.get("https://www.facebook.com/mathew.stirland/friends?lst=708685132%3A509902370%3A1546973221")

        sleep(2)

        if self.error is False:
            self.scrollDown()

        sleep(2)


        print("Scraper has finished scraping!!!")
        input("stop for test")
        self.driver.close()



    def scrollDown(self):
        try:
            for i in range(200):
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                sleep(3)
        except Exception:
            print("Problem with scrolling down")
            self.error=True

    def logIn(self):
        try:
            sleep(1)
            mail=self.driver.find_element_by_xpath("//input[@type='email']")
            password=self.driver.find_element_by_xpath("//input[@type='password']")
            mail.send_keys(self.username)
            password.send_keys(self.password)
            password.submit()
            sleep(2)
        except Exception:
            print("problem logging in")
            self.error=True





if __name__=='__main__':
    app=App()


