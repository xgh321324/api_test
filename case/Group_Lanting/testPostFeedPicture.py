#coding:utf-8
import requests,unittest,time
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Read_config import get_content
urllib3.disable_warnings()

class Feed(unittest.TestCase):
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

    def test_post_picture01(self):
        u'发布图片接口到圈子'
        self.log.info('测试发布图片接口到圈子')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {
            "pic":[
                {
                    "path":'TestObjectFiles/TestObjectFiles/1529560739750727.jpg',
                    "width":2016,
                    "height":1107
                }
            ],
            "groups":["G00001"],
            "token":self.auto_login_token,
            "text":"接口发布图片"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布图片接口到圈子结束！\n')


    def test_post_picture02(self):
        u'发布图片接口到大于3个圈子'
        self.log.info('测试发布图片接口到大于3个圈子')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {
            "pic":[
                {
                    "path":"TestObjectFiles/TestObjectFiles/1529560739750727.jpg",
                    "width":828,
                    "height":618
                }
            ],
            "groups":['G00001','G00003','G00007','G00006'],
            "token":self.auto_login_token,
            "text":"南京东路"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        self.assertEqual('最多只能分享到 3 个圈子.',r.json()['note'])
        self.log.info('测试发布图片接口到大于3个圈子结束！\n')

    def test_post_picture03(self):
        u'发布多张图片到圈子'
        self.log.info('测试发布发布多张图片到圈子')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {
            "pic":[
                {
                    "path":"TestObjectFiles/TestObjectFiles/1529560739750727.jpg",
                    "width":828,
                    "height":618
                },
                {
                    "path":"/TestObjectFiles/TestObjectFiles/1529561899406240.jpg",
                    "width":2016,
                    "height":1512
                },
                {
                    "path":"/TestObjectFiles/TestObjectFiles/1529561900655548.jpg",
                    "width":2016,
                    "height":1512
                },
                {

                    "path":"/TestObjectFiles/TestObjectFiles/1529561901530700.jpg",
                    "width":2016,
                    "height":1512
                },
                {

                    "path":"/TestObjectFiles/TestObjectFiles/1529561902244284.jpg",
                    "width":2016,
                    "height":1512
                },
                {

                    "path":"/TestObjectFiles/TestObjectFiles/1529561903256778.jpg",
                    "width":2016,
                    "height":1512
                },
                {

                    "path":"/TestObjectFiles/TestObjectFiles/152956190416515.jpg",
                    "width":2016,
                    "height":1512
                }
            ],
            "groups":['G00001'],
            "token":self.auto_login_token,
            "text":"发布多张图片到圈子"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布多张图片到圈子结束！\n')

    def tearDown(self):
        self.s.close()


if __name__=='__main__':
    unittest.main()
