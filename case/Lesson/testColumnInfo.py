#coding:utf-8
import requests,json
import unittest
from common.login import LG
import time
from common.Excel import Excel_util
import urllib3
urllib3.disable_warnings()

class ColumnInfo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.EXCEL = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    def testColumnInfo(self):
        u'测试专栏信息接口'
        url = 'https://api.lesson.wrightin.com/v1/spe'
        #将所有专栏的code放进list
        column_list = json.loads(self.EXCEL.read_value(4,6))
        print(column_list)

        new_column_list = []
        for x in column_list.values():
            new_column_list.append(x)
        #详情介绍链接
        detail_links = []
        for i in new_column_list:
            json_data = {"spe_code":i,"timestamp":str(time.time()),"token":self.uid_token}
            r = self.s.post(url,headers = self.header,json=json_data,verify=False)
            #print(r.json())
            detail_links.append(r.json()['data']['detail_link'])
            self.assertEqual('请求成功.',r.json()['note'],msg='专栏信息返回的状态不是请求成功，有问题！')
        #下面测试专栏介绍的链接

        for link in detail_links:
            r2 = self.s.get(link,verify=False)
            self.assertEqual(200,r2.status_code,msg='专栏介绍链接返回状态码不是200！')



    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()
