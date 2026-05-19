from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.ActionChains.by import 

driver = webdriver.Chrome()

driver.get("https://otzdarva.com/")

print(driver.title)
# print(driver)
Character = driver.find_element( By.XPATH'//*[@id="navbar"]/div/div[2]/div[1]/div/button')
Info = driver.find_element(By.XPATH'//*[@id="navbar"]/div/div[2]/div[1]/div/div/a[1]')
hover = ActionChains (driver).move_to_element(Character)
hover.perform()
time.sleep(1)
Info.click()


time.sleep(5)

driver.quit()jd