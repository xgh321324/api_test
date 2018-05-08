#coding:utf-8
import hashlib
import random
import string

def get_str():
    #随机生成32位字符串的方法
    '''
    x = string.ascii_letters
    print('x:',x)
    #将0-9赋值
    y = string.digits
    print('y:',y)
    z = x+y
    print('z:',z)

    '''

    s = ''.join(random.sample(string.ascii_letters+string.digits,32))
    #print(s)
    return s

def get_md5(target):
    u'传入参数，将此参数进行MD5加密'
    m = hashlib.md5()  #创建Md5对象
    m.update(target.encode('utf-8')) #生成加密串，其中target是要加密的字符串
    result = m.hexdigest()
    #print(result)
    return result

if __name__ == '__main__':
    #get_md5(get_str())
    get_str()

