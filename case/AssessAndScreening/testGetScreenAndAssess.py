#coding:utf-8
import unittest,requests
from common.logger import Log
from common.login_lanting import auto_login_by_UID
import time
from common.Excel import Excel_util

class Screening(unittest.TestCase):
    '''
    这是获取筛查价格的接口
    '''
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

    def test_screening_price(self):
        u'获取筛查价格接口'
        self.log.info('开始测试筛查价格接口！')
        url = 'http://api.rih.sunnycare.cc/API/V1/UserAssessRecord/screeninfo'
        json_data = {
            "token":self.auto_login_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('筛查价格返回内容是：%s' % r.json())
        try:
            self.assertEqual(200,r.json()['code'])
        except Exception as e:
            print(e)
            raise AssertionError

        self.log.info('筛查价格接口测试结束!')

    def test_get_report01(self):
        '查看我的筛查/评估报告列表'
        self.log.info('测试查看评估筛查报告列表接口：')
        url = 'http://api.rih.sunnycare.cc/API/V1/UserAssessRecord/getUserAssessRecordByUserID'
        json_data = {
            "token": self.auto_login_token,
            "timestamp": int(time.time()),
            "page": 1
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('评估筛查报告接口返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        #取出报告id写入excel
        id = r.json()['data']['content'][0]['local_id']
        self.excel.write_value(17,6,id)
        self.log.info('查看评估筛查报告接口测试结束！')


    def test_get_assess_count(self):
        u'获取可用评估次数接口'
        self.log.info('测试可用评估次数接口:')
        url = 'http://api.rih.sunnycare.cc/API/V1/UserAssessRecord/assesscount'
        json_data = {
            "token": self.auto_login_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('评估次数返回结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('可用评估次数接口测试结束！')

    def test_Assess_price(self):
        u'获取评估价格接口'
        self.log.info('开始测试评估价格接口：')
        url = 'http://api.rih.sunnycare.cc/API/V1/UserAssessRecord/assessinfo'
        json_data = {
            "token": self.auto_login_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('评估价格返回的结果是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('评估价格接口测试结束')

    def test_get_report02(self):
        u'查看评估/筛查详情接口'
        self.log.info('查看评估/筛查详情接口')
        url = 'http://api.rih.sunnycare.cc/API/V1/UserAssessRecord/getUserAssessRecord'
        #读取报告id作为入参
        read_id = self.excel.read_value(17,6)
        json_data = {
            "token": self.auto_login_token,
            "id": read_id
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('查看报告详情返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('查看评估/筛查详情接口结束！！')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

