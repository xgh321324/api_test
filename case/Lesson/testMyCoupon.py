#coding:utf-8
import requests
import unittest
from common.login import LG
import time
from common.logger import Log
class LessonInfo(unittest.TestCase):
    log = Log()#实例化记录日志的类
    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
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
    def testMyCouponList(self):
        u'测试我的优惠券列表接口--可用'
        self.log.info('-----------开始测试我的可用优惠券列表接口-------------')
        url = 'http://api.lesson.sunnycare.cc/v1/coupon/mine'
        #0.不可用/1.可用
        json_data = {"can_use":"1","timestamp":str(time.time()),"token":self.uid_token,"time":"0"}
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的可用优惠券参数是：%s' % r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            self.log.error('请求可用优惠券列表没有成功：%s' % e)
        #判断优惠券个数，如果个数不为0 ，那么优惠券不能重复！
        L = []
        coupons = r.json()['data']['list']
        if len(coupons) != 0:
            for x in coupons:
               L.append(x['code'])
        else:
            self.log.info('可用优惠券个数为空')
        self.log.info('可用优惠券的code是：%s' % L)

        #将code列表转为集合 set set会自动剔除重复的元素 以转为set后的长度来判断是否存在重复code
        s = set(L)
        if len(s) < len(L):
            self.log.error('可用优惠券存在重复的情况')
        self.log.info('--------我的可用优惠券列表接口测试结束----')

    def testMyCouponList2(self):
        u'测试我的优惠券列表接口--不可用'
        self.log.info('-----------开始测试我的不可用优惠券列表接口-------------')
        url = 'http://api.lesson.sunnycare.cc/v1/coupon/mine'
        #0.不可用/1.可用
        json_data = {"can_use":"1","timestamp":str(time.time()),"token":self.uid_token,"time":"0"}
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的不可用优惠券json是：%s' % r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
        except Exception as e:
            self.log.error('请求不可用优惠券列表没有成功：%s' % e)
        #判断优惠券个数，如果个数不为0 ，那么优惠券不能重复！
        L = []
        coupons = r.json()['data']['list']
        if len(coupons) != 0:
            for x in coupons:
               L.append(x['code'])
        else:
            self.log.info('不可用优惠券个数为空')
        self.log.info('不可用优惠券的code是：%s' % L)

        #将code列表转为集合 set set会自动剔除重复的元素 以转为set后的长度来判断是否存在重复code
        s = set(L)
        if len(s) < len(L):
            self.log.error('不可用优惠券存在重复的情况')
        self.log.info('--------不可用优惠券列表接口测试结束----')

    def tearDown(self):
        self.s.close()
if __name__=='__main__':
    unittest.main()
