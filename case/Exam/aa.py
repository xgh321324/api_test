#coding:utf-8
import json
import time
import datetime
s = {
      "action": "44803",
      "account": "1865998xxxx",
      "uniqueid": "00D7C889-06A0-426E-BAB1-5741A1192038",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    }
for x in s.items():
    print(x)

t = time.ctime()
print(t)
today = datetime.date.today()
print(today)
print('======================')

j = ''
if j == True:
    print('9999')
else:
    print('0000')

print('=============================')

def buid_person(first_naem,last_name,age=''):
    person = {'first':first_naem,'last':last_name}
    if age:
        person['age'] = age
    else:
        pass
    return person
a = buid_person('许','广会',age='99')
print(a)

print('=====================')
unread = ['iphone case','robot case','panda case']
completed = []
while unread:
    current = unread.pop()
    print(current)
    completed.append(current)
print('completed:',completed)
print('=============================================')
import string
import random
#将a-z大写和小写赋值
x = string.ascii_letters
print('x:',x)
#将0-9赋值
y = string.digits
print('y:',y)
z = x+y
print('z:',z)
print('=====================================')
import hashlib
#md5加密需要导入hashlib模块
n = ''.join(random.sample(string.ascii_letters+string.digits,32))
print('n:',n)
m = hashlib.md5() #创建Md5对象
m.update(n.encode('utf-8')) #生成加密串，其中n是要加密的字符串
result = m.hexdigest() #经过md5加密的字符串赋值
print('结果是：',result)
print('==============================')
import random
x = random.randint(0,9)#在此范围内生成随机整数
print(x)
print('哈哈',random.random())#生成随机小数
L = ['你好','你不好','我不好','他不好']#再次列表中随机选择一个
y = random.choice(L)
print('yy',y)

print('======================================')
import unittest
class A(unittest.TestCase):
    def test01(self):
        x = self.assertEqual(2,2)
        print(x)

    def test02(self):
        y = self.assertTrue(2>1)
        print(y)
if __name__ == '__main__':
    unittest.main()

print('====================')


