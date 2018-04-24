#coding:utf-8
import requests,unittest
from common.login import LG
from common.logger import Log
class Banner(unittest.TestCase):
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
        u'测试获取banner接口'
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

    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()
