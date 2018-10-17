#coding:utf-8
from common.login_lanting import auto_login_by_UID
import requests,unittest,time,json
from common.logger import Log
from common.Hash import get_digit,get_sign
from common.Excel import Excel_util

class Order(unittest.TestCase):
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

    def test_order01(self):
        u'我的订单列表接口'
        self.log.info('订单列表接口测试开始...')
        url = 'http://api-rec.sunnycare.cc/v1/order/list'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('订单列表返回：%s' % r.json())
        #断言
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        #订单列表中订单code
        data = r.json()['data']['list']
        n = 0
        d = {}
        for i in data:
            d['order_code'+ str(n)] = i['order_code']
            n += 1
        #将订单code写入excel
        self.excel.write_value(20,6,d)
        self.log.info('订单列表接口测试结束！\n')

    def test_order02(self):
        u'订单详情接口'
        self.log.info('开始测试订单详情接口...')
        url = 'http://api-rec.sunnycare.cc/v1/order/detail'
        read_code = self.excel.read_value(20,6)
        #将读取的str转换为dict
        real_code = json.loads(read_code)
        #依次请求订单详情
        for i in real_code.values():
            json_data = {
                'token': self.to,
                'timestamp': str(int(time.time())),
                'nonce': get_digit(),
                'order_code': i
            }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('%s 订单详情返回：%s' % (i,r.json()))
            #断言
            self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
            self.assertEqual('请求成功',r.json()['note'])
        self.log.info('订单详情接口测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__ == '__main__':
    unittest.main()


