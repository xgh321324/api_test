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


    def test_post_artical01(self):
        u'发布文章-纯文字'
        self.log.info('测试发布文章接口-纯文字')
        url = get_content('sns_base_url')+'/v1/post/add'
        json_data = {
            "token": self.auto_login_token,
            "title": "我的文章-纯文字",
            "cover": '/TestObjectFiles/TestObjectFiles/1529561033505542.jpg',
            "introduction": "文字文字文字",
            "content": [
                {
                    "sort":"0",
                    "type":"0",
                    "value": "这是第一个文本内容这是第一个文本内容这是第一个文本内容这是第一个文本内容"
                 },
                {
                    "sort":"1",
                    "type":"0",
                    "value": "这是第二个文本内容这是第二个文本内容这是第二个文本内容"
                 }
            ],
            "groups": ["G00001"]
        }
        #for i in range(1,100):
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual('文章发布成功.',r.json()['note'])
        self.log.info('测试发布文章接口-纯文字情况测试结束\n')

    def test_post_artical02(self):
        u'发布文章-纯图片'
        self.log.info('测试发布文章接口-纯图片')
        url = get_content('sns_base_url')+'/v1/post/add'
        json_data = {
            "token": self.auto_login_token,
            "title": "我的文章-纯图片",
            "cover": '/TestObjectFiles/TestObjectFiles/1529561033505542.jpg',
            "introduction": "图片图片",
            "content": [
                {
                    "sort":"0",
                    "type":"1",
                    "value": "TestObjectFiles/TestObjectFiles/1529560739750727.jpg",
                    "width":"4032",
                    "height":"3024"
                 },
                {
                    "sort":"1",
                    "type":"1",
                    "value": "/TestObjectFiles/TestObjectFiles/1529561900655548.jpg",
                    "width":"4032",
                    "height":"3024"
                 },
                {
                    "sort":"2",
                    "type":"1",
                    "value": "/TestObjectFiles/TestObjectFiles/1529561901530700.jpg",
                    "width":"4032",
                    "height":"3024"
                 }
            ],
            "groups": ["G00001"]
        }
        #for i in range(1,100):
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual('文章发布成功.',r.json()['note'])
        self.log.info('测试发布文章接口-纯文字情况测试结束\n')

    def test_post_artical03(self):
        u'发布文章-文字+图片'
        self.log.info('测试发布文章接口-文字+图片')
        url = get_content('sns_base_url')+'/v1/post/add'
        json_data = {
            "token": self.auto_login_token,
            "title": "我的文章-文字+图片",
            "cover": '/TestObjectFiles/TestObjectFiles/1529561033505542.jpg',
            "introduction": "文字+图片",
            "content": [
                {
                    "sort":"0",
                    "type":"0",
                    "value": "这是第一段文本内容",
                 },
                {
                    "sort":"1",
                    "type":"1",
                    "value": "/TestObjectFiles/TestObjectFiles/1529561900655548.jpg",
                    "width":"4032",
                    "height":"3024"
                 },
                {
                    "sort":"2",
                    "type":"0",
                    "value": "这是第二段文本内容",
                 },
                {
                    "sort":3,
                    "type":1,
                    "path":"/TestObjectFiles/TestObjectFiles/152956190416515.jpg",
                    "width":"4032",
                    "height":"3024"
                }

            ],
            "groups": ["G00001"]
        }
        #for i in range(1,100):


        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        #self.assertEqual('文章发布成功.',r.json()['note'])
        self.log.info('测试发布文章接口-文字+图片情况测试结束\n')


    def tearDown(self):
        self.s.close()


if __name__=='__main__':
    unittest.main()
