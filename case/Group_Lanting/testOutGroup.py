#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class Group(unittest.TestCase):
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

    def test_out_group(self):
        u'退出圈子接口-参数正确'
        self.log.info('退出圈子接口-参数正确')
        url = 'http://api.sns.sunnycare.cc/v1/group/out'
        json_data = {"token":self.auto_login_token,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是:%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('退出圈子成功.',r.json()['note'])
        self.log.info('退出圈子接口-参数正确情况测试结束\n')

    def test_out_group2(self):
        u'退出圈子接口-参数groupid不存在'
        self.log.info('退出圈子接口-roupid不存在')
        url = 'http://api.sns.sunnycare.cc/v1/group/out'
        json_data = {"token":self.auto_login_token,
                     "group_id":"G10000"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是:%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        #self.assertEqual('退出圈子成功.',r.json()['note'])
        self.log.info('退出圈子接口-roupid不存在情况测试结束\n')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main(warnings='ignore')

