import pytest
from selenium import webdriver

def test_01_goods():
    driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
    driver.get("http://132.232.44.158:9999/shopxo/")
    driver.maximize_window()

    goods_name = driver.find_element_by_xpath('//*[@id="floor1"]/div[2]/div[2]/div[1]/div/div/a').text
    assert goods_name == 'MARNI Trunk 女士 中号拼色十字纹小牛皮 斜挎风琴包'
"""
    这是生成、编译、打开测试报告的3个命令
    pytest --alluredir=result
    allure generate result -o report --clean
    allure open -h 127.0.0.1 -p 10086 report
"""



