import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # 显示等待：找元素的时候给点时间

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://132.232.44.158:9999/shopxo/")


driver.find_element_by_id('search-input').send_keys("纽芝兰") # 在输入框搜索纽芝兰
driver.find_element_by_id('ai-topsearch').click()               # 点击搜索按钮
# time.sleep(5)       # 等待之后，再去找元素
# driver.implicitly_wait(10) # 网页在5秒钟加载完成，节约测试时间，超时继续执行执行

# 显示等待
e = ("xpath", '/html/body/div[4]/div/ul/li/div/a/p')        # e是一个元祖，(定位方式, 定位方式的值)
a = WebDriverWait(driver, 10).until(lambda s: s.find_element(*e)) # 找打了就返回元素的对象，如果超时还没有找到，就直接报错
print(a.text)
assert a.text == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'

# 要去判断的内容：功能正常内容的
# e = driver.find_element_by_xpath('/html/body/div[4]/div/ul/li/div/a/p')
# assert e.text == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'