import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com/")


sz = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(sz).perform() # 一定要掉perform()

time.sleep(3)

driver.find_element_by_link_text('搜索设置').click()

time.sleep(4)
ptint('')


