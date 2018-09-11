#coding:utf-8
import hashlib
import random
import string


#下面的几个方法都是用于澜渟app中接口的加密

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
    #random.sample()  从中随机选择多少长度的值
    #print(s)
    return s

def get_digit():
    u'随机生成32位数字的方法'
    d =''.join(random.sample(string.digits,8))
    d1 = ''.join(random.sample(string.digits,8))
    d2 = ''.join(random.sample(string.digits,8))
    d3 = ''.join(random.sample(string.digits,8))
    final_d = d + d1 +d2 + d3
    #print(type(final_d))
    #print(final_d)
    return final_d

def get_md5(target):
    u'传入参数，将此参数进行MD5加密'
    m = hashlib.md5()  #创建Md5对象
    m.update(target.encode('utf-8')) #生成加密串，其中target是要加密的字符串
    result = m.hexdigest()
    #print(result)
    return result

def get_sha1(target):
    u'传入参数，将此参数进行SHA1加密'
    m = hashlib.sha1() #创建sha1对象
    m.update(target.encode('utf-8'))
    result = m.hexdigest()
    print(result)
    return result

def phone_nember():
    u'随机产生合法格式的手机号码'
    pre_list = [
        "130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"
    ]
    num = random.choice(pre_list) + ''.join(random.sample(string.digits,8))
    #print(num)
    return num

#API签名算法
def get_sign(t):
    #t是一个字典
    result = sorted(t.items(),key = lambda x:x[0],reverse=False)
    #print(result)
    target2 = ''
    for i in result:
        #将键值对拼接
        target1 = i[0]+'='+i[1]+'&'
        target2 += target1
    #print(target2)
    #拼接密钥
    target3 = target2+'secret=BCy94HkqITdAJDCPhw9Sjd6TwLoV8igR'
    #print(target3)
    #MD5加密
    target4 = get_md5(target3)
    #转换为大写
    target5 = target4.upper()
    #print(target5)
    return target5

if __name__ == '__main__':
    get_digit()



