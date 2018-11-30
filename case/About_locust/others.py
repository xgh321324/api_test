#coding:utf-8
import requests,unittest

def chaxun():
    u'查询接口'
    s = requests.session()
    url = 'http://183.59.151.14:8080/restful/api/authentication'
    #登录的入参
    in_data = {
        'username': "sendi",
        'password': "2MDL010618",
        'appid':"HDC2054490406A"
    }
    #请求头部
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'keep-alive',
    }
    #发送请求
    r =s.post(url,headers = header,data = in_data)
    #获取token
    t = r.json()['token']
    print('登录返回的token是：%s' % t)



    #'信息查询接口'
    url_2 = 'http://183.59.151.14:8080/restful/api/custinfo'
    #请求头部
    header2 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'keep-alive'
    }
    #查询的入参
    in_data_2 = {
        'customer':'佛山威立雅垃圾填埋处理有限公司',
        'elecode':'IPCYW2267381990',
        'elename':'IPCYW2267381990',
        'NEName':'高明杨梅杨梅二楼综合机房01/S-T64G-1',
        'portName':'gei_4/8',
        'disabled':0,
        'is_vip':0,
        'page':1,
        'pagesize':10,
        'token':t
    }

    r1 = s.post(url_2,headers = header2,data = in_data_2)
    print(r1.json())
    t1 = r1.json()['token']
    print('查询返回的token是：%s' % t1)


    url_3 = 'http://183.59.151.14:8080/restful/api/custflow'

    # 请求头部
    header3 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'keep-alive'
    }
    # 登录的入参
    in_data_3 = {
        'customer': '广东丹姿集团有限公司',
        'elecode': 'IPCYW2270156401',
        'elename': 'IPCYW2270156401',
        'starttime': '2018061217',
        'endtime': '2018062418',
        'type': 0,
        'page': 1,
        'pagesize': 10,
        'token': t1
    }
    r3 = s.post(url_3, headers=header, data = in_data_3)
    print(r3.json())


if __name__=='__main__':
    chaxun()


