#coding:utf-8
import time,requests,unittest
from common.login import LG
from common.logger import Log
from common.Hash import get_digit,get_sign

class LessonList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.lgin = LG(cls.s) #实例化
        cls.uid_token = cls.lgin.login()
        cls.header = {
            'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Type': 'application/json',
            'requestApp': '3',
            'requestclient': '2',
            'versionForApp': '2.4.0',
            'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
            'Connection': 'keep-alive'
        }
        cls.log = Log() #实例化日志的类

    def test_live_lesson_list01(self):
        u'直播课程列表接口-预告状态的直播'
        self.log.info('直播课程列表接口-预告状态列表')
        url = 'http://api-live.sunnycare.cc/v1/live/index'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'pageIndex': '1',
            'pageLimit': '10',
            'nonce': get_digit(),
            'status': '0' #直播课程状态 0.未开始 1.进行中 2.已结束（可选）
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('预告状态的直播课程返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('直播课程列表接口-预告状态列表测试结束！\n')

    def test_live_lesson_list02(self):
        u'直播课程列表接口-进行中的直播'
        self.log.info('直播课程列表接口-进行中状态列表')
        url = 'http://api-live.sunnycare.cc/v1/live/index'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'pageIndex': '1',
            'pageLimit': '10',
            'nonce': get_digit(),
            'status': '1' #直播课程状态 0.未开始 1.进行中 2.已结束（可选）
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('进行中的直播课程返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('直播课程列表接口-进行中列表测试结束！\n')

    def test_live_lesson_list03(self):
        u'直播课程列表接口-已结束状态的直播'
        self.log.info('直播课程列表接口-已结束状态列表')
        url = 'http://api-live.sunnycare.cc/v1/live/index'
        json_data = {
            'token': self.uid_token,
            'timestamp': str(int(time.time())),
            'pageIndex': '1',
            'pageLimit': '10',
            'nonce': get_digit(),
            'status': '2' #直播课程状态 0.未开始 1.进行中 2.已结束（可选）
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('已结束的直播课程返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('直播课程列表接口-已结束的列表测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()

