#coding:utf-8
import requests
import unittest
import time,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
class Meet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.s = requests.session()
        cls.lgin = LG(cls.s) #实例化登录类
        cls.uid_token = cls.lgin.login() #直接取第二部登录
        cls.header = {
            'RequestClient': '1',
            'RequestApp': '3',
            'VersionForApp': '2.1.0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.0.0.13547',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json; charset=utf-8',
            #'Content-Length': '55',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        cls.log = Log()#实例化日志的类
        cls.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    def test_meet_list01(self):
        u'会议列表接口-获取会议列表'
        self.log.info('会议列表接口')
        url = 'http://api.meet.sunnycare.cc/v2/meet/records'
        json_data = {
            "token":self.uid_token,
            "time": '0'
        }
        #print(self.uid_token)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('列表返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功.',r.json()['note'])
        #获取json中会议编号
        li = r.json()['data']['list']
        code = {}
        j = 1
        for i in li:
            code['code'+str(j)] = i['code']
            j += 1
        #将会议code写入excel
        self.excel.write_value(14,6,code)
        self.log.info('会议列表接口测试结束！')

    def test_meet_list02(self):
        u'会议详情接口-获取详情'
        self.log.info('会议详情接口')
        #读取code
        read = self.excel.read_value(14,6)
        use_read = json.loads(read)
        #下面调用详情接口
        info_url = 'http://api.meet.sunnycare.cc/v2/meet'
        for v in use_read.values():
            #print(type(v))
            info_json_data = {
                    "token": self.uid_token,
                    "meet_code":v
                }
            #print(self.uid_token)
            r2 = self.s.post(info_url,headers = self.header,json=info_json_data)
            self.log.info('会议：%s返回结果是：%s' % (v,r2.json()))
            self.assertEqual('请求成功.',r2.json()['note'])
        self.log.info('会议详情接口测试结束！！')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()

