#coding:utf-8
import unittest,time,requests
from common.login import LG
from common.logger import Log
from common import Hash
class Adress(unittest.TestCase):
    def setUp(self):
        self.log = Log()
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
                       'Connection': 'keep-alive'
                       }
        self.set_nonce = Hash.get_md5(Hash.get_str())
        self.set_sign = Hash.get_md5(Hash.get_str())

    def test_All_Adress(self):
        u'获取用户的全部收货地址接口'
        self.log.info('开始测试获取用户的全部收货地址接口')
        url = 'http://api.common.wrightin.com/v1/address/records'
        print(self.set_sign)
        print(self.set_nonce)
        json_data = {"nonce":self.set_nonce,
                     "timestamp":str(time.time()),
                     #"sign":self.set_sign,
                     "token":self.uid_token
                     }
        r = self.s.post(url,headers=self.header,json=json_data)
        print(r.json())

        if self.assertEqual('请求成功.',r.json()['note']):
            self.log.info('获取用户的全部收货地址接口成功')
        else:
            self.log.error('获取用户的全部收货地址接口失败')

        self.log.info('测试获取用户的全部收货地址接口结束')

    def testAddAdress(self):
        u'测试增加收货地址接口'
        self.log.info('开始测试新增收货地址接口')
        url = 'http://api.common.wrightin.com/v1/address/apend'
        json_data = {"zone":"江苏省南京市江宁区",
                     "content":"南京江宁区气象台",
                     "contact_call":"15651797525",
                     "contact_name":"许下会",
                     "token":self.uid_token,
                     "timestamp":"1525674917",
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'])

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()



