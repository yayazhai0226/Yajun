from selenium.webdriver.support.ui import WebDriverWait

# 这是咱们自定写的方法，不是selenium带的方法
def find_element(driver, locator, timeout=10):
    """
        方法名：diy查找元素
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - ("id", "username")
                    - ("name", "username")
                    - ("class name", "username")
                    - ("xpath", "username")
                    - ("css selector", "username")
                    - ("link text", "username")
                    - ("partial link text", "username")
            timeout: 超时间时间，默认10
        返回值：
            - 找到元素：返回元素
            - 没找到元素：直接报错
    """
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))

def assert_element_exist(driver, locator, timeout=10):
    """
        方法名：判断元素是否存在
        参数：
            driver: 浏览器的句柄/把柄
            locator: 元素定位方式
                格式： 
                    - ("id", "username")
                    - ("name", "username")
                    - ("class name", "username")
                    - ("xpath", "username")
                    - ("css selector", "username")
                    - ("link text", "username")
                    - ("partial link text", "username")
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