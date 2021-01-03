
import time 
from selenium import webdriver

#打开网址
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("http://www.baidu.com/")

#输入查找字符
driver.find_element_by_id("kw").send_keys('陈冠希')
driver.find_element_by_id("su").click()

#等几秒
time.sleep(5)

#多个元素查找
e = driver.find_element_by_class_name("opr-recommends-merge-mask")
print("----------------------")
print(e)
print("----------------------")
e.click()


