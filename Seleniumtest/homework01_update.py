import time
from selenium import webdriver
from seleniumtools import find_element
from seleniumtools import assert_element_exist

# 1. 打开网址
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()    # 把浏览器最大化
driver.get("http://132.232.44.158:9999/shopxo/")


# 2. 把元素的定位方式先收集起来，再去调用自己封装的方法
search_input = ('id', 'search-input')
search_buttn = ('id', 'ai-topsearch')
search_result = ("xpath", '/html/body/div[4]/div/ul/li/div/a/p')

find_element(driver, search_input).send_keys("纽芝兰")
find_element(driver, search_buttn).click()
# 这种断言是可以的
result = find_element(driver, search_result).text
assert result == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'
print(result)
# 如果出现只需要判断元素是否存在
# assert assert_element_exist(driver, search_resul) is True
# title = driver.title
# print(title)

find_element(driver, search_result).click()


# 切换window
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[0])

time.sleep(4)
# title = driver.title
# print(title)
driver.quit() # 退出测试