from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://www.baidu.com")

driver.find_element_by_id('kw').send_keys('自动化测试')
driver.find_element_by_xpath('//*[@id="su"]').click()

#driver.find_element_by_link_text("抗击肺炎")。click()
#driver.find_element_by_link_text("抗击肺炎")。click()

 
#导入selenium 
from selenium import webdriver

#打开浏览器
driver = webdriver.Chrome(executable_path="chromedriver.exe")

#访问网址
driver.get("http://www.baidu.com")

#操作元素
#id定位
driver.find_element_by_id("kw").send_keys("自动化测试")
driver.find_element_by_id("su").click()

#name定位
# driver.find_element_by_name("wd").send_keys("自动化测试")

#classname定位
# driver.find_element_by_classname("s_ipt").send_keys("自动化测试")

#xpath
# driver.find_element_by_xpath("//*[@id="kw"]").send_keys("自动化测试")

#css_selector
# driver.find_elements_by_css_selector("#kw").send_keys("自动化测试")



 