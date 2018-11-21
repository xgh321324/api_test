#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
from common.Read_config import get_content
urllib3.disable_warnings()

class User(unittest.TestCase):
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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_user_info01(self):
        u'我的信息接口'
        self.log.info('开始测试我的信息接口')
        url = get_content('sns_base_url')+'/v1/user/info'
        json_data = {
            "token":self.auto_login_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('接口返回结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('我的信息接口测试结束\n')

    def test_user_info02(self):
        u'用户的信息的接口'
        self.log.info('开始测试用户的信息的接口')
        url = get_content('sns_base_url')+'/v1/user/record'
        json_data = {
            "token":self.auto_login_token,
            "user_id":"U00013"  #18851838039的user_id
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('用户信息返回的结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        self.assertTrue(r.json()['data'])
        self.log.info('用户的信息的接口测试结束\n')

    #def test_user_info03(self):
     #   u''

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

