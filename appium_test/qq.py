from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '6.0.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'MuMu'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.tencent.mobileqq'       # app的名字：
desired_caps['appActivity'] = '.activity.LoginActivity'              # 同上↑
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
desired_caps['noReset'] = True                          # 使用缓存
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)