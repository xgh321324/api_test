#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
class Tickets(unittest.TestCase):


    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
        self.header = {'User-Agent':  'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding':  'gzip, deflate',
                       'Accept-Language':  'zh-Hans-CN;q=1',
                       'Content-Type':  'application/json',
                       'requestApp':  '3',
                       'requestclient':  '2',
                       'versionForApp':  '2.0',
                       'Authorization':  'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection':  'keep-alive'}
        self.log = Log()#实例化日志的类

    def test_tickets(self):
        u'我的会议门票接口'
        self.log.info('开始测试会议门票接口！')
        url = 'http://api.meet.sunnycare.cc/v2/ticket/mine'
        json_data = {
            "token":self.uid_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('会议门票返回的结果是：%s' % r.json())
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('会议门票接口测试结束！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
