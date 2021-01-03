#方法： 字符串拆解法
#把ip地址当作字符串，以.为分隔符分割，进行判断

import os , sys


def check_ip(ipaddr) :
    import sys
    addr = ipaddr.strip().split('.') # 去除前后的空格，再以‘.’切割IP地址为一个列表
    # print( addr )
    if len(addr) != 4 : #切割后列表必须有4个参数
        print('check ip address failed ! ')
        sys.exit()
    for i in range(4) :
        try :
            addr[i] = int(addr[i]) #每个参数必须为数字，否则校验失败
        except :
            print('check ip address failed !')
        if addr[i] <= 255 and addr[i] >= 0 : #每个参数值必须在0 - 255 之间
            pass
        else :
            print('check ip address failed !')
            sys.exit()
        i = i + 1
    else :
        print('check ip address success !')
if len(sys.argv) != 2 : #传参本身长度必须为2
    print('Example:%s 10.0.0.1 '%sys.argv[0]) 
    sys.exit()
else :
    check_ip(sys.argv[1])   #满足条件的，才进行调用检验IP函数


# a = ' 192.168.10.123   '
# addr = a.strip().split('.')
# print(addr)

