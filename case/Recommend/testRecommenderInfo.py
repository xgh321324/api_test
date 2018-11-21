#coding:utf-8
from common.login_lanting import auto_login_by_UID
import requests,unittest,time,json
from common.logger import Log
from common.Hash import get_digit,get_sign
from common.Excel import Excel_util

class Recommend(unittest.TestCase):
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

    def test_recommender01(self):
        u'获取推广大使信息接口'
        self.log.info('开始测试获取推广大使信息接口..')
        url = 'http://api-rec.sunnycare.cc/v1/level/mine'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('获取推广大使返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'],msg='返回状态码不是200')
        self.assertEqual('请求成功',r.json()['note'])
        self.log.info('推广大使信息接口测试结束！\n')

    def test_recommender02(self):
        u'推广活动列表'
        self.log.info('开始测试推广活动列表接口..')
        url = 'http://api-rec.sunnycare.cc/v1/promotion/list'
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('活动列表返回：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        #获取活动列表code
        get_code = []
        data = r.json()['data']['list']
        n = 0
        d = {}
        #循环给d字典赋值
        for i in data:
            get_code.append(i['promotion_code'])
            d['promotion_code'+str(n)] = i['promotion_code']
            n += 1
        #print(d)
        #赋值后将包含活动code写入excel
        self.excel.write_value(18,6,d)
        self.log.info('推广活动列表接口测试结束！\n')

    unittest.skip('no reason')
    def test_recommender03(self):
        u'获取推广活动详情接口'
        self.log.info('开始测试推广活动详情接口..')
        url = 'http://api-rec.sunnycare.cc/v1/promotion/detail'
        #读取excel中推广活动code
        read_code = self.excel.read_value(18,6)
        #将读取的str转换为dict
        real_code = json.loads(read_code)
        json_data = {
            'token': self.to,
            'timestamp': str(int(time.time())),
            'nonce': get_digit(),
            'promotion_code': real_code['promotion_code0']
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url,headers = self.header,json=json_data)
        #结果断言
        self.log.info('活动详情返回：%s' % r.json())
        #self.assertEqual(200,r.json()['code'])
        self.log.info('测试推广活动详情接口结束..\n')

    def test_recommender04(self):
        u'推广活动的推广明细'
        self.log.info('开始测试推广活动收入明细..')
        url = 'http://api-rec.sunnycare.cc/v1/promotion/invitelist'
        #读取excel中推广活动code
        read_code = self.excel.read_value(18,6)
        #将读取的str转换为dict
        real_code = json.loads(read_code)
        #循环去请求明细
        for i in real_code.values():
            json_data = {
                'token': self.to,
                'timestamp': str(int(time.time())),
                'nonce': get_digit(),
                'promotion_code': i
            }
            json_data['sign'] = get_sign(json_data)
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('%s明细返回的结果是%s:' % (i,r.json()))
            #断言
            self.assertEqual(200,r.json()['code'])
            self.assertEqual('请求成功',r.json()['note'])
        self.log.info('推广活动收入明细接口测试结束！\n')

    @classmethod
    def tearDownClass(cls):
        cls.s.close()

if __name__=='__main__':
    unittest.main()


