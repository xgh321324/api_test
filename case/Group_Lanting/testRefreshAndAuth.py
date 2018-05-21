#coding:utf-8
import requests,unittest
from common.logger import Log
from common.login_lanting import auto_login_by_UID

class Refresh(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()

    def testRefresh(self):
        u'刷新视频授权接口'
        self.log.info('开始测试刷新视频授权接口....')
        url = 'https://api.sns.wrightin.com/v1/auth/extend'
        json_data = {"token":self.auto_login_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.log.info('刷新视频授权接口测试结束！！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
