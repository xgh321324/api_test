#coding:utf-8
import requests
import unittest
from common.login import LG
from common.logger import Log
class Test_pay(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
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
        self.log = Log()
    def test_pay(self):
        u'测试支付接口,已购买的课程，去支付'
        self.log.info('开始测试支付接口,已购买的课程，去支付')
        url = 'http://api.exam.wrightin.com/v1/mldProductPay'
        json_data = {"payType":"0",
                     "product_type":"2",
                     "token":self.uid_token,
                     "product_code":"K00112"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        global out_trad_num   #设置为全局变量供下一case调用
        out_trad_num= r.json()['data']
        #print(out_trad_num)
        #global order_id
        #order_id = r.json()['data']['order_id']
        self.assertEqual('请求成功.',r.json()['note'],msg='支付请求状态不是200')
        self.log.info('支付接口,已购买的课程，去支付测试结束')

    def test_pay02(self):
        u'测试支付接口,未购买的课程，去支付'
        self.log.info('开始测试支付接口,未购买的课程，去支付')
        url = 'http://api.exam.wrightin.com/v1/mldProductPay'

        json_data = {"payType":"0",
                     "product_type":"2",
                     "token":self.uid_token,
                     "product_code":"K00008"
                     }

        r = self.s.post(url,headers = self.header,json=json_data)
        global out_trad_num   #设置为全局变量供下一case调用
        out_trad_num= r.json()['data']
        self.assertEqual('请求成功.',r.json()['note'],msg='支付请求状态没成功')
        self.log.info('支付接口,未购买的课程，去支付测试结束')


    def test_pay_suc(self):
        u'测试支付后的确认接口（未支付的orderid）'
        self.log.info('测试支付后的确认接口（未支付的orderid）')
        url = 'http://api.exam.wrightin.com/v1/mldProductPaySucessReq'

        json_data = {"payType":"0",
                     "out_trade_no":"",
                     "token":self.uid_token,
                     "orderid":"309251BA4A7C9A2C95C0F0A908DD3D66"
                     }

        r = self.s.post(url,headers=self.header,json=json_data)
        self.log.info('返回：%s'% r.json())
        self.assertEqual(201,r.json()['code'],msg=('未支付的orderid，支付确认接口有问题'))
        self.log.info('支付后的确认接口（未支付的orderid）测试结束')
    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()
