#coding:utf-8
import requests
import unittest
import time,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
from case.Meet.testContactsList import Contact

class Con(unittest.TestCase):

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

    def test_delete_contacts(self):
        u'删除联系人接口'
        self.log.info('删除联系人接口测试开始！')
        url = 'http://api.meet.sunnycare.cc/v2/contact/del'
        #读取contact_code
        code = self.exel.read_value(15,6)
        be_code = json.loads(code)
        #如果非空
        if code:
            for v in be_code.values():
                json_data = {
                    "token":self.uid_token,
                    "contact_code":v #读取excel中的code
                }
                r = self.s.post(url,headers = self.header,json=json_data)
                self.log.info('删除该条联系人返回结果是：%s' % r.json())
                self.assertEqual('请求成功.',r.json()['note'])
        else:
            self.log.warning('参会人code为空')
        self.log.info('删除联系人接口测试结束！！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


