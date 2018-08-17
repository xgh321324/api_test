#coding:utf-8
import requests
import unittest

def denglu():
    u'登录系统'
    url = 'http://183.59.151.14:8080/restful/api/authentication'
    #登录的入参
    in_data = {
        'username': "sendi",
        'password': "2MDL010618",
      'appid':"HDC2054490406A"
    }
    #请求头部
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    s = requests.session()
    #发送请求
    r = s.post(url,headers = header,data = in_data)
    #print(r.json())
    #获取token
    t = r.json()['token']
    print('登录返回的token是：%s' % t)
    return t

if __name__== '__main__':
    denglu()
