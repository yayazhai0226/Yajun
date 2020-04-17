import os


base_path = "C:\\Users\\SNake\\VSCodeProjects\\ljtest202003\\PytestTest\\"
os.popen("cd /d {}".format(base_path))
os.popen("call pytest case --alluredir=result")
os.popen("allure generate result -o report --clean")
os.popen("allure open -h 127.0.0.1 -p 10086 report")








