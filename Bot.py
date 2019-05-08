# coding: utf-8

###	MARKETWATCH BOT CLASS	###


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from contextlib import contextmanager
import time



class MarketWatchBot:
    
    def __init__(self, username, password, game_name, chromedriver_path):
        #INITIALIZES BOT
        self.username = username
        self.password = password
        self.game_name = game_name
        self.logged_in = False
        self.driver = webdriver.Chrome(chromedriver_path)
        

    def login(self):
        #LOGS BOT INTO MARKET WATCH USING GIVEN CREDENTIALS
        self.driver.get("https://www.marketwatch.com/login")
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_id("password")
        username.send_keys(self.username)
        time.sleep(1)
        password.send_keys(self.password, Keys.RETURN)
        time.sleep(5)
        self.logged_in = True
        self.driver.get("https://www.marketwatch.com/game/" + self.game_name + "/portfolio")

        
        
    #METHODS BELOW RETURN DIFFERENT VALUES OF RELEVANCE
        
    def getNetWorth(self):
        if(self.logged_in):
            net = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/ul/li[1]/span")
            return(getInnerHTML(net))


    def getCashRemaining(self):
        if(self.logged_in):
            cash = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/ul/li[5]/span")
            return(getInnerHTML(cash))


    def getTodaysGains(self):
        if(self.logged_in):
            gains = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/ul/li[2]/span")
            return(getInnerHTML(gains))

    def getOverallReturns(self):
        if(self.logged_in):
            returns = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[2]/ul/li[4]/span")
            return(getInnerHTML(returns))
        
def getInnerHTML(html):
    #GETS CONTENT INSIDE AN HTML CONTAINER
    html_content = html.get_attribute('innerHTML')
    return html_content.strip()


