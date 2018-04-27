#coding:utf-8
import requests
import unittest
from common.login import LG
class Test_pay(unittest.TestCase):
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
                       'Connection': 'keep-alive'}
    def test_pay(self):
        u'测试支付接口'
        url = 'http://api.exam.wrightin.com/v1/mldProductPay'
        json_data = {"payType":"0","product_type":"2","token":self.uid_token,"product_code":"K00001"}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        global out_trad_num   #设置为全局变量供下一case调用
        out_trad_num= r.json()['data']['out_trade_no']
        global order_id
        order_id = r.json()['data']['order_id']
        self.assertEqual('请求成功.',r.json()['note'],msg='支付请求状态不是200')
    def test_pay_success(self):
        u'测试支付成功后的确认接口'
        url = 'http://api.exam.wrightin.com/v1/mldProductPaySucessReq'
        json_data = {"payType":"0","out_trade_no":"","token":self.uid_token,"orderid":""}
        r = self.s.post(url,headers=self.header,json=json_data)
        print(r.json())
    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()
