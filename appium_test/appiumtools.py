from selenium.webdriver.support.ui import WebDriverWait

# 这是咱们自定写的方法，不是selenium带的方法
def find_element(driver, locator, timeout=10):
    """
        方法名：diy查找元素
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - find_element_by_id：("id", "value") find_element_by_id > resource_id
                    - find_element_by_xpath：("xpath", "value")
                    - find_element_by_accessibility_id：("aid", "value")
                    - find_element_by_android_uiautomator：("text", "Search")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错
    """
    if locator[0] == "aid":
        locator = ("accessibility id", locator[1]) # locator:appium能够识别
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))

    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))



def assert_element_exist(driver, locator, timeout=10):
    """
        方法名：判断元素是否存在
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - find_element_by_id：("id", "value") find_element_by_id > resource_id
                    - find_element_by_xpath：("xpath", "value")
                    - find_element_by_accessibility_id：("aid", "value")
                    - find_element_by_android_uiautomator：("text", "Search")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：true
            - 没找到元素：false
    """
    try:
        find_element(driver, locator, timeout=10)
        return True
    except:
        return False