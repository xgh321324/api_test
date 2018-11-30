#coding:utf-8

import requests
import unittest
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util

class Test_transaction(unittest.TestCase):

    def setUp(self):
        #self.url = 'http://api.lesson.sunnycare.cc/v1/orderHistory' #测试环境接口地址
        self.url = 'http://api.exam.sunnycare.cc/v1/orderHistoryNew'
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
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

    def test_transaction_0(self):
        u'测试交易记录接口(0:全部)'
        json_data = {'token':self.uid_token,"is_invoices_req":"0"} #0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('全部：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']
        try:

            self.assertEqual(200,code,msg='返回的状态码不是200')
            self.assertEqual('请求成功.',n,msg='消息未请求成功')
        except Exception as e:
            pass

        #取出交易记录中的订单号
        order_no_list = r.json()['data']['list']
        L=[]
        for i in order_no_list:
            L.append(i['order_no'])


    def test_transaction_1(self):
        u'测试交易记录接口(1:未申请发票)'
        json_data = {"token":self.uid_token,"is_invoices_req":"1"}#0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('未申请发票返回：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']

        try:
            self.assertEqual(200,code,msg='返回的状态码不是200')
            self.assertEqual('请求成功.',n,msg='消息未请求成功')
        except Exception as e:
            pass

    def test_transaction_2(self):
        u'测试交易记录接口(2:已经申请发票)'
        json_data = {"token":self.uid_token,"is_invoices_req":"2"}#0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('已申请发票返回：%s' % r.json())
        code = r.json()['code']
        n = r.json()['note']

        try:
            self.assertEqual(200,code,msg='返回的状态码不是200')
            self.assertEqual('请求成功.',n,msg='消息未请求成功')
        except Exception as e:
            print(e)


    def test_transacation_detail(self):
        u'测试交易详情接口'
        self.log.info('-------------开始测试交易详情接口--------')
        url = 'http://api.exam.sunnycare.cc/v1/orderDetail'

        json_data = {'token':self.uid_token,"is_invoices_req":"0"} #0全部 1未申请发票 2已经申请发票
        r = self.s.post(self.url,headers=self.header,json=json_data)
        print('全部：%s' % r.json())
        #取出交易记录中的订单号
        order_no_list = r.json()['data']['list']

        L=[]
        for i in order_no_list:
            L.append(i['order_no'])

        #循环订单号
        for x in L:
            json_data2 = {
                "token":self.uid_token,
                "order_no":str(x)
            }
            r2 = self.s.post(url,headers = self.header,json=json_data2)
            #断言请求返回状态
            try:
                self.assertEqual('请求成功.',r2.json()['note'])
                self.assertEqual(200,r2.json()['code'])
                self.log.info('商品交易详情请求成功')
            except Exception as e:
                self.log.error('交易详情获取失败，原因是：%s' % e)
    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main(warnings='ignore') #忽视警告