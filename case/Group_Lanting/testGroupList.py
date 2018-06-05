#coding:utf-8
import requests,unittest
import common.login_lanting
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class Groupinfo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = common.login_lanting.auto_login_by_UID()  #auto_login_by_UID返回的token
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

    def test_group_info(self):
        u'圈子的列表记录接口'
        self.log.info('开始测试按分页获取圈子的列表记录接口')
        url = 'http://api.sns.sunnycare.cc/v1/group/records'
        json_data = {"token":self.auto_login_token,
                     "time":0,"page":1
                     }
        #try:

        r = self.s.post(url,headers = self.header,json=json_data)
        print(self.log.info('返回的内容是：%s' % r.json()))
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        #except requests.exceptions.ConnectionError as e:
           # pass

        self.log.info('圈子列表接口测试结束！')

    def test_group_info2(self):
        u'圈子的列表记录第二页'
        self.log.info('开始测试按分页获取圈子的列表记录接口2')
        url = 'http://api.sns.sunnycare.cc/v1/group/records'
        json_data = {"token":self.auto_login_token,
                     "time":0,"page":2
                     }
        #try:

        r = self.s.post(url,headers = self.header,json=json_data)
        print(self.log.info('返回的内容是：%s' % r.json()))
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        #except requests.exceptions.ConnectionError as e:
           # pass

        self.log.info('圈子列表接口3测试结束！')

    def test_group_info3(self):
        u'圈子的列表记录,page为空'
        self.log.info('开始测试按分页获取圈子的列表记录接口3')
        url = 'http://api.sns.sunnycare.cc/v1/group/records'
        json_data = {"token":self.auto_login_token,
                     "time":0,"page":''
                     }
        #try:

        r = self.s.post(url,headers = self.header,json=json_data)
        print(self.log.info('返回的内容是：%s' % r.json()))
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        #except requests.exceptions.ConnectionError as e:
           # pass

        self.log.info('圈子列表接口3测试结束！')

    def tearDown(self):
        self.s.close()



if __name__=='__main__':
    unittest.main(warnings='ignore')
