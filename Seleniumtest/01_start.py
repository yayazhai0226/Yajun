#导入selenuium（固定式）
from selenium import webdriver

#打开浏览器（固定式）
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
#访问网址（固定式）
driver.get("http://www.baidu.com/")

#操作元素（去输入框输入内容，点击按钮.）
# e = driver.find_element_by_id("kw")
# e.send_keys("自动化测试")
#id 定位
driver.find_element_by_id("kw").send_keys("自动化测试")
#name定位
# driver.find_element_by_name("wd").send_key("自动化测试")

# classname定位
# driver.find_element_by_class_name("s_ipt").send_keys("zisonghguaceshi")

# xpath 定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("自动化测试")
    















