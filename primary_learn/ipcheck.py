
def ip_check(str) :
    res = str.split('.')
    for i in res :
        if len(res) == 4 :
            try :
                i = int(i)
                if  i >= 0 and i <= 255 :
                    return 'ip地址正确!'
                else :
                    return 'ip地址错误！'               
            except :
                return 'ip地址错误！'               
        else : 
            return 'ip地址错误!'        

a = input('请输入IP地址：')
print(ip_check(a))






