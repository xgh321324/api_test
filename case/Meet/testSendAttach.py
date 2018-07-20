#coding:utf-8
import requests
import unittest
import time,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
class Meet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.s = requests.session()
        cls.lgin = LG(cls.s) #实例化登录类
        cls.uid_token = cls.lgin.login() #直接取第二部登录
        cls.header = {
            'RequestClient': '1',
            'RequestApp': '3',
            'VersionForApp': '2.1.0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.0.0.13547',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json; charset=utf-8',
            #'Content-Length': '55',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        cls.log = Log()#实例化日志的类
        cls.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_send_attach01(self):
        u'发送讲义到邮箱接口'
        self.log.info('发送讲义接口测试开始')
        url = 'http://api.meet.sunnycare.cc/v2/attach/email'
        json_data = {
            "token": self.uid_token,
            "attach_code": 'A2018072075966',
            "email": '970185127@qq.com',
            "timestamp":int(time.time())
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('发送讲义到邮箱返回：%s' % r.json())
        self.assertEqual('请求成功.', r.json()['note'])
        self.log.info('发送讲义接口测试结束！')

    def test_send_attach02(self):
        u'发送讲义到163邮箱接口'
        self.log.info('发送讲义接口测试开始')
        url = 'http://api.meet.sunnycare.cc/v2/attach/email'
        json_data = {
            "token": self.uid_token,
            "attach_code": 'A2018072075966',
            "email": '15651797525@163.com',
            "timestamp":int(time.time())
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('发送讲义到163邮箱返回：%s' % r.json())
        self.assertEqual('请求成功.', r.json()['note'])
        self.log.info('发送讲义接口测试结束！')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()

