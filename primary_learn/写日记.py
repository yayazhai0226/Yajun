import time
'''
python 的常见技巧科普
'''
'''
文件的读写
# '''
now = time.strftime('%y-%m-%d %H:%M:%S')
text = input('请输入今天的心情：')
with open('日记.txt','a',encoding = 'utf8') as f :  #文件路路径（可以绝对路径，也可以相对路径）以及文件名，w写入（a追加）（r读取），编码是utf8
    f.write(now+'\n')
    f.write(text+"\n")
    f.write('-------------------\n')

'''
python的制表符
\t  #空格
\n  #换行
'''
'''
关于时间
'''
