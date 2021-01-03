import yaml
import os

"""
print("\tPython")#\t表示空四个字符，也称缩进，相当于按一下Tab键
print("\nPython\nJAVA\nC++\nJavaScript\nC#")#\n表示换行，相当于按一下回车
print("languages:\n\tPython\n\tJAVA\n\tC++\n\tJavaScript\n\tC#")#\n\t表示换行加每行空四格
"""
with open('data\\test_data.yml','rb') as f :
    data = yaml.safe_load(f)
    print(type(data))
    print(data)

    