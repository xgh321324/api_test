#coding:utf-8
import requests
import unittest
from common.login import LG
import time
from common.logger import Log
class Mystudy(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {
            'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
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

    def test_mystudy(self):
        u'测试我的学习接口'
        self.log.info('-----开始测试测试我的学习接口-----')
        url = 'http://api.lesson.sunnycare.cc/v1/learns'
        json_data = {"token":self.uid_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'])
        lessons = r.json()['data']['list']
        global L
        L = []
        for i in lessons:
            L.append(i['code'])
        print('L:  ',L)
        self.log.info('----测试我的学习接口结束----')


    def test_remove_study(self):
        u'这是测试取消加入学习接口'
        self.log.info('-----开始测试测试取消加入学习接口--------')
        url = 'http://api.lesson.sunnycare.cc/v1/learn/remove'
        for i in L:
            json_data = {
                "timestamp":str(time.time()),
                "learn_code":i,
                "token":self.uid_token
            }
            try:
                r2 = self.s.post(url,headers = self.header,json=json_data)
                self.assertEqual('请求成功',r2.json()['note'])
                self.log.info('取消加入学习成功')
            except Exception as e:
                self.log.error('取消介入学习失败。原因：%s' % e)
        self.log.info('-------测试取消加入学习接口结束------')


    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()

