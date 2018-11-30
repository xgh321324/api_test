#coding:utf-8
import requests
import unittest,time
from common.login import LG
from common.Hash import get_sign,get_digit

class Test_pay(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.token = self.lgin.login()
        self.duid = self.lgin.gettoken_loginbyUID()  #取登录成功后的uid
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


    def testpayment(self):
        u'测试通用-支付接口-微信支付'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        json_data1 = {"UID":self.duid,
                      }
        r = self.s.post(url,headers= self.header,json=json_data1) ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        t= r.json()['data']['Token']#取到我想要的token

        json_data2 = {'pay_method': '1',
                      'product_type': '3',
                      'timestamp': str(int(time.time())),
                      "token":t,
                      "product_code":"Z00028",
                      'nonce': get_digit()
                      }
        json_data2['sign'] = get_sign(json_data2)#上一接口返回的token现在用来做请求参数
        url2 ='http://api.pay.sunnycare.cc/v1/pay'#支付接口地址
        r2 = self.s.post(url2,headers=self.header,json=json_data2)
        print(r2.json())
        self.assertEqual(200,r2.json()['code'])

    def testpayment2(self):
        u'测试通用-支付接口-支付宝支付'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口
        json_data1 = {
            "UID":self.duid
        }
        ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        r = self.s.post(url,headers= self.header,json=json_data1)
        t= r.json()['data']['Token'] #取到我想要的token

        #上一接口返回的token现在用来做请求参数
        json_data2 = {'pay_method': '0',
                      'product_type': '3',
                      'timestamp': str(int(time.time())),
                      "token":t,
                      "product_code":"Z00028",
                      'nonce': get_digit()
                      }
        json_data2['sign'] = get_sign(json_data2)
        url2 ='http://api.pay.sunnycare.cc/v1/pay'#支付接口地址
        r2 = self.s.post(url2,headers=self.header,json=json_data2)
        print(r2.json())
        self.assertEqual(200,r2.json()['code'])



    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
