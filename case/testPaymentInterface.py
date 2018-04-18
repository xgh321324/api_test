#coding:utf-8
import requests
import unittest
from common.login import LG
class Test_pay(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.lgin.login()
        self.token = self.lgin.get_token()
        self.duid = self.lgin.get_duid()  #取登录成功后的uid
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}


    def testpayment(self):
        u'测试通用-支付接口-微信支付'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        json_data1 = {"UID":str(self.duid),"loginDevice":"2","loginCity":"no location"}
        r = self.s.post(url,headers= self.header,json=json_data1) ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        t= r.json()['data']['Token'] #取到我想要的token

        json_data2 = {"payType":"1","user_source":"1","product_type":"2","token":t,"product_code":"K2018041811121537300"}  #上一接口返回的token现在用来做请求参数
        url2 ='http://api.exam.sunnycare.cc/v1/mldProductPay'#支付接口地址
        r2 = self.s.post(url2,headers=self.header,json=json_data2)
        print(r2.json())
        self.assertEqual(200,r2.json()['code'])

    def testpayment2(self):
        u'测试通用-支付接口-支付宝支付'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        json_data1 = {"UID":str(self.duid),"loginDevice":"2","loginCity":"no location"}
        ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        r = self.s.post(url,headers= self.header,json=json_data1)
        t= r.json()['data']['Token'] #取到我想要的token

        #上一接口返回的token现在用来做请求参数
        json_data2 = {"payType":"0","user_source":"1","product_type":"2","token":t,"product_code":"K2018041811121537300"}
        url2 ='http://api.exam.sunnycare.cc/v1/mldProductPay'#支付接口地址
        r2 = self.s.post(url2,headers=self.header,json=json_data2)
        print(r2.json())
        self.assertEqual(200,r2.json()['code'])
    def testpayment3(self):
        u'测试通用-支付接口-专栏支付'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        json_data1 = {"UID":str(self.duid),"loginDevice":"2","loginCity":"no location"}
        ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        r = self.s.post(url,headers= self.header,json=json_data1)
        t= r.json()['data']['Token'] #取到我想要的token

        #上一接口返回的token现在用来做请求参数
        json_data2 = {"payType":"0","user_source":"1","product_type":"3","token":t,"product_code":"K2018041811121537300"}
        url2 ='http://api.exam.sunnycare.cc/v1/mldProductPay'#支付接口地址
        r2 = self.s.post(url2,headers=self.header,json=json_data2)
        print(r2.json())
        self.assertEqual(200,r2.json()['code'])


    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()
