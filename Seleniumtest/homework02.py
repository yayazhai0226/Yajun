import time
from selenium import webdriver
from seleniumtools import find_element
from seleniumtools import assert_element_exist

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://132.232.44.158:9999/shopxo/admin.php")

username = ('name', 'username')
password = ('name', 'login_pwd')
loginbtn = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
usermana = ('xpath', '//*[@id="admin-offcanvas"]/div/ul/li[5]/a/span[2]')
userlist = ('xpath', '//*[@id="power-menu-126"]/li[1]/a/span')
useradds = ('xpath', '/html/body/div[1]/div/div/a[1]')
frameobj = ('id', 'ifcontent')                      # iframe元素

find_element(driver, username).send_keys("admin")   # 输入用户名
find_element(driver, password).send_keys("shopxo")  # 输入密码
find_element(driver, loginbtn).click()              # 点击登录
find_element(driver, usermana).click()              # 点击用户管理
find_element(driver, userlist).click()              # 点击用户管理
print(driver.current_url)

# e = driver.find_element_by_id('ifcontent')
# driver.switch_to_frame(e)
driver.switch_to_frame(find_element(driver, frameobj))  # 把作用域切换到小网页
find_element(driver, useradds).click()              # 点击用户新增

print(driver.current_url)

driver.switch_to_default_content()      # 切换到默认作用域：把作用域切换到大网页
find_element(driver, usermana).click()              # 点击用户管理

time.sleep(4)
driver.quit()