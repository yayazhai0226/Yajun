'''
读日记
'''
with open('日记.txt','r',encoding = 'utf8') as f :  #文件路路径（可以绝对路径，也可以相对路径）以及文件名，w写入（a追加）（r读取），编码是utf8
    text = f.readlines()
for i in text :
    print(i)














