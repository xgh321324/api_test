#coding:utf-8
import time,requests,unittest
from common.login import LG
from common.logger import Log
from common.Hash import get_digit,get_sign

class Invite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.lgin = LG(cls.s) #实例化
        cls.uid_token = cls.lgin.login()
        cls.header = {
            'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Type': 'application/json',
            'requestApp': '3',
            'requestclient': '2',
            'versionForApp': '2.4.0',
            'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
            'Connection': 'keep-alive'
        }
        cls.log = Log() #实例化日志的类

    def test_invite_gust01(self):
        u'主持人邀请嘉宾接口-嘉宾不存在'
        self.log.info('邀请嘉宾接口-嘉宾不存在 测试开始...')
        url = 'http://api-live.sunnycare.cc/v1/live/invite'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'live_code': 'L2018091982508',
            'phone': '13816541144',
            'nonce': get_digit()
        }
        json_data['sign']= get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('邀请嘉宾返回结果是：%s' % r.json())
        self.assertEqual(203,r.json()['code'])
        self.assertEqual('平台不存在该用户',r.json()['note'])
        self.log.info('邀请嘉宾接口-嘉宾不存在 测试结束！\n')

    def test_invite_gust02(self):
        u'主持人邀请嘉宾接口-嘉宾存在'
        self.log.info('邀请嘉宾接口-邀请自己 测试开始...')
        url = 'http://api-live.sunnycare.cc/v1/live/invite'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'live_code': 'L2018091982508',
            'phone': '15651797525',
            'nonce': get_digit()
        }
        json_data['sign']= get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('邀请邀请自己返回结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('邀请嘉宾接口-邀请自己 测试结束！\n')

    def test_invite_gust03(self):
        u'主持人邀请嘉宾接口-嘉宾存在'
        self.log.info('邀请嘉宾接口-嘉宾存在 测试开始...')
        url = 'http://api-live.sunnycare.cc/v1/live/invite'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'live_code': 'L2018091982508',
            'phone': '18351928060',
            'nonce': get_digit()
        }
        json_data['sign']= get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('邀请嘉宾返回结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('邀请嘉宾接口-嘉宾存在 测试结束！\n')

if __name__=='__main__':
    unittest.main()



