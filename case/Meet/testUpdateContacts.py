#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
class Contact(unittest.TestCase):


    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent':  'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding':  'gzip, deflate',
                       'Accept-Language':  'zh-Hans-CN;q=1',
                       'Content-Type':  'application/json',
                       'requestApp':  '3',
                       'requestclient':  '2',
                       'versionForApp':  '2.0',
                       'Authorization':  'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection':  'keep-alive'}
        self.log = Log()#实例化日志的类

    def test_update_contacts01(self):
        u'更新联系人-更新名字'
        #先更新名字再从联系人列表中查看是否已成功更新
        #更新名字
        update_url = 'http://api.meet.sunnycare.com/v2/contact/update'
        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "phone": 13605246089,
            "sex": 0,
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1'
        }
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])
        #获取联系人列表中信息
        list_url = 'http://api.meet.sunnycare.com/v2/contact/records'
        json_data2 = {
            "token": self.uid_token
        }
        r2 = self.s.post(list_url,headers = self.header,json=json_data2)

    def test_update_contacts02(self):
        u'更新联系人-更新号码'
        #先更新名字再从联系人列表中查看是否已成功更新
        #更新号码
        update_url = 'http://api.meet.sunnycare.com/v2/contact/update'
        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "phone": 13888888888,
            "sex": 0,
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1'
        }
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])

    def test_update_contacts03(self):
        u'更新联系人-更新名字'
        #先更新名字再从联系人列表中查看是否已成功更新
        #更新地址
        update_url = 'http://api.meet.sunnycare.com/v2/contact/update'
        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "phone": 13888888888,
            "sex": 0,
            "address": '北京市江宁区天元东路122号',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1'
        }
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

    