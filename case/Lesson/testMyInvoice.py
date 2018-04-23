#coding:utf-8
import requests
import unittest
from common.login import LG
class TestInvoice(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.lgin.login()
        self.token = self.lgin.get_token()
        self.duid = self.lgin.get_duid()  #取登录成功后的uid


    def test_invoice(self):
        u'测试我的发票获取接口'
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '1.3',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        json_data1 = {"UID":str(self.duid),"loginDevice":"2","loginCity":"no location"}
        r = self.s.post(url,headers= header,json=json_data1) ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        t= r.json()['data']['Token']
        #print(t)
        url2 = 'http://api.exam.wrightin.com/v1/userInvoices'  #我的发票 接口
        json_data2 = {"token":t}  #请求的参数上一接口返回的token
        print(json_data2)
        r = self.s.post(url2,headers=header,json=json_data2)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'],msg='请求我的发票接口没用成功')



    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()

