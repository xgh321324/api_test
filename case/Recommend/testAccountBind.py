#coding:utf-8
from common.login_lanting import auto_login_by_UID
import requests,unittest,time,json
from common.logger import Log
from common.Hash import get_digit,get_sign
from common.Excel import Excel_util

class Account(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.to = auto_login_by_UID()
        cls.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.4.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
        }
        cls.log = Log()
        cls.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_bind_account01(self):
        u'绑定提现账号接口'
        self.log.info('开始测试绑定账号接口..')
        url = 'http://api-rec.sunnycare.cc/v1/account/bind'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'alipay_account': '2088012687108144',
            'real_name': '许广会',
            'nick_name': '许广会',
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('绑定支付宝返回：%s' % r.json())
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('绑定账号接口测试结束！\n')

    def test_bind_account02(self):
        u'解除绑定账号接口'
        self.log.info('开始测试解除绑定账号接口..')
        url = 'http://api-rec.sunnycare.cc/v1/account/unbind'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'type': '0',#0,支付宝；1，微信
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('解除绑定支付宝返回：%s' % r.json())
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('解除绑定账号接口测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()
