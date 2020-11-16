import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot():
    def __init__(self, *args, **kwargs):
         self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver.exe")

    def tarayiciAc(self):
        self.browser.get(r"http://www.vektorelakademi.com")
        time.sleep(20)
InstaBot().tarayiciAc()