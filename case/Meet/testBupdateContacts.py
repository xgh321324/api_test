#coding:utf-8
import requests
import unittest
import time,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
from common.Hash import get_digit,get_sign

class Contact(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\interface_testcase.xls')

    def test_update_contacts01(self):
        u'更新联系人-更新名字'
        #先读取一个参会人code然后更新其信息
        read_code = self.excel.read_value(15,6)
        be_use_code = json.loads(read_code)
        update_url = 'http://api.meet.sunnycare.cc/v2/contact/update'

        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "contact_code": be_use_code['contact_code1'],
            "phone": '13605246089',
            "sex": '0',
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        #入参加密
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])

    def test_update_contacts02(self):
        u'更新联系人-更新号码'
        read_code = self.excel.read_value(15,6)
        be_use_code = json.loads(read_code)
        update_url = 'http://api.meet.sunnycare.cc/v2/contact/update'
        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "contact_code": be_use_code['contact_code1'],
            "phone": '13888888888',
            "sex": '0',
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        #入参加密
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])

    def test_update_contacts03(self):
        u'更新联系人-更新名字'
        read_code = self.excel.read_value(15,6)
        be_use_code = json.loads(read_code)
        update_url = 'http://api.meet.sunnycare.cc/v2/contact/update'
        json_data = {
            "token": self.uid_token,
            "name": '更新后的名字',
            "contact_code": be_use_code['contact_code1'],
            "phone": '13888888888',
            "sex": '0',
            "address": '北京市江宁区天元东路122号',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        #入参加密
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(update_url,headers = self.header,json=json_data)
        self.assertEqual(200,r.json()['code'])

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

    