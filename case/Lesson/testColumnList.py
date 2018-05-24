#coding:utf-8
import requests
import unittest
from common.login import LG
import time
from common.Excel import Excel_util
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class ColumnList(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.EXCEL = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
        self.log = Log()

    def test_ColumnList(self):
        u'测试专栏列表接口'
        self.log.info('开始测试专栏列表接口....')
        url = 'https://api.lesson.wrightin.com/v1/spe/list'
        json_data = {"timestamp":str(time.time()),"token":self.uid_token}
        r = self.s.post(url,headers = self.header,json=json_data,verify=False)
        self.EXCEL.write_value(4,5,r.json())

        self.assertEqual('请求成功.',r.json()['note'])
        data = r.json()['data']
        content = data['list'] #专栏列表的内容
        self.assertTrue(len(content) >= 1,msg='专栏列表为空，肯定有问题！')

        spe_codes = {}
        n = 1
        for i in r.json()['data']['list']:
            spe_codes['spe_code'+ str(n)] = i['spe_code']
            n += 1
        self.EXCEL.write_value(4,6,(spe_codes))
        self.log.info('专栏列表接口测试结束！！')


    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()
