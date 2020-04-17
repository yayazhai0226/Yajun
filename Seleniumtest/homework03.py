import time
from selenium import webdriver
from seleniumtools import find_element

#后台添加商品
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html")

username = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[1]/input')
password = ('xpath', '/html/body/div[1]/div/div[2]/div/form/div/div[2]/input')
loginbtn = ('xpath','/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
goodsmag = ('xpath','//*[@id="admin-offcanvas"]/div/ul/li[6]/a/span[2]')
goodslist = ('xpath','//*[@id="power-menu-38"]/li[1]/a')
goodsadds = ('xpath','/html/body/div[1]/div/div/a')
frameobj = ('id', 'ifcontent')                      # iframe元素
goodstitle = ('xpath', '//*[@id="goods-nav-base"]/div[1]/div/input[2]')# 
goodsbrief = ('xpath', '//*[@id="goods-nav-base"]/div[2]/input')                      # iframe元素
goodsmodel = ('xpath', '//*[@id="goods-nav-base"]/div[3]/input')                      # iframe元素
goodsclass = ('xpath', '//*[@id="goods-nav-base"]/div[4]/div/ul')                      # iframe元素
goodsclass_01 = ('xpath', '//*[@id="goods-nav-base"]/div[4]/div/div/ul/li[3]')
goodsbrand = ('xpath', '//*[@id="goods-nav-base"]/div[5]/div/a/span')                      # iframe元素
goodsbrand_01 = ('xpath', '//*[@id="goods-nav-base"]/div[5]/div/div/ul/li[3]')                      # iframe元素
goods_prod_addr = ('xpath', '//*[@id="goods-nav-base"]/div[6]/div/a/span')                      # iframe元素
goods_prod_addr_01 = ('xpath', '//*[@id="goods-nav-base"]/div[6]/div/div/ul/li[2]')                      # iframe元素
goodsunit = ('xpath', '//*[@id="goods-nav-base"]/div[7]/input')                      # iframe元素
goods_buy_disc = ('xpath', '//*[@id="goods-nav-base"]/div[8]/input')                      # iframe元素
goods_mix_buy = ('xpath', '//*[@id="goods-nav-base"]/div[9]/input')                      # iframe元素
goods_max_buy = ('xpath', '//*[@id="goods-nav-base"]/div[10]/input')                      # iframe元素
goods_pic_upload = ('xpath', '//*[@id="goods-nav-base"]/div[11]/div')                      # iframe元素
goods_pic_upload_01 = ('xpath', '//*[@id="tabhead"]/span[2]')                      # iframe元素
goods_pic_upload_02 = ('xpath', '//*[@id="rt_rt_1e5favdo9kca120ue6v1qoo75d1"]/label')                      # iframe元素


goods_pic_choose = ('xpath', '//*[@id="rt_rt_1e5f9khhv1aa4ilnv3u1aib14bj1"]/label')                      # iframe元素
goods_first_pic_upload = ('xpath', '//*[@id="goods-nav-base"]/div[11]/div')                      # iframe元素
goods_reduce = ('id', 'ifcontent')                      # iframe元素
goods_visual = ('id', 'ifcontent')                      # iframe元素
goods_reccomend = ('id', 'ifcontent')

goods_price = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[1]/input')
goods_count = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[2]/input')
goods_weight = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[3]/input')
goods_specifications = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[4]/input')
goods_bar_code = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[5]/input')
goods_original_price = ('xpath', '//*[@id="goods-nav-operations"]/div/table/tbody/tr/td[6]/input')

goods_pictrues = ('id', 'ifcontent')
goods_vidio = ('id', 'ifcontent')
goods_save = ('xpath', '/html/body/div[1]/div/form/div[9]/button')


find_element(driver, username).send_keys("admin")   # 输入用户名
find_element(driver, password).send_keys("shopxo")  # 输入密码
find_element(driver, loginbtn).click()              # 点击登录
find_element(driver, goodsmag).click()
find_element(driver, goodslist).click()
driver.switch_to_frame(find_element(driver, frameobj))  # 把作用域切换到小网页
find_element(driver, goodsadds).click()
find_element(driver, goodstitle).send_keys('出租女朋友')
find_element(driver, goodsbrief).send_keys('很漂亮')
find_element(driver, goodsmodel).send_keys('一位')
find_element(driver, goodsclass).click()
find_element(driver, goodsclass_01).click()
find_element(driver, goodsbrand).click()
find_element(driver, goodsbrand_01).click()
find_element(driver, goods_prod_addr).click()
find_element(driver, goods_prod_addr_01).click()
find_element(driver, goodsunit).send_keys('2')
find_element(driver, goods_buy_disc).click()
find_element(driver, goods_mix_buy).click()
find_element(driver, goods_max_buy).click()
find_element(driver, goods_first_pic_upload).click()
find_element(driver, goods_first_pic_upload_01).click()
find_element(driver, goods_first_pic_upload_02).click()

find_element(driver, goods_price).send_keys('998')
find_element(driver, goods_count).send_keys('2')
find_element(driver, goods_specifications).send_keys('123456')
find_element(driver, goods_bar_code).send_keys('123456')
find_element(driver, goods_original_price).send_keys('1998')
find_element(driver, goods_save).click()



time.sleep(6)
driver.quit()



















 