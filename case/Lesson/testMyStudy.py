#coding:utf-8
import requests,time
import unittest
from common.login import LG
import time,json
from common.logger import Log
from common.Excel import Excel_util
from common.Hash import get_digit,get_sign
import urllib3
urllib3.disable_warnings()

class Mystudy(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #登录
        self.header = {
            'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_mystudy(self):
        u'测试我的学习接口'
        self.log.info('-----开始测试测试我的学习接口-----')
        url = 'http://api.lesson.sunnycare.cc/v1/learns'
        json_data = {
            "token":self.uid_token,
            "time": "0",
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data,verify=False)
        print(r.json())
        self.assertEqual('请求成功.',r.json()['note'])
        lessons = r.json()['data']['list']

        #定义全局变量 学习code
        global study_codes
        study_codes = []
        for i in lessons:
            study_codes.append(i['code'])
        print('study_codes:  ',study_codes)

        #课程code
        lesson_codes = []
        for x in lessons:
            lesson_codes.append(x['lesson_code'])
        print('lesson_codes',lesson_codes)
        #创建字典 写入excel
        m = {}
        j = 1
        for z in lesson_codes:
            m['lessoncode'+ str(j)] = z
            j += 1
        self.excel.write_value(7,6,m)

        self.log.info('----测试我的学习接口结束----')

    def test_add_study_chap(self):
        u'测试增加课程的学习进度接口'
        self.log.info('====开始测试增加课程的学习进度接口=====')
        #先通过课程接口来获取章节
        url = 'http://api.lesson.sunnycare.cc/v1/lesson'
        lesson_codes = json.loads(self.excel.read_value(7,6))

        #定义全局变量
        global chap_codes
        chap_codes = []
        for value in lesson_codes.values():
            json_data = {
                "lesson_code":value,
                "token":self.uid_token,
                "timestamp": str(int(time.time())),
                "nonce": get_digit()
                     }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data,verify=False)
            #断言，我的学习中的每一个课程的标签都应是‘已加入学习’
            print(r.json())
            self.assertEqual('已加入学习',r.json()['data']['btn'][0]['btn_name'])

            #将chap_code 加入chap_codes列表
            for y in (r.json()['data']['chap_list']):
                chap_codes.append(y['chap_code'])
        print('chap_codes:',chap_codes)

        url_2 = 'http://api.lesson.sunnycare.cc/v1/learn/chapadd'

        for i in chap_codes:
            json_data2 = {
                "chap_code":i,
                "timestamp":str(int(time.time())),
                "token":self.uid_token,
                "nonce": get_digit()
                       }
            json_data2['sign'] = get_sign(json_data2)
            r2 = self.s.post(url_2,headers = self.header,json=json_data2,verify=False)
            self.assertEqual('请求成功',r2.json()['note'],msg='增加课程的学习进度失败')

        self.log.info('====测试增加课程的学习进度接口结束=====')


    '''
    def test_remove_study(self):
        u'这是测试取消加入学习接口'
        self.log.info('-----开始测试测试取消加入学习接口--------')
        url = 'https://api.lesson.wrightin.com/v1/learn/remove'
        for i in study_codes:
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
    '''

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()

