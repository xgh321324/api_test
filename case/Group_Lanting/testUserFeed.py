#coding:utf-8
import requests,unittest,time
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
from common.Read_config import get_content
urllib3.disable_warnings()

class Feed(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')


    def test_user_feed01(self):
        u'测试发布文字-不发布到圈子-参数正常'
        self.log.info('测试发布文字接口-不发布到圈子')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {"token":self.auto_login_token,
                     "text":"你知道我在等你吗"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布文字接口-不发布到圈子情况测试结束\n')

    def test_user_feed02(self):
        u'获取用户动态接口-参数正常'
        self.log.info('测试用户动态接口-参数正常')
        url = get_content('sns_base_url')+'/v1/user/feed'
        json_data = {"user_id":"U00014","time":0,"page":1}
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('请求成功',r.json()['note'])
        self.assertTrue(r.json()['data']) #判断data不为空
        con = r.json()['data']['content']

        L = []
        for i in con:
            L.append(i['id'])
            #print(i['id'])
        #print('ids:',L)

        d = {}
        n = 1
        for x in L:
            d['feed_id-'+str(n)] = x
            n += 1
        self.excel.write_value(12,6,d)
        self.log.info('测试用户动态接口-参数正常情况结束！\n')
    time.sleep(2)


    def test_user_feed03(self):
        u'feed详情接口-参数正常'
        url = get_content('sns_base_url')+'/v1/feed/record'
        self.log.info('开始测试feed详情接口')
        read_feed_ids = self.excel.read_value(12,6)
        feed_ids = json.loads(read_feed_ids)
        #print(type(feed_ids))
        #迭代字典的value

        for x in feed_ids.values():

            json_data = {
            "feed_id":x,
            "token":self.auto_login_token}
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('%s详情返回的内容：%s' % (x,r.json()))
            #self.assertEqual(200,r.json()['code'])
            self.assertEqual('请求成功',r.json()['note'])
            self.assertTrue(r.json()['data']) #判断data不为空


        self.log.info('feed详情接口测试结束！\n')

    def test_user_feed04(self):
        u'删除动态接口-参数正常'
        self.log.info('测试删除动态接口-参数正常')
        url = get_content('sns_base_url')+'/v1/feed/delete'
        read_feed_ids = self.excel.read_value(12,6)
        feed_ids = json.loads(read_feed_ids)
        #print(type(feed_ids))
        #迭代字典的value
        for x in feed_ids.values():
            json_data = {
                "token":self.auto_login_token,
                "feed_id":x
            }
            #需要保留一个动态不删除，后面的接口要用到这条动态中的图片地址

            if json_data['feed_id'] == 'F00083':
                pass
            else:
                r = self.s.post(url,headers = self.header,json=json_data)
                self.log.info('%s返回的内容是：%s' % (x,r.json()))
                self.assertEqual(200,r.json()['code'])
        self.log.info('测试删除动态接口-参数正常情况测试结束！\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
