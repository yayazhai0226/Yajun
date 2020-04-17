import time
from selenium import webdriver
from seleniumtools import find_element
from seleniumtools import assert_element_exist
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://localhost:8080/test/")

kanwo = ('link text', '点我就送屠龙宝刀！')
sxd = ('link text', '点我就送251天免费套餐+10W！')
# find_element(driver, kanwo).click()


# driver.switch_to_alert().accept() # 点击确定


find_element(driver, sxd).click()
time.sleep(3)
driver.switch_to_alert().dismiss()