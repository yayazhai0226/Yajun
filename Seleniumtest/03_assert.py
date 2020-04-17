import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.baidu.com/")
driver.find_element_by_id('kw').send_keys("自动化测试")
driver.find_element_by_id('su').click()

time.sleep(3)
# assert driver.title == "自动化测试_百度搜索."

# url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&rsv_t=5580foecI4cusjTE%2B0zyhrqyA%2BpdcCP30jPsyYvBP6tF6fXfeSeZ%2F2k7Stw&rsv_enter=0&rsv_dl=tb&rsv_sug3=5&inputT=180&rsv_sug4=181"
# assert driver.current_url == url

print("搜索成功！")

