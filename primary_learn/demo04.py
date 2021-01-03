import dbtools 
# 也可以导入方法：from dbtools import chaxun
from dbtools import chaxun
# 如果封装了类，也可以： from dbtools import Db
from dbtools import Db

db = Db('59.110.143.227','root','1qaz!QAZ','test')
a = db.chaxun('show tables ;')
print(a)

