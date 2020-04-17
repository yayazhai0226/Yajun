import time
from selenium import webdriver
from seleniumtools import find_element
from seleniumtools import assert_element_exist
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://132.232.44.158:9999/shopxo/index.php?s=/index/user/logininfo.html")

cookies = {'domain': '132.232.44.158', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'fc1e7l94siqumtj10s4bpbicu7'}

driver.add_cookie(cookies)
driver.refresh()

# 手动登录，然后获取到cookie
# 以后每一次使用都带上已经登录的cookie
# time.sleep(20)
# print(driver.get_cookies())
# driver.quit()
