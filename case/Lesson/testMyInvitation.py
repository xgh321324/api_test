#coding:utf-8
import requests,time
from common.login import LG
from common.logger import Log
import unittest

class MyInvitation(unittest.TestCase):
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
        self.log = Log()

    def test_my_invitation(self):
        u'测试我的邀请接口'
        self.log.info('--------开始测试我的邀请接口--------')
        url = 'https://api.lesson.wrightin.com/v1/invite/mine'
        json_data = {
            "token":self.uid_token,
            "time":""
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        try:
            self.assertEqual('请求成功.',r.json()['note'])
            self.assertEqual(200,r.json()['code'])
            self.log.info('我的邀请接口请求成功！')
        except Exception as e:
            print(e)
            self.log.error('我的邀请接口请求失败，原因：%s' % e)

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()
