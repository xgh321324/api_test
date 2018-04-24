#coding:utf-8
import requests,unittest
from common.login import LG
from common.logger import Log
class Meet(unittest.TestCase):
    def setUp(self):
        #banner获取接口
        self.url = 'http://api.exam.wrightin.com/v1/banner'
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
        self.log = Log()

    def test_getbanner(self):
        u'测试获取banner链接接口'
        self.log.info('----------开始测试获取banner接口-----------')
        json_data = {"token":self.uid_token}
        r = self.s.post(self.url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
            self.assertEqual(200,r.json()['code'])
            self.log.info('接口返回状态成功！')
        except Exception as e:
            self.log.error('请求失败，原因是：%s' % e)

        #取出json中banner链接依次进行get
        links = r.json()['data']
        for link in links:
            super_link = link['link']
            r2 = self.s.get(url=super_link,headers = self.header)
            try:
                self.assertEqual(200,r2.status_code)
                self.log.info('banner链接请求成功')
            except Exception as e:
                self.log.error('banner链接请求失败，原因：%s' % e)
        self.log.info('----------banner接口测试结束-----------')
    def test_get_meets(self):
        u'测试获取会议接口'
        url = 'http://api.exam.wrightin.com/v1/meetNew'
        self.log.info('------开始获取会议接口测试-------')
        json_data = {
            "token":self.uid_token,
            "time":"0"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        #判断返回状态
        #print(r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
            self.log.info('获取会议接口返回状态成功')
        except Exception as e:
            self.log.error('返回状态不成功，原因：%s' % e)

        #判断会议内容不为空
        meet_list = r.json()['data']['list']
        try:
            self.assertLessEqual(1,len(meet_list))
            self.log.info('会议内容不为空')
        except Exception as e:
            self.log.error('会议内容为空。原因：%s' % e)
        self.log.info('------获取会议接口测试结束-------')

    def test_meet_info(self):
        u'测试每个具体的会议信息'
        self.log.info('=========开始测试会议信息接口==========')
        #要先获取到每个会议的code
        url_1 = 'http://api.exam.wrightin.com/v1/meetNew'
        json_data_1 = {
            "token":self.uid_token,
            "time":"0"
        }
        #先获取会议列表
        r1 = self.s.post(url_1,headers = self.header,json=json_data_1)
        #从会议列表中取会议code
        response = r1.json()['data']['list']
        codes = []
        for i in response:
            codes.append(i['code'])
        #print('code::::',codes)
        #循环对每一个会议code获取会议信息
        url_2 = 'http://api.exam.wrightin.com/v1/meetinfo'
        for code in codes:
            json_data_2 = {"token":self.uid_token,"code":code}
            r2 = self.s.post(url_2,headers = self.header,json=json_data_2)#json_data可以共用
            #断言每个会议信息的返回状态
            try:
                self.assertEqual('请求成功.',r2.json()['note'])
                self.log.info('会议信息返回状态成功')
            except Exception as e:
                self.log.error('会议信息返回状态失败，原因：%s' % e)
        self.log.info('=========测试会议信息接口结束==========')

    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()
