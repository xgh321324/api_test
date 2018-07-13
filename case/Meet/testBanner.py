#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
class Banner(unittest.TestCase):

    def setUp(self):

        self.header = {
            'RequestClient': '1',
            'RequestApp': '3',
            'VersionForApp': '2.1.0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.0.0.13547',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': '55',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        self.log = Log()#实例化日志的类

    def test_banner(self):
        u'首页banner接口'
        self.s = requests.session()
        lgin = LG(self.s) #实例化登录类
        uid_token = lgin.gettoken_loginbyUID() #直接取第二部登录
        url = 'http://api.meet.sunnycare.cc/v2/banner'
        json_data = {
            "token": uid_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        #self.assertEqual(200,r.json()['code'])
        d = r.json()['data']
        #取出链接,打开，判断状态码
        print(d)

        links = [x['link'] for x in d]
        for n in links:
            re = self.s.get(n)
            self.assertEqual(200,re.status_code,msg='这个链接有问题'+n+'!')

        #取出图片链接,打开，判断状态码
        image_links = [x['image'] for x in d]
        for y in links:
            re = self.s.get(y)
            self.assertEqual(200,re.status_code,msg='这个链接有问题'+n+'!')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

    

