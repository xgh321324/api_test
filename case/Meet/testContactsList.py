#coding:utf-8
import requests
import unittest
import time
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
class Contact(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        self.log = Log()#实例化日志的类
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\interface_testcase.xls')

    def test_contact_list(self):
        u'联系人列表接口'
        self.log.info('参会人列表接口测试开始')
        url = 'http://api.meet.sunnycare.cc/v2/contact/records'
        json_data = {
            "token":self.uid_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('参会人列表返回内容是：%s' % r.json())
        conten = r.json()['data']['content']
        contact_code = {}
        j = 1
        for i in conten:
            contact_code['contact_code'+str(j)] = i['contact_code']
            j += 1
        #将contact_code写入excel供其他借口调用
        self.excel.write_value(15,6,contact_code)
        self.log.info('参会人列表接口测试结束！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
