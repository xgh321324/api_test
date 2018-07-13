#coding:utf-8
import requests
import unittest
import xlrd
from common.login import LG
class Test_pay(unittest.TestCase):
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

    def test_lesson_frontpage(self):
        u'测试课程首页接口'
        #url = 'http://api.lesson.sunnycare.cc/v1/rec'#测试环境接口
        url = 'https://api.lesson.wrightin.com/v1/rec'
        json_data = {
            "timestamp":"1523937360",
            "token":self.uid_token
                     }
        r = self.s.post(url,headers = self.header,json=json_data,verify=False)
        print(r.json())
        #判断返回状态
        self.assertEqual('请求成功.',r.json()['note'],msg='请求返回状态不是200，有问题')
        imagelinks = []
        links= []
        L= r.json()['data']['banner_list']
        print(L)
        #将返回json中所有照片链接放进[]
        for i in L:
            imagelinks.append(i['image'])
            links.append(i['link'])
        print('照片链接：%s' %  imagelinks)
        print('内容链接:%s' % links)
        #下面测试banner=图片链接是否可用
        for image in imagelinks:
            r1 = self.s.get(image)
            self.assertEqual(200,r1.status_code,msg='banner图片链接打开失败')
        #下面测试banner链接是否可用
        for link in links:
            r2 = self.s.get(link)
            self.assertEqual(200,r2.status_code,msg='banner链接打开失败')


    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()

