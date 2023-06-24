from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SaskenMarbles:
    def test(self):
        BaseURL="https://sakshingp.github.io/assignment/login.html"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(3)
        
        driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('qawingify')
        driver.find_element(By.ID,'password').send_keys('qawingify')
        driver.find_element(By.ID,'log-in').click()

        driver.find_element(By.ID,'amount').click()
        table=driver.find_element(By.ID,'transactionsTable')
        # print(table.text())
        print("Amount are sorted")


obj=SaskenMarbles()
obj.test()