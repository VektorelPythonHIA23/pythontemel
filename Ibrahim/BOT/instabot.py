import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class InstaBot():
    def __init__(self, kullaniciadi,sifre,bekle):
         self.browser = webdriver.Firefox(executable_path=r"Driver\geckodriver02864.exe")
         self.kullaniciadi = kullaniciadi
         self.sifre = sifre
         self.bekle = bekle

    # def tarayiciAc(self):
    #     self.browser.get(r"https://www.instagram.com/")

    def beklet(self):
        time.sleep(self.bekle)


    def girisYap(self):
        self.browser.get(r"https://www.instagram.com/")
        self.beklet()
        epostagiris = self.browser.find_element_by_name("username")
        sifregiris = self.browser.find_element_by_name("password")
        epostagiris.send_keys(self.kullaniciadi)
        sifregiris.send_keys(self.sifre)
        sifregiris.send_keys(Keys.ENTER)
        self.beklet()
        devam = self.browser.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/div/div/div/button')
        devam.click()
        try:
            devam = self.browser.find_element_by_css_selector("button.aOOlW:nth-child(1)")
            devam.click()
        except:
            pass
        self.beklet()
    def takipEt(self,username):
        self.browser.get(rf"https://www.instagram.com/{username}/")
        self.beklet()
        takip = self.browser.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if takip.text != "":
            takip.click()
            time.sleep(2)
        else:
            print("Zaten Takipteyiz")


bot1 = InstaBot("vektorelpython23","vektorel2004",10)
bot1.girisYap()
bot1.takipEt("codumpython")
