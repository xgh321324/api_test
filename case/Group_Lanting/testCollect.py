#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')


    def test_collect01(self):
        u'测试收藏接口'
        #读取关联参数-用户的动态的id，再循环去收藏，断言结果
        self.log.info('开始测试收藏动态接口！')
        url = 'http://api.sns.sunnycare.cc/v1/collect/add'
        read_feed_ids = self.excel.read_value(12,6)
        feed_ids = json.loads(read_feed_ids)
        #print(type(feed_ids))
        #迭代字典的value
        for x in feed_ids.values():
            json_data = {
                "id":x,
                "token":self.auto_login_token
            }
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('返回的内容是：%s' % r.json())
            self.assertEqual(200,r.json()['code'])
            self.assertEqual('收藏成功.',r.json()['note'])

        self.log.info('收藏动态接口测试结束！\n')

    def test_collect02(self):
        u'测试取消收藏接口'
        self.log.info('开始测试取消收藏动态接口！')
        url = 'http://api.sns.sunnycare.cc/v1/collect/delete'
        read_feed_ids = self.excel.read_value(12,6)
        feed_ids = json.loads(read_feed_ids)
        #print(type(feed_ids))
        #迭代字典的value
        for x in feed_ids.values():
            json_data = {
                "id":x,
                "token":self.auto_login_token
            }
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('取消收藏返回的内容是：%s' % r.json())
            self.assertEqual(200,r.json()['code'])
            self.assertEqual('取消收藏成功.',r.json()['note'])

        self.log.info('取消收藏动态接口测试结束！\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
