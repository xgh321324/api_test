#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
urllib3.disable_warnings()

class Report(unittest.TestCase):
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
    @unittest.skip('no reson')
    def test_report01(self):
        u'举报渟说接口'
        self.log.info('测试举报接口-参数正确')
        url = 'http://api.sns.sunnycare.cc/v1/report'
        json_data = {
            "token":self.auto_login_token,
            "id":"P00001",
            "category":"G",
            "text":"天天"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('参数正确返回结果是：%s' % r.json())
        #self
        self.log.info('举报接口-参数正确情况测试结束！\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


