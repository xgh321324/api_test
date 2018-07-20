#coding:utf-8
import requests,unittest
from common.logger import Log
from common.login import LG

class Account_login(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
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
        self.log = Log()
        self.url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/loginByUsername'

    def test_account_login(self):
        u'测试账号登录-正确账号正确密码'
        self.log.info('开始测试正确账号正确密码登录.....')
        json_data = {
            "username":"15651797525",
            "password":"123456",
            "loginDevice":"2",
            "loginCity":"南京市"
                     }
        r = self.s.post(self.url,headers=self.header,json=json_data)
        self.assertEqual('登录成功',r.json()['msg'],msg='正确账号密码没有登录成功！！')
        self.log.info('测试正确账号正确密码登录结束')

    def test_account_login2(self):
        u'测试账号登录-正确账号错误密码'
        self.log.info('开始测试正确账号错误密码登录.....')
        json_data = {
            "username":"15651797525",
            "password":"123458",
            "loginDevice":"2",
            "loginCity":"南京市"
                     }
        r = self.s.post(self.url,headers=self.header,json=json_data)
        self.assertEqual('登录失败，请检查用户名或密码是否正确.',r.json()['msg'],msg='正确账号错误密码登录有问题！！')
        self.log.info('测试正确账号错误密码登录结束')

    def test_account_login3(self):
        u'测试账号登录-错误账号正确密码'
        self.log.info('开始测试错误账号正确密码登录.....')
        json_data = {
            "username":"15651797526",
            "password":"123456",
            "loginDevice":"2",
            "loginCity":"南京市"
                     }
        r = self.s.post(self.url,headers=self.header,json=json_data)
        self.assertEqual('登录失败，请检查用户名或密码是否正确.',r.json()['msg'],msg='错误账号正确密码登录有问题！！')
        self.log.info('测试错误账号正确密码登录结束')

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()



