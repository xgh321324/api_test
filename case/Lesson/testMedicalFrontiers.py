#coding:utf-8
import requests
import unittest
from PIL import Image
import time
class Medical_front(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.header = {'User-Agent':'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)'}
    def test_status(self):
        u'测试医学前沿中页面是否请求成功'
        url = 'http://api.sns.wrightin.com/v1/article/yixueqianyan/1'
        r = self.s.get(url,headers=self.header)
        print(r.json())
        response = r.json()
        status = response['note']
        self.assertEqual('请求成功.',status,msg='没有请求成功的标识，所以这是请求失败的！')
    def test_jpg(self):
        u'测试请求成功的数据中图片'
        url = 'http://api.sns.wrightin.com/v1/article/yixueqianyan/1'
        r2 = self.s.get(url,headers=self.header)
        response = r2.json()
        L = response['data']  #是一个列表

        try:
            for x in L:
                #print(x['cover'])
                jpg_link = x['cover']
                j = self.s.get(jpg_link)
                print(j.status_code)
                self.assertEqual(200,j.status_code)  #通过判断点击图片链接返回的状态码来看是否打开图片成功
                #return j.status_code
                '''
                with open(r'F:\test_picture\\'+time.strftime('%Y_%m_%d_%H_%M_%S')+'.jpg') as f :
                    f.write(j.content)
                '''
        except Exception as e:
            print(e)
    def test_link(self):
        u'测试返回数据中的链接'
        url = 'http://api.sns.wrightin.com/v1/article/yixueqianyan/1'
        r3 = self.s.get(url,headers=self.header)
        response = r3.json()
        L = response['data']  #是一个列表
        for x in L:
                link = x['link']
                c = self.s.get(link)
                print(c.status_code)
                self.assertEqual(200,c.status_code,msg='该链接返回的status不是200 ok！')


    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()

#user_exam_code=54D227C9DE5BFCA9AF26B4EE72C71B39