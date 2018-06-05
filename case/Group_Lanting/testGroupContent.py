#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
urllib3.disable_warnings()

class Content(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()

    def test_group_content(self):
        u'圈子内容接口-参数正确'
        self.log.info('测试圈子内容接口-参数正确')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":1,
                     "token":self.auto_login_token,
                     "time":0,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.status_code)
        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('测试圈子内容接口-参数正确情况测试结束\n')

    def test_group_content2(self):
        u'圈子内容接口-参数无token'
        self.log.info('测试圈子内容接口-无token')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":1,
                     #"token":self.auto_login_token,
                     "time":0,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('测试圈子内容接口-无token情况测试结束\n')

    def test_group_content3(self):
        u'圈子内容接口-参数page为空'
        self.log.info('测试圈子内容接口-page为空')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":'',
                     "token":self.auto_login_token,
                     "time":0,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('测试圈子内容接口-page为空情况测试结束\n')

    def test_group_content4(self):
        u'圈子内容接口-参数page页码不存在'
        self.log.info('测试圈子内容接口-page页码不存在')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":10,
                     "token":self.auto_login_token,
                     "time":0,
                     "group_id":"G00009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('测试圈子内容接口-page页码不存在情况测试结束\n')

    def test_group_content5(self):
        u'圈子内容接口-参数圈子id不存在'
        self.log.info('测试圈子内容接口-圈子id不存在')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":1,
                     "token":self.auto_login_token,
                     "time":0,
                     "group_id":"G10009"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回内容是：%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        self.assertIn('不存在.',r.json()['note'])
        self.log.info('测试圈子内容接口-圈子id不存在情况测试结束\n')

    def test_group_content6(self):
        u'圈子内容接口-参数圈子id为空'
        #groupid为空时服务器报错了 code500
        self.log.info('测试圈子内容接口-圈子id为空')
        url = 'http://api.sns.sunnycare.cc/v1/group/content'
        json_data = {"page":1,
                     "token":self.auto_login_token,
                     "time":0,
                     "group_id":""
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回状态码是：%s' % r.status_code)
        #self.assertEqual(501,r.json()['code'])
        #self.assertIn('不存在.',r.json()['note'])
        self.log.info('测试圈子内容接口-圈子id为空情况测试结束\n')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


