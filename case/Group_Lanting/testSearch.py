#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
urllib3.disable_warnings()

class Search(unittest.TestCase):
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

    def test_search01(self):
        u'测试搜索接口'
        self.log.info('搜索接口-参数正常')
        url = 'http://api.sns.sunnycare.cc/v1/search'
        json_data = {"keyword":"爱",
                     "token":self.auto_login_token,
                     "page":1
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('搜索结果返回是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('搜索接口-参数正常情况测试结束！\n')

    def test_search02(self):
        u'测试搜索接口-搜索内容不存在'
        self.log.info('搜索接口-搜索内容不存在')
        url = 'http://api.sns.sunnycare.cc/v1/search'
        json_data = {"keyword":"asdjas",
                     "token":self.auto_login_token,
                     "page":1
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('搜索结果返回是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        #断言结果content为空
        self.assertFalse(r.json()['data']['content'])
        self.log.info('搜索接口-搜索内容不存在情况测试结束！\n')

    def test_search03(self):
        u'测试搜索接口-搜索内容为空'
        self.log.info('搜索接口-搜索内容为空')
        url = 'http://api.sns.sunnycare.cc/v1/search'
        json_data = {"keyword":'',
                     "token":self.auto_login_token,
                     "page":1
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('搜索结果返回是：%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        self.assertEqual('keyword 的长度要求为 1 - 20.',r.json()['note'])
        #断言结果content为空
        #self.assertFalse(r.json()['data']['content'])
        self.log.info('搜索接口-搜索内容为空情况测试结束！\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()