#coding:utf-8
import requests
import unittest
from common.login import LG
import time
from common.logger import Log
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
                       'Connection': 'keep-alive'}
        self.log = Log()#实例化日志的类
    def testAvailabelCoupon(self):
        u'测试可领用优惠券列表接口'
        self.log.info('-----开始测试可领的优惠券列表接口-------')
        url = 'http://api.lesson.wrightin.com/v1/coupon/canget'
        json_DATA = {"where_code":"Z2018041914505917219",
                     "timestamp":str(time.time()),"for_where":"3",
                     "token":self.uid_token}
        r = self.s.post(url,headers = self.header,json=json_DATA)
        try:
            self.log.info('开始断言请求该接口返回的状态是否成功')
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            self.log.error('请求接口返回不成功，原因：%s' % e)
        self.log.info('---------------测试接口结束--------------------')
        print(r.json())
    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()
