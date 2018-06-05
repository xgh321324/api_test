#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class Detail(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()

    def test_group_details(self):
        u'圈子详情接口-参数正确'
        self.log.info('圈子详情接口-参数正确')
        url = 'http://api.sns.sunnycare.cc/v1/group/record'
        json_data = {"token":self.auto_login_token,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('圈子详情接口-参数正确情况测试结束！\n')

    def test_group_details2(self):
        u'圈子详情接口-无token'
        self.log.info('圈子详情接口-无token')
        url = 'http://api.sns.sunnycare.cc/v1/group/record'
        json_data = {#"token":self.auto_login_token,
                     "group_id":"G00008"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('圈子详情接口-无token情况测试结束！\n')



    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


