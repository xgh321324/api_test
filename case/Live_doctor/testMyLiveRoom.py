#coding:utf-8
import time,requests,unittest
from common.login import LG
from common.logger import Log
from common.Hash import get_digit,get_sign

class MyRoom(unittest.TestCase):

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

    def test_my_live_room(self):
        u'我的直播间接口'
        self.log.info('我的直播间接口测试开始..')
        url = 'http://api-live.sunnycare.cc/v1/room/mine'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        try:
            self.assertEqual(200,r.json()['code'])
            self.assertEqual('请求成功',r.json()['note'])
            self.log.info('我的直播间接口返回的结果是：%s' % r.json())
        except Exception:
            raise AssertionError
        self.log.info('我的直播间接口测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()


