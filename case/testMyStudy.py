#coding:utf-8
import requests
import unittest
from common.login import LG
import time
class Mystudy(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
    def test_mystudy(self):
        u'测试我的学习接口'
        url = 'http://api.lesson.sunnycare.cc/v1/learns'
        json_data = {"token":self.uid_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'])
    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()

