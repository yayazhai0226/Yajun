
from selenium import webdriver


# 1. 打开网址
driver = webdriver.Chrome(executable_path='suwo\\case\\chromedriver.exe')
driver.maximize_window()    # 把浏览器最大化
driver.get("https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage")

# 2. 把元素的定位方式先收集起来，再去调用自己封装的方法
search_input = ('xpath', '/html/body/div[2]/form/div[2]/div[1]/input')
search_buttn = ('id', 'ai-topsearch')
search_result = ("xpath", '/html/body/div[4]/div/ul/li/div/a/p')














