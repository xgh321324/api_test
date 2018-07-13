#coding:utf-8
import requests,unittest,time
from common.Excel import Excel_util
from common.logger import Log
from common.login import LG

class SystemInfo(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.lgin.login()
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/2.0.0 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}
        self.log = Log()
        self.Excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_sysinfo_list(self):
        u'测试系统消息列表接口'
        self.log.info('------> 开始测试系统消息列表接口 <-------')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/doctorInfoWithTelephone'
        url_1 = 'http://api.common.wrightin.com/v1/note/unread'
        url_2 = 'http://api.common.wrightin.com/v1/note/records'
        json_data = {"token":self.uid_token,
                     "Telephone":"15651797525"
                     }

        json_data_1 = {
                       "token":self.uid_token,
                        "timestamp":'1525245187.2932727'
                       }

        json_data_2 = {
                     "timestamp":str(time.time()),
                     "type":0,
                     "token":self.uid_token,
                     "page":1
                     }
        try:
            r = self.s.post(url,headers = self.header,json=json_data)
            r1 = self.s.post(url_1,headers = self.header,json=json_data_1)
            r2 = self.s.post(url_2,headers = self.header,json=json_data_2)
            print(r.json())
            print(r1.json())
            print(r2.json())
        except Exception as e:
            self.log.error('请求系统消息列表失败，原因：%s' % e)
        #self.assertEqual('请求成功.',r.json()['note'])
        self.log.info('------> 测试系统消息列表接口结束 <-------')

    #def test_read_sysinfo(self):
      #  u'测试读取系统信息接口'
     #   self.log.info('------> 开始读取系统信息接口 <-------')
     #   url = 'http://api.common.wrightin.com/v1/note/read'
     #   json_data = {"code":"cd95705e442444ba88d3b1fb8b348484",
     #                "token":self.uid_token}

    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()

