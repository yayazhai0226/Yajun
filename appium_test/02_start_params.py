from appium import webdriver

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



# accessibility id
# driver.find_element_by_accessibility_id('Accessibility').click()

# xpath
# driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Accessibility"]').click()

# id： resource id：可能会重复
# driver.find_element_by_id('android:id/text1').click()


# 文本值定位
e = driver.find_element_by_android_uiautomator('new UiSelector().text("App")')
print(e.text) # 显示元素的文本
e.click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Search")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("Invoke Search")').click()
e = driver.find_element_by_id('io.appium.android.apis:id/txt_query_prefill')
e.send_keys('appiumn好棒啊~')
e.clear()
e.send_keys('appiumn好男啊~')
driver.back()

driver.quit()