"""
文件的读写：
"w" 写入
"a" 追加
"""

# text = input("请输入今天的心情：")
# with open("日记.txt","w",encoding = "utf8") as f:     #f  是file的意思；with open () as f:  是一个固定的写法
#     f.write(text)

import time

now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("F:\日记.txt","a",encoding = "utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("------------------------"+"\n")


"""
python 的制表符

\t  Tab的意思
\n  换行的意思

"""