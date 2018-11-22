#coding:utf-8
from common.login_lanting import auto_login_by_UID
import requests,unittest,time,json
from common.logger import Log
from common.Hash import get_digit,get_sign
from common.Excel import Excel_util

class Wallet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        cls.to = auto_login_by_UID()
        cls.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.4.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
        }
        cls.log = Log()
        cls.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_accout01(self):
        u'账户收支明细接口'
        self.log.info('开始测试收支明细接口..')
        url = 'http://api-rec.sunnycare.cc/v1/account/records'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        #请求
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('收支明细返回：%s' % r.json())
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('收支明细接口测试结束！\n')

    @unittest.skip('该模块删除了')
    def test_accout02(self):
        u'推广收益接口'
        self.log.info('开始测试推广收益接口..')
        url = 'http://api-rec.sunnycare.cc/v1/promotion/incomelist'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        #请求
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('推广收益接口返回：%s' % r.json())
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        #收益列表中income_code
        data = r.json()['data']['list'][0]['items']

        n = 0
        d = {}
        for i in data:
            d['income_code'+ str(n)] = i['income_code']
            n += 1
        #将收益code写入excel
        self.excel.write_value(21,6,d)
        self.log.info('推广收益接口测试结束\n')

    @unittest.skip('该模块删除了')
    def test_accout03(self):
        u'收益详情接口'
        self.log.info('开始测试收益详情接口..')
        url = 'http://api-rec.sunnycare.cc/v1/promotion/incomedetail'
        #读取excel中收益code
        real_code = json.loads(self.excel.read_value(21,6))
        #循环请求收益详情
        for i in real_code.values():
            json_data = {
                'token': self.to,
                'timestamp': str(int(time.time())),
                'nonce': get_digit(),
                'income_code': i
            }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('%s收益返回的详情是：%s' % (i,r.json()))
            #断言
            self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
            self.assertEqual('请求成功',r.json()['note'])
        self.log.info('收益详情接口测试结束！\n')


    def test_accout04(self):
        u'提现记录接口'
        self.log.info('开始测试提现记录接口..')
        url = 'http://api-rec.sunnycare.cc/v1/withdraw/records'
        json_data = {
                'token': self.to,
                'timestamp': str(int(time.time())),
                'nonce': get_digit()
            }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('提现记录返回：%s' % (r.json()))
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('提现记录接口测试结束..')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()


