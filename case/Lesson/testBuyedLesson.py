#coding:utf-8
import requests,time,unittest
from common.login import LG
from common.logger import Log
from common.Hash import get_digit,get_sign

class Buyed_lesson(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #登录测试环境澜渟医生
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

    def test_buyed_lesson(self):
        u'这是测试已购课程接口-课程类型为所有'
        self.log.info('-----开始测试已购课程接口（课程类型是所有）------')
        url = 'http://api.lesson.sunnycare.cc/v1/orders'
        json_data = {
            "timestamp":str(int(time.time())),
            "product_type":"",
            "token":self.uid_token,
            "time":"0",
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        try:
            self.log.info('断言请求接口是否成功！')
            self.log.info('返回的内容是：%s' % r.json())
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            raise AssertionError
            self.log.error('请求已购课程接口失败，原因：%s' % e)


    def test_buyed_lesson2(self):
        u'这是测试已购课程接口-课程类型为所有课程'
        self.log.info('-----开始测试已购课程接口（课程类型是所有课程）------')
        url = 'http://api.lesson.sunnycare.cc/v1/orders'
        json_data = {
            "timestamp":str(int(time.time())),
            "product_type":"2",
            "token":self.uid_token,
            "time":"0",
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        try:
            self.log.info('断言请求接口是否成功！')
            self.log.info('返回的内容是：%s' % r.json())
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            raise AssertionError
            self.log.error('请求已购课程接口失败，原因：%s' % e)

    def test_buyed_lesson3(self):
        u'这是测试已购课程接口-课程类型为所有专栏'
        self.log.info('-----开始测试已购课程接口（课程类型是所有专栏）------')
        url = 'http://api.lesson.sunnycare.cc/v1/orders'
        json_data = {
            "timestamp":str(time.time()),
            "product_type":"3",
            "token":self.uid_token,
            "time":"0",
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        try:
            self.log.info('断言请求接口是否成功！')
            self.log.info('返回的内容是：%s' % r.json())
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            raise AssertionError
            self.log.error('请求已购课程接口失败，原因：%s' % e)

    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()




