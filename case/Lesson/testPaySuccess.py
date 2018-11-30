#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
from common.Hash import get_digit,get_sign

class Test_pay(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
        self.header = {'User-Agent': 'okhttp/3.8.1',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '1',
                       'versionForApp': '2.5.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        self.log = Log()

    def test_pay01(self):
        u'测试支付接口,已购买的课程，去支付'
        self.log.info('开始测试支付接口,已购买的课程再次支付')
        url = 'http://api.pay.sunnycare.cc/v1/pay'
        json_data = {"token":self.uid_token,
                     "pay_method":"1",
                     "product_type":"2",
                     "product_code":"K00134",
                     "timestamp":str(time.time()),
                     "nonce": get_digit()
                     }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        global out_trad_num   #设置为全局变量供下一case调用
        out_trad_num= r.json()['data']
        #print(out_trad_num)
        #global order_id
        #order_id = r.json()['data']['order_id']
        self.assertEqual('您已购买 不能重复购买.',r.json()['note'])
        self.log.info('支付接口,已购买的课程再次支付 测试结束')

    def test_pay02(self):
        u'测试支付接口,未购买的课程，去支付'
        self.log.info('开始测试支付接口,未购买的课程，去支付')
        url = 'http://api.pay.sunnycare.cc/v1/pay'

        json_data = {
            "pay_method":"1",
            "product_type":"2",
            "token":self.uid_token,
            "product_code":"K00129",
            "timestamp": str(time.time()),
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        global out_trad_num   #设置为全局变量供下一case调用
        out_trad_num= r.json()['data']
        self.assertEqual('请求成功.',r.json()['note'],msg='支付请求状态没成功')
        self.log.info('支付接口,未购买的课程，去支付测试结束')


    def test_pay_suc01(self):
        u'测试支付后的确认接口（已支付的orderid）'
        self.log.info('测试支付后的确认接口（已支付的orderid）')
        url = 'http://api.pay.sunnycare.cc/v1/success'

        json_data = {
            'order_id': '201811220310400201118252',
            'token': self.uid_token,
            'timestamp': str(time.time()),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers=self.header,json=json_data)
        self.log.info('返回：%s'% r.json())
        self.assertEqual(200,r.json()['code'],msg=('支付的orderid，支付确认接口有问题'))
        self.log.info('支付后的确认接口（已支付的orderid）测试结束')
    @unittest.skip('no reason')
    def test_pay_suc02(self):
        u'测试支付后的确认接口（未支付的orderid）'
        self.log.info('测试支付后的确认接口（未支付的orderid）')
        url = 'http://api.pay.sunnycare.cc/v1/success'

        json_data = {
            'order_id': '2018112309061402011185001',
            'token': self.uid_token,
            'timestamp': str(time.time()),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers=self.header,json=json_data)
        self.log.info('返回：%s'% r.json())
        self.assertEqual(502,r.json()['code'])
        self.assertEqual('订单未支付成功.',r.json()['note'])

        self.log.info('支付后的确认接口（未支付的orderid）测试结束')

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()
