"""
    pytest组织selenium测试用例
        py文件的测试用例;分隔不同类型的测试用例——比如：按照功能模块（业务模块）来划分
"""
# 第一步导入pytest
import pytest
from selenium import webdriver

# 自己写一个方法作为第一个测试用例。（自动化测试case）
# @pytest.mark.skip(reason="input your skip reason")
def test_01_hellopytest():
    print("你好")
    print("pytest")

# @pytest.mark.skip(reason="input your skip reason")
def test_02_selenium():
    driver = webdriver.Chrome(executable_path='driver\\chromedriver.exe')
    driver.get("http://132.232.44.158:9999/shopxo/")
    driver.maximize_window()
    driver.find_element_by_id('search-input').send_keys("包包")
    driver.find_element_by_id('ai-topsearch').click()
    driver.implicitly_wait(10)

    result = '/html/body/div[4]/div/ul/li/div/a/p'
    assert driver.find_element_by_xpath(result).text == '纽芝兰包包女士2018新款潮百搭韩版时尚单肩斜挎包少女小挎包链条'
    driver.quit()








