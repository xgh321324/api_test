#coding:utf-8
import unittest,requests
from common.logger import Log
from common.login_lanting import auto_login_by_UID
import urllib3

urllib3.disable_warnings()

class Add_Group(unittest.TestCase):
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

    def test_add_group(self):
        u'加入圈子接口'
        self.log.info('测试加入圈子接口之数据正常')
        url = 'http://api.sns.sunnycare.cc/v1/group/add'
        json_data = {
                    "token": self.auto_login_token,
                    "group_id": "G00001"
                    }
        r = self.s.post(url,headers = self.header,json=json_data)

        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('加入圈子成功.',r.json()['note'])
        self.log.info('加入圈子接口之数据正常情况测试结束！')

    def test_add_group2(self):
        u'加入圈子接口'
        self.log.info('测试加入圈子接口之group-id为空')
        url = 'http://api.sns.sunnycare.cc/v1/group/add'
        json_data = {
                    "token": self.auto_login_token,
                    "group_id": ''
                    }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回状态码：%s' % r.status_code)
        self.assertEqual(500,r.status_code)
        self.log.info('加入圈子接口之group-id情况为空测试结束！')

    def test_add_group3(self):
        u'加入圈子接口'
        self.log.info('测试加入圈子接口之group-id不存在')
        url = 'http://api.sns.sunnycare.cc/v1/group/add'
        json_data = {
                    "token": self.auto_login_token,
                    "group_id": 'G90001'
                    }
        r = self.s.post(url,headers = self.header,json=json_data)
        #print(r.json())

        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        self.assertIn('不存在.',r.json()['note'])
        self.log.info('加入圈子接口之group-id不存在情况测试结束！')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
