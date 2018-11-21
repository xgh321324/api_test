#coding:utf-8

from common.login_lanting import auto_login_by_UID
import requests,unittest,time,json
from common.logger import Log
from common.Hash import get_digit,get_sign
from common.Excel import Excel_util

class Goods(unittest.TestCase):
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

    def test_goods01(self):
        u'商品列表接口'
        self.log.info('开始测试商品列表接口...')
        url = 'http://api-rec.sunnycare.cc/v1/goods/list'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit(),
            'page': '1',
            'type': '1'
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('商品列表返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        #获取商品列表code
        data = r.json()['data']['goodslist']
        n = 0
        d = {}
        #循环给d字典赋值
        for i in data:
            d['goods_code'+str(n)] = i['goods_code']
            n += 1
        #赋值后将包含活动code写入excel
        self.excel.write_value(19,6,d)
        self.log.info('商品列表接口测试结束...\n')

    def test_goods02(self):
        u'商品详情接口'
        self.log.info('开始测试商品详情接口...')
        url = 'http://api-rec.sunnycare.cc/v1/goods/detail'
        #读取goods_code
        read_code = self.excel.read_value(19,6)
        #将读取的str转为dict
        real_code = json.loads(read_code)
        #循环请求商品详情
        for i in real_code.values():
            json_data = {
                'token': self.to,
                'timestamp': str(int(time.time())),
                'nonce': get_digit(),
                'goods_code': i
            }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('%s商品详情返回：%s' % (i,r.json()))
            #断言
            self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
            self.assertEqual('请求成功',r.json()['note'])
        self.log.info('商品详情接口测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()

