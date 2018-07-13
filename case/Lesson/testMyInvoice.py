#coding:utf-8
import requests
import unittest
from common.login import LG
from common.Excel import Excel_util
class TestInvoice(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}

    def test_invoice(self):
        u'测试我的发票获取接口'
        url = 'http://api.exam.wrightin.com/v1/myInvoices'



        json_data2 = {"token":self.uid_token}  #请求的参数上一接口返回的token
        print(json_data2)
        r = self.s.post(url,headers=self.header,json=json_data2)
        self.excel.write_value(6,5,r.json())
        self.assertEqual('请求成功.',r.json()['note'],msg='请求我的发票接口没有成功')
        list1 = r.json()['data']['list']
        global d
        d = {}
        x = 1
        for i in list1:
            d['code'+ str(x)] = i['code']
            x += 1
        self.excel.write_value(6,6,d)

    def test_invoice_detail(self):
        u'测试查看发票详情接口'
        url = 'http://api.exam.wrightin.com/v1/myInvoiceDetail'

        #for循环一次去请求每张发票详情
        for value in d.values():
            print('value',value)
            json_data = {"token":self.uid_token,"inv_code":value}
            r = self.s.post(url,headers = self.header,json=json_data)
            print(r.json())
            self.assertEqual('请求成功.',r.json()['note'],msg='发票详情获取失败！')



    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()

