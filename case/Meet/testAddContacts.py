#coding:utf-8
import requests
import unittest
import time,json
from common.Hash import phone_nember,get_digit,get_sign #生成随机手机号
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util


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
        self.exel = Excel_util(r'C:\Users\Administrator\Desktop\interface_testcase.xls')


    def test_add_contacts01(self):
        u'添加联系人-各个入参正常'

        self.log.info('开始测试添加参会人接口-参数正常')
        url = 'http://api.meet.sunnycare.cc/v2/contact/add'
        #for i in range(3):
        json_data = {
            "token": self.uid_token,
            "name": '你不知道我是谁',
            "phone": phone_nember(),
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
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('添加参会人返回结果：%s' % r.json())
        self.assertEqual(200, r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('添加参会人接口-参数正常情况测试结束！\n')

    def test_add_contacts02(self):
        u'添加联系人-姓名过长'
        self.log.info('新增参会人-名称过长')
        url = 'http://api.meet.sunnycare.cc/v2/contact/add'
        json_data = {
            "token": self.uid_token,
            "name": '大于32个字的名字大于32个字的名字大于32个字的名字大于32个字的名字大于32个字的名字大于32个字的名字',
            "phone": phone_nember(),
            "sex": '0',
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('新增名字过长返回结果是：%s' % r.json())
        self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('新增参会人-名称过长情况测试结束！\n')

    def test_add_contacts03(self):
        u'添加联系人-手机号码格式不正确'
        self.log.info('新增参会人-手机号格式不正确')
        url = 'http://api.meet.sunnycare.cc/v2/contact/add'
        json_data = {
            "token": self.uid_token,
            "name": '司马上官',
            "phone": '6666111122',
            "sex": '0',
            "address": '江苏省南京市江宁区',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('新增手机号格式不正确返回结果是：%s' % r.json())
        self.assertEqual(203, r.json()['code'])
        self.log.info('新增参会人-手机号格式不正确情况测试结束！\n')

    def test_add_contacts04(self):
        u'添加联系人-地址为空'
        self.log.info('新增参会人-地址为空')
        url = 'http://api.meet.sunnycare.cc/v2/contact/add'
        json_data = {
            "token": self.uid_token,
            "name": '司马上官',
            "phone": phone_nember(),
            "sex": '0',
            "address": '  ',
            "company": '南京麦澜德',
            "job": 'xxx',
            "job_title": 'sss',
            "is_from_base": '1',
            "timestamp": str(int(time.time())),
            "nonce": get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('新增参会人-地址为空返回结果是：%s' % r.json())
        self.assertEqual(203, r.json()['code'])
        self.log.info('新增参会人-地址为空情况测试结束！\n')

    @unittest.skip('无理由')
    def test_add_contacts05(self):
        u'添加联系人-新增人数过多'
        self.log.info('新增参会人-新增人数过多')
        url = 'http://api.meet.sunnycare.cc/v2/contact/add'
        for i in range(105):
            json_data = {
                "token": self.uid_token,
                "name": '司马上官',
                "phone": phone_nember(),
                "sex": '0',
                "address": ' 南京南京',
                "company": '南京麦澜德',
                "job": 'xxx',
                "job_title": 'sss',
                "is_from_base": '1',
                "timestamp": str(int(time.time())),
                "nonce": get_digit()
            }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            while  i == 101:
                self.assertEqual('数量达到上限',r.json()['note'])
                self.log.info('新增参会人-新增人数过多返回结果是：%s' % r.json())
                break
        self.log.info('新增参会人-新增人数过多情况测试结束！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

