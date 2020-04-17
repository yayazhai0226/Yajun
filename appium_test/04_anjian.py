import time
from appium import webdriver
from appiumtools import find_element
from appiumtools import assert_element_exist


desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '6.0.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'MuMu'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
desired_caps['noReset'] = True                          # 使用缓存
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 返回桌面
# driver.back()
# driver.back()

driver.press_keycode(3)

# 滑动
for i in range(10):
    driver.swipe(205, 1006, 829, 989)
    time.sleep(1)
    driver.swipe(829, 989, 205, 1006)
    time.sleep(1)