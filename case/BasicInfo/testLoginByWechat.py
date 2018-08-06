#coding:utf-8
import requests,unittest
from common.login import LG
from common.logger import Log
from common.logger import Log

class Wechat_login(unittest.TestCase):
    '''
    APP 编号：澜渟 - 1，澜渟私教 - 2，澜婷医生 - 3；
    客户端类型编号：Android - 1，iOS - 2，PC - 3，Web - 4;
    '''

    def setUp(self):
        self.log = Log()
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header1 = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
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

    def test_login_by_wechat(self):
        u'测试澜渟医生IOS微信登录接口'
        self.log.info('澜渟医生IOS微信登录接口测试开始')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorLoginByWeChat'
        json_data = {"WeChatOpenID":"ogCzv1U6KPBJxRu0-LgrHBhRiJpI",
                     "WeChatUnionID":"oh3fH06yJfDB6smX6kJACRNlglVY"
                     }
        r = self.s.post(url,headers = self.header1,json=json_data)
        self.assertEqual('登录成功',r.json()['msg'],msg='澜渟医生IOS微信方式登录失败')

        self.log.info('澜渟医生IOS微信登录接口测试结束')

    def test_login_by_wechat2(self):
        u'澜渟医生测试Andriod微信登录接口'
        self.log.info('澜渟医生Andriod微信登录接口测试开始')
        self.header1['requestclient'] = str(1)
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorLoginByWeChat'
        json_data = {"WeChatOpenID":"ogCzv1U6KPBJxRu0-LgrHBhRiJpI",
                     "WeChatUnionID":"oh3fH06yJfDB6smX6kJACRNlglVY"
                     }
        r = self.s.post(url,headers = self.header1,json=json_data)
        self.log.info('澜渟医生Andriod微信登录返回：%s' % r.json())
        self.assertEqual('登录成功',r.json()['msg'],msg='澜渟医生Andriod微信方式登录失败')

        self.log.info('澜渟医生Andriod微信登录接口测试结束')

    def test_login_by_wechat3(self):
        u'澜渟测试Andriod微信登录接口'
        self.header1['requestApp'] = str(1)
        self.log.info('澜渟Andriod微信登录接口测试开始')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorLoginByWeChat'
        json_data = {"WeChatOpenID":"ogCzv1U6KPBJxRu0-LgrHBhRiJpI",
                     "WeChatUnionID":"oh3fH06yJfDB6smX6kJACRNlglVY"
                     }
        r = self.s.post(url,headers = self.header1,json=json_data)
        self.log.info('澜渟Andriod微信登录返回：%s' % r.json())
        self.assertEqual('登录成功',r.json()['msg'],msg='澜渟Andriod微信方式登录失败')

        self.log.info('澜渟Andriod微信登录接口测试结束')


    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()


