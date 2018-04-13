#coding:utf-8

import requests
import unittest
from common.login import LG
class Test_transaction(unittest.TestCase):
    def setUp(self):
        self.url = 'http://api.exam.wrightin.com/v1/orderHistory'
        self.s = requests.session()
        self.log_in = LG() #实例化
        self.log_in.login() #登录
        self.token=self.log_in.get_token() #取token
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive',
                       'Connection': 'keep-alive'}
    def test_transaction_0(self):
        u'测试交易记录接口(0:全部)'
        json_data = {'token':str(self.token),"is_invoices_req":"0"} #0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('全部：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']
        self.assertEqual(200,code,msg='返回的状态码不是200')
        self.assertEqual('请求成功.',n,msg='消息未请求成功')

    def test_transaction_1(self):
        u'测试交易记录接口(1:未申请发票)'
        json_data = {"token":str(self.token),"is_invoices_req":"1"}#0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('未申请发票返回：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']
        self.assertEqual(200,code,msg='返回的状态码不是200')
        self.assertEqual('请求成功.',n,msg='消息未请求成功')

    def test_transaction_2(self):
        u'测试交易记录接口(2:已经申请发票)'
        json_data = {"token":str(self.token),"is_invoices_req":"2"}#0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('已申请发票返回：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']
        self.assertEqual(200,code,msg='返回的状态码不是200')
        self.assertEqual('请求成功.',n,msg='消息未请求成功')
    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()