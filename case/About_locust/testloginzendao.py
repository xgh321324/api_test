#coding:utf-8
import unittest,requests
from common.Hash import get_md5
class Zendao_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.header =  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        cls.s = requests.session()

    def test_login(self):
        u'登录'
        url = 'http://bug.zt.medohealth.com/index.php?m=user&f=login'
        da = {
            'account': 'xuguanghui',
            'password': get_md5('xuguanghui@123'),
            'keepLogin[]': 'on',
            'referer': '/index.php?m=my&f=index'
        }
        r = self.s.post(url,headers = self.header,data=da)
        print(r.text)

        #assert '我的地盘' in r.text

    def test_my(self):
        u'我的地盘'
        url = 'http://bug.zt.medohealth.com/index.php?m=my&f=index'
        r = self.s.get(url,headers = self.header)
        assert '我的地盘' in r.text

    def test_product(self):
        '产品'
        url = 'http://bug.zt.medohealth.com/index.php?m=product&f=index'
        r = self.s.get(url,headers = self.header)
        assert '产品' in r.text

    def test_project(self):
        u'项目'
        url = 'http://bug.zt.medohealth.com/index.php?m=project'
        r = self.s.get(url,headers = self.header)
        print(r.status_code)
        #print(r.text)
        assert '项目' in r.text

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()
