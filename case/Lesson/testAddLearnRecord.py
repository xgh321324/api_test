#coding:utf-8
import requests,time,unittest
from common.logger import Log
from common.login import LG
from common.Hash import get_sign,get_digit
from common.Database import Sqldriver
class AddLearnRecord(unittest.TestCase):
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
        self.log = Log()


    def test_addlearn_record(self):
        u'测试增加学习记录接口'
        self.log.info('--------开始测试增加学习记录接口---------')
        url = 'http://api.lesson.sunnycare.cc/v1/learn/chapadd'
        L = ['J00201']
        for i in L:
            #加入nonce
            json_data = {
                "chap_code":i,
                "timestamp":str(int(time.time())),
                "token":self.uid_token,
                "nonce": get_digit()
                         }
            #加入sign
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            try:
                self.log.info('请求返回的数据是%s' % r.json())
                self.assertEqual('请求成功',r.json()['note'])
            except Exception as e:
                raise AssertionError
                self.log.error('增加章节学习记录请求失败，原因是：%s' % e )

        '''
        #数据库查询出章节code，循环加入学习
        i = 0
        while i < len(chapters):

            json_data = {"chap_code":chapters[i][0].__str__(),
                         "timestamp":str(time.time()),
                         "token":self.uid_token}
            r = self.s.post(url,headers = self.header,json=json_data)
            try:
                self.log.info('请求返回的数据是%s' % r.json())
                self.assertEqual('请求成功',r.json()['note'])
            except Exception as e:
                self.log.error('增加'+ chapters[i][0].__str__() +'章节学习记录请求失败，原因是：%s' % e )
            i += 1
        '''
    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
